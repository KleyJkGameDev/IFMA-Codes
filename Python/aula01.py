import pandas as pd
import matplotlib.pyplot as plt

alunos = {
    "NOME": ["Kleyton", "Igor", "Jonas", "David"],
    "IDADE": [19, 18, 17, 18],
    "NOTA": [9.5, 9.0, 8.5, 7.5],
    "FACULDADE": ["IFMA", "UEMA", "UFMA", "UEMA"]
}

dados = pd.read_csv("/home/kley/Desktop/IFMA Codes/Python/athlete_events.csv")

dataframe = pd.DataFrame(alunos)
#dataframe["NOME"][0] = "Junior"
#esc = int(input("Escolha quem quer editar: "))
#
#for i in range(0, len(dataframe)):
#    if(esc == i):
#        name = str(input("Nome: "))
#        dataframe["NOME"][esc] = name    
#        idade = int(input("Idade: "))
#        dataframe["IDADE"][esc] = idade
#        nota = float(input("Nota: "))
#        dataframe["NOTA"][esc] = nota
#        facul = str(input("Faculdade: "))
#        dataframe["FACULDADE"][esc] = facul
#nick = pd.Series([None])
#for i in range(0, dataframe.shape[0]):
#    nick[i] = dataframe["NOME"][i]
#print(f" -- Nomes: -- \n",nick)
#print(dataframe.head())
#print(dataframe.loc[dataframe["FACULDADE"]=="UEMA"])
#univ = list(dict.fromkeys(dataframe["FACULDADE"]))
#print(f"\nLista de Universidades: {univ}")
#dados.rename(columns={"Name":"Nome", "Sex":"Sexo", "City":"Cidade", "Age":"Idade"}, inplace=True)
#dados.rename(level={"Football":"Futebol"})
#print(dados.head(8))
#dados.hist(column="Age", bins=15, grid=False)
#dataframe.boxplot(column=["IDADE", "NOTA"])
#dataframe.hist(column="IDADE", bins=5)
#faltantes_percentual = (dados.isnull().sum() / len(dados["ID"]))*100
#dados["Medal"].fillna("Nenhuma", inplace=True)
#dados["Height"].fillna(dados["Height"].mean(), inplace=True)
#dados["Weight"].fillna(dados["Weight"].mean(), inplace=True)
#dados["Age"].fillna(dados["Age"].mean(), inplace=True)
#print(dados[["Age", "Height", "Weight"]])

