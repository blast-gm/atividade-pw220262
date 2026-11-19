from sqlalchemy import Column, Integer, String
from flask_login import UserMixin
from models.Conexao import Base


class Administrador(Base, UserMixin):
    __tablename__ = "administrador"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50))
    usuario = Column(String(50), unique=True)
    senha = Column(String(200))

    def __init__(self, id, nome, usuario, senha):
        self.id = id
        self.nome = nome
        self.usuario = usuario
        self.senha = senha
