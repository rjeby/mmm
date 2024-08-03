from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.domain.PartenaireSanteClimat import PartenaireSanteClimat
from src.schema.PartenaireSanteClimatSchema import PartenaireSanteClimatSchema
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
partenaire_sante_climats_list_ns = Namespace(
    "partenaire-sante-climats-resource", path="/api/partenaire-sante-climats"
)

partenaire_sante_climats_schema = PartenaireSanteClimatSchema()
partenaire_sante_climats_list_schema = PartenaireSanteClimatSchema(many=True)


class PartenaireSanteClimatResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on PartenaireSanteClimatResource")
        partenaire_sante_climats = PartenaireSanteClimat.find_by_id(id)
        if partenaire_sante_climats is not None:
            return partenaire_sante_climats_schema.dump(partenaire_sante_climats), 200
        return {"message": "PartenaireSanteClimat not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on PartenaireSanteClimatResource")
        partenaire_sante_climats_json = request.get_json()
        if partenaire_sante_climats_json["id"] is None:
            return {"message": "Invalid PartenaireSanteClimat"}, 400
        if id != partenaire_sante_climats_json["id"]:
            return {"message": "Invalid PartenaireSanteClimat"}, 400
        partenaire_sante_climats = PartenaireSanteClimat.find_by_id(id)
        if partenaire_sante_climats.get_id() is None:
            return {"message": "Invalid PartenaireSanteClimat"}, 400
        try:
            updated_partenaire_sante_climats = partenaire_sante_climats_schema.load(
                partenaire_sante_climats_json,
                instance=partenaire_sante_climats,
                partial=True,
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_partenaire_sante_climats.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return (
            partenaire_sante_climats_schema.dump(updated_partenaire_sante_climats),
            200,
        )

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on PartenaireSanteClimatResource")
        partenaire_sante_climats_json = request.get_json()
        if partenaire_sante_climats_json["id"] is None:
            return {"message": "Invalid PartenaireSanteClimat"}, 400
        if id != partenaire_sante_climats_json["id"]:
            return {"message": "Invalid PartenaireSanteClimat"}, 400
        partenaire_sante_climats = PartenaireSanteClimat.find_by_id(id)
        if partenaire_sante_climats.get_id() is None:
            return {"message": "Invalid PartenaireSanteClimat"}, 400
        try:
            updated_partenaire_sante_climats = partenaire_sante_climats_schema.load(
                partenaire_sante_climats_json,
                instance=partenaire_sante_climats,
                partial=True,
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_partenaire_sante_climats.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return (
            partenaire_sante_climats_schema.dump(updated_partenaire_sante_climats),
            200,
        )

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on PartenaireSanteClimatResource")
        partenaire_sante_climats = PartenaireSanteClimat.find_by_id(id)
        if partenaire_sante_climats is None:
            return {"message": "PartenaireSanteClimat not found"}, 404
        try:
            partenaire_sante_climats.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "PartenaireSanteClimat deleted"}, 204


class PartenaireSanteClimatResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PartenaireSanteClimatResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        partenaire_sante_climats = PartenaireSanteClimat.find_all(page, size)
        if partenaire_sante_climats is not None:
            return (
                partenaire_sante_climats_list_schema.dump(partenaire_sante_climats),
                200,
            )
        return {"message": "PartenaireSanteClimat not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on PartenaireSanteClimatResourceList")
        partenaire_sante_climats_json = request.get_json()
        try:
            partenaire_sante_climats_data = partenaire_sante_climats_schema.load(
                partenaire_sante_climats_json, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            partenaire_sante_climats_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return partenaire_sante_climats_schema.dump(partenaire_sante_climats_data), 201


class PartenaireSanteClimatResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on PartenaireSanteClimatResourceListCount")
        partenaire_sante_climats_count = PartenaireSanteClimat.find_all_count()
        if partenaire_sante_climats_count is not None:
            return partenaire_sante_climats_count, 200
        return {"message": "PartenaireSanteClimat count not found"}, 404
