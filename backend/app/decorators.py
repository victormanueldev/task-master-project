from functools import wraps
from typing import Callable, Type

from flask import g, Response
from pydantic import BaseModel, ValidationError

from app.errors import UnprocessableEntityError, UnauthorizedError


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if g.user is None:
                return f(*args, **kwargs)
        except AttributeError as e:
            raise UnauthorizedError(
                message="Unauthorized access",
                details={
                    "reason": "USER_NOT_AUTHENTICATED",
                    "domain": "Auth login required",
                    "metadata": [str(e)],
                },
            )

    return decorated_function


def serialize_response(schema: Type[BaseModel]) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            data, status_code = func(*args, **kwargs)
            try:
                if isinstance(data, dict):
                    json_dump = schema(**data).model_dump_json()
                else:
                    json_dump = schema(**data.__dict__).model_dump_json()
                return Response(json_dump, status_code)
            except ValidationError as e:
                raise UnprocessableEntityError(
                    message=str(e),
                    details={
                        "reason": "INVALID_ENTITY_ERROR_SCHEMA",
                        "domain": "Serialize response decorator",
                        "metadata": e.errors,
                    },
                )

        return wrapper

    return decorator
