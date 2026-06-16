from fastapi import APIRouter, Depends
from sqlalchemy .orm  import Session
from app.database import get_db
from . import logic
from . schemas import BookingCreate, BookingUpdate

router = APIRouter(
    prefix="/booking", 
    tags=["Booking"])

@router.post('/')
def sent_booking(booking: BookingCreate, user_id: int, db: Session = Depends(get_db)):
    return logic.sent_booking(db, user_id, booking)

@router.get('/')
def all_booking(db: Session = Depends(get_db)):
    return logic.get_all_booking(db)

@router.get('/{id}')
def get_booking(id: int, db: Session = Depends(get_db)):
    return logic.get_booking(db, id)

@router.put("/{id}")
def update_booking(
    id: int,
    booking: BookingUpdate,
    db: Session = Depends(get_db)
):
    return logic.update_booking_status(
        booking, id, db
    )

