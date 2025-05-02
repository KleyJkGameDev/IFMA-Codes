#import gerador as gd
from gerador import gd_numb_arq
import pandas as pd
import time
import os
import csv
from tqdm import tqdm
#import functools

#def timed(func): # Para usar adicione @timed acima de cada def
#    """Decorator que mede e imprime o tempo de execução."""
#    @functools.wraps(func)
#    def wrapper(*args, **kwargs):
#        start = time.perf_counter()
#        result = func(*args, **kwargs)
#        end = time.perf_counter()
#        print(f"[TIMER] {func.__name__!r} levou {end - start:.4f} s")
#        return result
#    return wrapper    


def heapify(arr, n, i):
    largest = i
    left  = 2*i + 1
    right = 2*i + 2

    # Verifica se filho esquerdo é maior que o pai
    if left < n and arr[left] > arr[largest]:
        largest = left
    # Verifica se filho direito é maior que o maior até agora
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Se o maior não for o nó i, trocamos e reaplicamos heapify recursivamente
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

#@timed        
def heapsort(arr):
    n = len(arr)
    # 1) Construir o max-heap:
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    # 2) Ordenar retirando o maior para o fim:
    for end in range(n-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # leva o maior (raiz) para a posição end
        heapify(arr, end, 0)                # refaz heap no prefixo [0..end-1]

    return arr

def nano_seg(nano):
    s = (nano/1_000_000_000)
    return s

#@timed
def heap_10k(num_arq):
    ds_10k = pd.read_csv(f"/workspaces/IFMA-Codes/Projeto_Algoritmo/numb_arquives10k/rand_numb_{gd_numb_arq.lg[num_arq]}.csv", header=None)
    vetor_10k = ds_10k.values.flatten().tolist()
    
    #print(f"Antes: {vetor_10k[:10]}")
    #start = time.perf_counter_ns()
    start_cpu = time.process_time_ns()
    hp = heapsort(vetor_10k.copy())
    #end = time.perf_counter_ns()
    end_cpu = time.process_time_ns()
    #tempo = nano_seg(end - start)
    ins_arq_ord = arq_ord()
    ins_arq_ord.grava_numb(hp)
    tempo_cpu = nano_seg(end_cpu - start_cpu)
    #print(f"Depois: {hp[:10]}")
    #print(f"Tempo de execução com I/O: {nano_seg(end - start)} s   ou   {end - start} ns")
    #print(f"Tempo de execução apenas de CPU: {nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")
    #print(hp[:10])
    return tempo_cpu
    

#if __name__ == "__main__": # recomendado para execução no próprio script
#    heap_10k()

class arq_ord(gd_numb_arq):
    #print("TESTA EXECUÇÃO NÃO PLANEJADA DE ARQ_ORD EM LEITOR.PY") #########
    pasta_destin = "/workspaces/IFMA-Codes/Projeto_Algoritmo/ordenados_10k" # especificar a pasta
    os.makedirs(pasta_destin, exist_ok=True) # verificar se a pasta existe, senão, criar uma
    contador = 0
    total_f = 15
    def grava_numb(self, hp):
        line_bar = tqdm(total=self.total_f, desc="Gravando números ordenados", position=1)
        while(self.contador < self.total_f):
            print("TESTA EXECUÇÃO NÃO PLANEJADA DE ARQ_ORD.GRAVA_NUMB EM GERADOR.PY")

            caminho_arquivo = os.path.join(self.pasta_destin, f"rand_numb_{self.lg[self.contador]}.csv") # incrementar o nome do arquivo à pasta especificada
            #print(caminho_arquivo)

            with open(caminho_arquivo, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                #writer.writerow(["numeros"])
                for numero in hp:
                    writer.writerow([numero])
            
            if self.contador != 15:
                #print(f"ARQUIVO {gd.gd_numb_arq.lg[self.contador]} TOTALMENTE ORDENADO E GRAVADO")
                line_bar.update(1)
                contador+=1
            else:
                line_bar.close()
                break

        #print(f"Arquivos salvos em: {caminho_arquivo}")
        line_bar.close()
        
class arq_ord_new(gd_numb_arq):
    pasta_destin = "/workspaces/IFMA-Codes/Projeto_Algoritmo/ordenados_10k"
    os.makedirs(pasta_destin, exist_ok=True)

    def grava_numb(self, hp):
        total_files = len(self.lg)      # 15
        total_lines = len(hp)           # número de elementos em hp

        # 1) Barra de arquivos (position=0)
        bar_files = tqdm(
            total=total_files,
            desc="Arquivos",
            position=0,
            leave=True,
            dynamic_ncols=True
        )

        # 2) Barra de linhas (position=1)
        bar_lines = tqdm(
            total=total_lines,
            desc="Linhas",
            position=1,
            leave=False,
            dynamic_ncols=True
        )

        for idx in range(total_files):
            caminho = os.path.join(
                self.pasta_destin,
                f"rand_numb_{self.lg[idx]}.csv"
            )
            with open(caminho, "w", newline="") as csvfile:
                writer = csv.writer(csvfile)

                # antes de escrever cada arquivo, resetamos a barra de linhas
                bar_lines.reset()

                for numero in hp:
                    writer.writerow([numero])
                    bar_lines.update(1)

            # avançamos a barra de arquivos só depois de terminar o arquivo
            bar_files.update(1)

        # fechamos as barras
        bar_lines.close()
        bar_files.close()

        print("Todos os arquivos foram gravados.")
