from fastapi import FastAPI
from app.api.posts import router as posts_router
import app.models.posts
from app.core.database import SessionLocal, Base, engine

# Creates all the new tables mentioned in the models folder
Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(posts_router)

@app.get("/health")
async def root():
    return {"message":"Status: Health all good"}

