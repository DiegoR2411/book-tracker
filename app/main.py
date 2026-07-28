from fastapi import FastAPI

import app.models

from app.routers import user
from app.exceptions.handlers import register_exception_handlers

app = FastAPI()

register_exception_handlers(app)

app.include_router(user.router)

@app.get("/")
def root():
    return {"message": "Welcome to Book Tracker API"}