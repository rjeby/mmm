from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.ProgrammeHebdomadaire import ProgrammeHebdomadaire
from src.schema.ProgrammeHebdomadaireSchema import ProgrammeHebdomadaireSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
programme_hebdomadaire_list_ns = Namespace("programme-hebdomadaire-resource", path="/api/programme-hebdomadaire")

programme_hebdomadaire_schema = ProgrammeHebdomadaireSchema()
programme_hebdomadaire_list_schema = ProgrammeHebdomadaireSchema(many=True)


class ProgrammeHebdomadaireResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on ProgrammeHebdomadaireResource")
        programme_hebdomadaire = ProgrammeHebdomadaire.find_by_id(id)
        if programme_hebdomadaire is not None:
            return programme_hebdomadaire_schema.dump(programme_hebdomadaire), 200
        return {"message": "ProgrammeHebdomadaire not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on ProgrammeHebdomadaireResource")
        programme_hebdomadaire_json = request.get_json()
        if programme_hebdomadaire_json["id"] is None:
            return {"message": "Invalid ProgrammeHebdomadaire"}, 400
        if id != programme_hebdomadaire_json["id"]:
            return {"message": "Invalid ProgrammeHebdomadaire"}, 400
        programme_hebdomadaire = ProgrammeHebdomadaire.find_by_id(id)
        if programme_hebdomadaire.get_id() is None:
            return {"message": "Invalid ProgrammeHebdomadaire"}, 400
        try:
            updated_programme_hebdomadaire = programme_hebdomadaire_schema.load(
                programme_hebdomadaire_json, instance=programme_hebdomadaire, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_programme_hebdomadaire.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return programme_hebdomadaire_schema.dump(updated_programme_hebdomadaire), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on ProgrammeHebdomadaireResource")
        programme_hebdomadaire_json = request.get_json()
        if programme_hebdomadaire_json["id"] is None:
            return {"message": "Invalid ProgrammeHebdomadaire"}, 400
        if id != programme_hebdomadaire_json["id"]:
            return {"message": "Invalid ProgrammeHebdomadaire"}, 400
        programme_hebdomadaire = ProgrammeHebdomadaire.find_by_id(id)
        if programme_hebdomadaire.get_id() is None:
            return {"message": "Invalid ProgrammeHebdomadaire"}, 400
        try:
            updated_programme_hebdomadaire = programme_hebdomadaire_schema.load(
                programme_hebdomadaire_json, instance=programme_hebdomadaire, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_programme_hebdomadaire.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return programme_hebdomadaire_schema.dump(updated_programme_hebdomadaire), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on ProgrammeHebdomadaireResource")
        programme_hebdomadaire = ProgrammeHebdomadaire.find_by_id(id)
        if programme_hebdomadaire is None:
            return {"message": "ProgrammeHebdomadaire not found"}, 404
        try:
            programme_hebdomadaire.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "ProgrammeHebdomadaire deleted"}, 204


class ProgrammeHebdomadaireResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on ProgrammeHebdomadaireResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        programme_hebdomadaire = ProgrammeHebdomadaire.find_all(page, size)
        if programme_hebdomadaire is not None:
            return programme_hebdomadaire_list_schema.dump(programme_hebdomadaire), 200
        return {"message": "ProgrammeHebdomadaire not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on ProgrammeHebdomadaireResourceList")
        programme_hebdomadaire_json = request.get_json()
        try:
            programme_hebdomadaire_data = programme_hebdomadaire_schema.load(programme_hebdomadaire_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            programme_hebdomadaire_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return programme_hebdomadaire_schema.dump(programme_hebdomadaire_data), 201


class ProgrammeHebdomadaireResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on ProgrammeHebdomadaireResourceListCount")
        programme_hebdomadaire_count = ProgrammeHebdomadaire.find_all_count()
        if programme_hebdomadaire_count is not None:
            return programme_hebdomadaire_count, 200
        return {"message": "ProgrammeHebdomadaire count not found"}, 404
