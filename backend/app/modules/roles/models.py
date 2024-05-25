from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import String, Integer

from app.modules.shared.base_class import Base


class Permission(Base):
    name: Mapped[str] = mapped_column(String(20))
    role_id: Mapped[int] = mapped_column(Integer, ForeignKey("role.id"))
    role: Mapped["Role"] = relationship("Role", back_populates="permissions")


class Role(Base):
    name: Mapped[str] = mapped_column(String(30))
    permissions: Mapped[List[Permission]] = relationship(
        "Permission", passive_deletes=True
    )
