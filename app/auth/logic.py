from fastapi import FastAPI, HTTPException
from app.auth.schemas import UserRegister, UserLogin, VerifyOTP, ForgotPassword, ResetPassword
from app.auth.models import User
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth.security import get_password_hash, verify_password, create_access_token, validate_password, generate_otp
import smtplib
from email.message import EmailMessage
from datetime import datetime, timedelta


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
    otp = generate_otp()

    # create new user.
    new_user = User(
        name = user.name,
        email = user.email,
        hashed_password = hashed_password,
        otp = otp,
        otp_expiry = datetime.utcnow() + timedelta(minutes=5)
    )
    
    db.add(new_user)
    db.commit()
    
    db.refresh(new_user)
    send_otp_email(
    user.email,
    otp
    )
    return {"message": "Registered successfully"}


@app.post("/login")
def login_user(user: UserLogin, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.email == user.email).first()

    if not existing_user:
        return {"message": "Please register"}
    
    if not existing_user.is_verified:
        return {
            "message": "Please verify your email first"
        }
        
    if not verify_password(
    user.password,
    existing_user.hashed_password):
        return {"message": "Invalid password"}
    
    access_token = create_access_token(data={"sub": existing_user.email})

    return { 
        "access_token": access_token,
        "token_type": "bearer"}

def verify_otp(data: VerifyOTP, db: Session):
    user = db.query(User).filter(User.email == data.email).first()

    if not user:
        return {"message": "User not found"}
    
    if user.otp_expiry and datetime.utcnow() > user.otp_expiry:
        return {"message": "OTP expired"}
    
    if user.otp != data.otp:
        return {"message": "Invalid OTP"}
    
    user.is_verified = True
    user.otp = None
    # user.otp_expiry = None

    db.commit()
    return {"message": "Email verified successfully"}

def send_otp_email(receiver: str, otp: str):
    sender_email = ""
    app_password = ""

    msg = EmailMessage()
    msg["Subject"] = "Email Verification OTP"
    msg["From"] = sender_email
    msg["To"] = receiver

    msg.set_content(f"Your verification OTP is: {otp}")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465)as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)

# Forgot Password (Send OTP)
# Reset Password (Verify OTP+New Password)

def forgot_password(verify: ForgotPassword, db: Session = Depends(get_db)):
    user_exist = db.query(User).filter(User.email == verify.email).first()

    if not user_exist:
        raise HTTPException(
            status_code = 404,
            detail = "User Not Found"
        )
    otp = generate_otp()
    user_exist.otp = otp
    user_exist.otp_expiry = datetime.utcnow() + timedelta(minutes=5)

    db.commit()

    send_otp_email(user_exist.email, otp)

    return {
        "message": "OTP sent successfully"
    }


def reset_password(pwd: ResetPassword, db: Session = Depends(get_db)):
    user = db.query(User).filter(
        User.email == pwd.email
    ).first()
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    if user.otp != pwd.otp:
        raise HTTPException(
            status_code=400,
            detail="Invalid OTP"
        )
    
    password_error = validate_password(pwd.new_password)

    if password_error:
        return {
            "message": password_error
        }

    user.hashed_password = get_password_hash(
        pwd.new_password
    )

    user.otp = None

    db.commit()
    return {
    "message": "Password updated successfully"
}
