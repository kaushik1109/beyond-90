from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import SessionLocal, engine, Base
from models.posts import Blog
from schemas.blog import BlogCreate, BlogResponse

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
async def add_post(blog: BlogCreate, db: Session = Depends(get_db)):

    new_blog = Blog(title = blog.title, content = blog.content)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)

    return new_blog


@router.get("/{id}")
async def get_post_id(id: int, db: Session = Depends(get_db)):

    post = db.query(Blog).filter(Blog.id == id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return post

