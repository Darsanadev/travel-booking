from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy .orm  import Session
from app.database import get_db
from . import logic
from . schemas import BookingCreate, BookingUpdate
from app.auth.security import require_customer, require_admin
from. models import User

router = APIRouter(
    prefix="/booking", 
    tags=["Booking"])

@router.post('/')                      #   user_id: int, ntea pakran jwt token use cheythu
def create_booking(
    booking: BookingCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(require_customer)):

    return logic.sent_booking(
        db,
        booking,
        current_user.id
        )

@router.get('/')
def all_booking(db: Session = Depends(get_db), current_user:User = Depends(require_admin)):
    return logic.get_all_booking(db)

@router.get("/my-bookings")
def my_bookings(db: Session = Depends(get_db), current_user: User = Depends(require_customer)):

    return logic.get_user_bookings(
    db,
    current_user.id
)

@router.get('/{id}')
def get_booking(id: int, db: Session = Depends(get_db), current_user:User = Depends(require_admin)):
    return logic.get_booking(db, id)

@router.put("/{id}")
def update_booking(
    id: int, booking: BookingUpdate, db: Session = Depends(get_db), current_user:User = Depends(require_admin)):
    return logic.update_booking_status(
        booking, id, db
    )
