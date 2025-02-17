# Importar las librerías necesarias
from fastapi import FastAPI, HTTPException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
# Esto permite cargar credenciales y configuraciones desde un archivo .env, sin exponerlas en el código fuente
load_dotenv()

def send_email(subject: str, recipient: str, form_data: dict):
    """
    Envía un correo electrónico utilizando las credenciales y la plantilla especificadas.

    Args:
        subject (str): Asunto del correo.
        recipient (str): Dirección de correo del destinatario.
        form_data (dict): Datos del formulario para incluir en el correo.

    Returns:
        str: Mensaje de éxito.

    Raises:
        HTTPException: Si ocurre un error al enviar el correo.
    """
    try:
        # Obtener las credenciales de las variables de entorno
        # Estas variables se cargan desde el archivo .env y se utilizan para autenticar el envío del correo
        sender_email = os.getenv("EMAIL_ADDRESS")
        sender_password = os.getenv("EMAIL_PASSWORD")
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT", 465))  # Valor por defecto: 465 si no se especifica

        # Comprobar si todas las variables de entorno necesarias están presentes
        if not all([sender_email, sender_password, smtp_server, smtp_port]):
            raise ValueError("Faltan variables de entorno necesarias para enviar el correo.")
        
        # Leer la plantilla HTML para el correo
        # La plantilla puede incluir marcadores de posición que luego serán reemplazados por los datos del formulario
        with open("templates/email.html", "r", encoding="utf-8") as f:
            html_content = f.read()

        # Reemplazar los placeholders en la plantilla por los datos del formulario
        template = Template(html_content)
        html_message = template.safe_substitute(
            name=form_data["name"],
            last_name=form_data['last_name'],
            email=form_data['email'],
            phone=form_data['phone'],
            description=form_data['description']
        )

        # Crear el mensaje de correo utilizando MIMEMultipart
        # Esto permite enviar un correo que pueda tener múltiples partes, como texto y HTML
        msg = MIMEMultipart()
        msg["From"] = sender_email  # Dirección de correo del remitente
        msg["To"] = recipient  # Dirección del destinatario
        msg["Subject"] = subject  # Asunto del correo
        msg.attach(MIMEText(html_message, "html"))  # Adjuntar el contenido HTML del mensaje

        # Conectar al servidor SMTP_SSL
        # Usamos SSL para asegurar la conexión al servidor SMTP
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(sender_email, sender_password)  # Iniciar sesión en el servidor SMTP
            server.sendmail(sender_email, recipient, msg.as_string())  # Enviar el correo

        return "Email sent successfully"  # Mensaje de éxito si todo salió bien
    
    # Manejo de excepciones específicas
    except ValueError as ve:
        # Si faltan variables de entorno, se lanza una excepción con código 400
        raise HTTPException(status_code=400, detail=str(ve))
    except smtplib.SMTPException as smtp_e:
        # Si ocurre un error al interactuar con el servidor SMTP, se lanza una excepción con código 500
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo (SMTP): {str(smtp_e)}")
    except Exception as e:
        # Para cualquier otro error general, se lanza una excepción con código 500
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {str(e)}")

# Ejemplo de uso de la función send_email
# Si el archivo es ejecutado directamente, se puede probar el envío de un correo con datos de ejemplo
if __name__ == "__main__":
    example_form_data = {
        "name": "John",
        "last_name": "Doe",
        "email": "john.doe@example.com",
        "phone": "123456789",
        "description": "Este es un correo de prueba."
    }
    print(send_email("Asunto de prueba", "recipient@example.com", example_form_data))  # Llamar a la función de envío de correo