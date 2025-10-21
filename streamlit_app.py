import streamlit as st

# --- App Setup ---
st.set_page_config(page_title="NAG AI Prompt Generator", layout="wide")

# --- Navigation ---
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", ["Prompt Generator", "Concept Generator", "Building Design Generator"])

# --- Shared Variables ---
variables = {
    "View / Camera Angle": [
        "Eye Level", "Aerial View", "Low Angle", "Wide Shot", "Close-Up", "Isometric", "Perspective View"
    ],
    "Lighting Type": [
        "Natural Daylight", "Golden Hour", "Overcast", "Studio Light", "Soft Interior Light", "Night Scene", "Dusk Lighting"
    ],
    "Material Style": [
        "Concrete and Glass", "Wood and Stone", "Brick and Steel", "Minimal White", "Futuristic Metallic", "Eco-friendly Green Roof"
    ],
    "Render Style": [
        "Realistic Render", "Cinematic Render", "Concept Sketch", "Clay Render", "Photorealistic", "Digital Painting"
    ],
    "Environment": [
        "Urban City", "Coastal Area", "Forest", "Mountain", "Desert", "Suburban", "Countryside"
    ],
}

# --- Site Context Descriptions (Defined Before Use) ---
site_context_descriptions = {
    "Urban City": "Dense environment surrounded by modern buildings and streets.",
    "Coastal Area": "Near the ocean, with beach atmosphere and sea reflections.",
    "Forest": "Natural forest setting with trees and greenery around.",
    "Mountain": "Hilly or mountainous backdrop with fresh natural atmosphere.",
    "Desert": "Arid sandy environment with minimal vegetation.",
    "Suburban": "Residential neighborhood with greenery and quiet streets.",
    "Countryside": "Open landscape with fields, trees, and rural charm."
}

# --- Common UI Component ---
def shared_dropdowns():
    selections = {}
    for label, options in variables.items():
        selections[label] = st.selectbox(label, options)
    return selections

# --- Page 1: Prompt Generator ---
if page == "Prompt Generator":
    st.title("🧠 Universal AI Prompt Generator")

    st.write("Generate detailed AI prompts for architecture visualization or rendering.")

    selections = shared_dropdowns()
    concept = st.text_area("Describe your concept (e.g., modern villa with glass facade):", height=120)

    if st.button("Generate Prompt"):
        prompt = (
            f"{concept}, {selections['View / Camera Angle']}, {selections['Lighting Type']} lighting, "
            f"{selections['Material Style']}, {selections['Render Style']}, environment: {selections['Environment']}. "
            f"Highly detailed, realistic scale, sharp textures, correct lighting and reflection."
        )
        st.success("Prompt generated! ✅ Copy below:")
        st.code(prompt, language="text")

# --- Page 2: Concept Generator (Image Type-based) ---
elif page == "Concept Generator":
    st.title("🎨 Concept Generator (Image Type)")

    st.write("Describe what kind of image you have, and this will generate concept prompts in the same type or theme.")

    selections = shared_dropdowns()
    image_type_description = st.text_area("Describe your image type (e.g., interior of modern apartment, aerial of resort):", height=120)

    if st.button("Generate Concept Prompt"):
        prompt = (
            f"Concept generation for {image_type_description}. "
            f"Keep same theme and design logic but introduce creative variations. "
            f"Render from {selections['View / Camera Angle']} angle with {selections['Lighting Type']} lighting. "
            f"Use materials {selections['Material Style']} and style as {selections['Render Style']}. "
            f"Place design in a {site_context_descriptions.get(selections['Environment'], 'realistic site context')}."
        )
        st.success("Prompt generated! ✅ Copy below:")
        st.code(prompt, language="text")

# --- Page 3: Building Design Generator ---
elif page == "Building Design Generator":
    st.title("🏗️ New Building Design Generator")

    st.write("Generate new building concepts like villas, high-rises, shops, or commercial complexes.")

    selections = shared_dropdowns()
    building_type = st.selectbox("Building Type", ["Villa", "High-Rise", "Shop", "Commercial Complex", "Apartment", "Office Tower", "Resort", "Cultural Center", "Museum", "Mixed-Use Building"])
    theme_description = st.text_area("Describe design direction (e.g., futuristic glass villa, curved concrete tower):", height=120)

    if st.button("Generate Building Prompt"):
        prompt = (
            f"New {building_type} design concept — {theme_description}. "
            f"Rendered in {selections['View / Camera Angle']} view, with {selections['Lighting Type']} lighting. "
            f"Material palette: {selections['Material Style']}. Render style: {selections['Render Style']}. "
            f"Set in {selections['Environment']} context ({site_context_descriptions.get(selections['Environment'], 'detailed site')}), "
            f"show realistic scale, structure clarity, environmental integration, and architectural harmony."
        )
        st.success("Prompt generated! ✅ Copy below:")
        st.code(prompt, language="text")
