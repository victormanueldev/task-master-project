from typing import Any

from sqlalchemy.types import DateTime
from sqlalchemy.sql.functions import now
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column
from sqlalchemy.ext.declarative import declared_attr


class Base(MappedAsDataclass, DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), default=now())
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True), default=now(), onupdate=now()
    )
    __name__: str

    # Generate table name automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
