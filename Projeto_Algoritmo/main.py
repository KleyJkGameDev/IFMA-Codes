from leitor import nano_seg, heap_10k_new, arq_ord, selection_sort, heapsort_fast
from matplotlib.ticker import FuncFormatter, MaxNLocator
import time 
from tqdm import tqdm
from gerador import gd_numb_arq
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from statistics import mean
from concurrent.futures import ProcessPoolExecutor

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
    new_time_select = {
        f"ln{i}": [] for i in range(1, 16)
    }
    c_lg = gd_numb_arq.lg.copy() # nomes dos lns
    
    # Método para captar valores de cada arquivo e salvar como lista em ds
    def capta_val(self):
        ds = {}
        for name in self.c_lg:
            path = f"/workspaces/IFMA-Codes/Projeto_Algoritmo/numb_arquives10k/rand_numb_{name}.csv"
            #ds[name] = pd.read_csv(path, header=None)[0].tolist()
            #ds[name] = np.array(pd.read_csv(path, header=None)[0].tolist(), dtype=np.int64)
            ##ds[name] = pd.read_csv(path, header=None)[0]#.to_numpy(dtype=np.int64)
            # Lê a única linha do CSV como um DataFrame de 1 linha x N colunas
            ##df = pd.read_csv(path, header=None)
            # Transforma o DataFrame em um vetor numpy com dtype int64
            ##ds[name] = df.iloc[0].to_numpy(dtype=np.int64)
            ds[name] = np.fromfile(path, dtype=np.int64, sep=',')
        return ds
    
    def med_time(self):
        # Looping de somatório e média de tempo por arquivo
        for item in self.time_arq:
            # Salva tempo médio individual e adiciona em new_times
            #self.new_times[item] = ( sum(self.time_arq[item][-30:]) / (len(self.time_arq[item])) )
            self.new_times[item] = mean(self.time_arq[item][-30:])
    
    # Método de execução do algoritmo (40 vezes por arquivo) e funções posteriores
    def heap_ord(self, q_rep=40, plot=True, save=False):
        
        ds = self.capta_val() # Chama método capta_val e guarda no dicionário ds
        
        if save:
            vt = self.capta_val()
            arq = arq_ord(self.c_lg, pasta_destin="")
            for integer in range(0,15):
                v_aux = heapsort_fast(vt[self.c_lg[integer]])
                arq.grava_numb(v_aux)
            arq.close()
        
        if plot:
            start_cpu = time.process_time_ns() # Starta tempo com I/O (tempo de espera)
            start = time.perf_counter_ns() # Starta tempo de CPU (sem I/O)
            # Looping de ordenação dos arquivos
            for i in tqdm(range(0, 15), desc="Progresso de ordenação:", position=1):
                # Repetindo ordenação em cada arquivo
                    
                for j in range(0, q_rep):
                    self.time_arq[self.c_lg[i]].append(heap_10k_new(ds[self.c_lg[i]])) # Adicionando tempo individual em time_arq
                        
            end = time.perf_counter_ns() # Finaliza tempo com I/O (tempo de espera)
            end_cpu = time.process_time_ns() # Finaliza tempo de CPU (sem I/O)
                    
            self.med_time() # Chama método de média de tempos
                
            print(f"\n(HeapSort) - Tempo de execução com I/O: {nano_seg(end - start)} s   ou   {end - start} ns")
            print(f"(HeapSort) - Tempo de execução apenas de CPU: {nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")
            
            self.graf_continuo_geral(unidade="ns") # Chama método de gráfico contínuo
            self.graf_med() # Chama método de gráfico de média
            self.graf_pontual()
            #print(f"Lista LN1: {ds["ln1"][:20]}")
        else:
            print("função apenas para compilação")
            for i in range(0, 15):
                # Repetindo ordenação em cada arquivo
                for j in range(0, 10):
                    heap_10k_new(ds[self.c_lg[i]])
            
        return self.time_arq # Retorna todos os tempos salvos em time_arq
    

    def select_ord(self, q_rep=40, parallel=False):
        ds = self.capta_val()

        # Marca início de wall-time e CPU-time
        t_wall_start = time.perf_counter_ns()
        t_cpu_start  = time.process_time_ns()

        if parallel:
            # ProcessPoolExecutor para tirar vantagem de múltiplos núcleos
            with ProcessPoolExecutor() as exe:
                futures = []
                for name, arr in ds.items():
                    for _ in range(q_rep):
                        arr_copy = arr.copy()
                        futures.append((name, exe.submit(selection_sort, arr_copy)))
                # coleta resultados e mede tempo
                for name, fut in tqdm(futures, desc="Parallel sorting", total=len(futures)):
                    fut.result()  # força execução
                    # aqui podemos usar wall-time pra cada
                    self.new_time_select[name].append( 
                        (time.perf_counter_ns() - t_wall_start) / 1e9
                    )
        else:
            # Versão sequencial super enxuta
            for name in tqdm(self.c_lg, desc="Ordenando arquivos"):
                arr = ds[name]
                for _ in range(q_rep):
                    arr_copy = arr.copy()
                    t0 = time.perf_counter_ns()
                    selection_sort(arr_copy)
                    delta_s = (time.perf_counter_ns() - t0) / 1e9
                    self.new_time_select[name].append(delta_s)

        # mede fim
        t_cpu_end   = time.process_time_ns()
        t_wall_end  = time.perf_counter_ns()

        # imprime relatórios
        print(f"(SelectSort) Wall-time total: {(t_wall_end - t_wall_start)/1e9:.6f} s")
        print(f"(SelectSort) CPU-time total : {(t_cpu_end  - t_cpu_start )/1e9:.6f} s")
        self.graf_sel() # Chama método de gráfico de média

        return self.new_time_select


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
        
    def grafico_comparativo_log(self):
        labels = list(self.c_lg)  # ['ln1', 'ln2', ..., 'ln15']
        heap_means = [self.new_times[label] for label in labels]  # Em nanosegundos
        select_means = [np.mean(self.new_time_select[label]) * 1e9 for label in labels]  # Convertendo de segundos para ns

        x = np.arange(len(labels))  # Posições das labels no eixo X
        width = 0.35  # Largura das barras

        fig, ax = plt.subplots(figsize=(12, 6))
        bars1 = ax.bar(x - width/2, heap_means, width, label='HeapSort (ns)')
        bars2 = ax.bar(x + width/2, select_means, width, label='SelectionSort (ns)')

        ax.set_xlabel('Arquivos')
        ax.set_ylabel('Tempo médio (ns)')
        ax.set_title('Comparação de desempenho: HeapSort vs SelectionSort')
        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.legend()
        ax.grid(True, linestyle='--', alpha=0.5)

        ax.set_yscale('log')

        plt.tight_layout()
        plt.show()
        
    def graf_comp_norm(self):
        labels = list(self.c_lg)  # ['ln1', 'ln2', ..., 'ln15']
        heap_means = [self.new_times[label] for label in labels]  # Em nanosegundos
        select_means = [np.mean(self.new_time_select[label]) * 1e9 for label in labels]  # Convertendo de segundos para ns

        heap_norm = heap_means / np.max(heap_means)
        select_norm = select_means / np.max(select_means)

        fig, ax = plt.subplots()
        x = np.arange(len(labels))
        width = 0.35

        ax.bar(x - width/2, heap_norm, width, label='HeapSort (normalizado)')
        ax.bar(x + width/2, select_norm, width, label='SelectionSort (normalizado)')

        ax.set_xticks(x)
        ax.set_xticklabels(labels)
        ax.set_ylabel('Tempo relativo')
        ax.set_title('Desempenho relativo HeapSort vs SelectionSort')
        ax.legend()
        plt.grid(True, linestyle='--', alpha=0.5)
        plt.tight_layout()
        plt.show()


    def graf_comp_sub(self):
        labels = list(self.c_lg)  # ['ln1', 'ln2', ..., 'ln15']
        heap_means = [self.new_times[label] for label in labels]  # Em nanosegundos
        select_means = [np.mean(self.new_time_select[label]) * 1e9 for label in labels]  # Convertendo de segundos para ns

        fig, axs = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

        axs[0].scatter(labels, heap_means, color='steelblue')
        axs[0].set_title('HeapSort (ns)')
        axs[0].set_ylabel('Tempo médio (ns)')
        axs[0].grid(True, linestyle='--', alpha=0.5)

        axs[1].scatter(labels, select_means, color='darkorange')
        axs[1].set_title('SelectionSort (ns)')
        axs[1].set_ylabel('Tempo médio (ns)')
        axs[1].set_xlabel('Arquivos')
        axs[1].grid(True, linestyle='--', alpha=0.3)

        plt.tight_layout()
        plt.show()
        #plt.scatter(linewidths=0.9)


    def graf_continuo_geral(self, unidade='micro', y_bins=18):
        """
        Plota os tempos (em ns) convertidos para μs (ou ms) para melhor visualização.
        unidade: 'ns' | 'micro' | 'ms'
        """
        # fator de conversão de nanosegundos
        fatores = {'ns': 1, 'micro': 1e3, 'ms': 1e6}
        fator = fatores.get(unidade, 1e3)  # padrão para μs
        
        fig, ax = plt.subplots(figsize=(12, 7))

        series = [t for t in self.time_arq.values() if t]
        max_reps = max(len(t) for t in series) if series else 0

        for chave, tempos in self.time_arq.items():
            if not tempos:
                continue
            tempos_conv = [t / fator for t in tempos]
            rep = list(range(1, len(tempos_conv) + 1))
            ax.plot(rep, tempos_conv, marker='o', linestyle='-', label=chave)

        ax.set_title(f'Tempo de Execução por Repetição ({unidade})')
        ax.set_xlabel('Repetição')
        ax.set_ylabel(f'Tempo de Execução ({unidade})')

        if max_reps > 0:
            ax.set_xlim(1, max_reps)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=10))

        # Aqui configuramos o Y para até y_bins ticks
        ax.yaxis.set_major_locator(MaxNLocator(nbins=y_bins))

        # Mantém formatação com duas casas decimais
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.3f}'))

        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(ncol=3, fontsize='small', loc='best')
        fig.tight_layout()
        plt.show()


    def graf_sel(self):
        labels = list(self.new_time_select.keys())
        # calcula tempo médio por arquivo
        means = [np.mean(self.new_time_select[name]) for name in labels]

        plt.figure()
        plt.scatter(labels, means)           # usa cores default, sem especificar
        plt.xlabel('Arquivo')
        plt.ylabel('Tempo médio (s)')
        plt.title('Selection Sort – Tempo médio de execução')
        plt.xticks(rotation=45, ha='right')
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
    ord.heap_ord(plot=False)
    ord.heap_ord(q_rep=40, save=False) # Chamando método (HeapSort) otimizado da classe instanciada
    #ord.progresso_ord_new() # Chamando método (HeapSort) não otimizado da classe instanciada
    ord.select_ord(q_rep=1)
    ord.grafico_comparativo_log()
    ord.graf_comp_norm()
    ord.graf_comp_sub()
    #heap_10k(14)
