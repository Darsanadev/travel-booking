from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from . import crud
from . schemas import PackageCreate, PackageUpdate

router = APIRouter(
    prefix="/packages",
    tags=["Packages"])


@router.post('/')
def create_package(package: PackageCreate, db: Session = Depends(get_db)):
    return crud.create_package(db, package)


@router.get('/')
def get_all_packages(db: Session = Depends(get_db)):
    return crud.get_packages(db)


@router.get('/{id}')
def get_package(id: int, db:Session = Depends(get_db)):
    return crud.get_package(db, id)


@router.put('/{id}')
def update_package(id: int, package: PackageUpdate, db: Session = Depends(get_db)):
    return crud.update_package(db, package, id)


@router.patch('/{id}/toggle')
def hide_unhide(id: int, db: Session = Depends(get_db)):
    return crud.hide_unhide(db, id)
