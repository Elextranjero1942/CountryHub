from rich.console import Console
from rich.table import Table

console = Console()

def _crear_tabla_dict(titulo: str, info: dict):
    tabla = Table(title=titulo)
    tabla.add_column("Campo")
    tabla.add_column("Valor")
    for campo, valor in info.items():
        tabla.add_row(campo, str(valor))
    console.print(tabla)

def _crear_tabla_list(titulo: str, info: list):
    for i, noticia in enumerate(info, 1):
        tabla = Table(title=f"{titulo} {i}")
        tabla.add_column("Campo")
        tabla.add_column("Valor")
        for campo, valor in noticia.items():
            tabla.add_row(campo, str(valor))
        console.print(tabla)
    
def crear_tabla_pais(info: dict):
    _crear_tabla_dict("PAIS", info)

def crear_tabla_climas(info: dict):
    _crear_tabla_dict("CLIMAS", info)

def crear_tabla_noticias(info: list):
    _crear_tabla_list("NOTICIAS", info)