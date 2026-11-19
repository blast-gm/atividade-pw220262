from sqlalchemy import Column, Integer, Float, String
from models.Conexao import Base


class Aluno(Base):
    __tablename__ = "aluno"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100))
    nota1 = Column(Float)
    nota2 = Column(Float)
    nota3 = Column(Float)

    def __init__(self, id, nome, nota1, nota2, nota3):
        self.id = id
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    @property
    def media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3
