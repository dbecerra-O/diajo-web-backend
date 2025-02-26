from pydantic import BaseModel
from typing import Optional

class CategoryBase(BaseModel):
    name: str
    image: Optional[str] = None  # URL opcional para la imagen

class Category(CategoryBase):
    idCategory: int

    class Config:
        from_attributes = True