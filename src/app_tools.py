import streamlit as st
import os
from utils import Citation


def load_citation(model_parameters: dict[str, any]) -> None:

    model_formula = model_parameters["model"]["formula"]
    model_description = model_parameters["description"]
    model_citation = model_parameters["citation_cod"]

    st.write(f"Model formula: {model_formula}")
    st.write(f"Model description: {model_description}")

    citation = Citation(model_citation)

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