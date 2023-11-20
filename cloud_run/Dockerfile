FROM python:3.11

ENV PORT 8080

WORKDIR /app

COPY . /app

COPY templates/ templates/

COPY app/ app/

COPY requirements.txt .

ENV GOOGLE_APPLICATION_CREDENTIALS="/app/archivo-de-credenciales.json"

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
