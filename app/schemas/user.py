from typing import Annotated

from pydantic import BaseModel, EmailStr, StringConstraints, ConfigDict

from datetime import datetime

class UserCreate(BaseModel):
    username: Annotated[
        str, StringConstraints(
            min_length=3,
            max_length=50,
            strip_whitespace=True
        )
    ]
    email: EmailStr
    password: Annotated[
        str, StringConstraints(
            min_length=8,
            max_length=128
        )
    ]

class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    username: str
    email: EmailStr
    created_at: datetime