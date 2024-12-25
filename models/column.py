from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from .base import Base  # Импортируем Base из base.py
from .task import Task  # Импортируем Task


class ColumnModel(Base):
    __tablename__ = 'column'
    __table_args__ = {'extend_existing': True}  # Добавляем extend_existing

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tasks = relationship("Task", back_populates="column")