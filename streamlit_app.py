import streamlit as st

# --- App Setup ---
st.set_page_config(page_title="NAG AI Prompt Generator", layout="wide")

# --- Sidebar Navigation ---
page = st.sidebar.radio(
    "🧭 Navigate",
    ["1️⃣ Prompt Generator", "2️⃣ AI Concept Generator", "3️⃣ New Building Design Generator"]
)

# ============================================================
# PAGE 1: Prompt Generator
# ============================================================
if page == "1️⃣ Prompt Generator":
    st.title("NAG AI Prompt Generator")

    # --- Dropdown Options ---
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

    # --- Site Context Descriptions ---
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

    material_description = "accurately represent the materials visible in the input image (concrete, glass, wood, metal, etc.)"

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
            "Furniture":furniture,
            "Vehicles (Cars, Bikes)":vehicles,
            "People":people,
            "Trees & Vegetation":trees,
            "Street Furniture":street_furniture,
            "Foreground Elements":foreground_elements
        }.items() if val])
        
        prompt = f"""A highly detailed, photorealistic architectural rendering.
Materials: {material_description}.
View / Camera Angle: {view_angle}
Depth of Field: {depth_of_field}
Motion Blur: {motion_blur}
Time of Day: {time_of_day}
Weather: {weather}
Wind Strength: {wind_strength}
Interior Lights: {interior_lights}
Active Reflection: {active_reflection}
Render Style: {render_style}
Site Context: {site_context_descriptions.get(site_context, site_context)}
Mood / Style: {mood_style}
Objects included: {selected_objects if selected_objects else 'none'}.
Focus on realistic textures, materials, lighting, and perspective without adding predefined shapes or design elements.
Preserve the building’s original forms and proportions as seen in the input image."""
        st.text_area("Generated Prompt", prompt, height=400)
        st.success("Prompt generated! ✅ Copy manually to clipboard (works on mobile and PC).")

# ============================================================
# PAGE 2: AI Concept Generator
# ============================================================
elif page == "2️⃣ AI Concept Generator":
    st.title("AI Concept Generator 🧠")
    st.write("Upload an image — AI will understand its type and style, then generate a conceptual continuation or transformation.")

    uploaded_image = st.file_uploader("Upload image (JPG/PNG)", type=["jpg","jpeg","png"])
    concept_options = [
        "Concept Continuation (Same Type)",
        "Style Evolution (Modernized or Futuristic)",
        "Cultural Reinterpretation",
        "Material Redesign",
        "Environmental Adaptation",
        "Landscape Integration",
        "Interior Transformation",
        "Sustainable Design Upgrade",
        "Historical Revival",
        "Adaptive Reuse Concept"
    ]
    concept_type = st.selectbox("Concept Type", concept_options)
    mood_options = ["neutral","modern","minimalist","classic","futuristic","eco","conceptual"]
    mood = st.selectbox("Mood / Design Direction", mood_options)

    if st.button("Generate Concept Prompt"):
        if uploaded_image is None:
            st.warning("Please upload an image first.")
        else:
            prompt = f"""AI Concept Design Prompt:
Understand the uploaded image to identify the building type, scale, materials, and form language.
Generate a new architectural concept with the same type and proportion.

Concept Type: {concept_type}
Mood / Design Direction: {mood}

Instructions:
- Maintain building function and general massing.
- Innovate the design logic, façade rhythm, material palette, and surrounding context.
- Suggest improvements or futuristic reinterpretations without breaking the architectural essence.
- Produce a detailed, photorealistic render prompt suitable for AI image generation tools."""
            st.text_area("Generated Concept Prompt", prompt, height=350)
            st.success("Concept prompt generated successfully! ✅")

# ============================================================
# PAGE 3: New Building Design Generator
# ============================================================
elif page == "3️⃣ New Building Design Generator":
    st.title("New Building Design Generator 🏙️")
    st.write("Generate detailed prompts for new building designs — villas, shops, towers, and more.")

    building_types = [
        "Modern Villa","Luxury Villa","High-Rise Tower","Commercial Shop House",
        "Resort Hotel","Cultural Center","Office Building","Apartment Complex",
        "Mixed-Use Development","Museum / Gallery","Sports Facility","University Building",
        "Library","Retail Plaza","Public Pavilion"
    ]
    styles = ["Modern","Minimalist","Classic","Brutalist","Futuristic","Eco-Organic","Neo-Tropical","Vernacular Khmer Inspired"]
    materials = ["Concrete","Glass","Wood","Metal","Stone","Brick","Mixed Material"]
    site_context = ["Urban Center","Suburban Zone","Coastal Area","Mountain Slope","Forest Edge",
                    "Desert Plain","Island Beach","Urban Plaza","Riverfront","Cultural District"]
    time_of_day = ["Day","Golden Hour","Night","Blue Hour","Overcast"]
    render_style = ["Photorealistic","Ultra Realistic","Concept Sketch","Architectural Visualization"]

    col1, col2 = st.columns(2)
    with col1:
        b_type = st.selectbox("Building Type", building_types)
        b_style = st.selectbox("Architectural Style", styles)
        b_material = st.selectbox("Primary Material", materials)
    with col2:
        b_context = st.selectbox("Site Context", site_context)
        b_time = st.selectbox("Time of Day", time_of_day)
        b_render = st.selectbox("Render Style", render_style)

    if st.button("Generate Design Prompt"):
        prompt = f"""New Building Design Prompt:
Type: {b_type}
Architectural Style: {b_style}
Primary Material: {b_material}
Site Context: {b_context}
Time of Day: {b_time}
Render Style: {b_render}

Instructions:
- Generate a detailed, realistic architectural render.
- Focus on proportion, structure, and spatial hierarchy.
- Include appropriate lighting, textures, and environmental integration.
- Show believable landscape and context around the building.
- Emphasize the design identity and materiality clearly."""
        st.text_area("Generated Design Prompt", prompt, height=350)
        st.success("New building design prompt generated successfully! ✅")
