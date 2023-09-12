from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


# GET
@app.route("/")
def index():
    return "OK"


@app.route("/date")
def get_date():
    date = datetime.now().date().isoformat()
    return date


@app.route("/time")
def get_time():
    time = datetime.now().time().isoformat()
    return time


@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name}"


# POST
@app.route("/login", methods=["POST"])
def login():
    print(request.method)
    print(request.json)  # se afiseaza datele trimise ca payload in request
    # variabila request este o variabila locala din pachetul flask care retine date despre
    # request-ul curent
    return "OK"


# PUT
@app.route("/login", methods=["PUT"])
def login_put():
    data = request.json
    return jsonify(data)


if __name__ == '__main__':  # codul din acest if va fi rulat doar cand aplicatia porneste din fisierul curent
    # atributul __name__ ia valoarea __maim__ doar cand aplicatia este rulata din fisierul curent
    app.run(debug=True)  # debug -> restart aplicatie la fiecare modificare
