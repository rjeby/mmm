from flask import Flask
from flask_restx import Api
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from src.rest import add_api_namespace
from src.config import config
from src.DatabaseConfig import db
from src.WebSerializer import ma
from src.utils.MailConfiguration import mail
from src.utils.DataLoader import load_data


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})
api = add_api_namespace(Api(doc="/api-docs"))
jwt = JWTManager(app)


def create_app(app):
    app.config.from_object(config["development"])
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    with app.app_context():
        # db.drop_all() # Droping DB in dev mode (don't use this in production mode)
        db.create_all()
        load_data(app)
    return app


if __name__ == "__main__":
    create_app(app)
    app.run(host="0.0.0.0", port=5000)
