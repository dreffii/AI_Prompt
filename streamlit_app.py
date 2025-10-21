"Volcanic Sand Beach": "Situated on a remote black volcanic sand beach, with dramatic rock formations, powerful ocean waves, and a moody sky.",
    "Train Station Concourse": "Set in a busy train station concourse, with high ceilings, large information boards, and commuters walking through the space.",
    "High-Tech Agricultural": "Placed within a vast high-tech agricultural facility, featuring automated crop rows, controlled lighting, and modern structures.",
    "Temperate River": "Situated alongside a pristine river in a temperate forest, with clear flowing water, smooth rocks, lush greenery, and dappled sunlight.",
    "Exclusive Residential": "Located in an exclusive residential enclave, with architecturally distinct homes, private gardens, and winding, tree-lined streets.",
    "Art District": "Set within a vibrant art district, with colorful murals, unique galleries, street performances, and a lively bohemian atmosphere.",
    "Reflective Salt Flat": "Placed on a tranquil reflective salt flat at sunset, with a vast open horizon, mirror-like ground, and dramatic colorful sky.",
}

# Internal Material Description
material_description = "accurately represent the materials visible in the input image (concrete, glass, wood, metal, etc.)"

# --- Layout ---
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
    prompt += "Focus on realistic textures, materials, lighting, and perspective without adding predefined shapes or design elements.\n"
    prompt += "Preserve the building’s original forms and proportions as seen in the input image."

    st.text_area("Generated Prompt", prompt, height=400)
    st.success("Prompt generated! ✅ Copy manually to clipboard (works on mobile and PC).")
