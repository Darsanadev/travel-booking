from pydantic import BaseModel
from datetime import date, datetime


# user sent create booking
class BookingCreate(BaseModel):
    package_id: int
    travel_date: int
    travelers_count: int
    total_amount: int


# # Admin updates booking status put/patch
class BookingUpdate(BaseModel):
    booking_status: str | None = None

# read response
class BookingResponse(BaseModel):
    id: int
    user_id: int
    package_id: int
    traveldate: date
    travellers_count: int
    total_amount: float
    booking_status: str
    created_at: datetime
    updated_at: datetime


    class Config:
        from_attributes = True