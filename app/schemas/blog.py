from core.database import Base
from pydantic import BaseModel, ConfigDict, Field


class BlogCreate(BaseModel):
    title: str
    content: str


class BlogResponse(BaseModel):
    id: int
    title: str
    content: str

