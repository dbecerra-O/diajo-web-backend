from fastapi import APIRouter, HTTPException
from config.db import engine
from models.models import forms
from schemas.form import FormCreate, Form
from config.mail import send_email
from sqlalchemy import insert, select
import os
from dotenv import load_dotenv

# Crear el enrutador para los endpoints relacionados con los formularios
form = APIRouter()
load_dotenv() # Cargar variables de entorno del archivo .env

@form.post("/diajosac/api/forms", response_model=Form)
async def create_form(form_data: FormCreate):
    try:   
        # Insertar los datos del formulario en la base de datos
        query = insert(forms).values(**form_data.dict()) # Convierte el objeto en un diccionario

        with engine.connect() as connection:
            result = connection.execute(query) # Ejecutar la insercion
            connection.commit() # Confirmar los cambios en la base de dato
            new_form_id = result.inserted_primary_key[0] # Obtener el ID del nuevo registro
        
            # Recuperar el formulario insertado para obtener el campo 'created_at' 
            form_result = connection.execute(
                select(forms).where(forms.c.idForm == new_form_id) # Buscar por el ID recien generado
            ).mappings().fetchone() # Obtener el resultado en formato diccionario

        # Enviar un correo con los datos del formulario
        send_email("Nueva Solicitud", os.getenv("ADDRESS_SENDER"), dict(form_result))
        
        # Devolver el formulario insertado con sus datos
        return Form(**form_result) # Convertir el diccionario en un objeto de respuesta
    
    except Exception as e:
        # Manejar cualquier error y devolver un mensaje HTTP 500
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")