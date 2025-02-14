# schemas/form.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FormBase(BaseModel):
    name: str
    last_name: str
    email: str
    phone: str
    description: Optional[str] = None

class FormCreate(FormBase):
    pass

class Form(FormBase):
    idForm: int
    created_at: Optional[datetime]

    class Config:
        from_attributes = True
