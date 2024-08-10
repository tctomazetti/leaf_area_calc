import json
import streamlit as st

# Função para carregar modelos de um arquivo JSON
def load_models(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)
    return data

# Caminho para o arquivo JSON
models_file = 'src/data/models.json'

# Carregar dados de modelos
data = load_models(models_file)

# Obter lista de espécies
species_list = list(data.keys())

# Selecionar uma espécie
species = st.selectbox('Select species', species_list)

# Obter lista de variedades para a espécie selecionada
varieties = list(data[species].keys())

# Selecionar uma variedade
variety = st.selectbox('Select variety', varieties)

# Obter modelos disponíveis para a variedade selecionada
models_for_variety = data[species][variety]

# Se existir mais de um modelo, permitir seleção
model_names = list(models_for_variety.keys())
selected_model = st.selectbox('Select model', model_names)

# Exibir a fórmula e descrição do modelo selecionado
model_info = models_for_variety[selected_model]
model_formula = model_info.get('model', 'Model not available')
model_description = model_info.get('description', 'Description not available')

st.write(f'Model formula: {model_formula}')
st.write(f'Model description: {model_description}')

# Função para calcular a área foliar
def calculate_leaf_area(L, W, aLV):
    if model_formula:
        # Executa a expressão do modelo usando os valores L, W e aLV
        try:
            LA = eval(model_formula, {"L": L, "W": W, "aLV": aLV})
            return LA
        except Exception as e:
            st.error(f"Error calculating leaf area: {e}")
    else:
        st.error('No model formula available for the selected model')
    return None

# Entrada de dados do usuário
st.subheader('Enter the data required by the model')
L = st.number_input('Leaf length (L)', min_value=0.0, step=0.1)
W = st.number_input('Leaf width (W)', min_value=0.0, step=0.1)
aLV = st.number_input('Average length of lateral veins (aLV)', min_value=0.0, step=0.1)

# Calcular área foliar
if st.button('Calculate Leaf Area'):
    area = calculate_leaf_area(L, W, aLV)
    if area is not None:
        st.success(f'The estimated leaf area is {area:.2f} cm²')
