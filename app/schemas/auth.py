from core.database import Base
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
    created_at: str
    updated_at: str


