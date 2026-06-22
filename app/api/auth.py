from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import SessionLocal, engine, Base
from app.schemas.auth import CreateUser, UserResponse
from app.models.auth import User
from datetime import datetime
from passlib.context import CryptContext

router = APIRouter(prefix="/auth", tags=["auth"])
pwd_context = CryptContext(
        schemes=["bcrypt"],
        deprecated="auto"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/login")
async def login_user(email_id: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email==email_id).first()

    if user is None:
        raise HTTPException(
            status_code=400,
            detail="Email id invalid"
        )
    
    if pwd_context.verify(password, user.password):
        return {"message":"Login successful"}
    else:
        raise HTTPException(
            status_code=400,
            detail="Wrong Password"
        )


@router.post("/register")
async def register_user(user: CreateUser, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(user.password)
    print("HASHED PASSWORD:", hashed_password)
    new_user = User (name = user.name,
                email = user.email, 
                password = hashed_password,
                created_at = datetime.now(),
                updated_at = datetime.now() )
    existing_user = db.query(User).filter(User.email == new_user.email).first()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    db.add(new_user)
    db.commit()

    db.refresh(new_user)

    return {"message":"User created successfully"}


@router.get("/users", response_model = list[UserResponse])
async def get_users(db: Session = Depends(get_db)):
    user = db.query(User).all()

    return user

    

