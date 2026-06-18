from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy .orm import Session
from app.database import get_db
from . import logic
from .schemas import CreatePayment, UpdatePayment
from app.auth.security import get_current_user


router = APIRouter(
    prefix="/payment", 
    tags=["Payment"])

@router.post('/')
def create_payment(payment: CreatePayment,token: str, db: Session = Depends(get_db)):
    current_user = get_current_user(token, db)

    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return logic.create_payment(db, payment)

@router.get('/')
def get_all_payments(db: Session = Depends(get_db)):
    return logic.get_all_payments(db)

@router.get('/{id}')
def get_payment(id: int, db: Session = Depends(get_db)):
    return logic.get_payment(db, id)

@router.put('/{id}')
def update_payment(id: int,  payment: UpdatePayment, db: Session = Depends(get_db)):
    return logic.update_payment(db, id, payment)

@router.get('/my_payments')
def my_payments(token: str, db: Session = Depends(get_db)):
    current_user = get_current_user(token, db)

    if not current_user:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized"
        )
    return logic.get_user_payments(db, current_user.id)

