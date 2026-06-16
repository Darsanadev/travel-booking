from sqlalchemy import Column, String, Integer, DateTime
from app. database import Base
from datetime import datetime

class Enquiry(Base):
    __tablename__ = "enguiry"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    message = Column(String)
    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)