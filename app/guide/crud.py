from . models import Guide
from sqlalchemy .orm import Session
from .schemas import GuideCreate, GuideUpdate

def create_guide(guide: GuideCreate, db: Session):
    new_guide = Guide(
        name = guide.name,
        email = guide.email,
        phone = guide.phone,
        experience = guide.experience,
        languages = guide.languages
    )

    db.add(new_guide)
    db.commit()
    db. refresh(new_guide)

    return new_guide

def get_all_guide(db: Session):
    return db.query(Guide).filter(Guide.is_active.is_(True)).all()

def get_guide(id: int, db: Session):
    return db.query(Guide).filter(Guide.id==id, Guide.is_active.is_(True)).first()

def update_guide(id: int, guide: GuideUpdate, db: Session):
    update_guid = db.query(Guide).filter(Guide.id==id).first()

    if not update_guid:
        return None
    
    for key, value in guide.dict(exclude_unset=True).items():
        setattr(update_guid, key, value)

    db.commit()
    db.refresh(update_guid)

    return update_guid

def hide_unhide(id: int, db: Session):
    guide = db.query(Guide).filter(Guide.id==id).first()
         
    if not guide:
        return None

    guide.is_active = not guide.is_active

    db.commit()
    db.refresh(guide)
    return guide
