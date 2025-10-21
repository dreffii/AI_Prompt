import streamlit as st

# --- App Config ---
st.set_page_config(page_title="AI Prompt Generator by Oak Sopheaktra", layout="wide")

# --- Sidebar Navigation ---
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select Page:", [
    "Architectural Render Prompt",
    "Architectural Concept Prompt",
    "New Building Design Prompt"
])

# --- Shared Material Description ---
material_description = "accurately represent materials like concrete, glass, metal, and wood with realistic lighting, shadows, and reflections."

# --- PAGE 1: Architectural Render Prompt ---
if page == "Architectural Render Prompt":
    st.title("🏙️ Architectural Render Prompt Generator")

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
                         "Under Construction","Architect's Desk","Mood Board"]
    site_context_opts = [
        "Enhance Only (No Context)","Modern Metropolis (Day)","Modern Metropolis (Night)","Suburban Neighborhood",
        "Historic European Street","Japanese Zen Garden","Coastal Town","Mountain Valley","Lush Forest",
        "Tropical Island Beach","Desert Landscape","Upscale Plaza","Golf Course Sunrise","Waterfront Promenade",
        "Street Food Market","Botanical Garden","Highway Interchange Night","Glaciated Mountain Pass",
        "Luxury Resort","Financial District","Abandoned Industrial","University Campus Quad","Historic Cathedral Square",
        "Data Center Park","Volcanic Sand Beach","Train Station Concourse","High-Tech Agricultural",
        "Temperate River","Exclusive Residential","Art District","Reflective Salt Flat"
    ]
    mood_style_opts = ["neutral","modern","minimalist","classic","futuristic","conceptual"]

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

    st.subheader("Add Objects")
    furniture = st.checkbox("Furniture")
    vehicles = st.checkbox("Vehicles (Cars, Bikes)")
    people = st.checkbox("People")
    trees = st.checkbox("Trees & Vegetation")
    street_furniture = st.checkbox("Street Furniture")
    foreground_elements = st.checkbox("Foreground Elements")

    if st.button("Generate Prompt"):
        selected_objects = ", ".join([obj for obj, val in {
            "Furniture": furniture,
            "Vehicles (Cars, Bikes)": vehicles,
            "People": people,
            "Trees & Vegetation": trees,
            "Street Furniture": street_furniture,
            "Foreground Elements": foreground_elements
        }.items() if val])

        prompt = f"A highly detailed, {render_style.lower()} architectural rendering.\n"
        prompt += f"Materials: {material_description}.\n"
        prompt += f"View Angle: {view_angle}. Depth of Field: {depth_of_field}. Motion Blur: {motion_blur}.\n"
        prompt += f"Time: {time_of_day}, Weather: {weather}, Wind: {wind_strength}, Interior Lights: {interior_lights}.\n"
        prompt += f"Reflections: {active_reflection}. Site Context: {site_context}. Mood: {mood_style}.\n"
        prompt += f"Objects Included: {selected_objects if selected_objects else 'none'}.\n"
        prompt += "Ensure realistic lighting, texture fidelity, accurate perspective, and natural integration into the environment."

        st.text_area("Generated Prompt", prompt, height=400)
        st.success("Prompt generated! ✅ Copy manually to clipboard.")

# --- PAGE 2: Architectural Concept Prompt (Image-Aware) ---
elif page == "Architectural Concept Prompt":
    st.title("🧠 Architectural Concept Prompt Generator (Image-Aware)")

    concept_types = ["Cultural Center","Museum","Pavilion","Bridge","Public Library","Memorial","Art Installation",
                     "Temple / Spiritual Space","Eco Village","Parametric Facade Study","Urban Housing Block",
                     "Mixed-use Complex","Community Center","Student Housing"]
    design_style_opts = ["Futuristic","Biophilic","Parametric","Brutalist","Minimalist","Deconstructivist","Organic","Metaverse-Inspired"]
    concept_focus_opts = ["Form Exploration","Light Interaction","Material Experimentation","Spatial Experience","Symbolic Geometry","Context Integration"]
    environment_opts = ["Urban","Rural","Forest","Coastal","Mountain","Desert","Floating","Underground","Mars Habitat"]

    col1, col2 = st.columns(2)
    with col1:
        concept_type = st.selectbox("Building Type / Concept", concept_types)
        design_style = st.selectbox("Design Style", design_style_opts)
        focus = st.selectbox("Concept Focus", concept_focus_opts)

    with col2:
        environment = st.selectbox("Environment Context", environment_opts)
        time_of_day = st.selectbox("Time of Day", ["Day","Night","Golden Hour","Overcast"])
        render_style = st.selectbox("Render Style", ["Concept Visualization","Diagrammatic","Cinematic Render","Clay Render","Physical Model"])

    if st.button("Generate Concept Prompt"):
        prompt = f"Analyze the input image to understand its architectural type, structure, and style.\n"
        prompt += f"Identify if it’s a {concept_type.lower()} or a related building type, and generate an architectural concept that evolves from its existing design language.\n"
        prompt += f"Create a {design_style.lower()} concept focusing on {focus.lower()}, situated in a {environment.lower()} environment.\n"
        prompt += f"Depict at {time_of_day.lower()} using {render_style.lower()} approach.\n"
        prompt += f"Emphasize architectural form, spatial relationships, and the idea development behind the design.\n"
        prompt += f"Maintain material realism ({material_description}) and lighting consistent with the original image.\n"
        prompt += f"Do not redesign into an unrelated type — evolve the concept based on the image’s original form and intent.\n"
        prompt += f"Focus on how light, geometry, and space express architectural thinking and atmosphere."

        st.text_area("Generated Concept Prompt", prompt, height=400)
        st.success("Concept prompt generated successfully ✅")

# --- PAGE 3: New Building Design Prompt ---
elif page == "New Building Design Prompt":
    st.title("🏗️ New Building Design Prompt Generator")

    building_types = ["Modern Villa","High-Rise Tower","Shop House","Office Building","Apartment Complex","Resort","School","Hospital",
                      "Market Hall","Sport Facility","Cultural Center","Factory","Warehouse","Community Hall","Museum"]
    architectural_style_opts = ["Modern Minimalist","Tropical Modern","Neo-Futurist","Contemporary Classic","Sustainable Green","Industrial Loft",
                                "Vernacular Khmer","Brutalist","Scandinavian","Japanese Wabi-Sabi","Luxury Contemporary"]
    material_focus_opts = ["Concrete","Glass","Wood","Steel","Mixed Material","Earth & Bamboo","Stone"]
    environment_opts = ["Urban City","Suburban","Beachfront","Mountain","Countryside","Forest Edge","Lakeside"]
    scale_opts = ["Small Residential","Medium Building","Large Complex","Skyscraper"]
    time_opts = ["Day","Night","Golden Hour","Overcast","Dusk"]

    col1, col2 = st.columns(2)
    with col1:
        building_type = st.selectbox("Building Type", building_types)
        style = st.selectbox("Architectural Style", architectural_style_opts)
        materials = st.selectbox("Material Focus", material_focus_opts)
        scale = st.selectbox("Scale", scale_opts)

    with col2:
        environment = st.selectbox("Environment", environment_opts)
        time = st.selectbox("Time of Day", time_opts)
        render_style = st.selectbox("Render Style", ["Photorealistic","Cinematic","Conceptual","Clay Render","Physical Model"])
        mood = st.selectbox("Mood", ["Elegant","Peaceful","Dynamic","Futuristic","Warm","Natural"])

    if st.button("Generate New Building Prompt"):
        prompt = f"Design a {style.lower()} {building_type} in a {environment.lower()} setting.\n"
        prompt += f"Use {materials.lower()} materials emphasizing proportion, texture, and structure.\n"
        prompt += f"Scale: {scale.lower()}. Time of Day: {time.lower()}.\n"
        prompt += f"Render Style: {render_style.lower()}, Mood: {mood.lower()}.\n"
        prompt += f"Focus on innovative massing, environmental integration, realistic lighting, and architectural detail.\n"
        prompt += "Include landscape, surrounding context, and material interaction for a complete architectural presentation."

        st.text_area("Generated Building Prompt", prompt, height=400)
        st.success("Building design prompt generated successfully ✅")
