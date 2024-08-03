from flask import Flask, request, jsonify, render_template, make_response
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import create_access_token
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from sqlalchemy.exc import SQLAlchemyError
from src.utils.MailConfiguration import (
    send_activation_mail,
    confirm_token,
    send_reset_mail,
)
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
import json
import bcrypt
import logging
import re
from random import randint
from datetime import date
from src.domain.Menu import Menu
from src.domain.User import User
from src.domain.Inscrit import Inscrit
from src.domain.Preferences import Preferences
from src.domain.ProgrammeHebdomadaire import ProgrammeHebdomadaire, InscritProgrammeHebdomadaire
from src.schema.InscritSchema import InscritSchema, InscritInfosResourceSchema, InscritMenusResourceSchema
from src.schema.PreferencesSchema import PreferencesSchema
from src.schema.MenuSchema import MenuSchema
from src.schema.MembreFamilleSchema import MembreFamilleSchema
from src.schema.ProgrammeHebdomadaireSchema import ProgrammeHebdomadaireSchema
from src.domain.PetitDejeuner import PetitDejeuner
from src.domain.Plat import Plat
from src.domain.Entree import Entree
from src.domain.Encas import Encas
from src.domain.Dessert import Dessert
from src.domain.Vinaigrette import Vinaigrette
from src.DatabaseConfig import db
from src.utils.MMMUtils import get_random_menu, get_random_id, create_programme, create_default_programme, retrieve_programme_hebdomadaire, planning

from flask import url_for

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")

inscrits_infos_resource_schema = InscritInfosResourceSchema()
inscrits_menus_resource_schema = InscritMenusResourceSchema()
programme_hebdomadaire_schema = ProgrammeHebdomadaireSchema()
inscrits_schema = InscritSchema()
preferences_schema = PreferencesSchema()
famille_schema = MembreFamilleSchema(many=True)
menus_schema = MenuSchema()


frontend_inscription_ns = Namespace("frontend-resource", path="/api/formulaire-inscription")


class FormulaireInscriptionResource(Resource):
    @jwt_required()
    def post(self):
        logging.info("POST request received on FormulaireInscriptionList")
        email = get_jwt_identity()
        user = User.find_by_email(email)
        inscrits_json = request.get_json()
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        # Check if user is confirmed
        if not user.is_confirmed:
            return {
                "message": "L'utilisateur doit être confirmé pour effectuer cette action"
            }, 401
        # Check if user doesn't have infos
        if user.has_infos:
            return {"message": "L'utilisateur a déjà les informations requises"}, 401
        inscrits_json = request.get_json()
        try:
            inscrits_data = inscrits_schema.load(inscrits_json, partial=True)
            inscrits_data.user_id = user.id
            preferences = Preferences()
            inscrits_data.preferences = preferences
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            members = inscrits_data.membres_famille
            inscrits_data.save_to_db()
            for member in members:
                member.inscrit_id = inscrits_data.id
                member.save_to_db()
            user.has_infos = True
            user.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return inscrits_schema.dump(inscrits_data), 201


frontend_infos_ns = Namespace("frontend-resource", path="/api/mes-infos")


class InscritInfosResource(Resource):

    @jwt_required()
    def get(self):
        logging.info("GET request received on InscritInfosResource")
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        inscrit = user.inscrit
        if inscrit is not None:
            return inscrits_infos_resource_schema.dump(inscrit), 200
        return {"message": "Inscrit non trouvé"}, 404

    @jwt_required()
    def put(self):
        logging.info("PUT request received on InscritInfosResource")
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        inscrit = user.inscrit
        if not inscrit:
            return {"message": "Inscrit non trouvé"}, 404
        inscrit_json = request.get_json()
        try:
            inscrit_data = inscrits_schema.load(
                inscrit_json, instance=inscrit, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            inscrit_data.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Inscrit mis à jour avec succès"}, 200


frontend_preferences_ns = Namespace("frontend-resource", path="/api/mes-preferences")


class InscritPreferencesResource(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on InscritPreferencesResource")
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        inscrit = user.inscrit
        if not inscrit:
            return {"message": "Inscrit non trouvé"}, 404
        preferences = Preferences.find_by_inscrit_id(inscrit.id)
        if preferences is not None:
            return preferences_schema.dump(preferences), 200
        return {"message": "Préférences non trouvées"}, 404

    @jwt_required()
    def put(self):
        logging.info("PUT request received on InscritPreferencesResource")
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        inscrit = user.inscrit
        if not inscrit:
            return {"message": "Inscrit non trouvé"}, 404
        preferences_json = request.get_json()
        try:
            preferences_data = preferences_schema.load(
                preferences_json, instance=inscrit.preferences, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            preferences_data.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Préférences mises à jour avec succès"}, 200


frontend_famille_ns = Namespace("frontend-resource", path="/api/ma-famille")


class InscritFamilleResource(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on InscritFamilleResource")
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        inscrit = user.inscrit
        if not inscrit:
            return {"message": "Inscrit non trouvé"}, 404
        famille = inscrit.membres_famille
        return famille_schema.dump(famille), 200

    @jwt_required()
    def put(self):
        logging.info("PUT request received on InscritFamilleResource")
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        inscrit = user.inscrit
        if not inscrit:
            return {"message": "Inscrit non trouvé"}, 404
        famille_json = request.get_json()
        try:
            famille_data = famille_schema.load(famille_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            for member in inscrit.membres_famille:
                member.delete_from_db()
            for member in famille_data:
                member.inscrit_id = inscrit.id
                member.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Membres de la famille mis à jour avec succès"}, 200

frontend_menus_ns = Namespace("frontend-resource", path="/api/mes-meilleurs-menus")


class InscritMenusResource(Resource):
    @jwt_required()
    def get(self):
        logging.info("GET request received on InscritMenusResource")
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        inscrit = user.inscrit
        if not inscrit:
            return {"message": "Inscrit non trouvé"}, 404
        
        # Retrieve the latest ProgrammeHebdomadaire
        latest_programme = retrieve_programme_hebdomadaire(inscrit.id, False)
        latest_default_programme = retrieve_programme_hebdomadaire(inscrit.id, True)
        if not latest_programme and not latest_default_programme:
            # No ProgrammeHebdomadaire found, create a new one with default values
            vinaigrette_count = Vinaigrette.find_all_count()
            petit_dejeuner_count = PetitDejeuner.find_all_count()
            encas_count = Encas.find_all_count()
            # When a new progam is proposed default program is same as non default one, changes will be applied on non default program
            # default program will be used to restore old state
            latest_programme = create_programme(default=False, vinaigrette_count=vinaigrette_count, petit_dejeuner_count=petit_dejeuner_count, encas_count=encas_count )
            inscrit.programme_hebdomadaire.append(latest_programme)
            latest_default_programme = create_default_programme(latest_programme)
            inscrit.programme_hebdomadaire.append(latest_default_programme)
            inscrit.update_db()
        return {"inscrit": inscrits_menus_resource_schema.dump(inscrit), "programme_hebdomadaire": programme_hebdomadaire_schema.dump(latest_programme), "programme_hebdomadaire_default": programme_hebdomadaire_schema.dump(latest_default_programme)}, 200

    @jwt_required()
    def put(self):
    # TODO: Add verifications for BD integrity
      logging.info("PUT request received on InscritMenusResource")
      email = get_jwt_identity()
      user = User.find_by_email(email)
      if not user:
          return {"message": "Utilisateur non trouvé"}, 404
      inscrit = user.inscrit
      if not inscrit:
          return {"message": "Inscrit non trouvé"}, 404
      programme_hebdomadaire_json = request.get_json()
      try:
          programme_hebdomadaire_data = programme_hebdomadaire_schema.load(programme_hebdomadaire_json, partial=True)
      except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
      try:
        programme_hebdomadaire_data.lundi_dejeuner.update_db()
      except SQLAlchemyError as e:
        return {"message": str(e.__dict__["orig"])}, 400
      return {"message": "Programme Hebdomadaire mis à jour avec succès"}, 200