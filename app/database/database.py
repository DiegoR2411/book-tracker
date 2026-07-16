from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from app.core.config import settings

database_url = (
    f"mysql+pymysql://"
    f"{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}"
    f"/{settings.db_name}"
)

engine = create_engine(
    database_url,
    echo=True
)

SessionLocal = sessionmaker( bind=engine, autoflush=False)

Base = declarative_base()