from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.Plat import Plat
from src.schema.PlatSchema import PlatSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
plats_list_ns = Namespace("plats-resource", path="/api/plats")

plats_schema = PlatSchema()
plats_list_schema = PlatSchema(many=True)


class PlatResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on PlatResource")
        plats = Plat.find_by_id(id)
        if plats is not None:
            return plats_schema.dump(plats), 200
        return {"message": "Plat not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on PlatResource")
        plats_json = request.get_json()
        if plats_json["id"] is None:
            return {"message": "Invalid Plat"}, 400
        if id != plats_json["id"]:
            return {"message": "Invalid Plat"}, 400
        plats = Plat.find_by_id(id)
        if plats.get_id() is None:
            return {"message": "Invalid Plat"}, 400
        try:
            updated_plats = plats_schema.load(
                plats_json, instance=plats, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_plats.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return plats_schema.dump(updated_plats), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on PlatResource")
        plats_json = request.get_json()
        if plats_json["id"] is None:
            return {"message": "Invalid Plat"}, 400
        if id != plats_json["id"]:
            return {"message": "Invalid Plat"}, 400
        plats = Plat.find_by_id(id)
        if plats.get_id() is None:
            return {"message": "Invalid Plat"}, 400
        try:
            updated_plats = plats_schema.load(
                plats_json, instance=plats, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_plats.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return plats_schema.dump(updated_plats), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on PlatResource")
        plats = Plat.find_by_id(id)
        if plats is None:
            return {"message": "Plat not found"}, 404
        try:
            plats.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Plat deleted"}, 204


class PlatResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PlatResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        plats = Plat.find_all(page, size)
        if plats is not None:
            return plats_list_schema.dump(plats), 200
        return {"message": "Plat not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on PlatResourceList")
        plats_json = request.get_json()
        try:
            plats_data = plats_schema.load(plats_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            plats_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return plats_schema.dump(plats_data), 201


class PlatResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PlatResourceListCount")
        plats_count = Plat.find_all_count()
        if plats_count is not None:
            return plats_count, 200
        return {"message": "Plat count not found"}, 404
