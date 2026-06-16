from sqlalchemy import Column, String, Integer, Boolean
from app.database import Base

class Package(Base):
    __tablename__ = 'package'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    destination_id = Column(String)
    description = Column(String)
    days = Column(Integer)
    price = Column(Integer)
    image = Column(String)
    

    is_active = Column(Boolean, default=True)
