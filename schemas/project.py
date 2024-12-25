from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None  # Добавляем поле description

class ProjectCreate(ProjectBase):
    pass

class ProjectUpdate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True

    @classmethod
    def from_orm(cls, obj):
        return cls(
            id=obj.id,
            title=obj.title,
            description=obj.description,  # Добавляем поле description
            created_at=obj.created_at.isoformat(),
            updated_at=obj.updated_at.isoformat()
        )