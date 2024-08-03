from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.Preferences import Preferences


class PreferencesSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Preferences
        load_instance = True
        sqla_session = db.session
        exclude = (
            "id",
        )

    # Fields representing relationships must be added to Schema
    ingredients_exclus = fields.Nested("CiqualSchema", many=True, required=False)