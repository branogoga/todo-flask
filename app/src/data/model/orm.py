import logging
import os

from data.model.base import DeclarativeBase
from data.model.task import Task  # noqa: F401
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

logger = logging.getLogger(__name__)

def get_db_uri() -> str:
    db_uri = os.getenv('DATABASE_URL')
    if not db_uri:
        db_uri = "postgresql+pg8000://postgres:cicvor@localhost:5432/postgres"
    logger.warning(db_uri)
    return db_uri


def create_db_engine():
    engine = create_engine(get_db_uri(), connect_args={'timeout': 10})
    DeclarativeBase.metadata.create_all(engine, checkfirst=True)
    return engine


def create_db_session():
    engine = create_db_engine()
    return Session(engine)
