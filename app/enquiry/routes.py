from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app .database import get_db
from . import views
from .schema import EnquiryCreate, EnquiryUpdate


router = APIRouter(prefix="/enquiry", tags=["Enquiry"]) 

@router.post('/')
def create_enquiry(enquiry: EnquiryCreate, db: Session = Depends(get_db)):
    return views.create_enquiry(db, enquiry)

@router.get('/')
def get_all_enquiry(db: Session = Depends(get_db)):
    return views.get_all_enquiry(db)

@router.get('/{id}')
def get_enquiry(id: int, db: Session = Depends(get_db)):
    return views.get_enquiry(db, id)

@router.put('/{id}')
def update_enquiry(id: int, enquiry: EnquiryUpdate, db: Session = Depends(get_db)):
    return views.update_enquiry(db, enquiry, id)

