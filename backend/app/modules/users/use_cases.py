from app.modules.auth.errors import UnauthenticatedError
from app.modules.auth.services import AuthService
from app.modules.users.models import User
from app.modules.users.ports import UserRepositoryPort


class UserSignUp:
    """
    This class will have the signup use case and define the execute method to be used in views
    """

    def __init__(self, auth_service: AuthService, user_repository: UserRepositoryPort):
        self.auth_service = auth_service
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> dict:
        user = self.user_repository.get_by_email(email)
        if user:
            if user.check_password(password):

                return self.auth_service.authenticate(user_id=user.id, email=email)
            else:
                raise UnauthenticatedError(
                    message="Unauthenticated user",
                    details={
                        "reason": "WRONG_PASSWORD",
                        "domain": "Auth",
                        "metadata": [{"resource": f"User {email}"}],
                    },
                )
        else:
            raise UnauthenticatedError(
                message="Unauthenticated user",
                details={
                    "reason": "USER_NOT_FOUND",
                    "domain": "Auth",
                    "metadata": [{"resource": f"User {email}"}],
                },
            )


class UserSignIn:

    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def execute(self, name: str, email: str, password: str, role_id: int) -> User:
        user = User(name=name, email=email, role_id=role_id)
        user.password = password
        self.user_repository.create(user)
        return user


class UserGetMe:

    def __init__(self, user_repository: UserRepositoryPort):
        self.user_repository = user_repository

    def execute(self, user_id: int) -> User:
        return self.user_repository.get_by_id(user_id)
