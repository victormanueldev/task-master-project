from app.modules.auth.services import AuthService
from app.modules.users.ports import UserRepositoryPort


class UserSignUp:

    def __init__(self, auth_service: AuthService, user_repository: UserRepositoryPort):
        self.auth_service = auth_service
        self.user_repository = user_repository

    def execute(self, user_data: dict) -> dict:
        if self.auth_service.authenticate(
            username=user_data.get("email", ""), password=user_data.get("password", "")
        ):
            user = self.user_repository.filter_by(
                field="email", value=user_data.get("email")
            )
            return dict(
                access_token="access_token_generated_str",
                refresh_token="refresh_token_generated_str",
                user=user,
            )
