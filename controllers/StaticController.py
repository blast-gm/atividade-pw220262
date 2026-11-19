from flask import render_template
from models.Problema import Problema
from main import app


@app.route("/")
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html", enunciado=Problema.enunciado)
