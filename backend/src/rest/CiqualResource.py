from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.Ciqual import Ciqual
from src.schema.CiqualSchema import CiqualSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
ciquals_list_ns = Namespace("ciquals-resource", path="/api/ciquals")

ciquals_schema = CiqualSchema()
ciquals_list_schema = CiqualSchema(many=True)


class CiqualResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on CiqualResource")
        ciquals = Ciqual.find_by_id(id)
        if ciquals is not None:
            return ciquals_schema.dump(ciquals), 200
        return {"message": "Ciqual not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on CiqualResource")
        ciquals_json = request.get_json()
        if ciquals_json["id"] is None:
            return {"message": "Invalid Ciqual"}, 400
        if id != ciquals_json["id"]:
            return {"message": "Invalid Ciqual"}, 400
        ciquals = Ciqual.find_by_id(id)
        if ciquals.get_id() is None:
            return {"message": "Invalid Ciqual"}, 400
        try:
            updated_ciquals = ciquals_schema.load(
                ciquals_json, instance=ciquals, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_ciquals.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return ciquals_schema.dump(updated_ciquals), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on CiqualResource")
        ciquals_json = request.get_json()
        if ciquals_json["id"] is None:
            return {"message": "Invalid Ciqual"}, 400
        if id != ciquals_json["id"]:
            return {"message": "Invalid Ciqual"}, 400
        ciquals = Ciqual.find_by_id(id)
        if ciquals.get_id() is None:
            return {"message": "Invalid Ciqual"}, 400
        try:
            updated_ciquals = ciquals_schema.load(
                ciquals_json, instance=ciquals, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_ciquals.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return ciquals_schema.dump(updated_ciquals), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on CiqualResource")
        ciquals = Ciqual.find_by_id(id)
        if ciquals is None:
            return {"message": "Ciqual not found"}, 404
        try:
            ciquals.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Ciqual deleted"}, 204


class CiqualResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on CiqualResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        ciquals = Ciqual.find_all(page, size)
        if ciquals is not None:
            return ciquals_list_schema.dump(ciquals), 200
        return {"message": "Ciqual not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on CiqualResourceList")
        ciquals_json = request.get_json()
        try:
            ciquals_data = ciquals_schema.load(ciquals_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            ciquals_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return ciquals_schema.dump(ciquals_data), 201


class CiqualResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on CiqualResourceListCount")
        ciquals_count = Ciqual.find_all_count()
        if ciquals_count is not None:
            return ciquals_count, 200
        return {"message": "Ciqual count not found"}, 404
