import os


class Config:
    # General Config
    SECRET_KEY = os.environ.get(
        "SECRET_KEY",
        "29d85f555577db540eaf6aaeabe9a761f1a5f86271aaae7fb31475cba0df9682a50b98ea08d55feb2dc3beb2cca9b1527ee9",
    )
    SECURITY_PASSWORD_SALT = os.environ.get(
        "SECURITY_PASSWORD_SALT",
        "29d85f555577db540eaf6aaeabe9a761f1a5f86271aaae7fb31475cba0df9682a50b98ea08d55feb2dc3beb2cca9b1527ee9",
    )
    JWT_SECRET_KEY = os.environ.get(
        "JWT_SECRET_KEY",
        "MTAwOWNhNTM1YTUxNGUxYTBmNGZkM2RmYzdiZTQ1OTlmZDc0ZjdjZDIwYWJiM2RiM2I0OGE3MGRlMjhiMzVjZWMyMjYxYjAyYzgzZTQzODI2MTUwODA0NzBlZWExMWFjYmU1MmUwNzJlODcxOTNkY2E4MjBhYjNiYTU5OGM3ZDY=",
    )
    JWT_ALGORITHM = os.environ.get("JWT_ALGORITHM", "HS512")

    DEBUG = False
    TESTING = False

    # Database Config
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail Config
    MAIL_DEFAULT_SENDER = "noreply@mmmmenus.com"
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = False
    MAIL_USERNAME = "mmm.backend.2025@gmail.com"
    MAIL_PASSWORD = "ocdz zour kopq bsdm "

    # Cache Config


class DevelopmentConfig(Config):
    DEBUG = True
    FLASK_ENV = "development"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DEV_DATABASE_URL", "sqlite:///development.db"
    )


class TestingConfig(Config):
    TESTING = True
    FLASK_ENV = "testing"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "TEST_DATABASE_URL", "sqlite:///testing.db"
    )


class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    FLASK_ENV = "production"
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://postgres:password@database:5432/postgres"
    )


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
