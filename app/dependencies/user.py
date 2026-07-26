from app.repositories.user import UserRepository
from app.services.user import UserService

def get_user_service() -> UserService:
    user_repository = UserRepository()
    return UserService(user_repository)