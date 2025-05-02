#import leitor as lt
from leitor import heap_10k, nano_seg
import time 
from tqdm import tqdm
#import gerador as gd
from gerador import gd_numb_arq
#from leitor import arq_ord as aq
import matplotlib.pyplot as plt

class Ordena_Numb():

    new_times = {}
    time_arq = {
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

    def progresso_ord(self):
        
        start_cpu = time.process_time_ns()
        start = time.perf_counter_ns()
        
        for i in tqdm(range(0, 15), desc="Progresso de ordenação:", position=0):
            for j in range(0, 40):
                #lista_tempo = lt.heap_10k(i)
                #new_times[f"{gd.lg[i]}"] = lt.heap_10k(i)
                self.time_arq[gd_numb_arq.lg[i]].append(heap_10k(i))
                

        for item in self.time_arq:
            self.new_times[item] = ( sum(self.time_arq[item]) / (len(self.time_arq[item])) )
            
        end = time.perf_counter_ns()
        end_cpu = time.process_time_ns()
        print(f"Tempo de execução com I/O: {nano_seg(end - start)} s   ou   {end - start} ns")
        print(f"Tempo de execução apenas de CPU: {nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")
        self.graf_continuo()
        self.graf_med()
        print(self.new_times)
        return self.time_arq

    def graf_pontual(self):
        # Expandir todos os tempos individuais para o gráfico
        x = []
        y = []

        for tentativa, tempos in self.time_arq.items():
            for tempo in tempos:
                x.append(tentativa)
                y.append(tempo)

        # Criar o gráfico
        plt.figure(figsize=(10, 6))
        plt.scatter(x, y, color='green', alpha=0.7)
        plt.title('Todos os Tempos por Tentativa')
        plt.xlabel('Tentativas')
        plt.ylabel('Tempo de Execução (s)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    #graf_ind()

    def graf_continuo(self):
        plt.figure(figsize=(12, 7))

        for chave, tempos in self.time_arq.items():
            # ignora listas vazias
            if not tempos:
                continue
            # gera [1, 2, 3,…] até len(tempos)
            rep = list(range(1, len(tempos) + 1))
            plt.plot(rep, tempos, marker='o', linestyle='-', label=chave)

        plt.title('Tempo de Execução por Repetição para Cada Chave')
        plt.xlabel('Repetição')
        plt.ylabel('Tempo de Execução (s)')
        plt.xticks(range(1, max(len(t) for t in self.time_arq.values()) + 1))
        plt.grid(True, linestyle='--', alpha=0.5)

        # Se quiser evitar uma legenda gigante, você pode:
        # plt.legend(ncol=3, fontsize='small', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.legend(ncol=3, fontsize='small', loc='best')

        plt.tight_layout()
        plt.show()

    def graf_med(self):
        plt.scatter(self.new_times.keys(), self.new_times.values(), color="green", alpha=0.8)
        plt.title('Média de Tempo Por Arquivo')
        plt.xlabel('Arquivos Desordenados')
        plt.ylabel('Tempo Médio de Execução (s)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()


ord = Ordena_Numb()
ord.progresso_ord()
# MODULARIZAR O CÓDIGO