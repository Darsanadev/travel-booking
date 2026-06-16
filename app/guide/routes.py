from .schemas import GuideCreate, GuideUpdate
from fastapi import APIRouter, Depends
from . import crud
from app.database import get_db
from sqlalchemy .orm import Session

router = APIRouter(prefix="/guide", tags=["Guide"]) 

@router.post('/')
def create_guide(guide: GuideCreate, db: Session = Depends(get_db)):
    return crud.create_guide(db, guide)

@router.get('/')
def get_all_guides(db: Session = Depends(get_db)):
    return crud.get_all_guide(db)

@router.get('/{id}')
def get_guide(id: int, db: Session = Depends(get_db)):
    return crud.get_guide(db, id)

@router.put('/{id}')
def update_guide(id: int, guide: GuideUpdate, db: Session = Depends(get_db)):
    return crud.update_guide(db, guide, id)

@router.put('/{id}/toggle')
def hide_guide(id: int, db: Session = Depends(get_db)):
    return crud.hide_unhide(id, db)