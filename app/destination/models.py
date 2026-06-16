from sqlalchemy import Column, String, Integer, Boolean
from app.database import Base

class Destination(Base):
    __tablename__ = 'destination'

    id = Column(Integer, primary_key=True, index=True)
    destination_name = Column(String)
    description = Column(String)
    country = Column(String)
    state = Column(String)
    image = Column(String)

    is_active = Column(Boolean, default=True)