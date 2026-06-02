from fastapi import FastAPI
from api.posts import router as posts_router
import model.posts

# Creates all the new tables mentioned in the models folder
Base.metadata.create_all(bind=engine)


app = FastAPI()


app.include_router(posts_router)

@app.get("/health")
async def root():
    return {"message":"Status: Health all good"}

