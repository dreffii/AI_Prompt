import streamlit as st
from utils import *

st.title("Architectural Prompt Generator")

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

objects_dict = {
    "Furniture": furniture,
    "Vehicles (Cars, Bikes)": vehicles,
    "People": people,
    "Trees & Vegetation": trees,
    "Street Furniture": street_furniture,
    "Foreground Elements": foreground_elements
}

if st.button("Generate Prompt"):
    prompt = generate_prompt(
        view_angle, depth_of_field, motion_blur, time_of_day, weather, wind_strength,
        interior_lights, active_reflection, render_style, site_context, mood_style,
        objects_dict, concept_mode=False
    )
    st.text_area("Generated Prompt", prompt, height=400)
    st.success("Prompt generated! ✅ Copy manually to clipboard.")
