from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, String, Text, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.session import Base


if TYPE_CHECKING:
    from app.models.library import Library
    from app.models.book_author import BookAuthor
    from app.models.review import Review

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
    library_entries: Mapped[list["Library"]] = relationship(
        "Library",
        back_populates="book"
    )
    book_authors: Mapped[list["BookAuthor"]] = relationship(
    "BookAuthor",
    back_populates="book"
    )
    reviews: Mapped[list["Review"]] = relationship(
    "Review",
    back_populates="book"
)