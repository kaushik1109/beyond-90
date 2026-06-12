from app.core.database import Base
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime

class BlogCreate(BaseModel):
    title: str
    content: str


class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True) #this gives permission to pydantic to read the SQLAlchemy objects
