from pydantic import BaseModel
from typing import Optional

class ColorBase(BaseModel):
    color_name: str
    image: Optional[str] = None
    idProduct: int

class Color(ColorBase):
    idColor: int

    class Config:
        from_attributes = True
