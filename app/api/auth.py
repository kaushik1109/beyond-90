from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from core.database import SessionLocal, engine, Base

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login")
async def login_user():
    pass

@router.post("/register")
async def register_user():
    pass
