import leitor as lt
import time 
from tqdm import tqdm
from gerador import gd_numb_arq as gd

start_cpu = time.process_time_ns()
start = time.perf_counter_ns()

new_times = {}

for i in tqdm(range(0, 15), desc=f"Progresso de ordenação:"):
    for j in range(0, 10):
        #lista_tempo = lt.heap_10k(i)
        new_times[f"{gd.lg[i]}"] = lt.heap_10k(i)
        

end = time.perf_counter_ns()
end_cpu = time.process_time_ns()
print(f"Tempo de execução com I/O: {lt.nano_seg(end - start)} s   ou   {end - start} ns")
print(f"Tempo de execução apenas de CPU: {lt.nano_seg(end_cpu - start_cpu)} s   ou   {end_cpu - start_cpu} ns")

print(new_times)