import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")

def analyze_text(texto):
    """
    Analiza el texto y devuelve el puntaje de toxicidad.
    
    Args:
        texto (str): El texto a analizar.
    
    Returns:
        float | None: El puntaje de toxicidad del texto o None si falla la API.
    """
    url = f"{API_URL}:analyze?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    payload = {
        "comment": {"text": texto},
        "languages": ["es", "en"],  # Soporta español e inglés
        "requestedAttributes": {"TOXICITY": {}}
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()

        if response.status_code == 200:
            return response_data.get("attributeScores", {}).get("TOXICITY", {}).get("summaryScore", {}).get("value")

        print(f"Error en la API: {response.status_code} - {response_data}")
        return None  # Si falla, devolver None

    except requests.RequestException as e:
        print(f"Error de conexión con la API: {e}")
        return None
    except json.JSONDecodeError:
        print("Error al decodificar la respuesta de la API.")
        return None