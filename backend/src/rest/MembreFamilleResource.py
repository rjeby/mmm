from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.domain.MembreFamille import MembreFamille
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.schema.MembreFamilleSchema import MembreFamilleSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError


logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
membre_familles_list_ns = Namespace(
    "membre-familles-resource", path="/api/membre-familles"
)

membre_familles_schema = MembreFamilleSchema()
membre_familles_list_schema = MembreFamilleSchema(many=True)


class MembreFamilleResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on MembreFamilleResource")
        membre_familles = MembreFamille.find_by_id(id)
        if membre_familles is not None:
            return membre_familles_schema.dump(membre_familles), 200
        return {"message": "MembreFamille not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on MembreFamilleResource")
        membre_familles_json = request.get_json()
        if membre_familles_json["id"] is None:
            return {"message": "Invalid MembreFamille"}, 400
        if id != membre_familles_json["id"]:
            return {"message": "Invalid MembreFamille"}, 400
        membre_familles = MembreFamille.find_by_id(id)
        if membre_familles.get_id() is None:
            return {"message": "Invalid MembreFamille"}, 400
        try:
            updated_membre_familles = membre_familles_schema.load(
                membre_familles_json, instance=membre_familles, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_membre_familles.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return membre_familles_schema.dump(updated_membre_familles), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on MembreFamilleResource")
        membre_familles_json = request.get_json()
        if membre_familles_json["id"] is None:
            return {"message": "Invalid MembreFamille"}, 400
        if id != membre_familles_json["id"]:
            return {"message": "Invalid MembreFamille"}, 400
        membre_familles = MembreFamille.find_by_id(id)
        if membre_familles.get_id() is None:
            return {"message": "Invalid MembreFamille"}, 400
        try:
            updated_membre_familles = membre_familles_schema.load(
                membre_familles_json, instance=membre_familles, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_membre_familles.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return membre_familles_schema.dump(updated_membre_familles), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on MembreFamilleResource")
        membre_familles = MembreFamille.find_by_id(id)
        if membre_familles is None:
            return {"message": "MembreFamille not found"}, 404
        try:
            membre_familles.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "MembreFamille deleted"}, 204


class MembreFamilleResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on MembreFamilleResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        membre_familles = MembreFamille.find_all(page, size)
        if membre_familles is not None:
            return membre_familles_list_schema.dump(membre_familles), 200
        return {"message": "MembreFamille not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on MembreFamilleResourceList")
        membre_familles_json = request.get_json()
        try:
            membre_familles_data = membre_familles_schema.load(
                membre_familles_json, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            membre_familles_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return membre_familles_schema.dump(membre_familles_data), 201


class MembreFamilleResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on MembreFamilleResourceListCount")
        membre_familles_count = MembreFamille.find_all_count()
        if membre_familles_count is not None:
            return membre_familles_count, 200
        return {"message": "MembreFamille count not found"}, 404
