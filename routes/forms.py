from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from sqlalchemy.future import select
from config.db import get_session
from schemas.form import FormCreate, Form as FormSchema
from models.models import Form as FormModel
from config.mail import send_email
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv
from config.filter import analyze_text
import requests

# Crear el enrutador para los endpoints relacionados con los formularios
form = APIRouter()
load_dotenv()  # Cargar variables de entorno del archivo .env

async def send_email_task(form_dict):
    """
    Tarea en segundo plano para enviar un correo con los datos del formulario.
    """
    send_email("Diajo Web Solicitud", os.getenv("ADDRESS_SENDER"), form_dict)
    send_email("Diajo Web Solicitud", "diego.becerra@tecsup.edu.pe", form_dict)

@form.post("/diajosac/api/forms", response_model=FormSchema)
async def create_form(form_data: FormCreate, background_tasks: BackgroundTasks, session: Session = Depends(get_session)):
    """
    Crea un nuevo formulario y lo inserta en la base de datos.

    Args:
        form_data (FormCreate): Datos del formulario a crear.
        background_tasks (BackgroundTasks): Tareas en segundo plano.

    Returns:
        Form: El formulario creado.

    Raises:
        HTTPException: Si ocurre un error al insertar el formulario o al enviar el correo.
    """
    try:
        campos_a_validar = ["name", "last_name", "email", "phone", "description"]

        for campo in campos_a_validar:
            valor = getattr(form_data, campo)
            if valor:  # Verificar que no esté vacío
                try:
                    score = analyze_text(valor)
                    print(f"Toxicity Score para {campo}: {score}")  # Para depuración
                    if score is not None and score > 0.6:  # Ajusta el umbral si es necesario
                        raise HTTPException(status_code=400, detail=f"El contenido es inapropiado.")
                except requests.exceptions.RequestException:
                    raise HTTPException(status_code=503, detail="Servicio de análisis de texto no disponible.")
        # Insertar los datos del formulario en la base de datos
        new_form = FormModel(**form_data.dict())
        session.add(new_form)
        session.commit()
        session.refresh(new_form)

        # Agregar la tarea de envío de correo en segundo plano
        background_tasks.add_task(send_email_task, new_form.__dict__)

        # Devolver el formulario insertado con sus datos
        return new_form

    except Exception as e:
        # Manejar cualquier error y devolver un mensaje HTTP 500
        raise HTTPException(status_code=500, detail=f"Error: {str(e)}")