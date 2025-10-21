import streamlit as st

st.set_page_config(
    page_title="AI Prompt Generator by Oak Sopheaktra",
    layout="wide"
)

st.title("AI Prompt Generator by Oak Sopheaktra")

# Sidebar page selection
page = st.sidebar.selectbox(
    "Select a page",
    ["Home", "Prompt Generator", "Concept Development"]
)

if page == "Home":
    st.write("""
    Welcome! This app helps you generate high-quality AI prompts for architectural renderings and concept development.

    Use the sidebar to navigate between pages:

    - **Prompt Generator**: Generate standard architectural prompts.
    - **Concept Development**: Generate creative concept prompts to explore variations of your building designs.

    All dropdown options, site contexts, and prompt generation logic are managed in `utils.py` for easy maintenance.
    """)
elif page == "Prompt Generator":
    # import the page code here
    import pages._1_Prompt_Generator as pg
elif page == "Concept Development":
    import pages._2_Concept_Development as cd
