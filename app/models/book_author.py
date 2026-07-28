from datetime import datetime, timezone

from sqlalchemy import DateTime, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base

from typing import TYPE_CHECKING

from sqlalchemy.orm import relationship
if TYPE_CHECKING:
    from app.models.book import Book
    from app.models.author import Author


class BookAuthor(Base):
    __tablename__ = "book_authors"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"),
        nullable=False
    )

    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id", ondelete="CASCADE"),
        nullable=False
    )

    contribution_type: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
        default="Author"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    book: Mapped["Book"] = relationship(
    "Book",
    back_populates="book_authors"
    )
    author: Mapped["Author"] = relationship(
        "Author",
        back_populates="book_authors"
    )