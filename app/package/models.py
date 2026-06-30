from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from app.database import Base
from datetime import datetime

class Package(Base):
    __tablename__ = 'package'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    destination_id = Column(Integer, ForeignKey("destination.id"))
    description = Column(String)
    days = Column(Integer)
    price = Column(Integer)
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

