from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.domain.PAT import PAT
from src.schema.PATSchema import PATSchema
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
pats_list_ns = Namespace("pats-resource", path="/api/pats")

pats_schema = PATSchema()
pats_list_schema = PATSchema(many=True)


class PATResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on PATResource")
        pats = PAT.find_by_id(id)
        if pats is not None:
            return pats_schema.dump(pats), 200
        return {"message": "PAT not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on PATResource")
        pats_json = request.get_json()
        if pats_json["id"] is None:
            return {"message": "Invalid PAT"}, 400
        if id != pats_json["id"]:
            return {"message": "Invalid PAT"}, 400
        pats = PAT.find_by_id(id)
        if pats.get_id() is None:
            return {"message": "Invalid PAT"}, 400
        try:
            updated_pats = pats_schema.load(pats_json, instance=pats, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_pats.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return pats_schema.dump(updated_pats), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on PATResource")
        pats_json = request.get_json()
        if pats_json["id"] is None:
            return {"message": "Invalid PAT"}, 400
        if id != pats_json["id"]:
            return {"message": "Invalid PAT"}, 400
        pats = PAT.find_by_id(id)
        if pats.get_id() is None:
            return {"message": "Invalid PAT"}, 400
        try:
            updated_pats = pats_schema.load(pats_json, instance=pats, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_pats.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return pats_schema.dump(updated_pats), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on PATResource")
        pats = PAT.find_by_id(id)
        if pats is None:
            return {"message": "PAT not found"}, 404
        try:
            pats.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "PAT deleted"}, 204


class PATResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PATResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        pats = PAT.find_all(page, size)
        if pats is not None:
            return pats_list_schema.dump(pats), 200
        return {"message": "PAT not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on PATResourceList")
        pats_json = request.get_json()
        try:
            pats_data = pats_schema.load(pats_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            pats_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return pats_schema.dump(pats_data), 201


class PATResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PATResourceListCount")
        pats_count = PAT.find_all_count()
        if pats_count is not None:
            return pats_count, 200
        return {"message": "PAT count not found"}, 404
