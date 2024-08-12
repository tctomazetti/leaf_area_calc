import streamlit as st
import os
from utils import Citation, Leaf, get_model_parameters, get_terms, mlr_calc, simple_reg_calc


def collect_model_info(
        fully_models: dict[str, any],
        specie: str,
        variety: str,
        feature: str,
        cod: str
) -> tuple[str, str, str, dict[str, any]]:
    model_parameters = get_model_parameters(fully_models, specie, variety, feature, cod)
    formula = model_parameters["model"]["formula"]
    description = model_parameters["description"]
    citation_cod = model_parameters["citation_cod"]
    terms = get_terms(model_parameters)
    return formula, description, citation_cod, terms


def load_model_description(formula: str, description: str) -> None:
    st.write(f"Model formula: {formula}")
    st.write(f"Model description: {description}")


def load_citation(citation_cod) -> None:
    citation = Citation(citation_cod)

    st.markdown(f"[{citation.title}]({citation.url})")

    # Additional description
    st.write("Click the link above to access the full article.")

    if os.path.exists(citation.pdf_file):
        with open(citation.pdf_file, "rb") as pdf_file:
            pdf_data = pdf_file.read()
        
        # Message indicating success with a document emoji
        st.write("The PDF is available for download. 📄")

        # Download button for the PDF
        st.download_button(
            label="Download PDF",
            data=pdf_data,
            file_name=f"{citation.name}.pdf",
            mime="application/pdf"
        )
    else:
        # Show message or disabled button
        st.write("The PDF is not available at the moment. 😞")
        st.download_button(
            label="Download PDF (Unavailable)",
            data=None,
            disabled=True
        )


def leaf_area_calc(leaf: Leaf, feature: str, terms: dict[str, any]) -> None:
    if st.button('Calculate Leaf Area'):
        if "mlr" in feature:
            area = mlr_calc(leaf, terms)
        elif "length" in feature and "width" in feature:
            x_value = leaf.length * leaf.width
            area = simple_reg_calc(x_value, terms) if x_value is not None else 0
        else:
            x_value = leaf.length or leaf.width or leaf.alv
            area = simple_reg_calc(x_value, terms) if x_value is not None else 0
        if area is not None:
            st.success(f'The estimated leaf area is {area:.2f} cm²')
        
        if leaf.alv is not None:
            ldi = leaf.calc_ldi()
            st.success(f"Leaf Deformation Index: {ldi}")


def get_leaf(formula: str) -> Leaf:
    st.subheader("Enter the data required by the model")
    length = st.number_input("Leaf length (L)", min_value=0.0, step=0.1) if "* L" in formula else None
    width = st.number_input("Leaf width (W)", min_value=0.0, step=0.1) if "* W" in formula else None
    right_lv = st.number_input("Length of right vein (LVr)", min_value=0.0, step=0.1) if "* alv" in formula else None
    left_lv = st.number_input("Length of left vein (LVl)", min_value=0.0, step=0.1) if "* alv" in formula else None
    return Leaf(length, width, right_lv, left_lv)
