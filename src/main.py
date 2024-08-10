import streamlit as st
import polars as pl

# Lista de variedades a partir do artigo
varieties = [
    "Aromera", "Baron", "Bronner", "Calandro", "Calardis Blanc", 
    "Felicia", "ABS15", "ABS24", "Helios", "Prior", "Regent"
]

# Modelos por variedade (simplificado)
models = {
    "Aromera": "LA = 0.99 * L * W + 2.76",
    "Baron": "LA = 0.24 * L^2 + 0.32 * W^2 + 0.47 * aLV^2 + 1.85",
    "Bronner": "LA = 0.44 * L^2 + 0.30 * W^2 + 0.46 * aLV^2 + 0.12",
    # Adicione os demais modelos aqui
}

# Função para calcular a área foliar
def calculate_leaf_area(variety, L, W, aLV):
    if variety == "Aromera":
        return 0.99 * L * W + 2.76
    elif variety == "Baron":
        return 0.24 * L**2 + 0.32 * W**2 + 0.47 * aLV**2 + 1.85
    elif variety == "Bronner":
        return 0.44 * L**2 + 0.30 * W**2 + 0.46 * aLV**2 + 0.12
    # Adicione os demais cálculos de modelo aqui
    return None

# Configuração do Streamlit
st.title('Calculadora de Área Foliar de Videiras')
st.header('Selecione a espécie e variedade para calcular a área foliar')

# Menu suspenso para seleção de espécie
species = st.selectbox('Selecione a espécie', ['Grapevine (Vitis vinifera)'])

# Menu suspenso para seleção de variedade
variety = st.selectbox('Selecione a variedade', varieties)

# Menu suspenso para seleção do modelo
model_formula = models.get(variety, "Modelo não disponível")
st.write(f'Modelo selecionado para {variety}: {model_formula}')

# Entrada de dados do usuário
st.subheader('Insira os dados requeridos pelo modelo')
L = st.number_input('Leaf length (L)', min_value=0.0, step=0.1)
W = st.number_input('Leaf width (W)', min_value=0.0, step=0.1)
aLV = st.number_input('Comprimento médio das nervuras laterais (aLV)', min_value=0.0, step=0.1)

# Calcular área foliar
if st.button('Calcular Área Foliar'):
    area = calculate_leaf_area(variety, L, W, aLV)
    if area is not None:
        st.success(f'A área foliar estimada é {area:.2f} cm²')
    else:
        st.error('Modelo para a variedade selecionada não está disponível')

