from pydantic import BaseModel
from typing import List, Optional

class Color(BaseModel):
    idColor: int
    color_name: str
    image: Optional[str] = None

    class Config:
        from_attributes = True
