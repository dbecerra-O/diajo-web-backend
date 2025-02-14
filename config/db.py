from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv('DATABASE_URL')

# Crear el motor de la base de datos utilizando la URL obtenida
# El parámetro 'echo=True' es opcional y se utiliza para imprimir las consultas SQL en la consola, útil para depuración
engine = create_engine(DATABASE_URL, echo=True)

# Crear una instancia de MetaData
# MetaData es una colección de tablas y sus esquemas asociados
meta = MetaData()

# Establecer una conexión a la base de datos utilizando el motor creado
# Esta conexión se puede usar para ejecutar consultas y operaciones en la base de datos
conn = engine.connect()