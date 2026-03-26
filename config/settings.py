from dotenv import load_dotenv
import os

load_dotenv()

def _validar_variable(nombre: str) -> str:
        """
        Valida que una variable de entorno exista y no esté vacía.
        Si falta, lanza error al inicio en lugar de a mitad del flujo.
        """
        valor = os.getenv(nombre)
        if not valor:
                raise ValueError(f"{nombre} no está configurada en .env")
        return valor

API_PAIS_URL = _validar_variable("API_PAIS_URL")
API_CLIMA_URL = _validar_variable("API_CLIMA_URL")
API_NOTICIAS_URL = _validar_variable("API_NOTICIAS_URL")
API_CLIMA_KEY = _validar_variable("API_CLIMA_KEY")
API_NOTICIAS_KEY = _validar_variable("API_NOTICIAS_KEY")