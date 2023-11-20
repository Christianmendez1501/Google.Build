import requests

def obtener_estado_aplicacion():
    url = "https://myservice-5txgpbv7fq-ew.a.run.app/status"
    response = requests.get(url)
    return response.json()

def enviar_mensaje_slack(token, status):
    url = "https://slack.com/api/chat.postMessage"

    mensaje = (
        ":tada: :rocket: *Actualizacion-de-estado* :rocket: :tada:\n"
        "---------------------------------\n"
        "`Server`: [App desplegada]\n"
        f"`Status`: {status}\n"
        "---------------------------------"
    )

    payload = {
        "token": token,
        "channel": "#gcloud-app",
        "text": mensaje,
        "as_user": False,
    }

    response = requests.post(url, data=payload)
    return response.json()

# Uso de las funciones
token_slack = "xoxb-6001837293094-6005559897157-GOEdwPEOENCC3oSIbqBCOJPF"

# Obtener estado de la aplicación en Google Cloud
estado_aplicacion = obtener_estado_aplicacion()

# Enviar mensaje a Slack
respuesta_slack = enviar_mensaje_slack(token_slack, estado_aplicacion["status"])
print(respuesta_slack)
