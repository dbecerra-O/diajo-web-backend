from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv('DATABASE_URL')

# Crear el motor de la base de datos utilizando la URL obtenida
engine = create_engine(DATABASE_URL, echo=True)

# Crear una instancia de MetaData
meta = MetaData()

# Configurar una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión
def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()