from enum import Enum as PyEnum
from typing import Optional

from sqlalchemy.sql.sqltypes import String, Enum, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.base_class import Base
from app.modules.users.models import User


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
    type: Mapped[TaskType] = mapped_column(Enum(TaskType))
    due_date: Mapped[DateTime] = mapped_column(DateTime)
    assignee: Mapped[Optional["User"]] = relationship(
        back_populates="tasks", passive_deletes=True
    )
