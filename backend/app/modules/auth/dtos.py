from pydantic import BaseModel


class AuthSignInBody(BaseModel):
    email: str
    password: str


class AuthSignInResponse(BaseModel):
    access_token: str
    refresh_token: str


class AuthSignOut(BaseModel):
    token: str
