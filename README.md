# info-paises

Herramienta de consola en Python que, dado el nombre de un país, muestra en tiempo real el clima de su capital, datos generales del país y las últimas noticias relacionadas, consumiendo múltiples APIs externas.

## Requisitos

- Python 3.8+

## Instalación

```bash
pip install -r requirements.txt
```

## Variables de entorno

Crea un archivo `.env` con estas variables (son las que usa el código):

```env
API_PAIS_URL=
API_CLIMA_URL=
API_NOTICIAS_URL=
API_CLIMA_KEY=
API_NOTICIAS_KEY=
```

## Ejecución

```bash
python main.py
```

## Estructura del Proyecto

```
.
├── main.py                 # Punto de entrada de la aplicación
├── menu.py                 # Lógica del menú interactivo
├── exceptions.py           # Excepciones personalizadas
├── requirements.txt        # Dependencias del proyecto
├── config/
│   └── settings.py         # Carga y valida variables de entorno
├── models/
│   ├── pais.py             # Modelo Pydantic para País
│   ├── clima.py            # Modelo Pydantic para Clima
│   └── noticia.py          # Modelo Pydantic para Noticia
├── services/
│   ├── paises.py           # Servicios de API de países
│   ├── climas.py           # Servicios de API de clima
│   └── noticias.py         # Servicios de API de noticias
└── utils/
    ├── display.py          # Funciones para mostrar datos formateados
    └── wmo_codes.py        # Códigos WMO de condiciones meteorológicas
```

## Arquitectura

El proyecto sigue una arquitectura en capas:

- **main.py**: Punto de entrada
- **menu.py**: Lógica de interfaz de usuario
- **config/settings.py**: Configuración centralizada (validación al startup)
- **services/**: Consumo de APIs externas con manejo de excepciones
- **models/**: Validación de datos con Pydantic
- **utils/**: Funciones auxiliares de presentación

## Ejemplo de uso

```text
Elije una opción
1- Buscar informacion acerca de un país
2- Salir
: 1
Escribe el nombre del país: Peru

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ PAIS                                   ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ nombre_comun          Peru              │
│ nombre_oficial        Republic of Peru  │
│ capital               Lima              │
│ region                Americas          │
│ subregion             South America     │
└───────────────────────────────────────┘

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ CLIMAS                                 ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Temperatura           15.5              │
│ WMO                   Cielo despejado   │
└───────────────────────────────────────┘

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ NOTICIAS 1                             ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Titulo                Noticias de Perú │
│ Descripcion           ...              │
│ Fecha                 2026-03-26       │
└───────────────────────────────────────┘
```

## Dependencias

- requests
- pydantic
- python-dotenv
- rich

## Licencia

MIT

## Autor

Luis Mitma Parado  
GitHub: https://github.com/Elextranjero1942  
LinkedIn: https://www.linkedin.com/in/luis-mitma-parado-a83602302/
