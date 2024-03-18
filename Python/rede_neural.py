import matplotlib.pyplot as plt
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import warnings
warnings.filterwarnings("ignore")

 # SEPARANDO DADOS DO DATASET
ds = pd.read_csv("/home/kley/Desktop/IFMA Codes/Python/admission_dataset.csv")

y = ds["Chance of Admit "] # recebe a coluna target
x = ds.drop("Chance of Admit ", axis=1) # exclui a coluna target e salva o restante

x_treino, x_teste = x[0:300], x[300:]
y_treino, y_teste = y[0:300], y[300:]

 # CRIANDO ARQUITETURA DA REDE NEURAL
modelo = Sequential() # adicionar camadas de modo sequencial
        # densidade de neurônios              # nº de colunas
modelo.add(Dense(units=3, activation="relu", input_dim=7)) #ou input_dim=x_treino.shape[1]
modelo.add(Dense(units=1, activation="linear"))

 # TREINANDO REDE NEURAL 
modelo.compile(loss="mse", optimizer="metrics", metrics=["mae"])
resultado = modelo.fit(x_treino, y_treino, epochs=200, batch_size=32, validation_data=(x_teste, y_teste))

 # PLOTAR GRÁFICO DO HISTÓRICO DO TREINAMENTO
plt.plot(resultado.history["loss"])
plt.plot(resultado.history["val_loss"])
plt.title("Histórico de treinamento")
plt.ylabel("Função de custo")
plt.xlabel("Eṕocas de treinamento")
plt.legend(["Erro no treino", "Erro no teste"])
plt.show()