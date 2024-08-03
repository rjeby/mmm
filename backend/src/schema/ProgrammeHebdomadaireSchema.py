from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.ProgrammeHebdomadaire import ProgrammeHebdomadaire
from src.schema.MenuSchema import MenuSchema


class ProgrammeHebdomadaireSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ProgrammeHebdomadaire
        load_instance = True
        sqla_session = db.session

    # Fields representing relationships must be added to Schema
    id = auto_field()
    vinaigrette_semaine_id = auto_field()
    petit_dejeuner_0_id = auto_field()
    petit_dejeuner_0_count = auto_field()
    petit_dejeuner_1_id = auto_field()
    petit_dejeuner_1_count = auto_field()
    lundi_encas_id = auto_field()
    lundi_dejeuner = fields.Nested(MenuSchema)
    lundi_diner = fields.Nested(MenuSchema)
    mardi_encas_id = auto_field()
    mardi_dejeuner = fields.Nested(MenuSchema)
    mardi_diner = fields.Nested(MenuSchema)
    mercredi_encas_id = auto_field()
    mercredi_dejeuner = fields.Nested(MenuSchema)
    mercredi_diner = fields.Nested(MenuSchema)
    jeudi_encas_id = auto_field()
    jeudi_dejeuner = fields.Nested(MenuSchema)
    jeudi_diner = fields.Nested(MenuSchema)
    vendredi_encas_id = auto_field()
    vendredi_dejeuner = fields.Nested(MenuSchema)
    vendredi_diner = fields.Nested(MenuSchema)
    samedi_encas_id = auto_field()
    samedi_dejeuner = fields.Nested(MenuSchema)
    samedi_diner = fields.Nested(MenuSchema)
    dimanche_encas_id = auto_field()
    dimanche_dejeuner = fields.Nested(MenuSchema)
    dimanche_diner = fields.Nested(MenuSchema)