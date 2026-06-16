from fastapi import FastAPI
from app.database import Base, engine

from app.auth.models import User
from app.package.models import Package
from app.destination.models import Destination
from app.enquiry.models import Enquiry
from app.booking.models import Booking
from app.payment.models import Payment


from app.auth.routes import router as auth_router
from app.package.routes import router as package_router
from app.destination.routes import router as destination_router
from app.enquiry.routes import router as enquiry_router
from app.booking.routes import router as booking_router
from app.payment.routes import router as payment_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)
app.include_router(package_router)
app.include_router(destination_router)
app.include_router(enquiry_router)
app.include_router(booking_router)
app.include_router(payment_router)
