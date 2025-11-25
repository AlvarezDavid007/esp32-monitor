from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Servidor activo ESP32 ✔"

@app.route('/guardar')
def guardar():
    valor = request.args.get("valor", "No recibido")
    print("Dato recibido:", valor)
    return f"Dato recibido: {valor}"

if __name__ == "__main__":
    # Render asigna dinámicamente el puerto → lo tomamos de la variable de entorno PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

