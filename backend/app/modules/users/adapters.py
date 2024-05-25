from typing import Any, Type

from sqlalchemy.orm import Session

from app.modules.users.models import User
from app.modules.users.ports import UserRepositoryPort


class UserRepositoryAdapter(UserRepositoryPort):

    def __init__(self, db: Session, model: Type[User]):
        super().__init__(model)
        self.db = db

    def filter_by(self, field: str, value: Any) -> Type[User]:
        return self.db.query(self.model).filter_by(email=value).first()
