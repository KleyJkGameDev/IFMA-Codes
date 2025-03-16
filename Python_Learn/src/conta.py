import datetime
class Conta:

    _total_contas = 0
    __slots__ = ["__titular", "__idade", "__numero", "__saldo", "__limite", "__cpf", "__historico"]

    def __init__(self, cliente, numero, saldo, limite = 12000):
        self.__titular = cliente.nome
        self.__idade = cliente.idade
        self.__numero = numero
        self.__saldo = saldo
        self.__limite = limite
        self.__cpf = cliente.cpf
        Conta._total_contas += 1
        self.__historico = History()

    def read_saldo(self):
        return self.__saldo
    def read_numero(self):
        return self.__numero
    def read_titular(self):
        return self.__titular
    def read_idade(self):
        return self.__idade
    @staticmethod
    def get_totalContas():
        print(f" --> | Total de contas: {Conta._total_contas} |")
    
    def deposito(self, valor):
        self.__saldo += valor
        self.__historico.transacoes.append(f"Depósito: {valor} | Data: {datetime.datetime.today()}")
    def saque(self, valor):
        if (valor > self.saldo):
            return False
        else:
            self.__saldo -= valor
            self.__historico.transacoes.append(f"Saque: {valor} | Data: {datetime.datetime.today()}")
            return True
        
    def transfere(self, conta, valor):
        if (valor <= self.__saldo):
            conta.deposito(valor)
            self.__saldo -= valor
            self.__historico.transacoes.append(f"Transferência: {valor} | Destino: {conta.__titular} | Data: {datetime.datetime.today()}")
            return True
        else:
            return False
    
    def toString(self):
        print("\t------------------------ Conta Bancária -------------------------\t")
        print(f"\t|titular: {self.read_titular()}\t|Idade: {self.read_idade()}\t|Número: {self.read_numero()}\t|Saldo: {self.read_saldo()}\t|")
        print(f"\t|CPF: {self.__cpf} \t|")
        print(f"\t|{self.__historico.toString()} |")
        print("\t-----------------------------------------------------------------\t\n")

class History:
    def __init__(self):
        self.data_aberta = datetime.datetime.today()
        self.transacoes = []

    def toString(self):
        print(f"\t| --> Data de Abertura: {self.data_aberta} \t|")
        print("\t| --> Transações: ")
        for t in self.transacoes: print(f"\t|- {t}\t |")
        
#Executar classe em si própria
#from cliente import Cliente
#if __name__ == "__main__":
#    cli = Cliente("kleytinn", "28374389", 18)
#    conta = Conta(cli, 1001, 1000)
#    conta.toString()