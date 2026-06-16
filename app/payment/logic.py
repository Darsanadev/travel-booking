from sqlalchemy .orm import Session
from .models import Payment
from .schemas import CreatePayment, UpdatePayment
from app.booking.models import Booking
import uuid

def create_payment(db: Session, payment: CreatePayment):
    booking = db.query(Booking).filter(Booking.id == payment.booking_id).first()

    if not booking:
        return None

    new_payment = Payment(
        booking_id = booking.id,
        payment_method = payment.payment_method,
        amount=booking.total_amount,
        payment_status="Pending",
        transaction_id=str(uuid.uuid4())
    )

    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

def get_all_payments(db: Session):
    return db.query(Payment).all()

def get_payment(db: Session, payment_id: int):
    return db.query(Payment).filter(Payment.id == payment_id).first()

def update_payment(db: Session, pay_id: int, payment: UpdatePayment):
    payment_status = db.query(Payment).filter(Payment.id==pay_id).first()

    if not payment_status:
        return None
    payment_status.payment_status = payment.payment_status

    db.commit()
    db.refresh(payment_status)

    return payment_status


