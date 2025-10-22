import streamlit as st
from animated_title import show_animated_title

st.set_page_config(page_title="🏛️ AI Prompt Generator ✨", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("🧭 Navigation")

# Save selected page in session_state
if "page" not in st.session_state:
    st.session_state.page = "Prompt Generator"

page = st.sidebar.radio(
    "Go to:",
    ["Prompt Generator", "Blank Page"],
    index=0 if st.session_state.page == "Prompt Generator" else 1,
    label_visibility="collapsed"
)

st.session_state.page = page

