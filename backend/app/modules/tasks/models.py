from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.sqltypes import String, Enum, DateTime, Integer

from app.modules.shared.base_class import Base


class TaskStatus(str, PyEnum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    REJECTED = "REJECTED"
    BLOCKED = "BLOCKED"
    OPEN = "OPEN"


class TaskType(str, PyEnum):
    DEBT = "DEBT"
    REQUEST = "REQUEST"
    BUG = "BUG"
    PRODUCT = "PRODUCT"


class Task(Base):
    description: Mapped[str] = mapped_column(String(200))
    status: Mapped[TaskStatus] = mapped_column(
        Enum(TaskStatus), default=TaskStatus.OPEN
    )
    type: Mapped[Optional[TaskType]] = mapped_column(Enum(TaskType))
    due_date: Mapped[DateTime] = mapped_column(DateTime)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey("user.id"))
    user: Mapped[Optional["User"]] = relationship(
        "User", back_populates="tasks", passive_deletes=True
    )
