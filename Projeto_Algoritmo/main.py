import leitor as lt
import time 
from tqdm import tqdm
import gerador as gd

start_cpu = time.process_time_ns()
start = time.perf_counter_ns()

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


for i in tqdm(range(0, 15), desc="Progresso de ordenação:", position=0):
    for j in range(0, 10):
        #lista_tempo = lt.heap_10k(i)
        #new_times[f"{gd.lg[i]}"] = lt.heap_10k(i)
        time_arq[gd.gd_numb_arq.lg[i]].append(lt.heap_10k(i))
        
        
#print(time_arq)

for item in time_arq:
    new_times[item] = ( sum(time_arq[item]) / (len(time_arq[item])) )
    
end = time.perf_counter_ns()
end_cpu = time.process_time_ns()
print(f"Tempo de execução com I/O: {lt.nano_seg(end - start)} s   ou   {end - start} ns")
print(f"Tempo de execução apenas de CPU: {lt.nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")

print(new_times)

# LEMBRAR DE TRATAR OS TEMPOS REGISTRADOS
# GUARDAR OS TEMPOS EM UMA LISTA E TIRAR A MÉDIA
# SÓ DEPOIS ADICIONAR NO DIC new_times