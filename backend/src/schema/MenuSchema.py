from marshmallow_sqlalchemy import auto_field, fields
from src.domain.Menu import Menu
from src.DatabaseConfig import db
from src.WebSerializer import ma


class MenuSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Menu
        load_instance = True
        sqla_session = db.session
    entree_id = auto_field()
    plat_id = auto_field()
    dessert_id = auto_field()