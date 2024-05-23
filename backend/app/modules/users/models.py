from typing import Optional, List
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base_class import Base
from app.modules.tasks.models import Task


class User(Base):
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(128))
    tasks: Mapped[Optional[List["Task"]]] = relationship(
        back_populates="assignee", passive_deletes=True
    )
