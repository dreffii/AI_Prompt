# animated_title.py
import streamlit as st

def show_animated_title():
    st.markdown("""
    <h1 style='
        text-align: center; 
        font-family: "Arial Black", sans-serif; 
        font-size: 3em; 
        color: #FFFFFF;
        text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF;
        animation: lightning 1.2s infinite;
    '>
    ⚡ AI Prompt Generator by Oak Sopheaktra ⚡
    </h1>

    <style>
    @keyframes lightning {
        0% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; opacity: 1; }
        10% { text-shadow: 0 0 20px #00FFFF, 0 0 40px #00FFFF; opacity: 1; }
        20% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; opacity: 0.9; }
        30% { text-shadow: 0 0 25px #00FFFF, 0 0 50px #00FFFF; opacity: 1; }
        40% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; opacity: 0.95; }
        50% { text-shadow: 0 0 30px #00FFFF, 0 0 60px #00FFFF; opacity: 1; }
        60% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; opacity: 0.9; }
        70% { text-shadow: 0 0 25px #00FFFF, 0 0 50px #00FFFF; opacity: 1; }
        100% { text-shadow: 0 0 5px #00FFFF, 0 0 10px #00FFFF; opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)
