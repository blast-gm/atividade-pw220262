from flask import render_template, request
from models.Problema import Problema
from main import app


@app.route("/problema", methods=["POST"])
def problema():
    obj = Problema(request.form.get("nome"),
                   float(request.form.get("nota1")),
                   float(request.form.get("nota2")),
                   float(request.form.get("nota3")))
    return render_template("problema.html", enunciado=Problema.enunciado,
                           problema=obj, media=f"{obj.media():.2f}")
