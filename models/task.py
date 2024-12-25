from datetime import datetime
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .base import Base  # Импортируем Base из base.py


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(Text)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    project_id = Column(Integer, ForeignKey('project.id'))
    column_id = Column(Integer, ForeignKey('column.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

    project = relationship("Project", back_populates="tasks")
    column = relationship("ColumnModel", back_populates="tasks")
    user = relationship("User", back_populates="tasks")