import os
import random
import csv
from tqdm import tqdm  # Barra de progresso
import numpy as np

class gd_numb_arq():
    #print("TESTA EXECUÇÃO NÃO PLANEJADA DE GD_NUMB_ARQ EM GERADOR.PY") ###############
    pasta_destin = "/workspaces/IFMA-Codes/Projeto_Algoritmo/numb_arquives10k" # especificar a pasta
    os.makedirs(pasta_destin, exist_ok=True) # verificar se a pasta existe, senão, criar uma

    #lg = ["ln1", "ln2", "ln3", "ln4", "ln5", "ln6", "ln7", "ln8", "ln9", "ln10", "ln11", "ln12", "ln13", "ln14", "ln15"]

    #l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
    
    l = [v for v in range(10_000, 160_000, 10_000)]

    lg = [f"ln{i}" for i in range(1, 16)]
    

    def lista_algo(self):
        
        algo_novo = {
            #nome: [random.sample(range(1, 1_000_000), valor)] for nome, valor in zip(self.lg, self.l)
            nome: [np.random.randint(0, 1_000_000, size=valor, dtype=np.int64)] for nome, valor in zip(self.lg, self.l)
        }
        
        return algo_novo


    def gera_arquivos(self):
        contador = 0
        #print("TESTA EXECUÇÃO NÃO PLANEJADA DE GD_NUMB_ARQ.GERA_ARQUIVO EM GERADOR.PY") #############
        while(contador < 15):

            caminho_arquivo = os.path.join(self.pasta_destin, f"rand_numb_{self.lg[contador]}.csv") # incrementar o nome do arquivo à pasta especificada
            print(caminho_arquivo)
            rand_numb = self.lista_algo()
            
            with open(caminho_arquivo, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                #writer.writerow(["numeros"])
                for numero in tqdm(rand_numb[self.lg[contador]], desc="Gerando números", unit="linha"):
                    writer.writerow(numero)
            print(contador)
            if contador != 15:
                contador+=1
            else:
                break

        print(f"Arquivos salvos em: {caminho_arquivo}")
        
        
    def limpa_terminal():
        if os.name == 'nt':      # Windows
            os.system('cls')
        else:                    # Linux, macOS, etc.
            os.system('clear')

if __name__ == "__main__":
    ins = gd_numb_arq()
    ins.gera_arquivos()
            