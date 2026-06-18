from sqlalchemy import Column, String, Integer, Boolean, DateTime
from app.database import Base
from datetime import datetime

class Destination(Base):
    __tablename__ = 'destination'

    id = Column(Integer, primary_key=True, index=True)
    destination_name = Column(String)
    description = Column(String)
    country = Column(String)
    state = Column(String)
    image = Column(String)
    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )
    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )

    is_active = Column(Boolean, default=True)