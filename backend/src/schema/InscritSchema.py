from marshmallow_sqlalchemy import auto_field, fields
from src.domain.Inscrit import Inscrit
from src.DatabaseConfig import db
from src.WebSerializer import ma


class InscritSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Inscrit
        load_instance = True
        sqla_session = db.session

    # Fields representing relationships must be added to Schema
    membres_famille = fields.Nested("MembreFamilleSchema", many=True, required=False)
    preferences = fields.Nested("PreferencesSchema", required=False)

class InscritInfosResourceSchema(InscritSchema):
    # This Schema is used for InscritInfosResource to hide some InscritSchema fields
    class Meta:
        model = Inscrit
        load_instance = True
        sqla_session = db.session
        exclude = (
            "id",
            "membres_famille",
            "preferences"
        )

class InscritMenusResourceSchema(InscritSchema):
    # This Schema is used for InscritMenusResource to hide some InscritSchema fields
    class Meta:
        model = Inscrit
        load_instance = True
        sqla_session = db.session
        exclude = (
            "id",
            "code_postal"
        )