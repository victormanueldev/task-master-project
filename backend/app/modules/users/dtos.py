from typing import Optional

from pydantic import BaseModel

from app.modules.users.models import User


class UserBaseDTO(BaseModel):
    id: Optional[int]
    name: str
    email: str
    password: Optional[str] = None


class UserLoggedInDTO(BaseModel):
    access_token: str
    refresh_token: str
    user: User
