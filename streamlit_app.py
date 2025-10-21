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
site_context_opts = ["Enhance Only (No Context)","Modern Metropolis (Day)","Modern Metropolis (Night)","Suburban Neighborhood",
                     "Historic European Street","Japanese Zen Garden","Coastal Town","Mountain Valley","Lush Forest",
                     "Tropical Island Beach","Desert Landscape","Upscale Plaza","Golf Course Sunrise","Waterfront Promenade",
                     "Street Food Market","Botanical Garden","Highway Interchange Night","Glaciated Mountain Pass",
                     "Luxury Resort","Financial District","Abandoned Industrial","University Campus Quad","Historic Cathedral Square",
                     "Data Center Park","Volcanic Sand Beach","Train Station Concourse","High-Tech Agricultural",
                     "Temperate River","Exclusive Residential","Art District","Reflective Salt Flat"]
mood_style_opts = ["neutral","modern","minimalist","classic","futuristic","conceptual"]

# --- Site context descriptions ---
site_context_descriptions = {
    "Enhance Only (No Context)": "Focus on enhancing the architecture without adding any external context, keeping the surroundings minimal and unobtrusive.",
    "Modern Metropolis (Day)": "Placed in a bustling, modern city during the day, with glass skyscrapers, busy streets, pedestrians, and urban activity under clear daylight.",
    "Modern Metropolis (Night)": "Set in a modern city at night, with illuminated skyscrapers, street lights reflecting on wet pavements, and cars moving through the streets.",
    "Suburban Neighborhood": "Located in a calm suburban neighborhood, with neatly arranged houses, tree-lined streets, cars parked in driveways, and soft daylight.",
    "Historic European Street": "Set on a cobblestone street lined with historic European buildings, ornate facades, street lamps, and pedestrians strolling under soft daylight.",
    "Japanese Zen Garden": "Placed within a serene Japanese Zen garden, featuring traditional stone lanterns, koi ponds, bamboo, and carefully raked gravel paths.",
    "Coastal Town": "Situated on a picturesque coastal town, with small houses, seafront promenade, boats in the harbor, and sparkling ocean under a clear sky.",
    "Mountain Valley": "Set in a valley surrounded by majestic mountains, with lush greenery, a flowing river, and scattered farmhouses in natural lighting.",
    "Lush Forest": "Embedded in a dense, vibrant forest, with towering trees, soft sunlight filtering through leaves, moss-covered rocks, and a serene natural atmosphere.",
    "Tropical Island Beach": "Placed on a tropical island beach, with soft white sand, turquoise water, palm trees swaying, and gentle waves under bright sunlight.",
    "Desert Landscape": "Set in a vast desert, with golden sand dunes, sparse vegetation, rocky formations, and a clear blue sky overhead.",
    "Upscale Plaza": "Situated in an upscale urban plaza with designer seating, modern sculptures, clean paving, and reflective glass buildings under clear daylight.",
    "Golf Course Sunrise": "Placed on a meticulously landscaped golf course at sunrise, with dew-covered grass, pristine greens, and distant trees bathed in warm light.",
    "Waterfront Promenade": "Located on a contemporary waterfront promenade, with yachts docked in a marina, reflective surfaces, and modern apartment buildings nearby.",
    "Street Food Market": "Set within a lively, multi-ethnic street food market, with steam rising from stalls, colorful signs, and diverse crowds enjoying food.",
    "Botanical Garden": "Placed in a serene botanical garden, featuring diverse plant species, ornate greenhouses, walking paths, and sunlight filtering through trees.",
    "Highway Interchange Night": "Situated adjacent to a busy interstate highway interchange at night, with streaks of car lights, overpasses, and urban glow illuminating the scene.",
    "Glaciated Mountain Pass": "Located on a remote, glaciated mountain pass, with stark rocky cliffs, patches of snow, and a dramatic, overcast sky.",
    "Luxury Resort": "Set within a high-end luxury resort complex, featuring infinity pools, manicured gardens, palm trees, and ocean views under a tropical sun.",
    "Financial District": "Placed in a bustling financial district, surrounded by towering glass-and-steel skyscrapers, suited professionals, and urban activity.",
    "Abandoned Industrial": "Situated within an abandoned industrial complex, with decaying concrete structures, rusting machinery, and overgrown vegetation.",
    "University Campus Quad": "Located on a vibrant university campus quad, with historic academic buildings, students walking, and mature trees providing shade.",
    "Historic Cathedral Square": "Set against the backdrop of a grand historic European cathedral square, with ornate architecture, tourists, and pigeons in the open plaza.",
    "Data Center Park": "Placed within a modern data center park, with rows of sleek uniform buildings, minimalist landscaping, and service roads.",
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
