from pydantic import BaseModel
from typing import List

class ColorSchema(BaseModel):
    idColor: int
    color_name: str
    image: str

    class Config:
        from_attributes = True

class CharacteristicSchema(BaseModel):
    idCharacteristic: int
    description: str

    class Config:
        from_attributes = True

class ProductSimple(BaseModel):
    """Esquema para `get_products`, sin colores ni características"""
    idProduct: int
    name: str
    description: str
    technical_sheet: str
    image: str
    idCategory: int
    idBrand: int

    class Config:
        from_attributes = True

class Product(ProductSimple):
    """Esquema para `get_product`, incluye colores y características"""
    colors: List[ColorSchema] = []
    characteristics: List[CharacteristicSchema] = []