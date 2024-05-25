from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql.functions import now
from sqlalchemy.types import DateTime


class Base(DeclarativeBase):
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
