from aut import Autenticavel
class Cliente(Autenticavel):
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf