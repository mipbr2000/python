from flask import Flask, redirect, url_for, jsonify, request
import requests
import json

app = Flask(__name__)

class Motocicleta:
    def __init__(self, marca, modelo, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.cilindrada = cilindrada

@app.route("/")
def home():
    minha_nova_moto = None
    response = requests.get("http://localhost:5000/cria_motocicleta")
    
    if response.status_code == 200:
        try:
            minha_nova_moto = Motocicleta(**response.json())
        except:
            return "Erro ao criar motocicleta"
    
    if minha_nova_moto and minha_nova_moto.marca == "Honda":
        return redirect(url_for("rota_honda", moto=minha_nova_moto))
    else:
        return redirect(url_for("rota_yamaha", moto=minha_nova_moto))


@app.route("/cria_motocicleta", methods=["GET"])
def cria_motocicleta():
    moto = Motocicleta("Honda", "Twister", 350)
    return jsonify(moto.__dict__)


@app.route("/honda")
def rota_honda():
    moto = request.args.get("moto")
    return f"Esta é uma nova rota para motos Honda. {moto}"


@app.route("/yamaha")
def rota_yamaha():
    moto = request.args.get("moto")
    return f"Esta é uma nova rota para motos Yamaha. {moto}"


if __name__ == "__main__":
    app.run(debug=True)
