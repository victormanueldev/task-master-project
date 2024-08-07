from flask import Response
from pydantic import ValidationError

from app.modules.shared.error_schema import Status, ErrorSchema


class ErrorBase(Exception):
    """
    This class is responsible to handle all errors presented in the API.
    In the handler method, we serialize the errors and respond the request with
    the expected format and the corresponding status code.
    """

    def __init__(
        self, status: str, status_code: int, message: str, details: dict
    ) -> None:
        self.status_code = status_code
        self.status = status
        self.message = message
        self.details = details

    def handler(self) -> Response:
        """
        Serialize the error and respond the request with the corresponding
        flask response format.
        """
        try:
            error_json = ErrorSchema(
                status=self.status,
                status_code=self.status_code,
                message=self.message,
                details=self.details,
            ).model_dump_json()
            return Response(error_json, self.status_code)
        except ValidationError as e:
            # In case of error in the error serialization
            return Response(
                dict(
                    status=Status.UNPROCESSABLE.name,
                    status_code=Status.UNPROCESSABLE.value,
                    message=e.title,
                    details={
                        "reason": "INVALID_ERROR_SCHEMA",
                        "domain": "App errors",
                        "metadata": e.errors,
                    },
                ),
                422,
            )
        except Exception as e:
            # In the case of unexpected issue in the error serialization
            return Response(
                dict(
                    status=Status.INTERNAL_ERROR.name,
                    status_code=Status.INTERNAL_ERROR.value,
                    message=str(e),
                    details={
                        "reason": "UNKNOWN_ERROR_SCHEMA",
                        "domain": "App errors",
                        "metadata": [],
                    },
                ),
                500,
            )


def error_handler(e: ErrorBase) -> Response:
    return e.handler()
