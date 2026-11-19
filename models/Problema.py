class Problema:
    enunciado = ("Leia o nome de um aluno e suas três notas. Calcule a média "
                 "aritmética e informe se o aluno está aprovado (média >= 7) "
                 "ou reprovado.")

    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def media(self):
        return (self.nota1 + self.nota2 + self.nota3) / 3

    def situacao(self):
        return "Aprovado" if self.media() >= 7 else "Reprovado"
