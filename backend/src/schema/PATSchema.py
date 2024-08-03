from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.PAT import PAT


class PATSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PAT
        load_instance = True
        sqla_session = db.session
