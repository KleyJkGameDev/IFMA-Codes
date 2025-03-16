class Autenticavel:
    def authentic(self, senha):
        if self._senha == senha:
            print("Login realizado")
            return True
        else:
            print("Senha incorreta")
            return False