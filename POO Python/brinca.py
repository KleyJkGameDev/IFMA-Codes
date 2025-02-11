import numpy as np

np.random.seed(42)

lista = []
for i in range(0, 20):
    lista.append(np.random.randint(0, 30))

def maior(l):
    ma = me = l[0]
    par = []
    impar = []
    soma = 0
    for i in l:
        soma += i
        if i > ma:
            ma = i
        if i < me:
            me = i
        if (i % 2 == 0):
            par.append(i)
        if (i % 2 != 0):
            impar.append(i)

    return print(f"Maior: {ma}\nMenor: {me}\nPar: {par}\nImpar: {impar}\nMédia: {soma/len(lista)}")

def kwa(**kwargs):
    for i, value in kwargs.items():
        print(f"{i} = {value}")

dic = {"Nome":["Kleytinn", "Jonas", "Igu", "Pedro"],
       "Idade": [20, 19, 18, 17]}

print(dic.values())

arq = open("testando.txt", "w")
#for i in range(0, len(dic["Nome"])):
for i in dic["Nome"]:
    arq.write(f"{i}\n")

arq.close()
arq = open("testando.txt", "r")
print(arq.read())
arq.close()

#kwa(**dic)
#print(lista)
#maior(lista)