import json
from google.cloud import storage
from google.cloud import firestore

storage_client = storage.Client()
firestore_client = firestore.Client()

def functionprueba(event, context):
    # Descarga el archivo desde Cloud Storage
    blob = storage_client.bucket(event["bucket"]).get_blob(event["name"])
    content = blob.download_as_text()

    # Lee y muestra el contenido del archivo JSON
    data = json.loads(content)
    print(data)

    # Verifica si el campo "Nombre" está presente en el JSON
    if "Nombre" in data:
        nombre_documento = data["Nombre"]

        # Agrega los datos al documento con el nombre obtenido del campo "Nombre" en la colección "thebridge"
        firestore_client.collection("thebridge").document(nombre_documento).set(data)
    else:
        print("El campo 'Nombre' no está presente en el JSON. No se puede determinar el nombre del documento.")

