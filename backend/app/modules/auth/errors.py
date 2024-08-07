from werkzeug.exceptions import Unauthorized

from app.modules.shared.error_class import ErrorBase
from app.modules.shared.error_schema import Status


class UnauthenticatedError(ErrorBase, Unauthorized):
    def __init__(self, message: str, details: dict) -> None:
        super().__init__(
            status=Status.UNAUTHENTICATED.name,
            status_code=Status.UNAUTHENTICATED.value,
            message=message,
            details=details,
        )
