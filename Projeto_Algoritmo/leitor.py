#import gerador as gd
from gerador import gd_numb_arq
import time
import os
import csv
from tqdm import tqdm
from numba import njit
 

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


def nano_seg(nano):
    s = (nano/1_000_000_000)
    return s


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
        self.bar = tqdm(total=len(lg), desc="Gravando", position=0)

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

        
