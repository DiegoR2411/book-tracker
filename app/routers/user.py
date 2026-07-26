from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.dependencies.user import get_user_service
from app.repositories import user
from app.schemas.user import UserCreate, UserResponse
from app.services.user import UserService

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserResponse)
def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db),
    user_service: UserService = Depends(get_user_service)
):
    try:
        user = user_service.create_user(db, user_data)
        return user
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error))