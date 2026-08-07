from datetime import datetime, timezone
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.session import Base
from app.enums.reading_status import ReadingStatus

if TYPE_CHECKING:
    from app.models.user import User
    from app.models.book import Book


class Library(Base):
    __tablename__ = "library"

    __table_args__ = (
        UniqueConstraint("user_id", "book_id"),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )

    book_id: Mapped[int] = mapped_column(
        ForeignKey("books.id", ondelete="CASCADE"),
        nullable=False
    )

    status: Mapped[ReadingStatus] = mapped_column(
        Enum(ReadingStatus),
        nullable=False,
        default=ReadingStatus.WANT_TO_READ
    )

    rating: Mapped[int | None] = mapped_column(
        Integer,
        nullable=True
    )

    current_page: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    re_read_count: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=0
    )

    started_reading_at: Mapped[datetime | None] = mapped_column(
        DateTime(),
        nullable=True
    )

    finished_reading_at: Mapped[datetime | None] = mapped_column(
        DateTime(),
        nullable=True
    )

    added_at: Mapped[datetime] = mapped_column(
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

    user: Mapped["User"] = relationship(
        "User",
        back_populates="library_entries"
    )
    book: Mapped["Book"] = relationship(
        "Book",
        back_populates="library_entries"
    )