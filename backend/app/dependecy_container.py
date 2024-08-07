import os
from collections import namedtuple
from logging.config import dictConfig

from flask import Flask

from app.config import ENV_CONFIGS
from app.extensions.db import db
from app.modules.auth.adapters import AuthJWTAdapter
from app.modules.auth.services import AuthService
from app.modules.roles.models import Role
from app.modules.tasks.models import Task
from app.modules.users.adapters import UserRepositoryAdapter
from app.modules.users.models import User

Context = namedtuple("Context", ["user_repository", "auth_service"])


def create_context() -> namedtuple:
    global context
    Task()
    Role()
    User()
    user_repository = UserRepositoryAdapter(db.session, User)
    jwt_adapter = AuthJWTAdapter()
    auth_service = AuthService(jwt_adapter)
    context = Context(user_repository, auth_service)
    __app = create_app()
    return context, __app


def create_app():
    global app
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

    _app = Flask(__name__)

    # determine environment:

    # If you don't set the ENVIRONMENT env variable, or if you set it to an invalid
    # value,the app is going to run in production environment.
    environment: str = os.environ.get("ENVIRONMENT", default="production")
    config_obj = ENV_CONFIGS.get(environment) or ENV_CONFIGS["production"]
    _app.config.from_object(config_obj)

    app = _app
    return _app


context = None
app = None
