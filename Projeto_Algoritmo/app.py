import streamlit as st
import pandas as pd
import numpy as np
import time
from statistics import mean
from tqdm import tqdm
from leitor import heap_10k_new, select_10k
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MaxNLocator

# Supondo que heap_10k_new e select_10k estejam definidos em outro módulo
# from sorting_algorithms import heap_10k_new, select_10k

class OrdenaNumb:
    def __init__(self, file_paths, labels):
        self.file_paths = file_paths
        self.labels = labels
        self.time_arq = {label: [] for label in labels}
        self.new_times = {}

    @st.cache_data
    def capta_val(_self):  # Renomeado para evitar hashing de 'self'
        ds = {}
        for label, path in zip(_self.labels, _self.file_paths):
            data = pd.read_csv(path, header=None)[0].to_numpy(dtype=np.int64)
            ds[label] = data
        return ds

    def med_time(self):
        for label, times in self.time_arq.items():
            if times:
                self.new_times[label] = mean(times)

    def heap_ord(self, iterations=40):
        ds = self.capta_val()
        for label in self.labels:
            arr = ds[label].copy()
            for _ in range(iterations):
                start_ns = time.perf_counter_ns()
                # chamar algoritmo
                heap_10k_new(arr)
                delta = time.perf_counter_ns() - start_ns
                self.time_arq[label].append(delta)
        self.med_time()
        return self.time_arq

    def select_ord(self, iterations=40):
        ds = self.capta_val()
        for label in self.labels:
            arr = ds[label].copy()
            for _ in range(iterations):
                start_ns = time.perf_counter_ns()
                # chamar algoritmo
                select_10k(arr)
                delta = time.perf_counter_ns() - start_ns
                self.time_arq[label].append(delta)
        self.med_time()
        return self.time_arq

    def plot_continuous(self, unit='μs', y_bins=18):
        fatores = {'ns': 1, 'μs': 1e3, 'ms': 1e6}
        fator = fatores.get(unit, 1e3)
        fig, ax = plt.subplots(figsize=(10, 5))
        series = [t for t in self.time_arq.values() if t]
        max_reps = max(len(t) for t in series) if series else 0
        for label, times in self.time_arq.items():
            if not times:
                continue
            conv = [t / fator for t in times]
            ax.plot(range(1, len(conv)+1), conv, marker='o', label=label)
        ax.set_title(f'Tempo de Execução por Repetição ({unit})')
        ax.set_xlabel('Repetição')
        ax.set_ylabel(f'Tempo ({unit})')
        if max_reps > 0:
            ax.set_xlim(1, max_reps)
            ax.xaxis.set_major_locator(MaxNLocator(integer=True, nbins=10))
        ax.yaxis.set_major_locator(MaxNLocator(nbins=y_bins))
        ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.3f}'))
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(ncol=3, fontsize='small', loc='best')
        st.pyplot(fig)

    def plot_mean(self, unit='μs'):
        fatores = {'ns': 1, 'μs': 1e3, 'ms': 1e6}
        fator = fatores.get(unit, 1e3)
        labels = list(self.new_times.keys())
        means = [self.new_times[label] / fator for label in labels]
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.scatter(labels, means, color='green', alpha=0.6)
        ax.set_title(f'Média de Tempo Por Arquivo ({unit})')
        ax.set_xlabel('Arquivo')
        ax.set_ylabel(f'Tempo Médio ({unit})')
        ax.grid(True, linestyle='--', alpha=0.5)
        plt.xticks(rotation=45)
        st.pyplot(fig)

# App Streamlit
st.title("Comparação de Algoritmos de Ordenação")

# Upload de arquivos CSV
uploaded = st.file_uploader("Faça upload dos arquivos CSV", type="csv", accept_multiple_files=True)
if uploaded:
    paths = []
    labels = []
    for file in uploaded:
        paths.append(file)
        labels.append(file.name)
    ordena = OrdenaNumb(paths, labels)

    alg = st.sidebar.selectbox("Escolha o algoritmo", ["HeapSort", "Selection Sort"])
    iters = st.sidebar.slider("Número de repetições", min_value=1, max_value=100, value=40)
    unit = st.sidebar.selectbox("Unidade de tempo", ["ns", "μs", "ms"])

    if st.sidebar.button("Executar"):    
        with st.spinner("Executando ordenações..."):
            if alg == "HeapSort":
                ordena.heap_ord(iters)
            else:
                ordena.select_ord(iters)
        st.success("Concluído!")

        st.subheader("Gráfico Contínuo")
        ordena.plot_continuous(unit)

        st.subheader("Gráfico de Médias")
        ordena.plot_mean(unit)
