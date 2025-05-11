#import gerador as gd
from gerador import gd_numb_arq
import pandas as pd
import time
import os
import csv
from tqdm import tqdm
from numba import njit
import numpy as np
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

 # VERSÃO MAIS OTIMIZADA POSSÍVEL 
@njit(cache=True,fastmath=True) # DECORATOR PARA OTIMIZADOR DE COMPILADOR
def heapsort_fast(arr):
    # Cache da referência à lista e seu tamanho
    arr_local = arr
    n = len(arr_local)

    # Função heapify iterativa (sift-down)
    def sift_down(start, end):
        root = start
        # Enquanto o filho esquerdo existir
        while True:
            child = 2 * root + 1
            if child >= end:
                break
            # Seleciona o maior entre filho esquerdo e direito
            right = child + 1
            if right < end and arr_local[right] > arr_local[child]:
                child = right
            # Se o root já é maior que o maior filho, terminamos
            if arr_local[root] >= arr_local[child]:
                break
            # Senão, faz swap e continua descendo
            arr_local[root], arr_local[child] = arr_local[child], arr_local[root]
            root = child

    # 1) Construir max-heap em O(n)
    # Começamos do último pai até a raiz
    for start in range(n // 2 - 1, -1, -1):
        sift_down(start, n)

    # 2) Extrair máximo e refazer heap no prefixo reduzido
    for end in range(n - 1, 0, -1):
        # Move o maior (raiz) para a posição 'end'
        arr_local[0], arr_local[end] = arr_local[end], arr_local[0]
        # Refaz heap no prefixo [0..end)
        sift_down(0, end)

    return arr_local


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
    #ins_arq_ord = arq_ord()
    #ins_arq_ord.grava_numb(hp)
    tempo_cpu = nano_seg(end_cpu - start_cpu)
    #print(f"Depois: {hp[:10]}")
    #print(f"Tempo de execução com I/O: {nano_seg(end - start)} s   ou   {end - start} ns")
    #print(f"Tempo de execução apenas de CPU: {nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")
    #print(hp[:10])
    return tempo_cpu


def heap_10k_new(vetor):
    start_cpu = time.process_time_ns()
    #hp = heapsort(vetor.copy())
    #heapsort(vetor.copy())
    #heapsort(vetor)
    heapsort_fast(vetor)
    end_cpu = time.process_time_ns()
    tempo_cpu = nano_seg(end_cpu - start_cpu)
    return tempo_cpu

@njit(nogil=True, cache=True, fastmath=True)
def selection_sort(A):
    n = A.shape[0]
    arr = A            # referência local
    for i in range(n - 1):
        min_idx = i
        ai = arr[i]
        # percorre apenas uma vez, cache de arr[j] em 'v'
        for j in range(i + 1, n):
            v = arr[j]
            if v < ai:
                ai = v
                min_idx = j
        if min_idx != i:
            # swap manual usando o cache 'ai'
            arr[min_idx] = arr[i]
            arr[i] = ai
    return arr        # já ordenado in-place


def select_10k(vetor):
    start_cpu = time.process_time_ns()
    selection_sort(vetor)
    end_cpu = time.process_time_ns()
    tempo_cpu = nano_seg(end_cpu - start_cpu)
    return tempo_cpu
    

#if __name__ == "__main__": # recomendado para execução no próprio script
#    heap_10k()

class arq_ord(gd_numb_arq):
    #print("TESTA EXECUÇÃO NÃO PLANEJADA DE ARQ_ORD EM LEITOR.PY") #########
    pasta_destin = "/workspaces/IFMA-Codes/Projeto_Algoritmo/ordenados_10k" # especificar a pasta
    os.makedirs(pasta_destin, exist_ok=True) # verificar se a pasta existe, senão, criar uma
    contador = 0
    def __init__(self, lg, pasta_destin):
        pasta_destin = "/workspaces/IFMA-Codes/Projeto_Algoritmo/ordenados_10k"
        self.lg = lg
        self.pasta_destin = pasta_destin
        self.contador = 0
        self.bar = tqdm(total=len(lg), desc="Gravando", position=2)

    def grava_numb(self, hp):
        name = self.lg[self.contador]                             # pega o nome correto
        path = os.path.join(self.pasta_destin, f"rand_numb_{name}.csv")
        with open(path, "w", newline="") as f:
            writer = csv.writer(f)
            for x in hp:
                writer.writerow([int(x)])
        self.contador += 1
        self.bar.update(1)
    def close(self):
        self.bar.close()

        
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
