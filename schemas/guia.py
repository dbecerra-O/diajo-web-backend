from pydantic import BaseModel
from typing import Optional

class GuiaBase(BaseModel):
    name: str
    description: str
    archive: Optional[str]

class Guia(GuiaBase):
    id: int

    class Config:
        from_attributes = True