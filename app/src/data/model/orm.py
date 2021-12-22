import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.model.base import DeclarativeBase
from data.model.task import Task # noqa: F401


def create_db_engine():
    engine = create_engine("postgresql+pg8000://postgres:cicvor@localhost:5432/postgres", connect_args={'timeout': 10})

    DeclarativeBase.metadata.create_all(engine, checkfirst=True)

    return engine

def create_db_session():
    engine = create_db_engine()
    return Session(engine)

def get_version() -> str:
    return sqlalchemy.__version__


def get_db_time() -> str:
    with create_db_session() as session:
        with session.begin():
            result = session.execute("SELECT NOW()").first()
            return str(result)


