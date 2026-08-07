from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user import UserRepository
from app.schemas.user import UserCreate
from app.utils.password import hash_password
from app.exceptions.user import UsernameAlreadyExistsError, EmailAlreadyExistsError

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db: Session, user_data: UserCreate) -> User:

        existing_username = self.user_repository.get_by_username(
        db,
        user_data.username
        )

        if existing_username:
            raise UsernameAlreadyExistsError("Username already exists")

        existing_email = self.user_repository.get_by_email(
            db,
            user_data.email
        )

        if existing_email:
            raise EmailAlreadyExistsError("Email already exists")
        user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hash_password(user_data.password)
        )

        return self.user_repository.create(db, user)