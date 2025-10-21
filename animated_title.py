import streamlit as st

def show_animated_title():
    st.markdown("""
    <div class="luxury-title">
        <span>🏛️</span> 
        <span>A</span><span>I</span> 
        <span>P</span><span>r</span><span>o</span><span>m</span><span>p</span><span>t</span> 
        <span>G</span><span>e</span><span>n</span><span>e</span><span>r</span><span>a</span><span>t</span><span>o</span><span>r</span> 
        <span>b</span><span>y</span> 
        <span>O</span><span>a</span><span>k</span> 
        <span>S</span><span>o</span><span>p</span><span>h</span><span>e</span><span>a</span><span>k</span><span>t</span><span>r</span><span>a</span>
    </div>

    <style>
    .luxury-title {
        text-align: center;
        font-family: "Georgia", serif;
        font-size: 3em;
        color: #000000; /* Black text */
        position: relative;
    }

    .luxury-title span {
        display: inline-block;
        animation: bounce 4s infinite; /* slower */
        animation-delay: calc(var(--i) * 0.1s);
    }

    /* Staggered bounce delay */
    .luxury-title span:nth-child(1) { --i: 0; }
    .luxury-title span:nth-child(2) { --i: 1; }
    .luxury-title span:nth-child(3) { --i: 2; }
    .luxury-title span:nth-child(4) { --i: 3; }
    .luxury-title span:nth-child(5) { --i: 4; }
    .luxury-title span:nth-child(6) { --i: 5; }
    .luxury-title span:nth-child(7) { --i: 6; }
    .luxury-title span:nth-child(8) { --i: 7; }
    .luxury-title span:nth-child(9) { --i: 8; }
    .luxury-title span:nth-child(10) { --i: 9; }
    .luxury-title span:nth-child(11) { --i: 10; }
    .luxury-title span:nth-child(12) { --i: 11; }
    .luxury-title span:nth-child(13) { --i: 12; }
    .luxury-title span:nth-child(14) { --i: 13; }
    .luxury-title span:nth-child(15) { --i: 14; }
    .luxury-title span:nth-child(16) { --i: 15; }
    .luxury-title span:nth-child(17) { --i: 16; }
    .luxury-title span:nth-child(18) { --i: 17; }
    .luxury-title span:nth-child(19) { --i: 18; }
    .luxury-title span:nth-child(20) { --i: 19; }
    .luxury-title span:nth-child(21) { --i: 20; }
    .luxury-title span:nth-child(22) { --i: 21; }
    .luxury-title span:nth-child(23) { --i: 22; }
    .luxury-title span:nth-child(24) { --i: 23; }
    .luxury-title span:nth-child(25) { --i: 24; }
    .luxury-title span:nth-child(26) { --i: 25; }
    .luxury-title span:nth-child(27) { --i: 26; }
    .luxury-title span:nth-child(28) { --i: 27; }
    .luxury-title span:nth-child(29) { --i: 28; }
    .luxury-title span:nth-child(30) { --i: 29; }

    @keyframes bounce {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-3px); } /* short bounce */
    }

    /* Optional sparkles around the text */
    .luxury-title::before,
    .luxury-title::after {
        content: "✨";
        position: absolute;
        font-size: 1em;
        color: #FFD700;
        opacity: 0;
        animation: sparkle 1.5s infinite;
    }

    .luxury-title::before { top: -20px; left: 20%; animation-delay: 0s; }
    .luxury-title::after { top: -10px; right: 25%; animation-delay: 0.8s; }

    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0.5) rotate(0deg);}
        50% { opacity: 1; transform: scale(1.2) rotate(20deg);}
    }
    </style>
    """, unsafe_allow_html=True)
