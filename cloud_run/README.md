# Descripción de Archivos Relacionados a Nuestra Cloud Run

En esta carpeta, encontramos varios archivos cruciales para nuestra aplicación en Cloud Run:

1. **Dockerfile:** Este archivo es fundamental ya que se encarga de construir una imagen basada en Python. Copia el web.py, la carpeta templates, la carpeta static y el archivo requirements.txt. Luego, instala los requisitos y ejecuta el web.py.

2. **web.py:** Este archivo es nuestra aplicación en sí. Interactúa con los servicios de Google Cloud para el almacenamiento y procesamiento de datos. Se complementa con un index.html ubicado en la carpeta "templates" y un styles.css en la carpeta "static". Estos archivos proporcionan una interfaz atractiva para nuestra aplicación, dándole ese toque especial.
