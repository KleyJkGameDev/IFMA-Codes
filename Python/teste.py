import pandas as pd
#import matplotlib.pyplot as plt

dataset = pd.read_csv("/home/kley/Desktop/IFMA Codes/Python/wine_dataset.csv")

dataset["style"] = dataset["style"].replace("red", 0) # substitui red por 0
dataset["style"] = dataset["style"].replace("white", 1) # substitui white por 1

# Separando variáveis treino(preditoras) das variáveis de teste(alvo)
alvo = dataset["style"] # alvo
preditor = dataset.drop("style", axis=1) # preditoras

# Criando os conjuntos de dados de treino e teste
from sklearn.model_selection import train_test_split
x_treino, x_teste, y_treino, y_teste = train_test_split(preditor, alvo, test_size=0.3)
   # tes_size=0.3 --> 30% dos dados serão para teste e o resto para treino

# Criação de modelo
from sklearn.ensemble import ExtraTreesClassifier
modelo = ExtraTreesClassifier(n_estimators=300)
modelo.fit(x_treino, y_treino)

# Imprimindo resultados
resultado = modelo.score(x_teste, y_teste)
print(f"Precisão: {resultado}\n")

t = list(y_teste)
#print(t)
#print(x_teste[400:410])

previsao = modelo.predict(x_teste)
#print(previsao)
cont = 0
t2 = list(previsao)
for i in range(0, len(t)):
    if t2[i] != t[i]:
        print(f"x: {t2[i]} != y: {t[i]}")
        cont += 1
print(f"\nNumero de erros: {cont}")
