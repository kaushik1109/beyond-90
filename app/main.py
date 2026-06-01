from fastapi import FastAPI
from api.posts import router as posts_router

app = FastAPI()


app.include_router(posts_router)

@app.get("/health")
async def root():
    return {"message":"Status: Health all good"}

