from sqlalchemy import create_engine, MetaData
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Crear el motor de la base de datos utilizando la URL de la base de datos desde las variables de entorno
DATABASE_URL = os.getenv('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError("La variable de entorno DATABASE_URL no está configurada.")

engine = create_engine(DATABASE_URL, echo=True)  # echo=True para habilitar el registro de SQLAlchemy

# Crear una instancia de MetaData
meta = MetaData()

# Función para obtener una conexión a la base de datos
def get_db_connection():
    try:
        conn = engine.connect()
        return conn
    except SQLAlchemyError as e:
        print(f"Error al conectar a la base de datos: {e}")
        raise

# Ejemplo de uso de la conexión dentro de un contexto
def example_usage():
    try:
        with get_db_connection() as conn:
            # Realizar operaciones con la conexión
            print("Conexión exitosa a la base de datos.")
    except SQLAlchemyError as e:
        print(f"Error durante la operación de la base de datos: {e}")

# Llamar a la función de ejemplo para probar la conexión
if __name__ == "__main__":
    example_usage()