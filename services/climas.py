import requests
from pydantic import ValidationError
from config.settings import API_CLIMA_URL
from models.clima import ClimaModel
from utils.wmo_codes import WMO_CODES
from exceptions import ErrorConexionAPI, ClimaNoEncontradoError

def obtener_datos_clima(latitud: float, longitud: float) -> dict:
    
    url = f"{API_CLIMA_URL}?latitude={latitud}&longitude={longitud}&current=temperature_2m,windspeed_10m,weathercode"
    
    try:
        res = requests.get(url, timeout=5)

        if res.status_code == 400:
            raise ClimaNoEncontradoError(f"El clima no fue encontrado")
        if res.status_code != 200:
            raise ErrorConexionAPI(f"Respuesta inesperada {res.status_code}")
        return res.json()
    
    except requests.exceptions.Timeout as e:
        raise ErrorConexionAPI("La API no contesto en el tiempo limite") from e
    except requests.exceptions.ConnectionError:
        raise ErrorConexionAPI("No se pudo conectar con la API clima")
    except requests.RequestException as e:
        raise ErrorConexionAPI(f"Error en solicitud HTTP: {e}") from e

def obtener_info_clima(datos: dict) -> dict:
    if not datos:
        raise ClimaNoEncontradoError("La API devolvió una respuesta vacía para el WMO solicitado")
    try:
        clima = ClimaModel(**datos)
        if clima.current.temperature_2m is None:
            raise ClimaNoEncontradoError(f"El clima no fue encontrado.")
    except ValidationError as e:
        raise ErrorConexionAPI(f"Respuesta de API inválida: {e.errors()}") from e
    
    return _normalizar_clima(clima)

def obtener_info_wmo(codigo: int) -> str:
    return WMO_CODES.get(codigo, "Condición desconocida")

def _normalizar_clima(clima: ClimaModel) -> dict:

    return {
            "Temperatura": clima.current.temperature_2m,
            "WMO": clima.current.weathercode
        }