from typing import Any, Type, List, Optional

from sqlalchemy.orm import Session

from app.modules.shared.crud_base import ModelType
from app.modules.users.models import User
from app.modules.users.ports import UserRepositoryPort


class UserRepositoryAdapter(UserRepositoryPort):

    def __init__(self, db: Session, model: Type[User]):
        super().__init__(model)
        self.db = db

    def filter_by(self, field: str, value: Any) -> List[Type[User]]:
        return self.db.query(self.model).filter_by(email=value).all()

    def get_by_email(self, email: str) -> Optional[Type[User]]:
        return self.db.query(self.model).filter_by(email=email).one_or_none()

    def create(self, obj: ModelType) -> ModelType:
        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj
