from marshmallow_sqlalchemy import auto_field, fields
from src.domain.User import User
from src.DatabaseConfig import db
from src.WebSerializer import ma


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session
