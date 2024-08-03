from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.Entree import Entree
from src.schema.EntreeSchema import EntreeSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
entrees_list_ns = Namespace("entrees-resource", path="/api/entrees")

entrees_schema = EntreeSchema()
entrees_list_schema = EntreeSchema(many=True)


class EntreeResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on EntreeResource")
        entrees = Entree.find_by_id(id)
        if entrees is not None:
            return entrees_schema.dump(entrees), 200
        return {"message": "Entree not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on EntreeResource")
        entrees_json = request.get_json()
        if entrees_json["id"] is None:
            return {"message": "Invalid Entree"}, 400
        if id != entrees_json["id"]:
            return {"message": "Invalid Entree"}, 400
        entrees = Entree.find_by_id(id)
        if entrees.get_id() is None:
            return {"message": "Invalid Entree"}, 400
        try:
            updated_entrees = entrees_schema.load(
                entrees_json, instance=entrees, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_entrees.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return entrees_schema.dump(updated_entrees), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on EntreeResource")
        entrees_json = request.get_json()
        if entrees_json["id"] is None:
            return {"message": "Invalid Entree"}, 400
        if id != entrees_json["id"]:
            return {"message": "Invalid Entree"}, 400
        entrees = Entree.find_by_id(id)
        if entrees.get_id() is None:
            return {"message": "Invalid Entree"}, 400
        try:
            updated_entrees = entrees_schema.load(
                entrees_json, instance=entrees, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_entrees.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return entrees_schema.dump(updated_entrees), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on EntreeResource")
        entrees = Entree.find_by_id(id)
        if entrees is None:
            return {"message": "Entree not found"}, 404
        try:
            entrees.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Entree deleted"}, 204


class EntreeResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on EntreeResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        entrees = Entree.find_all(page, size)
        if entrees is not None:
            return entrees_list_schema.dump(entrees), 200
        return {"message": "Entree not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on EntreeResourceList")
        entrees_json = request.get_json()
        try:
            entrees_data = entrees_schema.load(entrees_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            entrees_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return entrees_schema.dump(entrees_data), 201


class EntreeResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on EntreeResourceListCount")
        entrees_count = Entree.find_all_count()
        if entrees_count is not None:
            return entrees_count, 200
        return {"message": "Entree count not found"}, 404
