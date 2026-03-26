import requests
from config.settings import API_PAIS_URL
from models.pais import PaisModel
from exceptions import ErrorConexionAPI, PaisNoEncontradoError
from pydantic import ValidationError

def obtener_datos_pais(nombre: str) -> list[dict]:
        # API_PAIS_URL ya fue validada al cargar config.settings, así que es seguro usarla.
        url = f"{API_PAIS_URL}{requests.utils.quote(nombre)}"
        try:
                res = requests.get(url, timeout=5)

                if res.status_code == 404:
                        raise PaisNoEncontradoError(f"País '{nombre}' no encontrado en la API")
                if res.status_code != 200:
                        raise ErrorConexionAPI(f"Respuesta inesperada: {res.status_code}")
                
                return res.json()
        
        except requests.exceptions.Timeout as e:
                raise ErrorConexionAPI(f"La API no respondió en el tiempo límite") from e
        except requests.exceptions.ConnectionError:
                raise ErrorConexionAPI("No se pudo conectar a la API de países")
        except requests.RequestException as e:
                raise ErrorConexionAPI(f"Error en solicitud HTTP: {e}") from e
        
def obtener_info_pais(datos: list[dict]) -> dict:
        if not datos:
                raise PaisNoEncontradoError("La API devolvió una respuesta vacía para el país solicitado")
        try:
                pais = PaisModel(**datos[0])
        except ValidationError as e:
                raise ErrorConexionAPI(f"Respuesta de API inválida: {e.errors()}") from e
        return _normalizar_pais(pais)

def _normalizar_pais(pais: PaisModel) -> dict:
        return {
                'nombre_comun': pais.name.common,
                'nombre_oficial': pais.name.official,
                'capital': pais.capital[0] if pais.capital else "N/A",
                'region': pais.region,
                "subregion": pais.subregion,
                'mapa': pais.maps.get("googleMaps", "N/A"),
                'cca2': pais.cca2,
                "Independiente": pais.independent,
                "Poblacion": pais.population,
                "lat": pais.capitalInfo.latlng[0] if len(pais.capitalInfo.latlng) >= 2 else None,
                "lng": pais.capitalInfo.latlng[1] if len(pais.capitalInfo.latlng) >= 2 else None,
        }