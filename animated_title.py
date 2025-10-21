import streamlit as st

def show_animated_title():
    st.markdown("""
    <div class="luxury-title">
        🏛️ AI Prompt Generator by Oak Sopheaktra
    </div>

    <style>
    .luxury-title {
        position: relative;
        text-align: center;
        font-family: "Georgia", serif;
        font-size: 3em;
        color: #FFFFFF;
        text-shadow: 0 0 10px rgba(255,255,255,0.6), 0 0 20px rgba(255,255,255,0.4);
    }

    /* Sparkle pseudo-elements */
    .luxury-title::before,
    .luxury-title::after {
        content: "✨";
        position: absolute;
        font-size: 1em;
        color: #FFD700;
        opacity: 0;
        animation: sparkle 1.5s infinite;
    }

    .luxury-title::before {
        top: -20px;
        left: 20%;
        animation-delay: 0s;
    }

    .luxury-title::after {
        top: -10px;
        right: 25%;
        animation-delay: 0.8s;
    }

    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0.5) rotate(0deg);}
        50% { opacity: 1; transform: scale(1.2) rotate(20deg);}
    }
    </style>
    """, unsafe_allow_html=True)
