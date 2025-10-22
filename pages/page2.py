import streamlit as st
from animated_title import show_animated_title
from data.site_contexts import site_context_descriptions, site_context_opts

def show_page_2():
    st.set_page_config(page_title="🏛️ Concept Developer ✨", layout="wide")

    # Show animated title
    show_animated_title()

    # --- Variables for dropdowns ---
    view_angles = ["Default","Professional Archviz","Eye-Level","High-Angle","Low-Angle",
                   "Aerial / Drone","Close-up","Wide Shot","Bird's Eye View","View From Inside (Building to Outside)"]
    
    depth_of_field_opts = ["Default","None","Subtle","Moderate","Strong"]
    motion_blur_opts = ["Default","None","Light","Medium","Heavy"]
    
    time_of_day_opts = ["Default","Day","Soft Daylight","Midday Sun","Night","Golden Hour","Blue Hour",
                        "Dawn","Dusk","Archviz Daylight","Purple Hour","Evening","Sunrise","Sunset",
                        "Early Morning","Late Afternoon","Twilight","Moonlit Night","Foggy Morning",
                        "Overcast Noon","Rainy Afternoon","Stormy Evening","Snowy Morning","Winter Sunset",
                        "Summer Sunrise","Autumn Evening","Spring Twilight","Cloudy Afternoon","Evening Glow",
                        "Evening Mist","Warm Sunset","Cold Sunrise","Night with Streetlights","Misty Morning",
                        "Foggy Evening","Purple Twilight"]
    
    weather_opts = ["Default","Clear","Overcast","Rainy","Light Rain","Stormy","Foggy","Snowy"]
    wind_strength_opts = ["Default","None","Light Breeze","Strong Wind"]
    interior_lights_opts = ["Default","On","Off"]
    active_reflection_opts = ["Default","None","Subtle","Moderate","Strong"]
    render_style_opts = ["Default","Photorealistic","Ultra Realistic","Interior Design","Isometric","Axonometric View",
                         "Architectural Presentation","Explosion Analysis","Handmade Wooden Model","Concept Sketch",
                         "Under Construction","Architect's Desk","Mood Board"]
    
    mood_style_opts = ["Default","neutral","modern","minimalist","classic","futuristic","conceptual",
                       "artistic","natural","surreal","urban","abstract","industrial","romantic",
                       "dramatic","luxurious","dark","bright","cinematic","fantasy","storytelling"]
    
    # --- Additional concept-specific variables ---
    corner_style_opts = ["Default","Sharp","Curved","Mixed"]
    terrace_connection_opts = ["Default","None","Single Curve","Double Curve","Custom LED Edge"]
    material_opts = ["Default","Glass","Concrete","Metal","Mixed"]
    lighting_edge_opts = ["Default","None","LED Warm White","LED Cool White","LED RGB"]
    building_volume_adjustment_opts = ["Default","Default","Increase Height","Decrease Height","Adjust Proportions"]

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
        mood_style = st.selectbox("Mood / Style", mood_style_opts)
        corner_style = st.selectbox("Corner Style", corner_style_opts)
        terrace_connection = st.selectbox("Terrace Connection", terrace_connection_opts)
        material = st.selectbox("Material", material_opts)
        lighting_edge = st.selectbox("Lighting Edge", lighting_edge_opts)
        building_volume_adjustment = st.selectbox("Building Volume Adjustment", building_volume_adjustment_opts)
        site_context = st.selectbox("Site Context", site_context_opts)

    # --- Additional Prompt Input ---
    additional_prompt = st.text_area("Additional Prompt (optional)")

    # --- Generate Prompt ---
    if st.button("Generate Concept Prompt"):
        # Handle defaults
        camera_view = "Maintain same view as input" if view_angle=="Default" else view_angle
        dof = "As in input image" if depth_of_field=="Default" else depth_of_field
        blur = "As in input image" if motion_blur=="Default" else motion_blur
        tod = "As in input image" if time_of_day=="Default" else time_of_day
        wea = "As in input image" if weather=="Default" else weather
        wind = "As in input image" if wind_strength=="Default" else wind_strength
        lights = "As in input image" if interior_lights=="Default" else interior_lights
        reflection = "As in input image" if active_reflection=="Default" else active_reflection
        rstyle = "As in input image" if render_style=="Default" else render_style
        mood = "As in input image" if mood_style=="Default" else mood_style
        corner = "As in input image" if corner_style=="Default" else corner_style
        terrace = "As in input image" if terrace_connection=="Default" else terrace_connection
        mat = "As in input image" if material=="Default" else material
        led_edge = "As in input image" if lighting_edge=="Default" else lighting_edge
        vol_adj = "As in input image" if building_volume_adjustment=="Default" else building_volume_adjustment
        site_ctx = site_context_descriptions.get(site_context, site_context)

        # Build prompt
        prompt = f"A concept architectural design based on the input image.\n"
        prompt += f"View / Camera Angle: {camera_view}\n"
        prompt += f"Depth of Field: {dof}\n"
        prompt += f"Motion Blur: {blur}\n"
        prompt += f"Time of Day: {tod}\n"
        prompt += f"Weather: {wea}\n"
        prompt += f"Wind Strength: {wind}\n"
        prompt += f"Interior Lights: {lights}\n"
        prompt += f"Active Reflection: {reflection}\n"
        prompt += f"Render Style: {rstyle}\n"
        prompt += f"Mood / Style: {mood}\n"
        prompt += f"Corner Style: {corner}\n"
        prompt += f"Terrace Connection: {terrace}\n"
        prompt += f"Material: {mat}\n"
        prompt += f"Lighting Edge: {led_edge}\n"
        prompt += f"Building Volume Adjustment: {vol_adj}\n"
        prompt += f"Site Context: {site_ctx}\n"
        if additional_prompt:
            prompt += f"Additional Notes: {additional_prompt}\n"
        prompt += "Ensure building fits in frame, preserve original proportions if Default, and adjust corners, terraces, and edges as specified.\n"

        st.text_area("Generated Concept Prompt", prompt, height=400)
        st.success("Concept Prompt generated! ✅ Copy manually to clipboard (works on mobile and PC).")
