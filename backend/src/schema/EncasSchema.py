from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.Encas import Encas 


class EncasSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Encas
        load_instance = True
        sqla_session = db.session