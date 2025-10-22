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

# --- Credit and QR code below navigation ---
st.sidebar.markdown("---")  # horizontal line
st.sidebar.markdown("**Created by Oak Sopheaktra👾**")  # your credit
# Add space for QR code
# st.sidebar.image("data/IMG_3172.PNG", use_container_width=True)

# --- Load Pages Dynamically ---
if st.session_state.page == "Prompt Generator":
    from pages.page1 import show_page_1
    show_page_1()
elif st.session_state.page == "Blank Page":
    from pages.page2 import show_page_2
    show_page_2()
