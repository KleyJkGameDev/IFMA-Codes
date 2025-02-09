import numpy as np
import matplotlib as plt

np.random.seed(42) #criar semente para itens random, sempre iguais
ages = np.random.randint(low=15, high=70, size=40)

labels = [] #rótulos

for i in ages:
    if i < 30:
        labels.append(0) # add 0 na lista
    else:
        labels.append(1) # add 1 na lista

plt.scatter(ages, labels, color="red")
plt.show()