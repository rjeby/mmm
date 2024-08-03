from flask_jwt_extended import get_jwt_identity
from functools import wraps
from flask import jsonify
from src.domain.User import User


def confirmed_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        email = get_jwt_identity()
        user = User.find_by_email(email)
        if not user.is_confirmed:
            return jsonify({"message": "Please confirm your account!"}), 403
        return fn(*args, **kwargs)

    return wrapper
