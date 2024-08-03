from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.Plat import Plat 


class PlatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Plat
        load_instance = True
        sqla_session = db.session