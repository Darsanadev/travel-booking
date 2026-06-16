from pydantic import BaseModel
from datetime import datetime


class EnquiryCreate(BaseModel):
    name: str
    email: str
    phone: str
    message: str


class EnquiryUpdate(BaseModel):
    status: str | None = None


class EnquiryRead(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    message: str
    status: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True