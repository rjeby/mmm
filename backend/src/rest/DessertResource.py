from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.domain.Dessert import Dessert
from src.schema.DessertSchema import DessertSchema
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
desserts_list_ns = Namespace("desserts-resource", path="/api/desserts")

desserts_schema = DessertSchema()
desserts_list_schema = DessertSchema(many=True)


class DessertResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on DessertResource")
        desserts = Dessert.find_by_id(id)
        if desserts is not None:
            return desserts_schema.dump(desserts), 200
        return {"message": "Dessert not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on DessertResource")
        desserts_json = request.get_json()
        if desserts_json["id"] is None:
            return {"message": "Invalid Dessert"}, 400
        if id != desserts_json["id"]:
            return {"message": "Invalid Dessert"}, 400
        desserts = Dessert.find_by_id(id)
        if desserts.get_id() is None:
            return {"message": "Invalid Dessert"}, 400
        try:
            updated_desserts = desserts_schema.load(
                desserts_json, instance=desserts, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_desserts.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return desserts_schema.dump(updated_desserts), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on DessertResource")
        desserts_json = request.get_json()
        if desserts_json["id"] is None:
            return {"message": "Invalid Dessert"}, 400
        if id != desserts_json["id"]:
            return {"message": "Invalid Dessert"}, 400
        desserts = Dessert.find_by_id(id)
        if desserts.get_id() is None:
            return {"message": "Invalid Dessert"}, 400
        try:
            updated_desserts = desserts_schema.load(
                desserts_json, instance=desserts, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_desserts.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return desserts_schema.dump(updated_desserts), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on DessertResource")
        desserts = Dessert.find_by_id(id)
        if desserts is None:
            return {"message": "Dessert not found"}, 404
        try:
            desserts.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Dessert deleted"}, 204


class DessertResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on DessertResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        desserts = Dessert.find_all(page, size)
        if desserts is not None:
            return desserts_list_schema.dump(desserts), 200
        return {"message": "Dessert not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on DessertResourceList")
        desserts_json = request.get_json()
        try:
            desserts_data = desserts_schema.load(desserts_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            desserts_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return desserts_schema.dump(desserts_data), 201


class DessertResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on DessertResourceListCount")
        desserts_count = Dessert.find_all_count()
        if desserts_count is not None:
            return desserts_count, 200
        return {"message": "Dessert count not found"}, 404
