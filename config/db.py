from sqlalchemy import create_engine, MetaData
from sqlalchemy.exc import SQLAlchemyError
import os
from dotenv import load_dotenv

# Cargar variables de entorno del archivo .env
load_dotenv()

# Configurar la conexión a la base de datos
DATABASE_URL = os.getenv('DATABASE_URL')

# Crear el motor de la base de datos con echo para depuración
engine = create_engine(DATABASE_URL, echo=True)

# Crear una instancia de MetaData
meta = MetaData()

def get_connection():
    """
    Establece una conexión a la base de datos y la devuelve.

    Returns:
        Connection: Conexión a la base de datos.

    Raises:
        SQLAlchemyError: Si ocurre un error al conectar a la base de datos.
    """
    try:
        conn = engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise

# Ejemplo de uso de la conexión
if __name__ == "__main__":
    try:
        with get_connection() as conn:
            # Aquí puedes ejecutar tus consultas
            print("Conexión exitosa a la base de datos")
    except SQLAlchemyError as e:
        print(f"Error al manejar la conexión: {e}")
