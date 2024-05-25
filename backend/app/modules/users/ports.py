from app.modules.shared.crud_base import CRUDBase
from app.modules.users.models import User


class UserRepositoryPort(CRUDBase[User]):
    pass
