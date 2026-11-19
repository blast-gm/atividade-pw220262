from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from main import app, login_manager, Session
from models import Aluno, Administrador


@login_manager.user_loader
def load_user(user_id):
    session = Session()
    return session.get(Administrador.Administrador, int(user_id))

@app.route("/admin/register", methods=["GET", "POST"])
def admin_register():
    if request.method == "POST":
        session = Session()
        if session.query(Administrador.Administrador).filter_by(
                usuario=request.form.get("usuario")).first():
            return render_template("admin/register.html", erro="Esse usuário já existe.")
        admin = Administrador.Administrador(
            None, request.form.get("nome"), request.form.get("usuario"),
            generate_password_hash(request.form.get("senha"))
        )
        session.add(admin)
        session.commit()
        return redirect(url_for("admin_login"))
    return render_template("admin/register.html")

@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        session = Session()
        admin = session.query(Administrador.Administrador).filter_by(
            usuario=request.form.get("usuario")).first()
        if admin and check_password_hash(admin.senha, request.form.get("senha")):
            login_user(admin)
            return redirect(url_for("admin_alunos"))
        return render_template("admin/login.html", erro="Usuário ou senha inválidos.")
    return render_template("admin/login.html")


@app.route("/admin/logout")
def admin_logout():
    logout_user()
    return redirect(url_for("admin_login"))


@app.route("/admin/alunos")
@login_required
def admin_alunos():
    session = Session()
    alunos = session.query(Aluno.Aluno).all()
    return render_template("alunos/list.html", alunos=alunos)


@app.route("/admin/aluno/cadastro")
@login_required
def admin_aluno_cadastro():
    return render_template("alunos/cad.html")


@app.route("/admin/aluno/editar/<int:id>")
@login_required
def admin_aluno_editar(id):
    session = Session()
    aluno = session.get(Aluno.Aluno, id)
    if not aluno:
        return redirect(url_for("admin_alunos"))
    return render_template("alunos/cad.html", aluno=aluno)


@app.route("/admin/aluno/salvar", methods=["POST"])
@login_required
def admin_aluno_salvar():
    session = Session()
    f = request.form
    if f.get("id"):
        aluno = session.get(Aluno.Aluno, int(f["id"]))
        if aluno:
            aluno.nome = f["nome"]
            aluno.nota1 = float(f["nota1"])
            aluno.nota2 = float(f["nota2"])
            aluno.nota3 = float(f["nota3"])
            session.commit()
    else:
        aluno = Aluno.Aluno(None, f["nome"], float(f["nota1"]),
                            float(f["nota2"]), float(f["nota3"]))
        session.add(aluno)
        session.commit()
    return redirect(url_for("admin_alunos"))


@app.route("/admin/aluno/deletar/<int:id>")
@login_required
def admin_aluno_deletar(id):
    session = Session()
    aluno = session.get(Aluno.Aluno, id)
    if aluno:
        session.delete(aluno)
        session.commit()
    return redirect(url_for("admin_alunos"))
