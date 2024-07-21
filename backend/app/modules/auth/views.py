from flask import Blueprint
from flask_pydantic import validate

from app.extensions.db import db
from app.modules.auth.dtos import AuthSignInBody, AuthSignInResponse
from app.modules.auth.services import AuthService
from app.modules.users.adapters import UserRepositoryAdapter
from app.modules.users.models import User
from app.modules.users.use_cases import UserSignUp

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["POST"])
@validate()
def login(body: AuthSignInBody) -> AuthSignInResponse:
    try:
        user_repository = UserRepositoryAdapter(db.session, User)
        auth_service = AuthService()
        res = UserSignUp(
            auth_service=auth_service, user_repository=user_repository
        ).execute(email=body.email, password=body.password)
        return AuthSignInResponse(**res)
    except Exception as e:
        raise e
