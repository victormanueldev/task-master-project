from werkzeug.exceptions import UnprocessableEntity, Unauthorized

from app.modules.shared.error_class import ErrorBase
from app.modules.shared.error_schema import Status


class InternalError(ErrorBase):
    def __init__(self, message: str, details: dict):
        super().__init__(
            status=Status.INTERNAL_ERROR.name,
            status_code=Status.INTERNAL_ERROR.value,
            message=message,
            details=details,
        )


class UnprocessableEntityError(ErrorBase, UnprocessableEntity):
    def __init__(self, message: str, details: dict):
        super().__init__(
            status=Status.UNPROCESSABLE.name,
            status_code=Status.UNPROCESSABLE.value,
            message=message,
            details=details,
        )


class UnauthorizedError(ErrorBase, Unauthorized):
    def __init__(self, message: str, details: dict):
        super().__init__(
            status=Status.UNAUTHENTICATED.name,
            status_code=Status.UNAUTHENTICATED.value,
            message=message,
            details=details,
        )
