from fastapi import FastAPI, HTTPException
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from string import Template
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def send_email(subject: str, recipient: str, form_data: dict):
    try:
        # Obtener las credenciales de las variables de entorno
        sender_email = os.getenv("EMAIL_ADDRESS")
        sender_password = os.getenv("EMAIL_PASSWORD")
        smtp_server = os.getenv("SMTP_SERVER")
        smtp_port = int(os.getenv("SMTP_PORT", 465)) # Valor por defecto: 465

        # Leer plantilla para correo HTML
        with open("templates/email.html", "r") as f:
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

        # Crear el mensaje de correo
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(html_message, "html")) # Indicamos que el cotenido es HTML

        # Conectar al servidor SMTP_SSL
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient, msg.as_string())
        server.quit()

        return "Email sent successfully"
    
    except Exception as e:
         # Si ocurre un error, lanzar una excepción HTTP con el mensaje de error
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {str(e)}")