from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.Encas import Encas
from src.schema.EncasSchema import EncasSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
encas_list_ns = Namespace("encas-resource", path="/api/encas")

encas_schema = EncasSchema()
encas_list_schema = EncasSchema(many=True)


class EncasResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on EncasResource")
        encas = Encas.find_by_id(id)
        if encas is not None:
            return encas_schema.dump(encas), 200
        return {"message": "Encas not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on EncasResource")
        encas_json = request.get_json()
        if encas_json["id"] is None:
            return {"message": "Invalid Encas"}, 400
        if id != encas_json["id"]:
            return {"message": "Invalid Encas"}, 400
        encas = Encas.find_by_id(id)
        if encas.get_id() is None:
            return {"message": "Invalid Encas"}, 400
        try:
            updated_encas = encas_schema.load(
                encas_json, instance=encas, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_encas.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return encas_schema.dump(updated_encas), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on EncasResource")
        encas_json = request.get_json()
        if encas_json["id"] is None:
            return {"message": "Invalid Encas"}, 400
        if id != encas_json["id"]:
            return {"message": "Invalid Encas"}, 400
        encas = Encas.find_by_id(id)
        if encas.get_id() is None:
            return {"message": "Invalid Encas"}, 400
        try:
            updated_encas = encas_schema.load(
                encas_json, instance=encas, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_encas.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return encas_schema.dump(updated_encas), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on EncasResource")
        encas = Encas.find_by_id(id)
        if encas is None:
            return {"message": "Encas not found"}, 404
        try:
            encas.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Encas deleted"}, 204


class EncasResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on EncasResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        encas = Encas.find_all(page, size)
        if encas is not None:
            return encas_list_schema.dump(encas), 200
        return {"message": "Encas not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on EncasResourceList")
        encas_json = request.get_json()
        try:
            encas_data = encas_schema.load(encas_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            encas_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return encas_schema.dump(encas_data), 201


class EncasResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on EncasResourceListCount")
        encas_count = Encas.find_all_count()
        if encas_count is not None:
            return encas_count, 200
        return {"message": "Encas count not found"}, 404
