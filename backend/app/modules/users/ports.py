from typing import Optional

from app.modules.shared.crud_base import CRUDBase
from app.modules.users.models import User


class UserRepositoryPort(CRUDBase[User]):

    def get_by_email(self, email: str) -> Optional[User]:
        pass
