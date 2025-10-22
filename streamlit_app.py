import streamlit as st

st.set_page_config(page_title="🏛️ AI Prompt Generator ✨", layout="wide")

# --- Sidebar Navigation ---
with st.sidebar:
    st.title("🧭 Navigation")
    page = st.radio(
        "Go to:",
        ["🏗️ AI Prompt Generator", "📝 Blank Page"],
        label_visibility="collapsed"
    )
    st.divider()
    st.markdown("Made by **Oak Sopheaktra** ✨")

# --- Page Switching ---
if page == "🏗️ AI Prompt Generator":
    st.switch_page("pages/1_Prompt_Generator")   # ✅ Correct file name (no .py)
elif page == "📝 Blank Page":
    st.switch_page("pages/2_Blank_Page")         # You can add this later
