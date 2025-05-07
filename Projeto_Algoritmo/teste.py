from statistics import mean
import random

lista = ["kleytinn", "pedro", "igu", "david", "igu"]
tempo = {
    label: [] for label in lista
}

print(tempo)
l = [1,2,3,4,5]

s = [nome for nome in tempo.keys() if nome]
name = None
r = {
    name: [valor] for name, valor in zip(tempo.keys(), l)
}
#print(r)

d = [v for v in range(10, 160, 10)]

n = [f"ln{i}" for i in range(1, 16)]

zip(n, d)
for i, j in zip(n, d): print(f"n: {i} | d: {j}")

a = random.sample(range(1, 1000000), d[0])
#print(f"valores de D[0]: {a}")

algo = {
    nome: [random.sample(range(1,1_000), valor) ] for nome, valor in zip(n, d)
}
teste = {"teste": [random.sample(range(1, 100), 10)]}
teste = {nome: [random.sample(range(1, 1_000_000), valor)] for nome, valor in zip(n, d)}
print(teste)

for i, j in algo.items():
    print(f"{i}: {j[0][:10]}")
    
for nome, valor in zip(n, d):
    print(valor)