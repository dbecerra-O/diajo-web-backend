from fastapi import APIRouter
from config.db import engine
from models.models import forms
from schemas.form import Form

form = APIRouter()

@form.post("/diajosac/api/forms", response_model=Form)
async def create_form(name: str, last_name: str, email: str, number: int, description: str):
    query = forms.insert().values(name=name, last_name=last_name, email=email, number=number, description=description)
    
    with engine.connect() as conn:
        result = conn.execute(query)
        conn.commit()
    
    return {"message": "Form created successfully"}
