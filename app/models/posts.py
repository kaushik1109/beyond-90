from sqlalchemy import Integer, String, Column, textwrap
from app.core.database import Base

class Post(Base):
    __tablename__ = "blogs"

    id = Colummn(Integer, primary_key = True, index = True)
    title = Column(String, nullable = False)
    content = Column(Text, nullable = False)


