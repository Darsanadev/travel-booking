from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy .orm import Session
from app.database import get_db
from . import logic
from .schemas import CreatePayment, UpdatePayment
from app.auth.security import get_current_user, require_admin, require_customer
from . models import User


router = APIRouter(
    prefix="/payment", 
    tags=["Payment"])

@router.post('/')
def create_payment(payment: CreatePayment, db: Session = Depends(get_db), current_user: User = Depends(require_customer)):

    return logic.create_payment(db, payment, current_user.id)

@router.get('/')
def get_all_payments(db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    return logic.get_all_payments(db)

@router.get('/my_payments')
def my_payments(db: Session = Depends(get_db), current_user: User = Depends(require_customer)):

    return logic.get_user_payments(db, current_user.id)

@router.get('/{id}')
def get_payment(id: int, db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    return logic.get_payment(db, id)

@router.put('/{id}')
def update_payment(id: int,  payment: UpdatePayment, db: Session = Depends(get_db), current_user: User = Depends(require_admin)):
    return logic.update_payment(db, id, payment)
