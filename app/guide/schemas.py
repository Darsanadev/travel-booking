from pydantic import BaseModel

class GuideCreate(BaseModel):
    name : str
    email: str
    phone: str
    experience: str
    languages: str


class GuideUpdate(BaseModel):
    name : str | None = None
    email: str | None = None
    phone: str | None = None
    experience: str | None = None
    languages: str | None = None


class GuideREsponse(BaseModel):
    id: int
    name : str
    email: str
    phone: str
    experience: str
    languages: str
    is_active: bool

    class Config:
        from_attributes = True