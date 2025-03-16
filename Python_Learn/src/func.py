import abc
class Funcionario(abc.ABC):

    def __init__(self, nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario

    @abc.abstractmethod
    def get_bonifica(self):
        return (self._salario * 0.1)
    
    def __str__(self):
        return (f"<Instância de {self.__class__.__name__}; Endereço: {id(self)}>")