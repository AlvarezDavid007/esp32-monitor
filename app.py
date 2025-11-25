from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    try:
        with open("datos.txt", "r") as f:
            contenido = f.read()
    except:
        contenido = "Aún no hay datos recibidos."
    return f"<h2>Datos recibidos del sensor</h2><pre>{contenido}</pre>"

@app.route('/guardar', methods=['GET'])
def guardar():
    valor = request.args.get('valor', 'N/A')
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha} - Valor: {valor}\n"
    with open("datos.txt", "a") as f:
        f.write(linea)
    return f"Dato recibido: {valor}"
