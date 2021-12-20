import sqlalchemy
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

DeclarativeBase = declarative_base()


def get_version() -> str:
    return sqlalchemy.__version__


def get_db_time() -> str:
    engine = create_engine("postgresql+pg8000://postgres:cicvor@localhost:5432/postgres", connect_args={'timeout': 10})
    # create session and add objects
    with Session(engine) as session:
        with session.begin():
            result = session.execute("SELECT NOW()").first()
            return str(result)


# class Task(DeclarativeBase):
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     description = Column(String)
