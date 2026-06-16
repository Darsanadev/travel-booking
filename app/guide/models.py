from app.database import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime
from datetime import datetime

class Guide(Base):
    __tablename__ = "guide"

    id = Column(Integer, primary_key=True, index=True),
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    experience = Column(String)
    languages = Column(String)
    is_active = Column(Boolean, default=True)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )