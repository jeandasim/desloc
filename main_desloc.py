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

def plot_individual_graphs(X, Y, dX, dY, dZ, title_suffix):
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Gráfico dX com colormap 'RdYlBu'
    norm_dX = Normalize(vmin=np.min(dX), vmax=np.max(dX))
    sc1 = axes[0].scatter(X, Y, c=dX, cmap='RdYlBu', norm=norm_dX)
    axes[0].set_title(f'Deslocamento em X (dX) {title_suffix}')
    fig.colorbar(sc1, ax=axes[0])

    # Gráfico dY com colormap 'RdYlBu'
    norm_dY = Normalize(vmin=np.min(dY), vmax=np.max(dY))
    sc2 = axes[1].scatter(X, Y, c=dY, cmap='RdYlBu', norm=norm_dY)
    axes[1].set_title(f'Deslocamento em Y (dY) {title_suffix}')
    fig.colorbar(sc2, ax=axes[1])

    # Gráfico dZ com colormap 'gist_rainbow'
    norm_dZ = Normalize(vmin=np.min(dZ), vmax=np.max(dZ))
    sc3 = axes[2].scatter(X, Y, c=dZ, cmap='gist_rainbow', norm=norm_dZ)
    axes[2].set_title(f'Deslocamento em Z (dZ) {title_suffix}')
    fig.colorbar(sc3, ax=axes[2])

    return fig, np.min(dX), np.min(dY), np.min(dZ)

def plot_comparison(X1, Y1, dZ1, X2, Y2, dZ2):
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Gráfico dZ vs X
    axes[0].scatter(X1, dZ1, color='red', label='Arquivo 1', s=10)
    axes[0].scatter(X2, dZ2, color='blue', label='Arquivo 2', s=10)
    axes[0].set_title('Deslocamento em Z (dZ) vs Coordenada X')
    axes[0].set_xlabel('Coordenada X')
    axes[0].set_ylabel('Deslocamento em Z (dZ)')
    axes[0].legend()

    # Gráfico dZ vs Y
    axes[1].scatter(Y1, dZ1, color='red', label='Arquivo 1', s=10)
    axes[1].scatter(Y2, dZ2, color='blue', label='Arquivo 2', s=10)
    axes[1].set_title('Deslocamento em Z (dZ) vs Coordenada Y')
    axes[1].set_xlabel('Coordenada Y')
    axes[1].set_ylabel('Deslocamento em Z (dZ)')
    axes[1].legend()

    plt.tight_layout()
    return fig

# Configuração da página do Streamlit
st.title("FLAC3D: Visualizador de subsidência .DAT")

# Carregar os arquivos .DAT
uploaded_file1 = st.file_uploader("Carregar Primeiro Arquivo .DAT", type="DAT")
uploaded_file2 = st.file_uploader("Carregar Segundo Arquivo .DAT", type="DAT")

if uploaded_file1 is not None:
    X1, Y1, dX1, dY1, dZ1 = load_dat_file(uploaded_file1)
    fig1, max_dX1, max_dY1, max_dZ1 = plot_individual_graphs(X1, Y1, dX1, dY1, dZ1, " - Arquivo 1")
    
    # Exibir os gráficos individuais do primeiro arquivo
    st.pyplot(fig1)
    st.write(f"Valor máximo de deslocamento em X para o primeiro arquivo: {max_dX1}")
    st.write(f"Valor máximo de deslocamento em Y para o primeiro arquivo: {max_dY1}")
    st.write(f"Valor máximo de deslocamento em Z para o primeiro arquivo: {max_dZ1}")

if uploaded_file2 is not None:
    X2, Y2, dX2, dY2, dZ2 = load_dat_file(uploaded_file2)
    fig2, max_dX2, max_dY2, max_dZ2 = plot_individual_graphs(X2, Y2, dX2, dY2, dZ2, " - Arquivo 2")
    
    # Exibir os gráficos individuais do segundo arquivo
    st.pyplot(fig2)
    st.write(f"Valor máximo de deslocamento em X para o segundo arquivo: {max_dX2}")
    st.write(f"Valor máximo de deslocamento em Y para o segundo arquivo: {max_dY2}")
    st.write(f"Valor máximo de deslocamento em Z para o segundo arquivo: {max_dZ2}")

if uploaded_file1 is not None and uploaded_file2 is not None:
    fig_comparison = plot_comparison(X1, Y1, dZ1, X2, Y2, dZ2)

    # Exibir os gráficos comparativos
    st.pyplot(fig_comparison)
