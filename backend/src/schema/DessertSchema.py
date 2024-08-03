from marshmallow_sqlalchemy import auto_field, fields
from src.WebSerializer import ma
from src.DatabaseConfig import db
from src.domain.Dessert import Dessert 


class DessertSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dessert
        load_instance = True
        sqla_session = db.session