import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="AI Prompt Generator & Concept Developer by Oak Sopheaktra", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["AI Prompt Generator", "AI Concept Developer"])

# --- Shared Dropdown Options ---
view_angles = ["Default Angle","Professional Archviz","Eye-Level","High-Angle","Low-Angle","Aerial / Drone",
               "Close-up","Wide Shot","Bird's Eye View","View From Inside (Building to Outside)"]
depth_of_field_opts = ["None","Subtle","Moderate","Strong"]
motion_blur_opts = ["None","Light","Medium","Heavy"]
time_of_day_opts = ["Day","Soft Daylight","Midday Sun","Night","Golden Hour","Blue Hour","Dawn","Dusk","Archviz Daylight"]
weather_opts = ["Clear","Overcast","Rainy","Light Rain","Stormy","Foggy","Snowy"]
wind_strength_opts = ["None","Light Breeze","Strong Wind"]
interior_lights_opts = ["On","Off"]
active_reflection_opts = ["None","Subtle","Moderate","Strong"]
render_style_opts = ["Photorealistic","Ultra Realistic","Interior Design","Isometric","Axonometric View",
                     "Architectural Presentation","Explosion Analysis","Handmade Wooden Model","Concept Sketch",
                     "Under Construction","Architect's Desk","Mood Board","Futuristic Concept","Clay Model"]
site_context_opts = ["Enhance Only (No Context)","Modern Metropolis (Day)","Modern Metropolis (Night)","Suburban Neighborhood",
                     "Historic European Street","Japanese Zen Garden","Coastal Town","Mountain Valley","Lush Forest",
                     "Tropical Island Beach","Desert Landscape","Upscale Plaza","Golf Course Sunrise","Waterfront Promenade",
                     "Street Food Market","Botanical Garden","Highway Interchange Night","Glaciated Mountain Pass",
                     "Luxury Resort","Financial District","Abandoned Industrial","University Campus Quad","Historic Cathedral Square",
                     "Data Center Park","Volcanic Sand Beach","Train Station Concourse","High-Tech Agricultural",
                     "Temperate River","Exclusive Residential","Art District","Reflective Salt Flat"]
mood_style_opts = ["neutral","modern","minimalist","classic","futuristic","conceptual","organic","parametric"]

# --- Site Context Descriptions ---
site_context_descriptions = {
    "Enhance Only (No Context)": "Focus on architecture only, minimal surroundings.",
    "Modern Metropolis (Day)": "Modern city skyline during daytime with glass skyscrapers and busy streets.",
    "Modern Metropolis (Night)": "Night view in a futuristic city, glowing lights and reflections.",
    "Suburban Neighborhood": "Calm suburban street with houses, trees, and soft daylight.",
    "Historic European Street": "Old cobblestone street with ornate facades and pedestrians.",
    "Japanese Zen Garden": "Minimal and peaceful garden with bamboo, koi pond, and stones.",
    "Coastal Town": "Seaside environment with boats, promenade, and bright sky.",
    "Mountain Valley": "Surrounded by mountains, rivers, and lush green scenery.",
    "Lush Forest": "Dense forest with soft sunlight filtering through trees.",
    "Luxury Resort": "Elegant resort with pools, palm trees, and ocean views."
}

material_description = "accurately represent the materials visible in the input image (concrete, glass, wood, metal, etc.)"

# --- Shared UI for Both Pages ---
def shared_ui():
    col1, col2 = st.columns(2)

    with col1:
        view_angle = st.selectbox("View / Camera Angle", view_angles)
        depth_of_field = st.selectbox("Depth of Field", depth_of_field_opts)
        motion_blur = st.selectbox("Motion Blur", motion_blur_opts)
        time_of_day = st.selectbox("Time of Day", time_of_day_opts)
        weather = st.selectbox("Weather", weather_opts)
        wind_strength = st.selectbox("Wind Strength", wind_strength_opts)
        interior_lights = st.selectbox("Interior Lights", interior_lights_opts)

    with col2:
        active_reflection = st.selectbox("Active Reflection", active_reflection_opts)
        render_style = st.selectbox("Render Style", render_style_opts)
        site_context = st.selectbox("Site Context", site_context_opts)
        mood_style = st.selectbox("Mood / Style", mood_style_opts)

    st.subheader("Add Elements")
    furniture = st.checkbox("Furniture")
    vehicles = st.checkbox("Vehicles (Cars, Bikes)")
    people = st.checkbox("People")
    trees = st.checkbox("Trees & Vegetation")
    street_furniture = st.checkbox("Street Furniture")
    foreground_elements = st.checkbox("Foreground Elements")

    selected_objects = ", ".join([obj for obj, val in {
        "Furniture": furniture,
        "Vehicles (Cars, Bikes)": vehicles,
        "People": people,
        "Trees & Vegetation": trees,
        "Street Furniture": street_furniture,
        "Foreground Elements": foreground_elements
    }.items() if val])

    return (view_angle, depth_of_field, motion_blur, time_of_day, weather, wind_strength,
            interior_lights, active_reflection, render_style, site_context, mood_style, selected_objects)


# ==========================
# PAGE 1: AI PROMPT GENERATOR
# ==========================
if page == "AI Prompt Generator":
    st.title("AI Prompt Generator by Oak Sopheaktra")

    st.markdown("""
    Generate **professional rendering prompts** for architectural AI visualization.
    This tool focuses on realism, materials, lighting, and accurate architectural representation.
    """)

    (view_angle, depth_of_field, motion_blur, time_of_day, weather, wind_strength,
     interior_lights, active_reflection, render_style, site_context, mood_style, selected_objects) = shared_ui()

    if st.button("Generate Prompt"):
        prompt = f"A highly detailed, photorealistic architectural rendering.\n"
        prompt += f"Materials: {material_description}.\n"
        prompt += f"View / Camera Angle: {view_angle}\n"
        prompt += f"Depth of Field: {depth_of_field}\n"
        prompt += f"Motion Blur: {motion_blur}\n"
        prompt += f"Time of Day: {time_of_day}\n"
        prompt += f"Weather: {weather}\n"
        prompt += f"Wind Strength: {wind_strength}\n"
        prompt += f"Interior Lights: {interior_lights}\n"
        prompt += f"Active Reflection: {active_reflection}\n"
        prompt += f"Render Style: {render_style}\n"
        prompt += f"Site Context: {site_context_descriptions.get(site_context, site_context)}\n"
        prompt += f"Mood / Style: {mood_style}\n"
        prompt += f"Objects included: {selected_objects if selected_objects else 'none'}.\n"
        prompt += "Focus on realistic materials, textures, lighting, and scale. "
        prompt += "Do not modify building form or proportions seen in the input image."

        st.text_area("Generated Prompt", prompt, height=400)
        st.success("Prompt generated! ✅ Copy manually to clipboard (works on mobile and PC).")


# ==========================
# PAGE 2: AI CONCEPT DEVELOPER
# ==========================
elif page == "AI Concept Developer":
    st.title("AI Concept Developer by Oak Sopheaktra")

    st.markdown("""
    Generate **creative and conceptual prompts** based on your architectural model.
    This tool **does not upload or analyze images**, but helps you tell the AI how to 
    reinterpret, evolve, or creatively extend the concept of your design.
    """)

    (view_angle, depth_of_field, motion_blur, time_of_day, weather, wind_strength,
     interior_lights, active_reflection, render_style, site_context, mood_style, selected_objects) = shared_ui()

    if st.button("Generate Concept Prompt"):
        prompt = f"Develop a creative architectural concept inspired by the design shown in the input image.\n"
        prompt += f"Preserve the general form and proportion, but reinterpret materials, massing, and spatial rhythm.\n"
        prompt += f"Introduce architectural creativity, alternative facade logic, or evolved design gestures.\n\n"
        prompt += f"Render Context:\n"
        prompt += f"- View / Camera Angle: {view_angle}\n"
        prompt += f"- Depth of Field: {depth_of_field}\n"
        prompt += f"- Motion Blur: {motion_blur}\n"
        prompt += f"- Time of Day: {time_of_day}\n"
        prompt += f"- Weather: {weather}\n"
        prompt += f"- Wind Strength: {wind_strength}\n"
        prompt += f"- Interior Lights: {interior_lights}\n"
        prompt += f"- Active Reflection: {active_reflection}\n"
        prompt += f"- Render Style: {render_style}\n"
        prompt += f"- Site Context: {site_context_descriptions.get(site_context, site_context)}\n"
        prompt += f"- Mood / Style: {mood_style}\n"
        prompt += f"- Creative Objects: {selected_objects if selected_objects else 'none'}.\n\n"
        prompt += "Encourage subtle changes in structure, form, and lighting to explore alternative design interpretations "
        prompt += "while maintaining architectural coherence and proportion."

        st.text_area("Generated Concept Prompt", prompt, height=400)
        st.success("Concept prompt generated! ✨ Copy manually to clipboard.")
