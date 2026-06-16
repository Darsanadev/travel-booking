from sqlalchemy .orm import Session
from .models import Booking
from .schemas import BookingCreate, BookingUpdate
from app.package.models import Package

# new create booking
def sent_booking(db: Session, booking: BookingCreate, user_id: int):
    package = db.query(Package).filter(Package.id==booking.package_id).first()

    if not package:
        return None
    
    total_amount = package.price * booking.travellers_count

    new_booking = Booking(
        user_id = user_id,
        package_id = booking.package_id,
        travel_date = booking.travel_date,
        travellers_count = booking.travellers_count,
        total_amount = total_amount
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)

    return new_booking

def get_all_booking(db: Session):
    return db.query(Booking).all()

def get_booking(book_id: int, db:Session):
    return db.query(Booking).filter(Booking.id==book_id).first()

def update_booking_status(booking: BookingUpdate, book_id: int, db: Session):
    book_status = db.query(Booking).filter(
        Booking.id == book_id
    ).first()

    if not book_status:
        return None
    
    book_status.booking_status = booking.booking_status

    db.commit()
    db.refresh(book_status)

    return book_status

