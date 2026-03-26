import requests
from pydantic import ValidationError
from config.settings import API_NOTICIAS_URL, API_NOTICIAS_KEY
from models.noticia import NoticiasModel
from exceptions import ErrorConexionAPI, NoticiasNoEncontradasError


def obtener_noticias_pais(nombre: str, cca2: str) -> list[dict]:
    
    url = f"{API_NOTICIAS_URL}?apikey={API_NOTICIAS_KEY}&q={requests.utils.quote(nombre)}&country={cca2.lower()}"
    try:
        res = requests.get(url, timeout=5)

        if res.status_code == 400:
            raise NoticiasNoEncontradasError(f"Noticias de {nombre} no encontrado en la API")
        if res.status_code == 401:
            raise ErrorConexionAPI(f"API key inválida")
        if res.status_code == 422:
            raise ErrorConexionAPI(f"Datos invalidos enviados a la API")
        if res.status_code != 200:
            raise ErrorConexionAPI(f"Respuesta inesperada {res.status_code}")
        return res.json()
        
    except requests.exceptions.Timeout as e:
        raise ErrorConexionAPI("La API no contesto en el tiempo limite") from e
    except requests.exceptions.ConnectionError:
        raise ErrorConexionAPI("No se pudo conectar con la API noticias")
    except requests.RequestException as e:
        raise ErrorConexionAPI(f"Error en solicitud HTTP: {e}") from e

def obtener_info_noticias(datos: dict) -> list[dict]:
    if not datos:
        raise NoticiasNoEncontradasError("La API devolvió una respuesta vacía para el país solicitado")
    
    articulos_raw = datos.get("results", [])
    
    if not articulos_raw:
        raise NoticiasNoEncontradasError("No se encontraron noticias para el país solicitado")
    
    try:
        noticias = [NoticiasModel(**articulo) for articulo in articulos_raw]
    except ValidationError as e:
        raise ErrorConexionAPI(f"Respuesta de API inválida: {e.errors()}") from e
    
    return _normalizar_noticias(noticias)
    

def _normalizar_noticias(articulos: list[NoticiasModel]) -> list[dict]:
    return [{
        "Titulo": articulo.title,
        "Descripcion": articulo.description,
        "Fecha": articulo.pubDate,
        "Video": articulo.video_url
    }
        for articulo in articulos[:3]
    ]