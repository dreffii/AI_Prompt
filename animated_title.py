import streamlit as st

def show_animated_title(
    title="🤖 Prompt Generator by Oak Sopheaktra",
    font_size="3em",  # This will now be the *desktop* font size
    text_color="#000000",
    bounce_height="3px",
    bounce_speed="4s"
):
    """
    Display a luxury animated title with:
    - Subtle per-letter bounce
    - Random blinking sparkles
    - Responsive font size for mobile (NEW)
    Spaces are preserved.
    """
    
    # Wrap each character in a span, replace space with &nbsp;
    wrapped_title = "".join(f"<span>{c if c != ' ' else '&nbsp;'}</span>" for c in title)

    st.markdown(f"""
    <div class="luxury-title">{wrapped_title}</div>

    <style>
    .luxury-title {{
        text-align: center;
        font-family: "Georgia", serif;
        font-size: {font_size}; /* Default/Desktop font size */
        color: {text_color};
        position: relative;
        word-wrap: break-word; /* Added for safety on long words */
    }}

    .luxury-title span {{
        display: inline-block;
        animation: bounce {bounce_speed} infinite;
        animation-delay: calc(var(--i) * 0.05s);
    }}

    /* Automatically assign --i for staggered animation */
    .luxury-title span {{
        --i: 0;
    }}
    .luxury-title span:nth-child(n) {{
        --i: calc(var(--i) + 1);
    }}

    @keyframes bounce {{
        0%, 100% {{ transform: translateY(0); }}
        50% {{ transform: translateY(-{bounce_height}); }}
    }}

    /* Sparkles */
    .luxury-title::before,
    .luxury-title::after {{
        content: "✨";
        position: absolute;
        font-size: 1em; /* Sparkle size relative to title font */
        color: #FFD700;
        opacity: 0;
        animation: sparkle 1.5s infinite;
    }}

    /* Changed top position from px to em to scale with font */
    .luxury-title::before {{ top: -0.2em; left: 22%; animation-delay: 0s; }}
    .luxury-title::after {{ top: -0.1em; right: 22%; animation-delay: 0.8s; }}

    /* --- START OF ADDED RESPONSIVE CODE --- */
    @media (max-width: 600px) {{
        .luxury-title {{
            font-size: 1.7em; /* Smaller font size for mobile */
        }}

        .luxury-title::before {{
            left: 10%; /* Adjust sparkle position for mobile */
            font-size: 0.8em; /* Slightly smaller sparkles */
        }}
        .luxury-title::after {{
            right: 10%; /* Adjust sparkle position for mobile */
            font-size: 0.8em; /* Slightly smaller sparkles */
        }}
    }}
    /* --- END OF ADDED RESPONSIVE CODE --- */

    @keyframes sparkle {{
        0%, 100% {{ opacity: 0; transform: scale(0.5) rotate(0deg); }}
        50% {{ opacity: 1; transform: scale(1.2) rotate(20deg); }}
    }}
    </style>
    """, unsafe_allow_html=True)

# Example of how to use it in your app
# st.set_page_config(layout="wide")
# show_animated_title() 
