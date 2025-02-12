from pydantic import BaseModel
from typing import List, Optional
from schemas.color import Color

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    technical_sheet: Optional[str] = None  # URL de la hoja técnica
    image: Optional[str] = None  # URL de la imagen
    idCategory: int
    idBrand: int

class Product(ProductBase):
    idProduct: int
    colors: List[Color]

    class Config:
        from_attributes = True
