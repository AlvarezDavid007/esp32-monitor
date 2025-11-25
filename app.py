from flask import Flask, request

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
    app.run(host="0.0.0.0", port=10000)
