from pydantic import BaseModel
from datetime import date, datetime


class CreatePayment(BaseModel):
    booking_id: int
    payment_method: str


class UpdatePayment(BaseModel):
    booking_id: int | None = None


class PaymentResponse(BaseModel):
    id: int
    booking_id: int
    payment_method: str
    amount: float
    payment_status: str
    transaction_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

