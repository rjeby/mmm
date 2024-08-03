from flask import request
import logging
import json
from flask_restx import Resource, Namespace, fields
from src.domain.User import User
from src.utils.SecurityUtils import has_role
from src.domain.User import Roles
from src.schema.UserSchema import UserSchema
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import jwt_required
from marshmallow.exceptions import ValidationError

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")
users_list_ns = Namespace("users-resource", path="/api/users")

users_schema = UserSchema()
users_list_schema = UserSchema(many=True)


class UserResource(Resource):

    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self, id):
        logging.info("GET request received on UserResource")
        users = User.find_by_id(id)
        if users is not None:
            return users_schema.dump(users), 200
        return {"message": "User not found"}, 404


class UserResourceList(Resource):

    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on UserResourceList")
        page = request.args.get("page", default=1, type=int)
        size = request.args.get("size", default=20, type=int)
        users = User.find_all(page, size)
        if users is not None:
            return users_list_schema.dump(users), 200
        return {"message": "User not found"}, 404


class UserResourceListCount(Resource):

    @jwt_required()
    @has_role(Roles.ADMIN)
    def get(self):
        logging.info("GET request received on UserResourceListCount")
        users_count = User.find_all_count()
        if users_count is not None:
            return users_count, 200
        return {"message": "User count not found"}, 404
