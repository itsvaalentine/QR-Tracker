from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    # Obtener IP (real o por proxy) y User-Agent
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    ua = request.headers.get('User-Agent')
    # Escribir en el archivo de logs (crear carpeta si es necesario)
    os.makedirs('/app/data/logs', exist_ok=True)
    with open('/app/data/logs/logs.txt', 'a') as f:
        f.write(f"{ip} - {ua}\n")
    return "<h1>Gracias por registrarte</h1>"
