# Importar las clases necesarias de SQLAlchemy y otras librerías
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
# Esto permite que las variables sensibles, como la URL de la base de datos, estén fuera del código fuente.
load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
# 'DATABASE_URL' debería estar definida en el archivo .env y contiene la cadena de conexión a la base de datos
DATABASE_URL = os.getenv('DATABASE_URL')

# Crear el motor de la base de datos utilizando la URL obtenida
# El motor es el responsable de establecer la conexión con la base de datos y ejecutar las consultas
engine = create_engine(DATABASE_URL, echo=True)

# Crear una instancia de MetaData
# MetaData es un objeto que contiene las definiciones de las tablas y otros objetos relacionados con la base de datos
meta = MetaData()

# Configurar una fábrica de sesiones
# La fábrica de sesiones permite la creación de objetos sesión que interactúan con la base de datos
# 'autocommit=False' y 'autoflush=False' indican que la sesión no hará commits o flush automáticos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Función para obtener una sesión de base de datos
# La sesión se utiliza para realizar consultas y transacciones en la base de datos
# La función utiliza el patrón de generador (yield) para asegurar que la sesión sea cerrada correctamente después de su uso
def get_session():
    session = SessionLocal()
    try:
        yield session  # Devuelve la sesión para su uso
    finally:
        session.close()  # Asegura que la sesión sea cerrada después de su uso
