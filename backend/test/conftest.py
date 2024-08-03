import pytest
from flask import Flask
from flask_restx import Api
from src.config import config
from src.rest import add_api_namespace
from src.utils.DataLoader import load_data
from src.DatabaseConfig import db
from src.WebSerializer import ma
from src.utils.MailConfiguration import mail
from flask_jwt_extended import JWTManager, create_access_token


@pytest.fixture(scope='session')
def test_client():
    app = Flask(__name__)
    api = add_api_namespace(Api())
    jwt = JWTManager(app)
    app.config.from_object(config["testing"])
    api.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    with app.test_client() as testing_client:
      with app.app_context():
        db.drop_all()
        db.create_all()
        load_data(app)
        yield testing_client
