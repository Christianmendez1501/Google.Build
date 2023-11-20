import os
from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage, firestore
import json
import time

app = Flask(__name__)

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/app/app/application_default_credenciales.JSON"

storage_client = storage.Client()
bucket_name = 'proyecto-gcp-christian1328'

db = firestore.Client()
collection_name = 'thebridge'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        fecha = request.form['fecha']

        usuario = {
            "Nombre": nombre,
            "Correo electrónico": correo,
            "Fecha de registro": fecha
        }

        try:
            doc_ref = db.collection(collection_name).add(usuario)
            generated_id = doc_ref[1].id


            timestamp = int(time.time())
            file_name = f'datos{timestamp}.json'

            bucket = storage_client.get_bucket(bucket_name)
            blob = bucket.blob(file_name)
            blob.upload_from_string(json.dumps(usuario),content_type='application/json')

            time.sleep(0)
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error a guardar en Firestore o GCS: {e}")

    return render_template('index.html')

@app.route('/consulta', methods=['GET'])
def consulta():
    users = db.collection(collection_name).stream()
    users = [user.to_dict() for user in users]

    return render_template('consulta.html', users=users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

