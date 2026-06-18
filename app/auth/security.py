from pwdlib import PasswordHash
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel
from . models import User
import re


# Password Hash and verify the passwords

# "Hashing" means converting some content (a password in this case) into a sequence of bytes (just a string) that looks like gibberish.
# # But you cannot convert from the gibberish back to the password.

# import secrets
# print(secrets.token_hex(32))

SECRET_KEY = "7c69187bd82de56b863e1c97cc645af273842b4cf9e535e97a06bed5bc86d173"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

password_hash = PasswordHash.recommended()

def get_password_hash(password: str):
    return password_hash.hash(password)


def verify_password(plain_password: str, hashed_password: str):
    return password_hash.verify(
        plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        email = payload.get("sub")
        if email is None:
            return None
        
        return email
    except JWTError:
        return None

def get_current_user(token: str, db):
    email = verify_token(token)

    if not email:
        return None
    
    user = db.query(User).filter(
        User.email == email
    ).first()

    return user

def validate_password(password: str):
    if len(password) < 8:
        return "Password must be at least 8 characters"
    
    if not re.search(r"[A-Z]", password):
        return "Password must contain an uppercase letter"
    
    if not re.search(r"[a-z]", password):
        return "Password must contain a lowercase letter"
    
    if not re.search(r"\d", password):
        return "Password must contain a number"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return "Password must contain a special character"
    
    return None
  
