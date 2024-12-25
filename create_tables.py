from sqlalchemy import create_engine
from models.base import Base
from models.user import User
from models.task import Task
from models.column import ColumnModel
from models.project import Project

engine = create_engine('sqlite:///kanban_board.db')

print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)

print("Creating all tables...")
Base.metadata.create_all(bind=engine)

print("Tables created successfully.")