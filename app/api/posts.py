from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal, engine, Base
from models.posts import Blog

router = APIRouter(prefix="/posts", tags=["posts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/")
async def get_posts(db: Session = Depends(get_db)):
    posts = db.query(Blog).all()

    return posts

@router.post("/")
async def add_post():
    pass


