
def criaConta(nome, saldo):
    conta = {
        "Nome":nome,
        "Saldo":saldo
    }
    return conta
def deposita(conta, valor):
    conta["Saldo"] += valor

c1 = criaConta("kleytinn", 1200) # objeto instanciado
c2 = criaConta("Pedro", 1000)
c3 = criaConta("Igor", 1500)

deposita(c1, 2000)
print(c1)