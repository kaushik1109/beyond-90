from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base

from datetime import datetime
from passlib.context import CryptContext

router = APIRouter(prefix="/admin", tags=["auth"])

@router.post("/analyse-match")
async def analyse_match():
    pass
 #this will have all the stats of a football match and call an llm to then generate analysis, it will also take in user's analysis where needed and if required

@router.post("/get-fixtures")
async def get_fixtures():
    pass
# use an api to get the latest fixtuyres that have happened, this wil be manual for nwo, can be a batch job later