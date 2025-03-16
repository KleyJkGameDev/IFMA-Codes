import os
import numpy as np
import pandas as pd
import scipy.stats as stats
from statsmodels.stats.diagnostic import het_breuschpagan
import statsmodels as sm

from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
import lightgbm as lgb

import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
#%matplotlib inline


import warnings
warnings.filterwarnings("ignore")

class ProcessadorDados:
    def __init__(self):
        pass

    # Função que recebe o caminho de um arquivo e retorna um dataframe do pacote pandas com os dados contidos no arquivo
    def importar_dados(self, caminho_arquivo, index_col = None, parse_dates = None):
        df = pd.read_csv(caminho_arquivo, index_col = index_col, parse_dates = parse_dates)
        return df
    
    # Função de correlação em gráfico triangular
    def correlacao(self, data, show_high = False):
        corr = data.corr() # Gerando a tabela de correlação
        # Criando um filtro para mostrar apenas correlações significativas
        if show_high == True:
            corr = corr[((corr >= .5) | (corr <= -.5)) & (corr != 1)]
        # Criando uma matriz de valores booleanos, onde os dados só aparecerão, caso o valor seja False
        mask = np.zeros_like(corr, dtype = bool)
        mask[np.triu_indices_from(mask)] = True
        fig, aux = plt.subplots(figsize=(11, 11))

        # Gerando paleta de cores
        cmap = sns.diverging_palette(240, 10, as_cmap=True)

        sns.heatmap(
            corr,
            mask=mask,  # Máscara triangular de True/False
            vmin = -2,
            vmax = 1,
            cmap = "RdBu",  # Paleta de Cores
            annot = True,  # Plotar os valores dentro das células
            square = True,  # Forçar células a serem quadradas
            linewidths = .5,  # Largura das linhas que dividem as células
            cbar_kws = {"shrink": .5}
        )
        fig.show()


        # Define a importância das variáveis para um desfecho
        def importancia(self, data = pd.DataFrame(), nomes_colunas_x = [], nome_y = [], shuffle = True, test_size = 0.3,
                        titulo_grafico = "Titulo Padrão", random_state = 0, xgb_n_estimators = 100):
            # Definindo variáveis dependentes e independentes
            X = data[nomes_colunas_x]
            y = data[nome_y]

            # Separando os dados
            X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle = shuffle,
                                                                test_size = test_size, random_state = random_state)
            
            # Instanciando e treinando o modelo com os dados de treino
            xgb = XGBRegressor(n_estimators = xgb_n_estimators)
            xgb.fit(X_train, y_train)

            # Calculando a importância e transformando os dados de retorno
            valores_importancia = xgb.feature_importances_
            feat_imp = pd.DataFrame(valores_importancia).sort_values(by = 0, ascending = False).T
            feat_imp.columns = X.columns
            feat_imp = feat_imp.T.reset_index()
            feat_imp.columns = ["Característica", "Importância para as vendas"]

            # Plotando os resultados
            fig = px.bar(feat_imp,
                         x = "Caracteristica",
                         y = "Importância para as vendas",
                         title = titulo_grafico,
                         width = 800,
                         height = 400)
            fig.update_layout(xaxis = dict(showgrid = False),
                              yaxis = dict(showgrid = False))
            return feat_imp, fig
        

        def heterocedasticidade(self, y_pred, y_test):
            # Calcular o teste de Levene
            levene_test = stats.levene(y_pred, y_test)