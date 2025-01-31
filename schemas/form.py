from pydantic import BaseModel
from typing import Optional

class FormBase(BaseModel):
    name: str
    last_name: str
    email: str
    number: int
    description: Optional[str] = None

class FormCreate(FormBase):
    pass  # Para crear, solo heredamos el modelo base

class Form(FormBase):
    idForm: int

    class Config:
        orm_mode = True
