from typing import Optional, List

from sqlalchemy import ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import String, Integer

from app.extensions.bcrypt import bcrypt
from app.modules.shared.base_class import Base


class User(Base):
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    _password: Mapped[str] = mapped_column(String(128))
    tasks: Mapped[Optional[List["Task"]]] = relationship(
        "Task",
        back_populates="user",
        passive_deletes=True,
    )
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("role.id"))
    role: Mapped["Role"] = relationship("Role", passive_deletes=True)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = bcrypt.generate_password_hash(password)
