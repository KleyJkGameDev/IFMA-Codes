import os
import random
import csv
from tqdm import tqdm  # Barra de progresso

class gd_numb_arq():
    pasta_destin = "/workspaces/IFMA-Codes/Projeto_Algoritmo/numb_arquives10k" # especificar a pasta
    os.makedirs(pasta_destin, exist_ok=True) # verificar se a pasta existe, senão, criar uma

    contador = 0

    lg = ["ln1", "ln2", "ln3", "ln4", "ln5", "ln6", "ln7", "ln8", "ln9", "ln10", "ln11", "ln12", "ln13", "ln14", "ln15"]

    l = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]

    algo = {
        l[0]: random.sample(range(1, 1_000_000), 10_000),
        l[1]: random.sample(range(1, 1_000_000), 20_000),
        l[2]: random.sample(range(1, 1_000_000), 30_000),
        l[3]: random.sample(range(1, 1_000_000), 40_000),
        l[4]: random.sample(range(1, 1_000_000), 50_000),
        l[5]: random.sample(range(1, 1_000_000), 60_000),
        l[6]: random.sample(range(1, 1_000_000), 70_000),
        l[7]: random.sample(range(1, 1_000_000), 80_000),
        l[8]: random.sample(range(1, 1_000_000), 90_000),
        l[9]: random.sample(range(1, 1_000_000), 100_000),
        l[10]: random.sample(range(1, 1_000_000), 110_000),
        l[11]: random.sample(range(1, 1_000_000), 120_000),
        l[12]: random.sample(range(1, 1_000_000), 130_000),
        l[13]: random.sample(range(1, 1_000_000), 140_000),
        l[14]: random.sample(range(1, 1_000_000), 150_000),
    }

    def gera_arquivos(self):
        while(contador < 15):

            caminho_arquivo = os.path.join(self.pasta_destin, f"rand_numb_{self.lg[contador]}.csv") # incrementar o nome do arquivo à pasta especificada
            print(caminho_arquivo)

            with open(caminho_arquivo, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                #writer.writerow(["numeros"])
                for numero in tqdm(self.algo[self.l[contador]], desc="Gerando números", unit="linha"):
                    writer.writerow([numero])
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


            