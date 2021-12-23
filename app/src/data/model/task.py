from sqlalchemy import Column, Integer, String, DateTime, func

from data.model.base import DeclarativeBase


class Task(DeclarativeBase):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
