from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .schemas import UserRegister, UserLogin, VerifyOTP, ForgotPassword, ResetPassword, ResendOtp
from .logic import register_user, login_user, verify_otp, forgot_password, reset_password, resendotp
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

@router.post("/verif-yotp")
def verifyotp(data: VerifyOTP, db: Session = Depends(get_db)):
    return verify_otp(data, db)

@router.post("/forgot-password")
def forgotpassword(pwd: ForgotPassword, db: Session = Depends(get_db)):
    return forgot_password(pwd, db)

@router.post("/reset-password")
def resetpassword(data: ResetPassword, db: Session = Depends(get_db)):
    return reset_password(data, db)

@router.post("/resend-otp")
def resendotp(data: ResendOtp, db: Session = Depends(get_db)):
    return resendotp(data, db)
