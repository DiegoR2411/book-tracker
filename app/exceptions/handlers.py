from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.exceptions.user import (
    UsernameAlreadyExistsError,
    EmailAlreadyExistsError,
)


def register_exception_handlers(app: FastAPI):

    @app.exception_handler(UsernameAlreadyExistsError)
    async def username_exists_handler(
        request: Request,
        exc: UsernameAlreadyExistsError,
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": "Username already exists"},
        )

    @app.exception_handler(EmailAlreadyExistsError)
    async def email_exists_handler(
        request: Request,
        exc: EmailAlreadyExistsError,
    ):
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"detail": "Email already exists"},
        )