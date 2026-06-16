from sqlalchemy import Column, String, Integer, DateTime
from app.database import Base
from sqlalchemy import Date, ForeignKey, Numeric
from datetime import datetime

class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    package_id = Column(Integer, ForeignKey("package.id"))
    travel_date = Column(Date)
    travellers_count = Column(Integer)
    total_amount = Column(Numeric(10, 2))
    booking_status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

"""
    # special_request = Column(String, nullable=True) 

"""