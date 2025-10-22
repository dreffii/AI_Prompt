import streamlit as st
from animated_title import show_animated_title
from data.site_contexts import site_context_descriptions, site_context_opts

def show_page_2():
    st.set_page_config(page_title="🏛️ Concept Developer ✨", layout="wide")

    # Show animated title
    show_animated_title()

    # --- Variables (Page 1 + Concept Development) ---
    view_angles = ["Default Angle","Professional Archviz","Eye-Level","High-Angle","Low-Angle","Aerial / Drone",
                   "Close-up","Wide Shot","Bird's Eye View","View From Inside (Building to Outside)"]

    depth_of_field_opts = ["None","Subtle","Moderate","Strong"]
    motion_blur_opts = ["None","Light","Medium","Heavy"]

    time_of_day_opts = [
        "Day","Soft Daylight","Midday Sun","Night","Golden Hour","Blue Hour","Dawn","Dusk","Archviz Daylight",
        "Purple Hour","Evening","Sunrise","Sunset","Early Morning","Late Afternoon","Twilight","Moonlit Night",
        "Foggy Morning","Overcast Noon","Rainy Afternoon","Stormy Evening","Snowy Morning","Winter Sunset",
        "Summer Sunrise","Autumn Evening","Spring Twilight","Cloudy Afternoon","Evening Glow","Evening Mist",
        "Warm Sunset","Cold Sunrise","Night with Streetlights","Misty Morning","Foggy Evening","Purple Twilight"
    ]

    weather_opts = ["Clear","Overcast","Rainy","Light Rain","Stormy","Foggy","Snowy"]
    wind_strength_opts = ["None","Light Breeze","Strong Wind"]
    interior_lights_opts = ["On","Off"]
    active_reflection_opts = ["None","Subtle","Moderate","Strong"]
    render_style_opts = ["Photorealistic","Ultra Realistic","Interior Design","Isometric","Axonometric View",
                         "Architectural Presentation","Explosion Analysis","Handmade Wooden Model","Concept Sketch",
                         "Under Construction","Architect's Desk","Mood Board"]

    mood_style_opts = [
        "neutral","modern","minimalist","classic","futuristic","conceptual","artistic","natural","surreal",
        "urban","abstract","industrial","romantic","dramatic","luxurious","dark","bright","cinematic",
        "fantasy","storytelling"
    ]

    # --- Concept Development Specific Variables ---
    corner_style_opts = ["Sharp", "Curved", "Mixed"]
    terrace_connection_opts = ["None", "Single Curve", "Double Curve", "Custom LED Edge"]
    material_opts = ["Glass", "Concrete", "Metal", "Mixed"]
    lighting_edge_opts = ["None", "LED Warm White", "LED Cool White", "LED RGB"]
    building_volume_adjustment_opts = ["Default", "Increase Height", "Decrease Height", "Adjust Proportions"]
    roof_profile_opts = ["Flat", "Sloped", "Curved", "Custom"]
    floor_count_opts = list(range(1, 21))  # numeric input
    focus_area_opts = ["Front Facade", "Rooftop Terrace", "Corner Detailing", "Full Building"]
    special_features_opts = ["Overhangs", "Sky Bridges", "Cantilevered Sections", "Green Walls"]

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
        corner_style = st.selectbox("Corner Style", corner_style_opts)
        terrace_connection = st.selectbox("Terrace Connection", terrace_connection_opts)

    with col2:
        active_reflection = st.selectbox("Active Reflection", active_reflection_opts)
        render_style = st.selectbox("Render Style", render_style_opts)
        site_context = st.selectbox("Site Context", site_context_opts)
        mood_style = st.selectbox("Mood / Style", mood_style_opts)
        material = st.selectbox("Material Option", material_opts)
        lighting_edge = st.selectbox("Lighting Edge", lighting_edge_opts)
        building_volume = st.selectbox("Building Volume Adjustment", building_volume_adjustment_opts)
        roof_profile = st.selectbox("Roof Profile", roof_profile_opts)
        floor_count = st.selectbox("Number of Floors", floor_count_opts)
        focus_area = st.selectbox("Focus Area", focus_area_opts)
        special_features = st.multiselect("Special Features", special_features_opts)

    # Additional custom prompt input
    additional_prompt = st.text_area("Additional Concept Details / Instructions", "")

    # --- Generate Prompt ---
    if st.button("Generate Concept Prompt"):
        selected_features = ", ".join(special_features) if special_features else "none"
        camera_view = "Maintain same view as input" if view_angle=="Default Angle" else view_angle

        prompt = f"A detailed architectural concept development.\n"
        prompt += f"Materials: {material}.\n"
        prompt += f"View / Camera Angle: {camera_view}\n"
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
        prompt += f"Corner Style: {corner_style}\n"
        prompt += f"Terrace Connection: {terrace_connection}\n"
        prompt += f"Roof Profile: {roof_profile}\n"
        prompt += f"Building Volume Adjustment: {building_volume}\n"
        prompt += f"Number of Floors: {floor_count}\n"
        prompt += f"Focus Area: {focus_area}\n"
        prompt += f"Special Features: {selected_features}\n"
        prompt += f"Additional Details: {additional_prompt if additional_prompt else 'none'}\n"
        prompt += "Ensure building fits fully inside the view, volume and corner adjustments follow the concept instructions."

        # Show in text_area
        st.text_area("Generated Concept Prompt", prompt, height=450)

        # Copy button using JS
        st.button("Copy Prompt", on_click=lambda: st.experimental_set_query_params(copy=prompt))
