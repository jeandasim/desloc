import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def load_dat_file(file):
    lines = file.readlines()[16:32306]  # Alterado para ler até a linha 32306
    # Parsear os dados
    data = np.array([list(map(float, line.decode().split())) for line in lines])
    X = data[:, 0]
    Y = data[:, 1]
    dZ = data[:, 5]
    return X, Y, dZ

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
st.title("FLAC3D: Comparação de subsidência .DAT")

# Carregar os arquivos .DAT
uploaded_file1 = st.file_uploader("Carregar Primeiro Arquivo .DAT", type="DAT")
uploaded_file2 = st.file_uploader("Carregar Segundo Arquivo .DAT", type="DAT")

if uploaded_file1 is not None and uploaded_file2 is not None:
    X1, Y1, dZ1 = load_dat_file(uploaded_file1)
    X2, Y2, dZ2 = load_dat_file(uploaded_file2)

    fig = plot_comparison(X1, Y1, dZ1, X2, Y2, dZ2)

    # Exibir os gráficos
    st.pyplot(fig)

    # Exibir os valores máximos de deslocamento
    st.write(f"Valor máximo de deslocamento em Z para o primeiro arquivo: {np.min(dZ1)}")
    st.write(f"Valor máximo de deslocamento em Z para o segundo arquivo: {np.min(dZ2)}")

