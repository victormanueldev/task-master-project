from typing import Tuple

from flask import Blueprint
from flask_pydantic import validate

from app.decorators import serialize_response
from app.dependecy_container import context
from app.modules.auth.dtos import AuthSignInBody, AuthSignInResponse
from app.modules.users.use_cases import UserSignUp

auth = Blueprint("auth", __name__)
user_repository = context.user_repository
auth_service = context.auth_service


@auth.route("/login", methods=["POST"])
@validate()
@serialize_response(AuthSignInResponse)
def login(body: AuthSignInBody) -> Tuple[dict, int]:
    res = UserSignUp(
        auth_service=auth_service, user_repository=user_repository
    ).execute(email=body.email, password=body.password)
    return res, 200
