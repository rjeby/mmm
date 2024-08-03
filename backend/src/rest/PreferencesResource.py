from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.domain.Preferences import Preferences
from src.schema.PreferencesSchema import PreferencesSchema
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
preferences_list_ns = Namespace("preferences-resource", path="/api/preferences")

preferences_schema = PreferencesSchema()
preferences_list_schema = PreferencesSchema(many=True)


class PreferencesResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on PreferencesResource")
        preferences = Preferences.find_by_id(id)
        if preferences is not None:
            return preferences_schema.dump(preferences), 200
        return {"message": "Preferences not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on PreferencesResource")
        preferences_json = request.get_json()
        if preferences_json["id"] is None:
            return {"message": "Invalid Preferences"}, 400
        if id != preferences_json["id"]:
            return {"message": "Invalid Preferences"}, 400
        preferences = Preferences.find_by_id(id)
        if preferences.get_id() is None:
            return {"message": "Invalid Preferences"}, 400
        try:
            updated_preferences = preferences_schema.load(
                preferences_json, instance=preferences, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_preferences.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return preferences_schema.dump(updated_preferences), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on PreferencesResource")
        preferences_json = request.get_json()
        if preferences_json["id"] is None:
            return {"message": "Invalid Preferences"}, 400
        if id != preferences_json["id"]:
            return {"message": "Invalid Preferences"}, 400
        preferences = Preferences.find_by_id(id)
        if preferences.get_id() is None:
            return {"message": "Invalid Preferences"}, 400
        try:
            updated_preferences = preferences_schema.load(
                preferences_json, instance=preferences, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_preferences.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return preferences_schema.dump(updated_preferences), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on PreferencesResource")
        preferences = Preferences.find_by_id(id)
        if preferences is None:
            return {"message": "Preferences not found"}, 404
        try:
            preferences.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Preferences deleted"}, 204


class PreferencesResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PreferencesResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        preferences = Preferences.find_all(page, size)
        if preferences is not None:
            return preferences_list_schema.dump(preferences), 200
        return {"message": "Preferences not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on PreferencesResourceList")
        preferences_json = request.get_json()
        try:
            preferences_data = preferences_schema.load(preferences_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            preferences_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return preferences_schema.dump(preferences_data), 201


class PreferencesResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PreferencesResourceListCount")
        preferences_count = Preferences.find_all_count()
        if preferences_count is not None:
            return preferences_count, 200
        return {"message": "Preferences count not found"}, 404
