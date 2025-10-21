import streamlit as st

# --- App Title ---
st.set_page_config(page_title="AI Prompt Generator by Oak Sopheaktra", layout="wide")
st.title("AI Prompt Generator by Oak Sopheaktra")

# --- Variables for dropdowns ---
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
mood_style_opts = ["neutral","modern","minimalist","classic","futuristic","conceptual"]

# --- Site contexts ---
site_context_opts = [
    "Enhance Only (No Context)","Modern Metropolis (Day)","Modern Metropolis (Night)","Suburban Neighborhood",
    "Historic European Street","Japanese Zen Garden","Coastal Town","Mountain Valley","Lush Forest",
    "Tropical Island Beach","Desert Landscape","Upscale Plaza","Golf Course Sunrise","Waterfront Promenade",
    "Street Food Market","Botanical Garden","Highway Interchange Night","Glaciated Mountain Pass",
    "Luxury Resort","Financial District","Abandoned Industrial","University Campus Quad","Historic Cathedral Square",
    "Data Center Park","Volcanic Sand Beach","Train Station Concourse","High-Tech Agricultural",
    "Temperate River","Exclusive Residential","Art District","Reflective Salt Flat",
    "Residential Area – Suburban","Residential Area – Urban","Riverside Residential","Urban Market / Street Market",
    "Supermarket / Retail Complex","Urban Street / Downtown","Hospital / Medical Campus","School Campus",
    "University Campus","Office / Company Campus","Urban Green Park","Public Parking Lot",
    "Riverside / Waterfront Urban","Mixed-use Urban Development","Industrial / Warehouse Area",
    "Transport Hub – Bus / Train Station","Community Center / Civic Plaza","Riverside Park / Recreation Area",
    "Urban Intersection / Street Network","Hospital Rooftop / Helipad Area",
    "Pedestrian Street / Promenade","Urban Plaza / Square","Residential Courtyard","Riverside Walkway",
    "Parking Garage / Multilevel Parking","Suburban Shopping Street","Industrial Park / Logistics Area",
    "University Library Area","Hospital Entrance / Ambulance Area","School Playground / Sports Area",
    "Botanical Conservatory / Greenhouse","Corporate Office Plaza","Mixed Residential & Retail Street",
    "Community Park with Playground","Harbor / Marina","Mountain Lodge / Resort Area",
    "Urban Rooftop Garden","Bus Terminal / Transit Hub","City Intersection with Roundabout","Waterfront Park / Pier"
]

# --- Site context descriptions ---
site_context_descriptions = {
    "Enhance Only (No Context)": "Focus on the building itself without adding any external surroundings. Keep the background minimal and neutral.",
    "Modern Metropolis (Day)": "Situated in a contemporary city during daytime, with clean streets, glass and steel skyscrapers, moderate pedestrian and vehicle activity, under natural daylight.",
    "Modern Metropolis (Night)": "Set in a modern urban area at night, with illuminated skyscrapers, streetlights, reflections on wet pavements, and scattered traffic.",
    "Suburban Neighborhood": "Located in a calm suburban neighborhood with houses, lawns, tree-lined streets, and soft daylight.",
    "Japanese Zen Garden": "Set in a tranquil Japanese Zen garden with rocks, ponds, bamboo, and raked gravel paths.",
    "Coastal Town": "A small coastal town with houses, a seafront promenade, boats, and sparkling water under daylight.",
    "Mountain Valley": "Nestled in a valley surrounded by mountains, greenery, and a flowing river.",
    "Lush Forest": "Dense forest with tall trees, sunlight filtering through leaves, moss-covered rocks, and natural atmosphere.",
    "Tropical Island Beach": "White sand beach with palm trees, turquoise water, gentle waves, and bright sunlight.",
    "Desert Landscape": "Vast desert with golden dunes, sparse vegetation, rocky formations, and clear skies.",
    # ... continue descriptions for all 70+ contexts ...
}

# --- Site context sample images ---
site_context_images = {
    "Enhance Only (No Context)":"data/enhance_only.jpg",
    "Modern Metropolis (Day)":"data/modern_day.jpg",
    "Modern Metropolis (Night)":"data/modern_night.jpg",
    "Suburban Neighborhood":"data/suburban.jpg",
    "Historic European Street":"data/historic_europe.jpg",
    "Japanese Zen Garden":"data/zen_garden.jpg",
    "Coastal Town":"data/coastal_town.jpg",
    "Mountain Valley":"data/mountain_valley.jpg",
    "Lush Forest":"data/lush_forest.jpg",
    "Tropical Island Beach":"data/tropical_beach.jpg",
    "Desert Landscape":"data/desert.jpg",
    "Upscale Plaza":"data/upscale_plaza.jpg",
    "Golf Course Sunrise":"data/golf_course.jpg",
    "Waterfront Promenade":"data/waterfront.jpg",
    "Street Food Market":"data/street_food.jpg",
    "Botanical Garden":"data/botanical_garden.jpg",
    # ... continue mapping all site contexts to images in data/ folder ...
}

# --- Internal Material Description ---
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

# --- Show preview image ---
if site_context in site_context_images:
    st.image(site_context_images[site_context], caption=site_context, use_column_width=True)

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
    
    # Default Angle handling
    camera_view = "Maintain same view as input" if view_angle=="Default Angle" else view_angle

    prompt = f"A highly detailed, photorealistic architectural rendering.\n"
    prompt += f"Materials: {material_description}.\n"
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
    prompt += f"Objects included: {selected_objects if selected_objects else 'none'}.\n"
    prompt += "Focus on realistic textures, materials, lighting, and perspective without adding predefined shapes or design elements.\n"
    prompt += "Preserve the building’s original forms and proportions as seen in the input image."

    st.text_area("Generated Prompt", prompt, height=500)
    st.success("Prompt generated! ✅ Copy manually to clipboard (works on mobile and PC).")
