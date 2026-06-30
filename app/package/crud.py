from sqlalchemy.orm import Session
from .models import Package
from .schemas import PackageCreate, PackageUpdate

def create_package(db: Session, package: PackageCreate):
    new_package = Package(
        title = package.title,
        destination_id=package.destination_id,
        description = package.description,
        days = package.days,
        price = package.price,
        image = package.image
    )
    db.add(new_package)
    db.commit()
    db.refresh(new_package)
    return new_package

def get_packages(db: Session):
    return db.query(Package).filter(Package.is_active.is_(True)).all()
    
def get_package(db: Session, id: int):
    return db.query(Package).filter(Package.id==id, Package.is_active == True).first()

def update_package(db: Session, package: PackageUpdate, package_id: int):
    pack_age = db.query(Package).filter(Package.id==package_id).first()

    if not pack_age:
        return None
    
    for key, value in package.dict(exclude_unset=True).items():
        setattr(pack_age, key, value)

    db.commit()
    db.refresh(pack_age)
    return pack_age

def hide_unhide(db:Session, id: int):
    hidepack = db.query(Package).filter(Package.id==id).first()

    if not hidepack:
        return None
    hidepack.is_active = not hidepack.is_active

    db.commit()
    db.refresh(hidepack)
    return hidepack
