from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.PetitDejeuner import PetitDejeuner 


class PetitDejeunerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PetitDejeuner
        load_instance = True
        sqla_session = db.session