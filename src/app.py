import streamlit as st
from utils import load_model_info, get_model_parameters, get_terms, calculate_leaf_area


MODEL_INFO = load_model_info()
SPECIES_LIST = list(MODEL_INFO.keys())

specie = st.selectbox('Select species', SPECIES_LIST, index=None)

# Select the variety according with teh specie
if specie is not None:
    varieties = list(MODEL_INFO[specie].keys())
    variety = st.selectbox('Select variety', varieties, index=None)
else:
    st.selectbox('Select variety', [], index=None, disabled=True, key='disabled_variety')
    st.info('Please select a species first to enable variety selection.')
    variety = None

# Select the feature measure according with the variety
if variety is not None:
    feature_measure = list(MODEL_INFO[specie][variety].keys())
    feature_measure = st.selectbox('Select feature', feature_measure, index=None)
else:
    st.selectbox('Select feature', [], index=None, disabled=True, key='disabled_feature')
    st.info('Please select a variety first to enable feature selection.')
    feature_measure = None

# Select the model_cod according with the feature_measure
if feature_measure is not None:
    models_cod = list(MODEL_INFO[specie][variety][feature_measure].keys())
    model_cod = st.selectbox('Select model', models_cod, index=None)
else:
    st.selectbox('Select model', [], index=None, disabled=True, key='disabled_model')
    model_cod = None

if model_cod is not None:
    model_parameters = get_model_parameters(MODEL_INFO, specie, variety, feature_measure, model_cod)
    terms = get_terms(model_parameters)

    # Print the selected model description
    model_formula = model_parameters["model"]["formula"]
    model_description = model_parameters["description"]
    model_citation = model_parameters["citation_cod"]

    st.write(f"Model formula: {model_formula}")
    st.write(f"Model description: {model_description}")
    st.write(f"Model citation: {model_citation}")

    # Input user data
    st.subheader('Enter the data required by the model')
    L = st.number_input('Leaf length (L)', min_value=0.0, step=0.1)
    W = st.number_input('Leaf width (W)', min_value=0.0, step=0.1)
    aLV = st.number_input('Average length of lateral veins (aLV)', min_value=0.0, step=0.1)

    # Leaf area calculator
    if st.button('Calculate Leaf Area'):
        area = calculate_leaf_area(L, terms)
        if area is not None:
            st.success(f'The estimated leaf area is {area:.2f} cm²')
