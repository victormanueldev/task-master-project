from typing import Optional

from pydantic import BaseModel, ConfigDict


class UserBaseDTO(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: Optional[int]
    name: str
    email: str
    password: Optional[str] = None


class UserLoggedInDTO(BaseModel):
    access_token: str
    refresh_token: str


class UserSignUpDTO(BaseModel):
    email: str
    password: str
    name: str
    role_id: int


class UserGetMeDTO(BaseModel):
    email: str
    name: str
    role_id: int
