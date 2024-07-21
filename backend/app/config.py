import os
from typing import TypedDict, Type

from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv()


class Config(object):
    ENV: str = "production"
    DEBUG: bool = False
    TESTING: bool = False
    STD_ERROR_MSG: str = os.environ.get(
        "STD_ERROR_MSG", "Internal server error. Please contact support."
    )

    # SQLAlchemy:
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    SQL_USER: str = os.environ.get("SQL_USER")
    SQL_PASSWORD: str = os.environ.get("SQL_PASSWORD")
    SQL_PORT: str = os.environ.get("SQL_PORT")
    SQL_HOST: str = os.environ.get("SQL_HOST")
    SQL_DATABASE: str = os.environ.get("SQL_DATABASE")
    SQLALCHEMY_DATABASE_URI: str = (
        f"postgresql+psycopg2://{SQL_USER}:{SQL_PASSWORD}@{SQL_HOST}:{SQL_PORT}/{SQL_DATABASE}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    FLASK_PYDANTIC_VALIDATION_ERROR_STATUS_CODE: int = 422


class DevelopmentConfig(Config):
    ENV: str = "development"
    DEBUG: bool = True
    TESTING: bool = False


class TestingConfig(Config):
    ENV: str = "testing"
    DEBUG: bool = True
    TESTING: bool = True


class EnvConfigs(TypedDict):
    development: Type[Config]
    testing: Type[Config]
    production: Type[Config]


ENV_CONFIGS: EnvConfigs = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": Config,
}
