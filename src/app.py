import streamlit as st
from utils import load_model_info
from app_tools import load_citation, load_model_description, collect_model_info, leaf_area_calc, get_leaf


MODEL_INFO = load_model_info()
SPECIES_LIST = list(MODEL_INFO.keys())

def select_model_app() -> tuple[str, ...]:
    specie = st.selectbox("Select specie", SPECIES_LIST, index=None)

    # Select the variety according with the specie
    if specie is not None:
        varieties = list(MODEL_INFO[specie].keys())
        variety = st.selectbox("Select variety", varieties, index=None)
    else:
        st.selectbox("Select variety", [], index=None, disabled=True, key="disabled_variety")
        # st.info("Please select a species first to enable variety selection.")
        variety = None

    # Select the feature measure according with the variety
    if variety is not None:
        feature_measure = list(MODEL_INFO[specie][variety].keys())
        feature_measure = st.selectbox("Select feature", feature_measure, index=None)
    else:
        st.selectbox("Select feature", [], index=None, disabled=True, key="disabled_feature")
        # st.info("Please select a variety first to enable feature selection.")
        feature_measure = None

    # Select the model_cod according with the feature_measure
    if feature_measure is not None:
        models_cod = list(MODEL_INFO[specie][variety][feature_measure].keys())
        model_cod = st.selectbox("Select model", models_cod, index=None)
    else:
        st.selectbox("Select model", [], index=None, disabled=True, key="disabled_model")
        model_cod = None
    
    return specie, variety, feature_measure, model_cod


def result_model_app(model_input: tuple[str, ...]) -> None:
    specie, variety, feature_measure, model_cod = model_input
    formula, description, citation_cod, terms = collect_model_info(
        MODEL_INFO, specie, variety, feature_measure, model_cod
    )
    load_model_description(formula, description)
    load_citation(citation_cod)

    leaf = get_leaf(formula)
    leaf_area_calc(leaf, feature_measure, terms)

if __name__ == "__main__":
    model_input = select_model_app()
    if model_input[-1] is not None:
        result_model_app(model_input)
