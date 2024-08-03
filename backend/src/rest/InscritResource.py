from flask import request
import logging
import json
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from src.domain.Inscrit import Inscrit
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.User import User
from src.domain.Preferences import Preferences
from src.schema.InscritSchema import InscritSchema
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
inscrits_list_ns = Namespace("inscrits-resource", path="/api/inscrits")

inscrits_schema = InscritSchema()
inscrits_list_schema = InscritSchema(many=True)


class InscritResource(Resource):

    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on InscritResource")
        inscrits = Inscrit.find_by_id(id)
        if inscrits is not None:
            return inscrits_schema.dump(inscrits), 200
        return {"message": "Inscrit not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on InscritResource")
        inscrits_json = request.get_json()
        if inscrits_json["id"] is None:
            return {"message": "Invalid Inscrit"}, 400
        if id != inscrits_json["id"]:
            return {"message": "Invalid Inscrit"}, 400
        inscrits = Inscrit.find_by_id(id)
        if inscrits.get_id() is None:
            return {"message": "Invalid Inscrit"}, 400
        try:
            updated_inscrits = inscrits_schema.load(
                inscrits_json, instance=inscrits, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_inscrits.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return inscrits_schema.dump(updated_inscrits), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on InscritResource")
        inscrits_json = request.get_json()
        if inscrits_json["id"] is None:
            return {"message": "Invalid Inscrit"}, 400
        if id != inscrits_json["id"]:
            return {"message": "Invalid Inscrit"}, 400
        inscrits = Inscrit.find_by_id(id)
        if inscrits.get_id() is None:
            return {"message": "Invalid Inscrit"}, 400
        try:
            updated_inscrits = inscrits_schema.load(
                inscrits_json, instance=inscrits, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_inscrits.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return inscrits_schema.dump(updated_inscrits), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on InscritResource")
        inscrits = Inscrit.find_by_id(id)
        if inscrits is None:
            return {"message": "Inscrit not found"}, 404
        try:
            inscrits.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Inscrit deleted"}, 204


class InscritResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on InscritResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        inscrits = Inscrit.find_all(page, size)
        if inscrits is not None:
            return inscrits_list_schema.dump(inscrits), 200
        return {"message": "Inscrit not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on InscritResourceList")
        inscrits_json = request.get_json()
        try:
            inscrits_data = inscrits_schema.load(inscrits_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            inscrits_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return inscrits_schema.dump(inscrits_data), 201


class InscritResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on InscritResourceListCount")
        inscrits_count = Inscrit.find_all_count()
        if inscrits_count is not None:
            return inscrits_count, 200
        return {"message": "Inscrit count not found"}, 404
