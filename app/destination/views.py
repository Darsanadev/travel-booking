from sqlalchemy.orm import Session
from . models import Destination
from . schemas import DestinationCreate, DestinationUpdate


def crate_destiniation(db: Session, destini: DestinationCreate):
    new_destination = Destination(
        destination_name = destini.destination_name,
        description = destini.description,
        country = destini.country,
        state = destini.state,
        image = destini.image
    )
    db.add(new_destination)
    db.commit()
    db.refresh(new_destination)
    return new_destination

def get_all_destination(db: Session):
    return db.query(Destination).filter(Destination.is_active.is_(True)).all()

def get_destinatioon(db:Session, id: int):
    return db.query(Destination).filter(Destination.id==id, Destination.is_active.is_(True)).first()

def update_destination(db: Session, destini: DestinationUpdate, destini_id: int):
    update_destini = db.query(Destination).filter(Destination.id==destini_id).first()

    if not update_destini:
        return None
    
    for key, value in destini.dict(exclude_unset=True).items():
        setattr(update_destini, key, value)

    db.commit()
    db.refresh(update_destini)
    return update_destini

def hide_unhide(db: Session, id: int):
    hide_destini = db.query(Destination).filter(Destination.id==id).first()

    if not hide_destini:
        return None
    hide_destini.is_active = not hide_destini.is_active

    db.commit()
    db.refresh(hide_destini)
    return hide_destini

