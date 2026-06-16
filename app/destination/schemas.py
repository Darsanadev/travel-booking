from pydantic import BaseModel

class DestinationCreate(BaseModel):
    destination_name: str
    description: str
    country: str
    state: str
    image: str


class DestinationUpdate(BaseModel):
    destination_name: str | None = None
    description: str | None = None
    country: str | None = None
    state: str | None = None
    image: str | None = None


class DestinationRead(BaseModel):
    id: int
    destination_name: str
    description: str
    country: str
    state: str
    image: str

    class Config:
        from_attributes = True
    