from flask import render_template
from main import app
from models.Autor import Autor, Formacao, Experiencia


@app.route("/autor", methods=["GET"])
def autor():
    obj = Autor(
        nome="Francisco Vaylton",
        formacoes=[Formacao("Curso", "IFCE", 2026)],
        experiencias=[Experiencia("Função", "Empresa", 2026)],
    )
    return render_template("autor.html", autor=obj)
