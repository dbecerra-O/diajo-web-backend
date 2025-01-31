from pydantic import BaseModel
from typing import Optional

class BrandBase(BaseModel):
    name: str
    image: Optional[str] = None  # URL opcional para la imagen

class Brand(BrandBase):
    idBrand: int

    class Config:
        orm_mode = True
