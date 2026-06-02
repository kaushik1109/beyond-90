from fastapi import APIRouter

router = APIRouter(prefix="/posts", tags=["posts"])

@router.get("/")
async def get_posts():
    return []

@router.put("/post")
async def add_post():
    pass


