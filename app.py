from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def registrar():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('logs.txt', 'a') as f:
        f.write(f"[{timestamp}] IP: {ip}, User-Agent: {user_agent}\n")

    return """
    <html>
        <head>
            <title>Gracias</title>
        </head>
        <body style="text-align:center; font-family:sans-serif; margin-top:10%;">
            <h2>¡Gracias por registrarte!</h2>
            <p>Tu acceso ha sido registrado con éxito.</p>
        </body>
    </html>
    """
