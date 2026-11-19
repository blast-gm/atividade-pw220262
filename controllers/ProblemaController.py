from flask import render_template, request
from main import app


@app.route("/")
@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    nome = request.form.get("nome")
    nota1 = float(request.form.get("nota1"))
    nota2 = float(request.form.get("nota2"))
    nota3 = float(request.form.get("nota3"))
    media = (nota1 + nota2 + nota3) / 3
    situacao = "Aprovado" if media >= 7 else "Reprovado"
    return render_template("resultado.html", nome=nome,
                           nota1=nota1, nota2=nota2, nota3=nota3,
                           media=f"{media:.2f}", situacao=situacao)
