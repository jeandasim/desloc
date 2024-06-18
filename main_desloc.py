import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

def load_dat_file(file):
    lines = file.readlines()[16:32306]  # Alterado para ler até a linha 32306

    # Parsear os dados
    data = np.array([list(map(float, line.decode().split())) for line in lines])

    X = data[:, 0]
    Y = data[:, 1]
    dX = data[:, 3]
    dY = data[:, 4]
    dZ = data[:, 5]

    return X, Y, dX, dY, dZ

def plot_graphs(X, Y, dX, dY, dZ):
    fig, axes = plt.subplots(1, 3, figsize=(12, 6))
    
    # Gráfico dX com colormap 'RdYlBu'
    norm_dX = Normalize(vmin=np.min(dX), vmax=np.max(dX))
    sc1 = axes[0].scatter(X, Y, c=dX, cmap='RdYlBu', norm=norm_dX)
    axes[0].set_title('Deslocamento em X (dX)')
    fig.colorbar(sc1, ax=axes[0])

    # Gráfico dY com colormap 'RdYlBu'
    norm_dY = Normalize(vmin=np.min(dY), vmax=np.max(dY))
    sc2 = axes[1].scatter(X, Y, c=dY, cmap='RdYlBu', norm=norm_dY)
    axes[1].set_title('Deslocamento em Y (dY)')
    fig.colorbar(sc2, ax=axes[1])

    # Gráfico dZ com colormap 'gist_rainbow'
    norm_dZ = Normalize(vmin=np.min(dZ), vmax=np.max(dZ))
    sc3 = axes[2].scatter(X, Y, c=dZ, cmap='gist_rainbow', norm=norm_dZ)
    axes[2].set_title('Deslocamento em Z (dZ)')
    fig.colorbar(sc3, ax=axes[2])

    return fig, np.max(dX), np.max(dY), np.max(dZ)

# Configuração da página do Streamlit
st.title("Visualizador de Arquivos .DAT")

# Carregar o arquivo .DAT
uploaded_file = st.file_uploader("Carregar Arquivo .DAT", type="DAT")

if uploaded_file is not None:
    X, Y, dX, dY, dZ = load_dat_file(uploaded_file)
    fig, max_dX, max_dY, max_dZ = plot_graphs(X, Y, dX, dY, dZ)

    # Exibir os gráficos
    st.pyplot(fig)

    # Exibir os valores máximos de deslocamento
    st.write(f"Valor máximo de deslocamento em X: {max_dX}")
    st.write(f"Valor máximo de deslocamento em Y: {max_dY}")
    st.write(f"Valor máximo de deslocamento em Z: {max_dZ}")
