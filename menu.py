from exceptions import (
    ErrorConexionAPI,
    PaisNoEncontradoError,
    NoticiasNoEncontradasError,
    ClimaNoEncontradoError,
)
from services.climas import (
    obtener_datos_clima,
    obtener_info_clima,
    obtener_info_wmo,
)
from services.noticias import (
    obtener_noticias_pais,
    obtener_info_noticias,
)
from services.paises import (
    obtener_datos_pais, 
    obtener_info_pais,
)
from utils.display import (
    crear_tabla_pais,
    crear_tabla_climas,
    crear_tabla_noticias,
)

def nombre_pais():
    while True:
            nombre = input("Escribe el nombre del país (en inglés): ")
            if not nombre or nombre.strip() == "":
                print("Escribe un nombre valido.")
                continue
            if any(char.isdigit() for char in nombre):
                print("El nombre no puede contener números")
                continue
            if not all(char.isalpha() or char in "-'" for char in nombre):
                print("El nombre solo puede contener letras.")
                continue
            if not 3 <= len(nombre) <= 50:
                print("El nombre debe contener entre 3 y 50 caracteres.")
                continue
            return nombre.title()

def obtener_opcion() -> int:
    print("Elije una opción \n"
        "1- Buscar informacion acerca de un país \n"
        "2- Salir")
    while True:
        try:
            opcion = int(input(": "))
            if opcion not in (1,2):
                print("Solo puedes elegir la opcion 1 o 2.")
                continue
            return opcion
        except ValueError:
            print("Error: Debes ingresar un número (1 o 2)")

def menu():

    while True:
            o = obtener_opcion()
            if o == 1:
                try:
                    nombre = nombre_pais()

                    datos_pais = obtener_datos_pais(nombre)
                    
                    info_pais = obtener_info_pais(datos_pais)
                    crear_tabla_pais(info_pais)

                    if info_pais["lat"] is None or info_pais["lng"] is None:
                        print("No se pudo obtener las coordenadas de la capital del país.")
                        continue

                    datos_clima = obtener_datos_clima(info_pais["lat"], info_pais["lng"])
                    info_clima = obtener_info_clima(datos_clima)
                    
                    info_clima["WMO"] = obtener_info_wmo(info_clima["WMO"])
                    crear_tabla_climas(info_clima)

                    datos_noticias = obtener_noticias_pais(nombre, info_pais["cca2"])
                    info_noticias = obtener_info_noticias(datos_noticias)
                    crear_tabla_noticias(info_noticias)

                except NoticiasNoEncontradasError as e:
                    print(f"Error {e}")
                except PaisNoEncontradoError as e:
                    print(f"Error {e}")
                except ClimaNoEncontradoError as e:
                    print(f"Error {e}")
                except ErrorConexionAPI as e:
                    print(f"Error {e}")
                except Exception as e:
                    print(f"Error {e}")

            elif o == 2:
                print("Saliendo")
                break

