# Solución a prueba técnica ofrecida por Intelli Next

## Instalar requerimientos
Para instalar los paquetes necesarios, solo debe ejecutar el comando `pip install -r requirements.txt` en la raíz del proyecto.
Si obtiene el error **'/psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory'**, 
debe instalar el paquete libpq-dev con el comando `sudo apt-get install libpq-dev` y luego volver a ejecutar el comando anterior.

## Ejecutar el proyecto
Antes de ejecutar el proyecto es necesario copiar el archivo `.env.example` y renombrarlo a `.env`. Luego de esto,
es necesario configurar las variables de entorno que se encuentran en el archivo `.env` para que el proyecto pueda 
funcionar correctamente (El proyecto se realizó utilizando una base de datos PostgreSQL, por lo que se recomienda 
utilizar el mismo manejador). Una vez los datos de configuración estén listos, se puede proceder a ejecutar el 
proyecto siguiendo estos pasos:

### 1. Correr migraciones
Para correr las migraciones, debe ejecutar el comando `python manage.py migrate` en la raíz del proyecto.

### 2. Poblar la base de datos
Para poblar la base de datos, debe ejecutar el comando `python manage.py seed` en la raíz del proyecto.

### 3. Correr servidor
Para correr el servidor, debe ejecutar el comando `python manage.py runserver` en la raíz del proyecto.

### 4. Acceder a la aplicación
Para acceder a la aplicación, debe ingresar a la siguiente URL: http://localhost:8000/api/ en su navegador.
Aqui se mostrará una lista de las rutas disponibles que puede consultar.