from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.Vinaigrette import Vinaigrette
from src.schema.VinaigretteSchema import VinaigretteSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
vinaigrettes_list_ns = Namespace("vinaigrettes-resource", path="/api/vinaigrettes")

vinaigrettes_schema = VinaigretteSchema()
vinaigrettes_list_schema = VinaigretteSchema(many=True)


class VinaigretteResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on VinaigretteResource")
        vinaigrettes = Vinaigrette.find_by_id(id)
        if vinaigrettes is not None:
            return vinaigrettes_schema.dump(vinaigrettes), 200
        return {"message": "Vinaigrette not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on VinaigretteResource")
        vinaigrettes_json = request.get_json()
        if vinaigrettes_json["id"] is None:
            return {"message": "Invalid Vinaigrette"}, 400
        if id != vinaigrettes_json["id"]:
            return {"message": "Invalid Vinaigrette"}, 400
        vinaigrettes = Vinaigrette.find_by_id(id)
        if vinaigrettes.get_id() is None:
            return {"message": "Invalid Vinaigrette"}, 400
        try:
            updated_vinaigrettes = vinaigrettes_schema.load(
                vinaigrettes_json, instance=vinaigrettes, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_vinaigrettes.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return vinaigrettes_schema.dump(updated_vinaigrettes), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on VinaigretteResource")
        vinaigrettes_json = request.get_json()
        if vinaigrettes_json["id"] is None:
            return {"message": "Invalid Vinaigrette"}, 400
        if id != vinaigrettes_json["id"]:
            return {"message": "Invalid Vinaigrette"}, 400
        vinaigrettes = Vinaigrette.find_by_id(id)
        if vinaigrettes.get_id() is None:
            return {"message": "Invalid Vinaigrette"}, 400
        try:
            updated_vinaigrettes = vinaigrettes_schema.load(
                vinaigrettes_json, instance=vinaigrettes, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_vinaigrettes.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return vinaigrettes_schema.dump(updated_vinaigrettes), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on VinaigretteResource")
        vinaigrettes = Vinaigrette.find_by_id(id)
        if vinaigrettes is None:
            return {"message": "Vinaigrette not found"}, 404
        try:
            vinaigrettes.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Vinaigrette deleted"}, 204


class VinaigretteResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on VinaigretteResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        vinaigrettes = Vinaigrette.find_all(page, size)
        if vinaigrettes is not None:
            return vinaigrettes_list_schema.dump(vinaigrettes), 200
        return {"message": "Vinaigrette not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on VinaigretteResourceList")
        vinaigrettes_json = request.get_json()
        try:
            vinaigrettes_data = vinaigrettes_schema.load(vinaigrettes_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            vinaigrettes_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return vinaigrettes_schema.dump(vinaigrettes_data), 201


class VinaigretteResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on VinaigretteResourceListCount")
        vinaigrettes_count = Vinaigrette.find_all_count()
        if vinaigrettes_count is not None:
            return vinaigrettes_count, 200
        return {"message": "Vinaigrette count not found"}, 404
