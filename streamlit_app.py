import streamlit as st

st.set_page_config(
    page_title="AI Prompt Generator by Oak Sopheaktra",
    layout="wide"
)

st.title("AI Prompt Generator by Oak Sopheaktra")

st.markdown("""
Welcome! This app helps you generate high-quality AI prompts for architectural renderings and concept development.

Use the sidebar to navigate between pages:

- **Prompt Generator**: Generate standard architectural prompts.
- **Concept Development**: Generate creative concept prompts to explore variations of your building designs.

All dropdown options, site contexts, and prompt generation logic are managed in `utils.py` for easy maintenance.
""")

st.info("Select a page from the left sidebar to get started.")
