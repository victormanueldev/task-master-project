from flask_jwt_extended import create_access_token, create_refresh_token

from app.modules.auth.ports import AuthPort


class AuthJWTAdapter(AuthPort):

    def create_access_token(self, identity, fresh, additional_claims) -> str:
        return create_access_token(
            identity=identity, additional_claims=additional_claims, fresh=fresh
        )

    def create_refresh_token(self, identity, additional_claims) -> str:
        return create_refresh_token(
            identity=identity, additional_claims=additional_claims
        )
