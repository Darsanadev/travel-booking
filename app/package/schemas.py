from pydantic import BaseModel

# creat
class PackageCreate(BaseModel):
    title: str
    destination_id: int 
    description: str
    days: int
    price: int
    image: str

# PUT/Patch
class PackageUpdate(BaseModel):
    title: str | None = None
    destination_id: int | None = None
    description: str | None = None
    days: int | None = None
    price: int | None = None
    image: str | None = None

# Read
class PackageResponse(BaseModel):
    id: int
    title: str
    destination_id: int
    description: str
    days: int
    price: int
    image: str

    class Config:
        from_attributes = True


