from fastapi import APIRouter, HTTPException, BackgroundTasks, Depends
from sqlalchemy.future import select
from config.db import get_session
from schemas.form import FormCreate, Form as FormSchema
from models.models import Form as FormModel
from config.mail import send_email
from sqlalchemy.orm import Session
import os
from dotenv import load_dotenv

# Crear el enrutador para los endpoints relacionados con los formularios
form = APIRouter()
load_dotenv()  # Cargar variables de entorno del archivo .env

async def send_email_task(form_dict):
    """
    Tarea en segundo plano para enviar un correo con los datos del formulario.
    """
    send_email("Nueva Solicitud", os.getenv("ADDRESS_SENDER"), form_dict)

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