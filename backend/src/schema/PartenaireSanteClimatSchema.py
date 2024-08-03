from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.PartenaireSanteClimat import PartenaireSanteClimat


class PartenaireSanteClimatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PartenaireSanteClimat
        load_instance = True
        sqla_session = db.session
