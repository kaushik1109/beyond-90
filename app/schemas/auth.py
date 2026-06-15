from app.core.database import Base
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class CreateUser(BaseModel):
    name: str
    email: str
    password: str

class UserResponse(BaseModel):
    id: int
    email: str
    name: str
    created_at: datetime
    updated_at: datetime


