# animated_title.py
import streamlit as st

def show_animated_title():
    st.markdown("""
    <h1 style='
        text-align: center;
        font-family: "Georgia", serif;
        font-size: 3em;
        color: #FFFFFF;
        text-shadow: 0 0 10px rgba(255,255,255,0.6), 0 0 20px rgba(255,255,255,0.4);
        animation: luxuryGlow 2s ease-in-out infinite alternate;
    '>
    🏛️ AI Prompt Generator by Oak Sopheaktra
    </h1>

    <style>
    @keyframes luxuryGlow {
        0% { text-shadow: 0 0 10px rgba(255,255,255,0.6), 0 0 20px rgba(255,255,255,0.4); }
        100% { text-shadow: 0 0 20px rgba(255,255,255,0.8), 0 0 40px rgba(255,255,255,0.6); }
    }
    </style>
    """, unsafe_allow_html=True)
