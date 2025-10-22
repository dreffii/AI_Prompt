import streamlit as st

st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to:", ["Prompt Generator", "Page 2"])

if page == "Prompt Generator":
    from pages.page1_prompt_generator import show_prompt_page
    show_prompt_page()
else:
    from pages.page2_blank import show_page2
    show_page2()
