from flask import request
import logging
import json
from flask_restx import Resource, Namespace
from src.domain.Menu import Menu
from src.schema.MenuSchema import MenuSchema
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from flask_jwt_extended import jwt_required
from sqlalchemy.exc import SQLAlchemyError
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
menus_list_ns = Namespace("menus-resource", path="/api/menus")

menus_schema = MenuSchema()
menus_list_schema = MenuSchema(many=True)


class MenuResource(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on MenuResource")
        menus = Menu.find_by_id(id)
        if menus is not None:
            return menus_schema.dump(menus), 200
        return {"message": "Menu not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def put(self, id):
        logging.info("PUT request received on MenuResource")
        menus_json = request.get_json()
        if menus_json["id"] is None:
            return {"message": "Invalid Menu"}, 400
        if id != menus_json["id"]:
            return {"message": "Invalid Menu"}, 400
        menus = Menu.find_by_id(id)
        if menus.get_id() is None:
            return {"message": "Invalid Menu"}, 400
        try:
            updated_menus = menus_schema.load(
                menus_json, instance=menus, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_menus.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return menus_schema.dump(updated_menus), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def patch(self, id):
        logging.info("PATCH request received on MenuResource")
        menus_json = request.get_json()
        if menus_json["id"] is None:
            return {"message": "Invalid Menu"}, 400
        if id != menus_json["id"]:
            return {"message": "Invalid Menu"}, 400
        menus = Menu.find_by_id(id)
        if menus.get_id() is None:
            return {"message": "Invalid Menu"}, 400
        try:
            updated_menus = menus_schema.load(
                menus_json, instance=menus, partial=True
            )
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            updated_menus.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return menus_schema.dump(updated_menus), 200

    @jwt_required()
    @has_role(Roles.ADMIN)
    def delete(self, id):
        logging.info("DELETE request received on MenuResource")
        menus = Menu.find_by_id(id)
        if menus is None:
            return {"message": "Menu not found"}, 404
        try:
            menus.delete_from_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Menu deleted"}, 204


class MenuResourceList(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on MenuResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        menus = Menu.find_all(page, size)
        if menus is not None:
            return menus_list_schema.dump(menus), 200
        return {"message": "Menu not found"}, 404

    @jwt_required()
    @has_role(Roles.ADMIN)
    def post(self):
        logging.info("POST request received on MenuResourceList")
        menus_json = request.get_json()
        try:
            menus_data = menus_schema.load(menus_json, partial=True)
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        try:
            menus_data.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return menus_schema.dump(menus_data), 201


class MenuResourceListCount(Resource):
    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on MenuResourceListCount")
        menus_count = Menu.find_all_count()
        if menus_count is not None:
            return menus_count, 200
        return {"message": "Menu count not found"}, 404
