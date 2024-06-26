# Implementación de un Escenario Específico en una Herramienta Low-code

## Maestría en Ingeniería de Software
### Asignatura: Desarrollo de Software Dirigido por Modelos

### Autores:
- Johanna Patricia Montaño Guaman
- Omar Alexis Sanmartin Tapia

### Tema: Implementación de un escenario específico en una herramienta Low-code

---

## Descripción del Proyecto
Este proyecto demuestra la implementación de un escenario específico utilizando una herramienta Low-code. La aplicación está desarrollada con Django, un framework de alto nivel para el desarrollo rápido de aplicaciones web con Python.

## Instalación y Configuración

### Prerrequisitos
Antes de comenzar, asegúrate de tener instalados los siguientes componentes:
- Python 3.8 o superior
- pip (el gestor de paquetes de Python)
- Git (para clonar el repositorio)

### Pasos para la Instalación

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/omarAlexis1999/Low-Code-Django-Maestria.git
   ```
   ```bash
   cd Low-Code-Django-Maestria
   ```
2. **Ejecutar proyecto**
   ```bash
   python manage.py runserver
### Arbol de Proyecto

LowCode/
│
├── LowCode/         # Configuración del proyecto
│   ├── __init__.py
│   ├── settings.py            # Configuración principal del proyecto
│   ├── urls.py                # Enrutamiento de URL
│   └── wsgi.py
│
├── GestorGastos/                  # Aplicación específica
│   ├── migrations/            # Migraciones de base de datos
│   ├── static/                # Archivos estáticos
│   ├── templates/             # Plantillas HTML
│   ├── admin.py               # Configuración del administrador
│   ├── apps.py                # Configuración de la aplicación
│   ├── models.py              # Modelos de base de datos
│   ├── tests.py               # Pruebas unitarias
│   └── views.py               # Vistas de la aplicación
│
├── manage.py                  # Herramienta de línea de comandos de Django
├── requirements.txt           # Lista de dependencias
└── .env                       # Variables de entorno
