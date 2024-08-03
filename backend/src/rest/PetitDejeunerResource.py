from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.PetitDejeuner import PetitDejeuner
from src.schema.PetitDejeunerSchema import PetitDejeunerSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
petit_dejeuner_list_ns = Namespace("petit-dejeuner-resource", path="/api/petit-dejeuner")

petit_dejeuner_schema = PetitDejeunerSchema()
petit_dejeuner_list_schema = PetitDejeunerSchema(many=True)


class PetitDejeunerResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on PetitDejeunerResource")
        petit_dejeuner = PetitDejeuner.find_by_id(id)
        if petit_dejeuner is not None:
            return petit_dejeuner_schema.dump(petit_dejeuner), 200
        return {"message": "PetitDejeuner not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on PetitDejeunerResource")
        petit_dejeuner_json = request.get_json()
        if petit_dejeuner_json["id"] is None:
            return {"message": "Invalid PetitDejeuner"}, 400
        if id != petit_dejeuner_json["id"]:
            return {"message": "Invalid PetitDejeuner"}, 400
        petit_dejeuner = PetitDejeuner.find_by_id(id)
        if petit_dejeuner.get_id() is None:
            return {"message": "Invalid PetitDejeuner"}, 400
        try:
            updated_petit_dejeuner = petit_dejeuner_schema.load(
                petit_dejeuner_json, instance=petit_dejeuner, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_petit_dejeuner.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return petit_dejeuner_schema.dump(updated_petit_dejeuner), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on PetitDejeunerResource")
        petit_dejeuner_json = request.get_json()
        if petit_dejeuner_json["id"] is None:
            return {"message": "Invalid PetitDejeuner"}, 400
        if id != petit_dejeuner_json["id"]:
            return {"message": "Invalid PetitDejeuner"}, 400
        petit_dejeuner = PetitDejeuner.find_by_id(id)
        if petit_dejeuner.get_id() is None:
            return {"message": "Invalid PetitDejeuner"}, 400
        try:
            updated_petit_dejeuner = petit_dejeuner_schema.load(
                petit_dejeuner_json, instance=petit_dejeuner, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_petit_dejeuner.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return petit_dejeuner_schema.dump(updated_petit_dejeuner), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on PetitDejeunerResource")
        petit_dejeuner = PetitDejeuner.find_by_id(id)
        if petit_dejeuner is None:
            return {"message": "PetitDejeuner not found"}, 404
        try:
            petit_dejeuner.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "PetitDejeuner deleted"}, 204


class PetitDejeunerResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PetitDejeunerResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        petit_dejeuner = PetitDejeuner.find_all(page, size)
        if petit_dejeuner is not None:
            return petit_dejeuner_list_schema.dump(petit_dejeuner), 200
        return {"message": "PetitDejeuner not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on PetitDejeunerResourceList")
        petit_dejeuner_json = request.get_json()
        try:
            petit_dejeuner_data = petit_dejeuner_schema.load(petit_dejeuner_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            petit_dejeuner_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return petit_dejeuner_schema.dump(petit_dejeuner_data), 201


class PetitDejeunerResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PetitDejeunerResourceListCount")
        petit_dejeuner_count = PetitDejeuner.find_all_count()
        if petit_dejeuner_count is not None:
            return petit_dejeuner_count, 200
        return {"message": "PetitDejeuner count not found"}, 404
