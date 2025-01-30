from fastapi import APIRouter
from sqlalchemy import insert
from config.db import engine, meta
from models.models import forms

form = APIRouter()

@form.post("/diajosac/api/forms")
async def create_form(name: str, last_name: str, email: str, number: int, description: str):
    query = forms.insert().values(name=name, last_name=last_name, email=email, number=number, description=description)
    
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
    
    return {"message": "Form created successfully"}
