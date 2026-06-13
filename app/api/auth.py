from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.schemas.auth import CreateUser, UserResponse

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login_user():
    pass

@router.post("/register")
async def register_user(user: CreateUser):
    pass
