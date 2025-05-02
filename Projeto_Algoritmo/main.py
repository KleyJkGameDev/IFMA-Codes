from leitor import heap_10k, nano_seg
from leitor import arq_ord
import time 
from tqdm import tqdm
from gerador import gd_numb_arq
import matplotlib.pyplot as plt

class Ordena_Numb():

    new_times = {} # Dicionário com nome e tempo médio de cada arquivo
    time_arq = { # Dicionário com nome e todos os tempos de execução de cada arquivo
        "ln1":[],
        "ln2":[],
        "ln3":[],
        "ln4":[],
        "ln5":[],
        "ln6":[],
        "ln7":[],
        "ln8":[],
        "ln9":[],
        "ln10":[],
        "ln11":[],
        "ln12":[],
        "ln13":[],
        "ln14":[],
        "ln15":[]
    }

    # Método de execução do algoritmo (40 vezes por arquivo) e funções posteriores
    def progresso_ord(self):
        
        start_cpu = time.process_time_ns() # Starta tempo com I/O (tempo de espera)
        start = time.perf_counter_ns() # Starta tempo de CPU (sem I/O)
        
        # Looping de ordenação dos arquivos
        for i in tqdm(range(0, 15), desc="Progresso de ordenação:", position=0):
            # Repetindo ordenação em cada arquivo
            for j in range(0, 40):
                self.time_arq[gd_numb_arq.lg[i]].append(heap_10k(i)) # Adicionando tempo individual em time_arq
                
        # Looping de somatório e média de tempo por arquivo
        for item in self.time_arq:
            # Salva tempo médio individual e adiciona em new_times
            self.new_times[item] = ( sum(self.time_arq[item]) / (len(self.time_arq[item])) )
            
        end = time.perf_counter_ns() # Finaliza tempo com I/O (tempo de espera)
        end_cpu = time.process_time_ns() # Finaliza tempo de CPU (sem I/O)
        print(f"Tempo de execução com I/O: {nano_seg(end - start)} s   ou   {end - start} ns")
        print(f"Tempo de execução apenas de CPU: {nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")
        self.graf_continuo() # Chama método de gráfico contínuo
        self.graf_med() # Chama método de gráfico de média
        #print(self.new_times)
        return self.time_arq # Retorna todos os tempos salvos em time_arq

    # Método de Gráfico Scatter - tempos pontuais de cada arquivo
    def graf_pontual(self):
        # Expandir todos os tempos individuais para o gráfico
        x = []
        y = []

        # Looping de adição de chaves e valores em listas x, y
        for tentativa, tempos in self.time_arq.items(): # Para cada chave e valor em time_arq
            for tempo in tempos: # Para cada valor na lista de valores na chave atual de time_arq
                x.append(tentativa) # Adiciona nome da chave em x
                y.append(tempo) # Adiciona valor da chave em y

        # Criar o gráfico
        plt.figure(figsize=(10, 6)) # Define tamanho da figura/gráfico
        plt.scatter(x, y, color='green', alpha=0.7) # Define eixos, cor e tamanho
        plt.title('Todos os Tempos por Tentativa')
        plt.xlabel('Tentativas')
        plt.ylabel('Tempo de Execução (s)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    # Método de Gráfico Contínuo - Tempo por Tentativa de todos os arquivos
    def graf_continuo(self):
        plt.figure(figsize=(12, 7)) # Define tamanho da figura/gráfico

        for chave, tempos in self.time_arq.items(): # Para cada chave e valor em time_arq
            # ignora listas vazias
            if not tempos:
                continue
            # gera [1, 2, 3,…] até len(tempos)
            rep = list(range(1, len(tempos) + 1))
            plt.plot(rep, tempos, marker='o', linestyle='-', label=chave) # Define eixos x e y, tipo de marcador e linha

        plt.title('Tempo de Execução por Repetição para Cada Chave')
        plt.xlabel('Repetição')
        plt.ylabel('Tempo de Execução (s)')
        # Definindo número e local das marcações no eixo x
        plt.xticks(range(1, max(len(t) for t in self.time_arq.values()) + 1)) 
        plt.grid(True, linestyle='--', alpha=0.5)

        # Para evitar uma legenda gigante usar:
        # plt.legend(ncol=3, fontsize='small', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.legend(ncol=3, fontsize='small', loc='best')

        plt.tight_layout()
        plt.show()

    # Método de Gráfico(Scatter) de Média de Tempo de Cada Arquivo
    def graf_med(self):
        plt.scatter(self.new_times.keys(), self.new_times.values(), color="green", alpha=0.8)
        plt.title('Média de Tempo Por Arquivo')
        plt.xlabel('Arquivos Desordenados')
        plt.ylabel('Tempo Médio de Execução (s)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    #ord = Ordena_Numb() # Criando instância da classe
    #ord.progresso_ord() # Chamando método da classe instanciada
    heap_10k(14)
