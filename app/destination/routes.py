from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from . import views
from .schemas import DestinationCreate, DestinationUpdate

router = APIRouter(prefix="/destini", tags=["Destination"]) 

@router.post('/')
def create_destini(destini: DestinationCreate, db: Session = Depends(get_db)):
    return views.crate_destiniation(db, destini)

@router.get('/')
def get_all(db: Session = Depends(get_db)):
    return views.get_all_destination(db)

@router.get('/{id}')
def get_destini(id: int, db: Session = Depends(get_db)):
    return views. get_destinatioon(db, id)

@router.put('/{id}')
def update_destini(id: int, destini: DestinationUpdate, db: Session = Depends(get_db)):
    return views.update_destination(db, destini, id)

@router.patch('/{id}/toggle')
def hide_destini(id: int, db: Session = Depends(get_db)):
    return views.hide_unhide(db, id)

