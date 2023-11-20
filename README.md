![Gcloud](img/1.png)

# Aplicación de Formulario con Despliegue Automático y centralizacion de datos a traves del servicio de Google Cloud Platform

Este emocionante proyecto se divide en dos partes clave:

1. **Desarrollo de la Aplicación Web:**
   - Creación de una aplicación web que recopila datos ingresados por el usuario.
   - Almacenamiento de estos datos en una base de datos en la nube (Cloud Storage).
   - Transferencia de datos a una tabla específica en Firestore/Datastore.
   - Visualización de los datos a través de la interfaz de la web, todo gracias a los potentes servicios de Google Cloud.

2. **Despliegue Automático con Cloud Function y Cloud Run:**
   - Implementación de Cloud Function y Cloud Run para poner en marcha toda la aplicación.
   - Configuración de activadores que, al realizar un commit en las carpetas asociadas, activan automáticamente los despliegues y levantan la aplicación web.

## Pasos a Seguir:

1. **Preparación de Cloud Storage y Firestore/Datastore:**
   - Crea un bucket en Cloud Storage.
   - Establece tu entidad o tabla en Firestore/Datastore.

2. **Despliegue de Cloud Function:**
   - Utiliza `cloudbuild_function.yml` para describir el entorno, la carpeta asociada a la función, el activador y la región.

3. **Despliegue de Cloud Run:**
   - Emplea `cloudbuild_run.yml` para configurar el despliegue de Cloud Run.
   - El archivo realiza la configuración del entorno, crea la imagen desde la carpeta asociada (cloud_run), la sube al repositorio de Google Cloud y finalmente la despliega según las especificaciones.

4. **Documentación Detallada:**
   - En cada carpeta, encontrarás un ReadMe que proporciona información detallada sobre esa parte específica del proceso.

¡Espero que esta guía te sea de gran ayuda en tu aventura con la implementación y despliegue de la aplicación!
