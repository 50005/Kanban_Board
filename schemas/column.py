from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class ColumnCreate(BaseModel):
    title: str


class ColumnUpdate(BaseModel):
    title: str


class ColumnModel(BaseModel):
    id: int
    title: str
    created_at: str
    updated_at: str

    class Config:
        from_attributes = True