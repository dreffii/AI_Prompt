import streamlit as st
from animated_title import show_animated_title
from data.site_contexts import site_context_descriptions, site_context_opts

def show_page_2():
    st.set_page_config(page_title="🏛️ Concept Developer ✨", layout="wide")

    # Show animated title
    show_animated_title()

    # --- Variables for dropdowns ---
    view_angles = ["Default Angle","Professional Archviz","Eye-Level","High-Angle","Low-Angle","Aerial / Drone",
                   "Close-up","Wide Shot","Bird's Eye View","View From Inside (Building to Outside)"]

    depth_of_field_opts = ["Default", "None","Subtle","Moderate","Strong"]
    motion_blur_opts = ["Default", "None","Light","Medium","Heavy"]

    time_of_day_opts = ["Default"] + [
        "Day","Soft Daylight","Midday Sun","Night","Golden Hour","Blue Hour","Dawn","Dusk","Archviz Daylight",
        "Purple Hour","Evening","Sunrise","Sunset","Early Morning","Late Afternoon","Twilight","Moonlit Night",
        "Foggy Morning","Overcast Noon","Rainy Afternoon","Stormy Evening","Snowy Morning","Winter Sunset",
        "Summer Sunrise","Autumn Evening","Spring Twilight","Cloudy Afternoon","Evening Glow","Evening Mist",
        "Warm Sunset","Cold Sunrise","Night with Streetlights","Misty Morning","Foggy Evening","Purple Twilight"
    ]

    weather_opts = ["Default","Clear","Overcast","Rainy","Light Rain","Stormy","Foggy","Snowy"]
    wind_strength_opts = ["Default","None","Light Breeze","Strong Wind"]
    interior_lights_opts = ["Default","On","Off"]
    active_reflection_opts = ["Default","None","Subtle","Moderate","Strong"]
    render_style_opts = ["Default","Photorealistic","Ultra Realistic","Interior Design","Isometric","Axonometric View",
                         "Architectural Presentation","Explosion Analysis","Handmade Wooden Model","Concept Sketch",
                         "Under Construction","Architect's Desk","Mood Board"]
    mood_style_opts = ["Default"] + [
        "neutral","modern","minimalist","classic","futuristic","conceptual","artistic","natural","surreal","urban",
        "abstract","industrial","romantic","dramatic","luxurious","dark","bright","cinematic","fantasy","storytelling"
    ]

    # New variables for concept developer
    corner_style_opts = ["Default","Sharp","Curved","Mixed"]
    terrace_connection_opts = ["Default","None", "Single Curve", "Double Curve", "Custom LED Edge"]
    material_opts = ["Default","Glass","Concrete","Metal","Mixed"]
    lighting_edge_opts = ["Default","None","LED Warm White","LED Cool White","LED RGB"]
    building_volume_adjustment_opts = ["Default","Increase Height","Decrease Height","Adjust Proportions"]

    # --- Internal Material Description ---
    material_description = "accurately represent the materials visible in the input image (concrete, glass, wood, metal, etc.)"

    # --- Layout ---
    col1, col2 = st.columns(2)

    with col1:
        view_angle = st.selectbox("🎥 View / Camera Angle", view_angles)
        depth_of_field = st.selectbox("🔍 Depth of Field", depth_of_field_opts)
        motion_blur = st.selectbox("💨 Motion Blur", motion_blur_opts)
        time_of_day = st.selectbox("🌞 Time of Day", time_of_day_opts)
        weather = st.selectbox("🌦 Weather", weather_opts)
        wind_strength = st.selectbox("🌬 Wind Strength", wind_strength_opts)
        interior_lights = st.selectbox("💡 Interior Lights", interior_lights_opts)
        corner_style = st.selectbox("🔹 Corner Style", corner_style_opts)
        terrace_connection = st.selectbox("🌈 Terrace Connection", terrace_connection_opts)

    with col2:
        active_reflection = st.selectbox("✨ Active Reflection", active_reflection_opts)
        render_style = st.selectbox("🎨 Render Style", render_style_opts)
        site_context = st.selectbox("🏙 Site Context", site_context_opts)
        additional_site_prompt = st.text_area("Additional Prompt (optional)", placeholder="Add any extra description or concept...")
        mood_style = st.selectbox("🎭 Mood / Style", mood_style_opts)
        material_choice = st.selectbox("🏗 Material", material_opts)
        lighting_edge = st.selectbox("💡 Edge Lighting", lighting_edge_opts)
        building_volume = st.selectbox("🏢 Building Volume Adjustment", building_volume_adjustment_opts)

    # --- Add Objects ---
    st.subheader("🛠 Add Objects")
    furniture = st.checkbox("🪑 Furniture")
    vehicles = st.checkbox("🚗 Vehicles (Cars, Bikes)")
    people = st.checkbox("🧑 People")
    trees = st.checkbox("🌳 Trees & Vegetation")
    street_furniture = st.checkbox("🪑 Street Furniture")
    foreground_elements = st.checkbox("🌟 Foreground Elements")

    # --- Generate Prompt ---
    if st.button("Generate Prompt"):
        selected_objects = ", ".join([obj for obj, val in {
            "Furniture": furniture,
            "Vehicles (Cars, Bikes)": vehicles,
            "People": people,
            "Trees & Vegetation": trees,
            "Street Furniture": street_furniture,
            "Foreground Elements": foreground_elements
        }.items() if val])

        camera_view = "Maintain same view as input" if view_angle=="Default Angle" else view_angle

        prompt = f"A highly detailed, photorealistic architectural concept rendering.\n"
        prompt += f"View / Camera Angle: {camera_view}\n"

        # Only add if not Default
        if depth_of_field != "Default": prompt += f"Depth of Field: {depth_of_field}\n"
        if motion_blur != "Default": prompt += f"Motion Blur: {motion_blur}\n"
        if time_of_day != "Default": prompt += f"Time of Day: {time_of_day}\n"
        if weather != "Default": prompt += f"Weather: {weather}\n"
        if wind_strength != "Default": prompt += f"Wind Strength: {wind_strength}\n"
        if interior_lights != "Default": prompt += f"Interior Lights: {interior_lights}\n"
        if corner_style != "Default": prompt += f"Corner Style: {corner_style}\n"
        if terrace_connection != "Default": prompt += f"Terrace Connection: {terrace_connection}\n"
        if active_reflection != "Default": prompt += f"Active Reflection: {active_reflection}\n"
        if render_style != "Default": prompt += f"Render Style: {render_style}\n"
        if material_choice != "Default": prompt += f"Material: {material_choice}\n"
        if lighting_edge != "Default": prompt += f"Edge Lighting: {lighting_edge}\n"
        if building_volume != "Default": prompt += f"Building Volume Adjustment: {building_volume}\n"
        if site_context != "Default":
            prompt += f"Site Context: {site_context_descriptions.get(site_context, site_context)}\n"
        if additional_site_prompt:
            prompt += f"Additional Context: {additional_site_prompt}\n"
        if mood_style != "Default": prompt += f"Mood / Style: {mood_style}\n"
        prompt += f"Objects included: {selected_objects if selected_objects else 'none'}.\n"
        prompt += "Focus on realistic textures, materials, lighting, perspective, and architectural concept adjustments while preserving the building’s general proportions.\n"

        st.text_area("Generated Concept Prompt", prompt, height=450)
        st.success("Prompt generated! ✅ Copy generated prompt and paste the AI prompt 🐰")
