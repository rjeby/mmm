from marshmallow_sqlalchemy import auto_field, fields
from src.domain.Ciqual import Ciqual
from src.DatabaseConfig import db
from src.WebSerializer import ma


class CiqualSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Ciqual
        load_instance = True
        sqla_session = db.session
        exclude = (
            "alim_grp_code",
            "alim_ssgrp_code",
            "alim_ssssgrp_code",
            "rayon",
            "energieKj",
            "energieKcal",
            "fibres",
            "calcium",
            "cuivre",
            "fer",
            "iode",
            "magnesium",
            "manganese",
            "phosphore",
            "potassium",
            "selenium",
            "sodium",
            "zinc",
            "vitamineA",
            "vitamineD",
            "vitamineE",
            "vitamineK1",
            "vitamineC",
            "vitamineB1",
            "vitamineB2",
            "vitamineB3",
            "vitamineB5",
            "vitamineB6",
            "vitamineB9",
            "vitamineB12",
        )
