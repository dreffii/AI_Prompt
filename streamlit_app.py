import streamlit as st

# --- App Title ---
st.set_page_config(page_title="AI Prompt Generator by Oak Sopheaktra", layout="wide")
st.title("AI Prompt Generator by Oak Sopheaktra")

# --- Variables for dropdowns ---
view_angles = ["Default Angle","Professional Archviz","Eye-Level","High-Angle","Low-Angle","Aerial / Drone",
               "Close-up","Wide Shot","Bird's Eye View","View From Inside (Building to Outside)"]

depth_of_field_opts = ["None","Subtle","Moderate","Strong"]
motion_blur_opts = ["None","Light","Medium","Heavy"]

# Expanded Time of Day Options
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
    "Enhance Only (No Context)": "Focus on enhancing the building itself without any external surroundings. Keep the background minimal and neutral.",
    "Modern Metropolis (Day)": "Placed in a contemporary city during daytime, with clean streets, glass and steel skyscrapers, moderate pedestrian and vehicle activity under natural daylight.",
    "Modern Metropolis (Night)": "Set in a modern urban area at night, with illuminated skyscrapers, streetlights reflecting on wet pavements, and scattered traffic.",
    "Suburban Neighborhood": "A calm suburban area with houses, lawns, tree-lined streets, and soft daylight ambiance.",
    "Historic European Street": "Set on a cobblestone street lined with historic European buildings, ornate facades, vintage street lamps, and pedestrians strolling.",
    "Japanese Zen Garden": "A tranquil Japanese garden with raked gravel, koi ponds, stone lanterns, bamboo, and carefully placed plants.",
    "Coastal Town": "A small coastal town with seafront promenade, boats in the harbor, small houses, and sparkling water under daylight.",
    "Mountain Valley": "Nestled in a valley surrounded by majestic mountains, lush greenery, and a flowing river.",
    "Lush Forest": "Dense forest with tall trees, sunlight filtering through leaves, moss-covered rocks, and serene natural atmosphere.",
    "Tropical Island Beach": "White sand beach with turquoise water, palm trees, gentle waves, and bright sunlight.",
    "Desert Landscape": "A vast desert with golden sand dunes, sparse vegetation, rocky formations, and clear skies.",
    "Upscale Plaza": "A modern urban plaza with designer seating, sculptures, clean paving, and surrounding glass buildings.",
    "Golf Course Sunrise": "A meticulously landscaped golf course at sunrise, with dew-covered grass, pristine greens, and distant trees in warm light.",
    "Waterfront Promenade": "Contemporary waterfront with yachts docked, reflective surfaces, and modern apartments nearby.",
    "Street Food Market": "Lively multi-ethnic street market with steam from stalls, colorful signs, and diverse crowds enjoying food.",
    "Botanical Garden": "Serene botanical garden with diverse plants, greenhouses, walking paths, and sunlight filtering through trees.",
    "Highway Interchange Night": "Busy highway interchange at night, with streaks of car lights, overpasses, and urban glow illuminating the scene.",
    "Glaciated Mountain Pass": "Remote glaciated mountain pass with rocky cliffs, snow patches, and dramatic overcast sky.",
    "Luxury Resort": "High-end resort with infinity pools, manicured gardens, palm trees, and ocean views under tropical sun.",
    "Financial District": "Bustling financial district with glass-and-steel skyscrapers, suited professionals, and urban activity.",
    "Abandoned Industrial": "Decaying industrial complex with rusted machinery, broken concrete structures, and overgrown vegetation.",
    "University Campus Quad": "Vibrant university quad with historic academic buildings, students walking, and mature trees providing shade.",
    "Historic Cathedral Square": "Grand cathedral square with ornate architecture, tourists, pigeons, and open plaza.",
    "Data Center Park": "Modern data center park with rows of uniform buildings, minimalist landscaping, and service roads.",
    "Volcanic Sand Beach": "Remote black sand beach with dramatic rocks, powerful waves, and moody sky.",
    "Train Station Concourse": "Busy train station concourse with high ceilings, large boards, and commuters walking.",
    "High-Tech Agricultural": "Advanced agricultural facility with automated crop rows, controlled lighting, and modern structures.",
    "Temperate River": "Alongside a pristine river with clear water, smooth rocks, lush greenery, and dappled sunlight.",
    "Exclusive Residential": "Private residential enclave with distinct homes, private gardens, and tree-lined streets.",
    "Art District": "Vibrant art district with colorful murals, galleries, street performances, and bohemian atmosphere.",
    "Reflective Salt Flat": "Open salt flat with reflective surface at sunset, dramatic sky, and horizon stretching infinitely.",
    # Remaining site contexts can be added here with same style
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

    st.text_area("Generated Prompt", prompt, height=400)
    st.success("Prompt generated! ✅ Copy manually to clipboard (works on mobile and PC).")
