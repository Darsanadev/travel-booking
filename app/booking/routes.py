from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy .orm  import Session
from app.database import get_db
from . import logic
from . schemas import BookingCreate, BookingUpdate
from app.auth.security import get_current_user
from . models import Booking

router = APIRouter(
    prefix="/booking", 
    tags=["Booking"])

@router.post('/')                      #   user_id: int, ntea pakran jwt token use cheythu
def create_booking(booking: BookingCreate, token: str, db: Session = Depends(get_db)):
    current_user = get_current_user(token, db)

    if not current_user:
        return {"message": "Unauthorized"}  
    
    return logic.sent_booking(
        db,
        booking,
        current_user.id
        )


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

@router.get("/my-bookings")
def my_bookings(token: str, db: Session = Depends(get_db)):

    current_user = get_current_user(token, db)
    if not current_user:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    return logic.get_user_bookings(
    db,
    current_user.id
)
