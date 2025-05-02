import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from main import Ordena_Numb as od
# --- Dados de exemplo (no seu caso, substitua pelo seu time_arq já populado) ---
st.set_page_config(page_title="Análise de Tempos de Execução", layout="wide")

# --- Preparação dos dados ---
@st.cache_data
def prepare_dataframe(data_dict):
    # transforma em dataframe long-form
    df = pd.DataFrame([
        {"Chave": chave, "Repeticao": i + 1, "Tempo": tempo}
        for chave, tempos in data_dict.items()
        for i, tempo in enumerate(tempos)
    ])
    return df

df = prepare_dataframe(od.time_arq)

# --- Título da aplicação ---
st.title("⏱️ Análise de Tempo de Execução por Repetição")

# --- Sidebar de controle ---
st.sidebar.header("Filtros")
chaves_disponiveis = df['Chave'].unique().tolist()
selecionadas = st.sidebar.multiselect(
    "Selecione quais chaves mostrar:",
    options=chaves_disponiveis,
    default=chaves_disponiveis
)

# --- Filtrar dataframe ---
if selecionadas:
    df_plot = df[df['Chave'].isin(selecionadas)]
else:
    st.warning("Nenhuma chave selecionada. Exibindo todas por padrão.")
    df_plot = df.copy()

# --- Exibir tabela de dados ---
st.subheader("Dados Filtrados")
st.dataframe(df_plot)

# --- Plotagem com Matplotlib ---
st.subheader("Gráfico de Tempo por Repetição")
fig, ax = plt.subplots(figsize=(10, 6))
for chave in df_plot['Chave'].unique():
    sub = df_plot[df_plot['Chave'] == chave]
    ax.plot(sub['Repeticao'], sub['Tempo'], marker='o', linestyle='-', label=chave)

ax.set_xlabel('Repetição')
ax.set_ylabel('Tempo de Execução (s)')
ax.set_title('Tempo por Repetição para cada Chave')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(ncol=3, fontsize='small', loc='best')

st.pyplot(fig)

# --- Fim do app ---
