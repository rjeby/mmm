from functools import wraps
from flask_jwt_extended import get_jwt, verify_jwt_in_request


def has_role(ROLE):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()
            if ROLE in claims["role"]:
                return fn(*args, **kwargs)
            else:
                return {"message": "You are not allowed to perform this operation"}, 405

        return decorator

    return wrapper
