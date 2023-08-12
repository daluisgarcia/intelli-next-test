# Solución a prueba técnica ofrecida por Intelli Next

## Instalar requerimientos
Para instalar los paquetes necesarios, solo debe ejecutar el comando `pip install -r requirements.txt` en la raíz del proyecto.
Si obtiene el error **'/psycopg/psycopg.h:36:10: fatal error: libpq-fe.h: No such file or directory'**, 
debe instalar el paquete libpq-dev con el comando `sudo apt-get install libpq-dev` y luego volver a ejecutar el comando anterior.

## Correr migraciones
Para correr las migraciones, debe ejecutar el comando `python manage.py migrate` en la raíz del proyecto.

## Poblar la base de datos
Para poblar la base de datos, debe ejecutar el comando `python manage.py seed` en la raíz del proyecto.

## Correr servidor
Para correr el servidor, debe ejecutar el comando `python manage.py runserver` en la raíz del proyecto.

## Acceder a la aplicación
Para acceder a la aplicación, debe ingresar a la siguiente URL: http://localhost:8000/api/ en su navegador.
Aqui se mostrará una lista de las rutas disponibles que puede consultar.