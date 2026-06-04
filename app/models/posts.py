from sqlalchemy import Integer, String, Column, Text
from core.database import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key = True, index = True)
    title = Column(String, nullable = False)
    content = Column(Text, nullable = False)


