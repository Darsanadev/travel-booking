from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .schemas import UserRegister, UserLogin
from .logic import register_user, login_user
from app.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    return register_user(user, db)


@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    return login_user(user, db)

