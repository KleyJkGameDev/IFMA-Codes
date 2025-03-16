from func import Funcionario
from aut import Autenticavel
class Gerente(Funcionario, Autenticavel):

    def __init__(self, nome, cpf, salario, senha, qtd_func):
        super().__init__(nome, cpf, salario)
        self._senha = senha
        self._qtd_func = qtd_func
        

    def authentic(self, senha):
        if self._senha == senha:
            print("Acesso Permitido")
            return True
        else:
            print("Acesso Negado")
            return False
    def get_bonifica(self):
        #return super().get_bonifica() + 1000
        return (self._salario * 0.15)
    
    def __str__(self):
        return super().__str__()