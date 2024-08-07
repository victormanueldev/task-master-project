from enum import Enum
from typing import List, Any

from pydantic import BaseModel


class Status(int, Enum):
    CANCELLED = 499
    INTERNAL_ERROR = 500
    INVALID_ARGUMENT = 400
    DEADLINE_EXCEEDED = 504
    NOT_FOUND = 404
    ALREADY_EXISTS = 409
    PERMISSION_DENIED = 403
    UNAUTHENTICATED = 401
    RESOURCE_EXHAUSTED = 429
    UNAVAILABLE = 503
    UNIMPLEMENTED = 501
    UNPROCESSABLE = 422


class ErrorDetails(BaseModel):
    reason: str
    domain: str
    metadata: List[Any]


class ErrorSchema(BaseModel):
    status_code: int
    message: str
    status: str
    details: ErrorDetails
