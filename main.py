from flask import Flask
from flask_login import LoginManager
from sqlalchemy.orm import sessionmaker
from werkzeug.security import generate_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ATIVIDADE_FLASK'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'admin_login'

from models import Aluno, Administrador
from models.Conexao import engine, Base

Session = sessionmaker(bind=engine)

from controllers.ProblemaController import *
from controllers.AutorController import *
from controllers.AdminController import *


if __name__ == "__main__":
    Base.metadata.create_all(engine)
    # cria o administrador padrão na primeira execução
    session = Session()
    if not session.query(Administrador.Administrador).first():
        session.add(Administrador.Administrador(
            None, "Administrador", "admin", generate_password_hash("admin")))
        session.commit()
    app.run(debug=True, port=5002)
