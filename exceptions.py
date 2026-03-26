class PaisNoEncontradoError(Exception):
        """Se lanza cuando la API no encuentra el país solicitado."""
        pass

class ErrorConexionAPI(Exception):
        """Se lanza cuando hay problemas de red con la API externa."""
        pass

class NoticiasNoEncontradasError(Exception):
        """Se lanza cuando la API no encuentra noticias del país solicitado"""
        pass

class ClimaNoEncontradoError(Exception):
        """Se lanza cuando la API no encuentra clima de lat y lon solicitados"""