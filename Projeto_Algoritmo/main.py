from leitor import heap_10k, nano_seg, heap_10k_new
from leitor import arq_ord
import time 
from tqdm import tqdm
from gerador import gd_numb_arq
import matplotlib.pyplot as plt
import pandas as pd

import timeit
from statistics import mean

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
    c_lg = gd_numb_arq.lg.copy()
    
    # Método para captar valores de cada arquivo e salvar como lista em ds
    def capta_val(self):
        ds = {}
        for name in self.c_lg:
            path = f"/workspaces/IFMA-Codes/Projeto_Algoritmo/numb_arquives10k/rand_numb_{name}.csv"
            ds[name] = pd.read_csv(path, header=None)[0].tolist()
        return ds
    
    def med_time(self):
        # Looping de somatório e média de tempo por arquivo
        for item in self.time_arq:
            # Salva tempo médio individual e adiciona em new_times
            self.new_times[item] = ( sum(self.time_arq[item][-30:]) / (len(self.time_arq[item])) )
    
    # Método de execução do algoritmo (40 vezes por arquivo) e funções posteriores
    def progresso_ord(self):
        
        ds = self.capta_val() # Chama método capta_val e guarda no dicionário ds
        start_cpu = time.process_time_ns() # Starta tempo com I/O (tempo de espera)
        start = time.perf_counter_ns() # Starta tempo de CPU (sem I/O)
        
        # Looping de ordenação dos arquivos
        for i in tqdm(range(0, 15), desc="Progresso de ordenação:", position=0):
            # Repetindo ordenação em cada arquivo
            for j in range(0, 40):
                #self.time_arq[self.c_lg[i]].append(heap_10k(i)) # Adicionando tempo individual em time_arq
                self.time_arq[self.c_lg[i]].append(heap_10k_new(ds[self.c_lg[i]])) # Adicionando tempo individual em time_arq
                
             
        end = time.perf_counter_ns() # Finaliza tempo com I/O (tempo de espera)
        end_cpu = time.process_time_ns() # Finaliza tempo de CPU (sem I/O)
                
        self.med_time() # Chama método de média de tempos
            
        print(f"Tempo de execução com I/O: {nano_seg(end - start)} s   ou   {end - start} ns")
        print(f"Tempo de execução apenas de CPU: {nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")
        self.graf_continuo() # Chama método de gráfico contínuo
        self.graf_med() # Chama método de gráfico de média
        #print(self.new_times)
        return self.time_arq # Retorna todos os tempos salvos em time_arq

    def progresso_ord_new(self):
        files = self.c_lg[:15]    # lista de 15 nomes
        time_arq = {name: [] for name in files}

        io_start  = time.perf_counter_ns()
        cpu_start = time.process_time_ns()

        # enumerate devolve (idx, name)
        for idx, name in tqdm(list(enumerate(files)), desc="Progresso de ordenação:"):
            for _ in range(40):
                t0 = time.perf_counter_ns()
                heap_10k(idx)            # passa o índice como antes
                t1 = time.perf_counter_ns()
                time_arq[name].append(t1 - t0)

        io_end  = time.perf_counter_ns()
        cpu_end = time.process_time_ns()

        # médias em ns
        new_times = {name: mean(times) for name, times in time_arq.items()}

        delta_io  = io_end  - io_start
        delta_cpu = cpu_end - cpu_start
        print(f"Tempo total (I/O incluído): {nano_seg(delta_io)} s   |   {delta_io} ns")
        print(f"Tempo só CPU:              {nano_seg(delta_cpu)} s   |   {delta_cpu} ns")

        # guarda no objeto e desenha gráficos
        self.time_arq  = time_arq
        self.new_times = new_times
        self.graf_continuo()
        self.graf_med()

        return time_arq



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
        plt.figure(figsize=(24, 14)) # Define tamanho da figura/gráfico

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
        plt.scatter(self.new_times.keys(), self.new_times.values(), color="green", alpha=0.5)
        plt.title('Média de Tempo Por Arquivo')
        plt.xlabel('Arquivos Desordenados')
        plt.ylabel('Tempo Médio de Execução (s)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    ord = Ordena_Numb() # Criando instância da classe
    ord.progresso_ord() # Chamando método (HeapSort) otimizado da classe instanciada
    ord.progresso_ord_new() # Chamando método (HeapSort) não otimizado da classe instanciada
    #heap_10k(14)
