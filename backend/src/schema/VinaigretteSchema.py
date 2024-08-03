from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.Vinaigrette import Vinaigrette


class VinaigretteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vinaigrette
        load_instance = True
        sqla_session = db.session