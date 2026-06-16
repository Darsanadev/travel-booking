from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Numeric
from app.database import Base
from datetime import datetime

class Payment(Base):
    __tablename__ = 'payment'
    
    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, ForeignKey("booking.id"))
    payment_method = Column(String)
    amount = Column(Numeric(10, 2))
    payment_status = Column(String)
    transaction_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

