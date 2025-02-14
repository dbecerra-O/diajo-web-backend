from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    technical_sheet: Optional[str] = None
    image: Optional[str] = None
    idCategory: int
    idBrand: int

class Product(ProductBase):
    idProduct: int

    class Config:
        from_attributes = True
