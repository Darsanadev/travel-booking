from fastapi import FastAPI
from app.auth.schemas import UserRegister, UserLogin
from app.auth.models import User
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.security import get_password_hash, verify_password, create_access_token, validate_password

app = FastAPI()


@app.post("/register")
def register_user(user: UserRegister, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if existing_user:
        return {"message": "Already Registered "}
    
    password_error = validate_password(user.password)

    if password_error:
        return {"message": password_error}
    
    hashed_password = get_password_hash(user.password)

    # create new user.
    new_user = User(
        name = user.name,
        email = user.email,
        hashed_password = hashed_password,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Registered successfully"}


@app.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user:
        return {"message": "Please register"}
    
    if not verify_password(
    user.password,
    existing_user.hashed_password):
        return {"message": "Invalid password"}
    
    access_token = create_access_token(data={"sub": existing_user.email})

    return { 
        "access_token": access_token,
        "token_type": "bearer"}
