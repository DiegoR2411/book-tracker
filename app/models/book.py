from datetime import datetime, timezone

from sqlalchemy import DateTime, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    api_id: Mapped[str | None] = mapped_column(
        String(50),
        unique=True,
        nullable=True
    )

    source: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    cover_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True
    )

    isbn: Mapped[str | None] = mapped_column(
        String(20),
        nullable=True
    )

    language: Mapped[str | None] = mapped_column(
        String(10),
        nullable=True
    )

    publication_year: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    total_pages: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
        nullable=False
    )