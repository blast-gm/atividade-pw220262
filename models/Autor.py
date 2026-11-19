class Formacao:
    def __init__(self, curso, instituicao, ano):
        self.curso = curso
        self.instituicao = instituicao
        self.ano = ano


class Experiencia:
    def __init__(self, funcao, empresa, ano):
        self.funcao = funcao
        self.empresa = empresa
        self.ano = ano


class Autor:
    def __init__(self, nome, formacoes, experiencias):
        self.nome = nome
        self.formacoes = formacoes
        self.experiencias = experiencias
