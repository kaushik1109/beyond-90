from core.database import Base
from pydantic import BaseModel, ConfigDict, Field


class BlogCreate(BaseModel):
    title: str
    content: str


class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    model_config = ConfigDict(from_attributes=True) #this gives permission to pydantic to read the SQLAlchemy objects
