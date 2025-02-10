import numpy as np
import matplotlib.pyplot as plt
import math
import time
from sklearn.linear_model import LogisticRegression

start_time = time.perf_counter()

def sigmoid(x):
    a = []
    for i in x:
        a.append(1 / (1 + math.exp(-i)) ) # Ysig = 1 / (1 + e^(-x))

    return a

np.random.seed(42) #criar semente para itens random, sempre iguais
ages = np.random.randint(low=15, high=70, size=40)

labels = [] #rótulos

for i in ages:
    if i < 30:
        labels.append(0) # add 0 na lista
    else:
        labels.append(1) # add 1 na lista

#random swap (trocando valores)
for i in range(0, 3):
    r = np.random.randint(0, len(labels)-1)
    if labels[r] == 0:
        labels[r] = 1
    else:
        labels[r] = 0

model = LogisticRegression()
model.fit(ages.reshape(-1, 1), labels)
#LogisticRegression(copy_X=True, fit_intercept=True, n_jobs=None)
# y = m.x + b (m = coeficiente, x = inclinação, b = altura)
# nesse caso, Z = w1.x1 + bias --> x1 = x, w1 = m, b = bias
m = model.coef_[0][0]
b = model.intercept_[0]
x = np.arange(0, 70, 0.1)
sig = sigmoid(m * x + b)
limiar_ages = abs(b / m)

# plotar reta, ages no eixo x, equação no eixo y, cor da reta
plt.plot(x, sig, color="blue")
# plotar pontos, ages no eixo x, labels no eixo y, cor dos pontos
plt.scatter(ages, labels, color="red")
plt.axvline(x=limiar_ages, color="green", linestyle="--", label="Limiar de Decisão")
plt.title("Regressão Logística")
plt.xlabel("Idade")
plt.ylabel("Probabilidade (0 a 100%)")
plt.legend()
plt.show()
end_time = time.perf_counter()
print(f"Tempo de execução: {(end_time-start_time):.6f}s")