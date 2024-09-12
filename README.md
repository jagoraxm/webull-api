# Proyecto Django con API

Este proyecto es una aplicación Django que ofrece una API para consultar símbolos de la NYSE y obtener datos de los últimos 7 días. Este archivo README proporciona información sobre la instalación, el uso y la configuración de la aplicación.

## Requisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Django 4.2 o superior
- Django REST Framework
- requests

## Instalación

Sigue estos pasos para configurar el entorno y ejecutar el proyecto en tu máquina local:

1. **Clona el repositorio:**

   ```
   git clone https://github.com/tuusuario/tu-repositorio.git
   cd tu-repositorio
   ```
2. **Crea y activa un entorno virtual:

    ```
    python -m venv env
    source env/bin/activate   # En Windows usa `env\Scripts\activate`
    ```

3. **Instala las dependencias::

    ```
    pip install -r requirements.txt
    ```

4. **Configura las variables de entorno:

    ```
    DJANGO_SECRET_KEY=tu_clave_secreta
    ```
    Asegúrate de reemplazar tu_clave_secreta con una clave secreta segura.

5. **Aplica las migraciones::

    ```
    python manage.py migrate
    ```

6. **Crea un superusuario para acceder al panel de administración:

    ```
    python manage.py createsuperuser
    ```

7. **Inicia el servidor de desarrollo:

    ```
    python manage.py runserver
    ```

## Uso y Acceso a la API
La API está disponible en http://localhost:8000/api/. Puedes utilizar herramientas como Postman para realizar peticiones.

Importar JSON desde Postman
Para importar un archivo JSON en Postman, sigue estos pasos:

Abre Postman.
1. Haz clic en "Importar" en la esquina superior izquierda.
2. Selecciona "Archivo" y elige tu archivo JSON. (webull-api.postman_collection.json)
3. Haz clic en "Importar" para añadir las peticiones al entorno de Postman.
4. El archivo JSON debe contener las peticiones que desees realizar a la API.

## Estructura del Proyecto
- webull_api/ - Carpeta principal del proyecto.
    - webull_api/settings.py - Configuración del proyecto.
    - webull_api/urls.py - Rutas del proyecto.
    - insert_data/ - Aplicación Django que contiene la lógica de la API.
        - models.py - Modelos de la aplicación.
        - views.py - Vistas de la API.
        - serializers.py - Serializadores de los datos.
        - urls.py - Rutas de la aplicación.

## Contribuciones
  Si deseas contribuir al proyecto, por favor sigue estos pasos:

  1. Haz un fork del repositorio.
  2. Crea una rama para tus cambios.
     ```
     git checkout -b nombre-de-tu-rama
     ```
  4. Haz un commit de tus cambios.
     ```
     git add .
     git commit -m "Descripción de los cambios"
     ```
  6. Envía un pull request.

## Licencia
  Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto
  Si tienes alguna pregunta o necesitas ayuda, no dudes en contactarme en jagoraxr.moucha@gmail.com
