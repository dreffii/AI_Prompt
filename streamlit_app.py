import streamlit as st

st.set_page_config(page_title="🏛️ AI Prompt Generator ✨", layout="wide")

# --- Force sidebar to appear ---
with st.sidebar:
    st.title("🧭 Navigation")
    st.markdown("""
    **Pages**
    - 🏗️ [AI Prompt Generator](1_AI_Prompt_Generator)
    - 📝 [Blank Page](2_Blank_Page)
    """)
    st.divider()
    st.markdown("Made by **Oak Sopheaktra** ✨")

# --- Main page content ---
st.title("🏛️ AI Prompt Generator by Oak Sopheaktra")

st.markdown("""
Welcome! 👋  
Use the sidebar on the left to navigate between pages:
- **AI Prompt Generator** → Generate professional architectural prompts.  
- **Blank Page** → Reserved for your future ideas or tools.
""")
