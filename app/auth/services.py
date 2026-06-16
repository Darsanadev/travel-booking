from fastapi import FastAPI
from app.auth.schemas import UserRegister, UserLogin
from app.auth.models import User
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.security import get_password_hash
from pwdlib import PasswordHash

app = FastAPI()

password_hash = PasswordHash.recommended()

@app.post("/register")
def register_user(user: UserRegister,
    db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()
    if existing_user:
        return {"message": "Already Registered "}
    hashed_password=get_password_hash(user.password)
    hashed_pwd = password_hash.hash(user.password)

    
    # create new user.
    new_user = User(
        name = user.name,
        email = user.email,
        hashed_password = hash_password(user.password),
        password = user.password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return {"message": "Registered successfully"}

@app.post("/login")
def login_user(user: UserLogin):
    existing_user = db.query(User).filter(
        User.email == user.email
    ).first()
    if existing_user:
        return {"message": "Already Registered "}
    
    return {"meassage": "plz register"}

