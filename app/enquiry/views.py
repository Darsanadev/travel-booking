from sqlalchemy.orm import Session
from .models import Enquiry
from .schema import EnquiryCreate, EnquiryUpdate

def create_enquiry(db: Session, enquiry: EnquiryCreate):
    new_enquiry = Enquiry(
        name = enquiry.name,
        email = enquiry.email,
        phone = enquiry.phone,
        message = enquiry.message
    )

    db.add(new_enquiry)
    db.commit()
    db.refresh(new_enquiry)
    return {"send message confirmed we will contact you", new_enquiry}

def get_all_enquiry(db: Session):
    return db.query(Enquiry).all()

def get_enquiry(enq_id: int, db: Session):
    return db.query(Enquiry).filter(Enquiry.id==enq_id).first()

def update_enquiry(enq_id: int, db: Session, enquiry: EnquiryUpdate):
    update_enquiry = db.query(Enquiry).filter(Enquiry.id==enq_id).first()

    if not update_enquiry:
        return None
    
    for key, value in enquiry.dict(exclude_unset=True).items():
        setattr(update_enquiry, key, value)
    
    db.commit()
    db.refresh(update_enquiry)

    return update_enquiry



