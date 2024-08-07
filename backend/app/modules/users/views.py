from typing import Tuple, Any

from flask import Blueprint
from flask_pydantic import validate

from app.decorators import login_required, serialize_response
from app.dependecy_container import context
from app.modules.users.dtos import UserSignUpDTO, UserGetMeDTO
from app.modules.users.use_cases import UserSignIn, UserGetMe

users = Blueprint("users", __name__, url_prefix="/users")
user_repository = context.user_repository
auth_service = context.auth_service


@users.route("/signup", methods=["POST"])
@validate()
@serialize_response(UserGetMeDTO)
def signup(body: UserSignUpDTO) -> Tuple[Any, int]:
    res = UserSignIn(user_repository).execute(
        name=body.name, email=body.email, password=body.password, role_id=body.role_id
    )
    return res, 201


@users.route("/me/<user_id>", methods=["GET"])
@login_required
@validate()
@serialize_response(UserGetMeDTO)
def get_me(user_id: int) -> Tuple[Any, int]:
    user = UserGetMe(user_repository).execute(user_id)
    return user, 200
