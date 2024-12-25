from pydantic import BaseModel

class LogCreate(BaseModel):
    message: str
    timestamp: str
    # Добавьте другие поля, необходимые для логов

class Log(BaseModel):
    id: int
    message: str
    timestamp: str
    # Добавьте другие поля, которые могут быть полезны