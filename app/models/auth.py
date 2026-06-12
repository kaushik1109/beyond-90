from sqlalchemy import Integer, String, Column, Text, DateTime
from core.database import Base

class User(Base):
    __tablename__="user"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)