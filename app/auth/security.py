from pwdlib import PasswordHash
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from pydantic import BaseModel


# Password Hash and verify the passwords

# "Hashing" means converting some content (a password in this case) into a sequence of bytes (just a string) that looks like gibberish.
# # But you cannot convert from the gibberish back to the password.

# import secrets
# print(secrets.token_hex(32))

SECRET_KEY = "7c69187bd82de56b863e1c97cc645af273842b4cf9e535e97a06bed5bc86d173"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Token(BaseModel):
    access_token: str
    token_type: str


password_hash = PasswordHash.recommended()

def verify_password(plain_password:str, hashed_password: str):
    return password_hash.verify(plain_password, hashed_password)


def get_password_hash(password):
    return password_hash.hash(password)


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

