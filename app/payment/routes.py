from fastapi import APIRouter, Depends
from sqlalchemy .orm import Session
from app.database import get_db
from . import logic
from .schemas import CreatePayment, UpdatePayment


router = APIRouter(
    prefix="/payment", 
    tags=["Payment"])

@router.post('/')
def create_payment(payment: CreatePayment, db: Session = Depends(get_db)):
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