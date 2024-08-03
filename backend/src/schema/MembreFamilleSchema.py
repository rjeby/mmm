from marshmallow_sqlalchemy import auto_field, fields
from src.domain.MembreFamille import MembreFamille
from src.DatabaseConfig import db
from src.WebSerializer import ma


class MembreFamilleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MembreFamille
        load_instance = True
        sqla_session = db.session
