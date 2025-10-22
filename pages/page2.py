import streamlit as st
from animated_title import show_animated_title
from data.site_contexts import site_context_descriptions, site_context_opts

def show_page_2():
    st.set_page_config(page_title="🏛️ Concept Developer ✨", layout="wide")

    # Animated title
    show_animated_title()

    # --- Variables for dropdowns ---
    view_angles = ["Default Angle","Professional Archviz","Eye-Level","High-Angle","Low-Angle","Aerial / Drone",
                   "Close-up","Wide Shot","Bird's Eye View","View From Inside (Building to Outside)"]
    depth_of_field_opts = ["Default", "None","Subtle","Moderate","Strong"]
    motion_blur_opts = ["Default", "None","Light","Medium","Heavy"]
    time_of_day_opts = ["Default",
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
    mood_style_opts = [
        "neutral",
        "modern",
        "minimalist",
        "classic",
        "futuristic",
        "conceptual",
        "organic",
        "artistic",
        "natural",
        "surreal",
        "urban",
        "abstract",
        "industrial",
        "romantic",
        "dramatic",
        "luxurious",
        "dark",
        "bright",
        "cinematic",
        "fantasy",
        "storytelling"
    ]
    corner_style_opts = ["Default","Sharp", "Curved", "Mixed"]
    terrace_connection_opts = ["Default","None", "Single Curve", "Double Curve", "Custom LED Edge"]
    material_opts = ["Default","Glass", "Concrete", "Metal", "Mixed"]
    lighting_edge_opts = ["Default","None", "LED Warm White", "LED Cool White", "LED RGB"]
    building_volume_adjustment_opts = ["Default","Default", "Increase Height", "Decrease Height", "Adjust Proportions"]

    # --- Layout ---
    st.subheader("Scene Settings")
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

    st.subheader("Concept Modifications")
    col3, col4 = st.columns(2)
    with col3:
        corner_style = st.selectbox("Corner Style", corner_style_opts)
        terrace_connection = st.selectbox("Terrace Connection", terrace_connection_opts)
        material = st.selectbox("Material", material_opts)
        # --- Objects checkboxes like Page 1 ---
        furniture = st.checkbox("Furniture")
        vehicles = st.checkbox("Vehicles (Cars, Bikes)")
        people = st.checkbox("People")
        trees = st.checkbox("Trees & Vegetation")
    with col4:
        lighting_edge = st.selectbox("Lighting Edge", lighting_edge_opts)
        building_volume_adjustment = st.selectbox("Building Volume Adjustment", building_volume_adjustment_opts)
        additional_prompt = st.text_area("Additional Notes / Custom Prompt", placeholder="Optional extra instructions...")
        street_furniture = st.checkbox("Street Furniture")
        foreground_elements = st.checkbox("Foreground Elements")

    # --- Generate Prompt ---
    if st.button("Generate Concept Prompt"):
        def include_val(name, val, always_include=False):
            if always_include or not val.startswith("Default"):
                return f"{name}: {val}\n"
            return ""

        prompt = "As an expet architect, reimagine this architecture and change the design to: \n"

        # Scene Settings
        prompt += include_val("View / Camera Angle", view_angle, always_include=True)
        prompt += include_val("Depth of Field", depth_of_field)
        prompt += include_val("Motion Blur", motion_blur)
        prompt += include_val("Time of Day", time_of_day)
        prompt += include_val("Weather", weather)
        prompt += include_val("Wind Strength", wind_strength)
        prompt += include_val("Interior Lights", interior_lights)
        prompt += include_val("Active Reflection", active_reflection)
        prompt += include_val("Render Style", render_style)
        prompt += include_val("Mood / Style", mood_style)
        if not site_context.startswith("Default"):
            prompt += f"Site Context: {site_context_descriptions.get(site_context, site_context)}\n"

        # Concept Modifications
        prompt += include_val("Corner Style", corner_style)
        prompt += include_val("Terrace Connection", terrace_connection)
        prompt += include_val("Material", material)
        prompt += include_val("Lighting Edge", lighting_edge)
        prompt += include_val("Building Volume Adjustment", building_volume_adjustment)

        # Objects
        selected_objects = ", ".join([obj for obj, val in {
            "Furniture": furniture,
            "Vehicles (Cars, Bikes)": vehicles,
            "People": people,
            "Trees & Vegetation": trees,
            "Street Furniture": street_furniture,
            "Foreground Elements": foreground_elements
        }.items() if val])
        if selected_objects:
            prompt += f"Objects included: {selected_objects}\n"

        # Additional prompt
        if additional_prompt.strip():
            prompt += f"Additional Notes: {additional_prompt}\n"

        prompt += "Ensure building fits in frame, preserve original proportions if Default, adjust corners, terraces, and edges."

        st.text_area("Generated Concept Prompt", prompt, height=400)
        st.success("Concept Prompt generated! ✅ Copy manually to clipboard (works on mobile and PC).")

