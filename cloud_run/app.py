import os
import random
from flask import Flask, render_template, request, redirect, url_for
from google.cloud import storage, firestore
import json
import time
from datetime import datetime

app = Flask(__name__)

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
            blob.upload_from_string(json.dumps(usuario), content_type='application/json')

            time.sleep(0)
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error al guardar en Firestore o GCS: {e}")

    return render_template('index.html')

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    mensaje = None

    if request.method == 'POST':
        # Si se envía el formulario, obtén los datos y guárdalos en Firestore
        nombre = request.form['nombre']
        email = request.form['email']

        # Genera una ID aleatoria para el usuario
        user_id = random.randint(100000, 999999)

        usuario = {
            'ID': user_id,
            'Nombre': nombre,
            'Correo electrónico': email,
            'Fecha de registro': datetime.today().strftime('%Y-%m-%d')
        }

        try:
            doc_ref = db.collection(collection_name).add(usuario)
            mensaje = f'Gracias por registrarte, guarda tu ID para ver tus datos: {user_id}'
        except Exception as e:
            mensaje = f'Error al enviar el formulario: {e}'

    return render_template('formulario.html', mensaje=mensaje)

@app.route('/tabla_usuarios', methods=['GET'])
def consulta():
    user_id = request.args.get('id')

    if user_id:
        # Si se proporciona la ID, filtrar datos del usuario específico
        users = db.collection(collection_name).where('ID', '==', int(user_id)).stream()
        users = [user.to_dict() for user in users]
        return render_template('tabla_usuarios.html', data=users, user_id=user_id)
    else:
        return render_template('tabla_usuarios.html', mensaje='Ingresa tu ID para ver tus datos')

#prrueba
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
