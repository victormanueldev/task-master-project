import os
from logging.config import dictConfig

from flask import Flask

from app.config import ENV_CONFIGS
from app.extensions.bcrypt import bcrypt
from app.extensions.db import db
from app.extensions.jwt import jwt
from app.modules.auth.views import auth


def create_app():
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                }
            },
            "root": {
                "level": "INFO" if os.environ.get("DEBUG") else "DEBUG",
                "handlers": ["wsgi"],
            },
        }
    )

    app = Flask(__name__)

    # determine environment:

    # If you don't set the ENVIRONMENT env variable, or if you set it to an invalid
    # value,the app is going to run in production environment.
    environment = os.environ.get("ENVIRONMENT", default="production")
    config_obj = ENV_CONFIGS.get(environment) or ENV_CONFIGS["production"]
    app.config.from_object(config_obj)

    # Initialize extensions:
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Register blueprints:
    app.register_blueprint(auth, url_prefix="/api/v1/auth")

    return app
