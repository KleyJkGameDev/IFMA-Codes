import gerador as gd
import pandas as pd
import time
#from tqdm import tqdm
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
    for end in (n-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]  # leva o maior (raiz) para a posição end
        heapify(arr, end, 0)                # refaz heap no prefixo [0..end-1]

    return arr

def nano_seg(nano):
    s = (nano/1_000_000_000)
    return s

#@timed
def heap_10k(num_arq):
    ds_10k = pd.read_csv(f"/workspaces/IFMA-Codes/Projeto_Algoritmo/numb_arquives10k/rand_numb_{gd.gd_numb_arq.lg[num_arq]}.csv", header=None)
    vetor_10k = ds_10k.values.flatten().tolist()
    
    #print(f"Antes: {vetor_10k[:10]}")
    start = time.perf_counter_ns()
    start_cpu = time.process_time_ns()
    hp = heapsort(vetor_10k.copy())
    end = time.perf_counter_ns()
    end_cpu = time.process_time_ns()
    tempo = [nano_seg(end - start), nano_seg(end_cpu - start_cpu)]
    #print(f"Depois: {hp[:10]}")
    #print(f"Tempo de execução com I/O: {nano_seg(end - start)} s   ou   {end - start} ns")
    #print(f"Tempo de execução apenas de CPU: {nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")
    #print(hp[:10])
    return tempo

#if __name__ == "__main__": # recomendado para execução no próprio script
#    heap_10k()
    

    