from app.modules.auth.ports import AuthPort


class AuthService:

    def __init__(self, auth: AuthPort):
        self.auth = auth

    def authenticate(self, user_id: int, email: str) -> dict:
        access = {
            "access_token": self.auth.create_access_token(
                identity=user_id, additional_claims={"email": email}, fresh=False
            ),
            "refresh_token": self.auth.create_refresh_token(
                identity=user_id, additional_claims={"email": email}
            ),
        }
        return access
