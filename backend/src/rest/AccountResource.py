from flask import Flask, request, jsonify, render_template, make_response
from flask_restx import Resource, Namespace, fields
from flask_jwt_extended import create_access_token
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from sqlalchemy.exc import SQLAlchemyError
from src.utils.MailConfiguration import (
    send_activation_mail,
    confirm_token,
    send_reset_mail,
)
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from datetime import timedelta
import json
import bcrypt
import logging
import re
from src.domain.User import Roles
from src.domain.User import User
from src.schema.UserSchema import UserSchema

from flask import url_for

logging.basicConfig(format="%(asctime)s - %(message)s", datefmt="%d-%b-%y %H:%M:%S")


def valid_password(password):
    """
    Validate the password with the following rules:
    - At least one digit
    - At least one uppercase letter
    - At least one lowercase letter
    - At least one special character
    - Minimum length of 8 characters
    """
    pattern = re.compile(
        r"^(?=.*\d)(?=.*[A-Z])(?=.*[a-z])(?=.*[!@#$%^&*])[\w!@#$%^&*]{8,}$"
    )
    return bool(pattern.match(password))


def valid_email(email):
    """
    Validate the email address using a regular expression pattern.
    """
    pattern = re.compile(r"^[^\s@]+@[^\s@]+\.[^\s@]+$", re.IGNORECASE)
    return bool(pattern.match(email))


account_register_ns = Namespace("account-resource", path="/api/register")
user_schema = UserSchema()

user_model = account_register_ns.model(
    "register",
    {
        "email": fields.String(required=True, description="User's email"),
        "password": fields.String(required=True, description="User's password"),
    },
)


# Resource for user registration
class UserRegister(Resource):
    @account_register_ns.expect(user_model)
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # Check if the email is already in use
        if User.find_by_email(email):
            return {"message": "L'utilisateur existe déjà"}, 400

        # Validate the password
        if not valid_email(email):
            return {"message": "L'email ne répond pas aux critères requis"}, 400

        # Validate the password
        if not valid_password(password):
            return {"message": "Le mot de passe ne répond pas aux critères requis"}, 400

        # Hash the password with bcrypt
        data["password"] = bcrypt.hashpw(
            password.encode("utf-8"), bcrypt.gensalt()
        ).decode("utf-8")

        # Create and save the new user
        try:
            new_user = user_schema.load(data, partial=True)
            new_user.role = Roles.USER
        except ValidationError as err:
            return {"message": json.dumps(err.messages)}, 400
        # The user record is inserted into the database
        try:
            new_user.save_to_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        # Send registration mail
        try:
            send_activation_mail(new_user)
        except Exception as e:
            return {
                "message": "L'utilisateur est créé mais impossible d'envoyer le mail"
            }, 500
        
        # Returning JWT token to connect the user immediatly after registering
        role = {"role": new_user.role}
        access_token = "Bearer " + create_access_token(
            identity=new_user.email,
            expires_delta=timedelta(hours=8766),
            additional_claims=role,
        )
        return {
            "access_token": access_token,
            "is_confirmed": new_user.is_confirmed,
            "has_infos": new_user.has_infos,
            "role": new_user.role,
        }, 201

account_confirm_ns = Namespace("account-resource", path="/api/confirm")


class ConfirmEmail(Resource):

    def get(self, token):
        try:
            email = confirm_token(token)
        except:
            return {"message": "Le lien de confirmation est invalide ou a expiré"}, 400

        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404

        if user.is_confirmed:
            headers = {"Content-Type": "text/html"}
            return make_response(render_template("activated.html"), 200, headers)

        user.is_confirmed = True
        try:
            user.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        headers = {"Content-Type": "text/html"}
        return make_response(render_template("activated.html"), 200, headers)


account_resend_ns = Namespace("account-resource", path="/api/resend")


class ResendEmail(Resource):
    @jwt_required()
    def get(self):
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        if user.is_confirmed:
            return {"message": "Votre compte est déjà activé"}, 400
        try:
            send_activation_mail(user)
        except Exception as e:
            return {"message": "Impossible d'envoyer le mail"}, 200

        return {"message": "Un nouvel email de confirmation a été envoyé"}, 200


account_login_ns = Namespace("account-resource", path="/api/login")


# Resource for user login
class UserLogin(Resource):

    @account_login_ns.expect(user_model)
    def post(self):
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        # Check if any of the inputs is empty
        if email is None or password is None:
            return {
                "message": "L'email et/ou le mot de passe ne peuvent pas être vides"
            }, 400

        # Check if user exists
        try:
            user = User.find_by_email(email)
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400

        if not user or not bcrypt.checkpw(
            password.encode("utf-8"), user.password.encode("utf-8")
        ):
            return {"message": "Identifiants invalides"}, 401

        role = {"role": user.role}
        access_token = "Bearer " + create_access_token(
            identity=user.email,
            expires_delta=timedelta(hours=8766),
            additional_claims=role,
        )
        return {
            "access_token": access_token,
            "is_confirmed": user.is_confirmed,
            "has_infos": user.has_infos,
            "role": user.role,
        }, 200


account_forgot_password_ns = Namespace("account-resource", path="/api/forgot-password")


class ForgotPassword(Resource):

    def post(self):
        data = request.get_json()
        email = data.get("email")

        if not email:
            return {
                "message": "L'email est requis pour réinitialiser le mot de passe"
            }, 400

        # Check if user exists
        try:
            user = User.find_by_email(email)
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400

        if not user:
            return {"message": "Utilisateur non trouvé"}, 404

        try:
            send_reset_mail(user)
        except Exception as e:
            return {
                "message": "L'utilisateur est créé mais impossible d'envoyer le mail"
            }, 500

        return {
            "message": "Un email de réinitialisation de mot de passe a été envoyé"
        }, 200


account_reset_password_ns = Namespace("account-resource", path="/api/reset-password")


class ResetPassword(Resource):
    def get(self, token):
        try:
            email = confirm_token(token)
        except:
            return {
                "message": "Le lien de réinitialisation du mot de passe est invalide ou a expiré"
            }, 400

        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404

        headers = {"Content-Type": "text/html"}
        return make_response(render_template("resetPassword.html"), 200, headers)

    def post(self, token):
        data = request.get_json()
        password = data["password"]
        try:
            email = confirm_token(token)
        except:
            return {
                "message": "Le lien de réinitialisation du mot de passe est invalide ou a expiré"
            }, 400

        user = User.find_by_email(email)
        if not user:
            return {"message": "Utilisateur non trouvé"}, 404
        # Validate the password
        if not valid_password(password):
            return {"message": "Le mot de passe ne répond pas aux critères requis"}, 400
        # Hash the password with bcrypt
        password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode(
            "utf-8"
        )
        try:
            user.password = password
            user.update_db()
        except SQLAlchemyError as e:
            return {"message": str(e.__dict__["orig"])}, 400
        return {"message": "Mot de passe changé avec succès"}, 201
