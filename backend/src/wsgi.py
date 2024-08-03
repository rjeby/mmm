""" Web Server Gateway Interface: app entry point """

from flask import Flask
from flask.cli import FlaskGroup
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from rest import add_api_namespace
from config import config
from src.DatabaseConfig import db
from src.WebSerializer import ma
from src.utils.MailConfiguration import mail
from src.utils.DataLoader import load_data


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://test.mmmenus.fr"]}})
api = add_api_namespace(Api(doc=False))
jwt = JWTManager(app)

app.config.from_object(config["production"])
api.init_app(app)
db.init_app(app)
ma.init_app(app)
mail.init_app(app)

cli = FlaskGroup(app)

@cli.command("create_db")
def create_db():
    with app.app_context():
        db.create_all()
        load_data(app)
    return app


if __name__ == "__main__":
    cli()
