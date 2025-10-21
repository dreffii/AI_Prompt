import streamlit as st

# --- App Title / Config ---
st.set_page_config(page_title="AI Prompt Generator by Oak Sopheaktra", layout="wide")
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", [
    "Architectural Render Prompt",      # keep this first page exactly like your original code
    "Architectural Concept Prompt",     # page 2 - image-aware concept (prompts only)
    "New Building Design Prompt"        # page 3 - new building types (villa, high-rise, shop...)
])

# --- Shared variables (same across all pages) ---
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

# --- Site context descriptions (same object as your original) ---
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

# --- Internal Material Description (shared) ---
material_description = "accurately represent the materials visible in the input image (concrete, glass, wood, metal, etc.)"

# ----------------------------------------------------------
# PAGE 1: Architectural Render Prompt (kept like your original)
# ----------------------------------------------------------
if page == "Architectural Render Prompt":
    st.title("AI Prompt Generator by Oak Sopheaktra")

    # --- Layout (kept the same structure and labels as your original code) ---
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

# ----------------------------------------------------------
# PAGE 2: Architectural Concept Prompt (image-type aware; prompts only)
# ----------------------------------------------------------
elif page == "Architectural Concept Prompt":
    st.title("Architectural Concept Prompt Generator (Image-Aware)")

    # Use the same controls (variables) as page 1
    col1, col2 = st.columns(2)

    with col1:
        view_angle = st.selectbox("View / Camera Angle", view_angles, key="p2_view")
        depth_of_field = st.selectbox("Depth of Field", depth_of_field_opts, key="p2_dof")
        motion_blur = st.selectbox("Motion Blur", motion_blur_opts, key="p2_mb")
        time_of_day = st.selectbox("Time of Day", time_of_day_opts, key="p2_time")
        weather = st.selectbox("Weather", weather_opts, key="p2_weather")
        wind_strength = st.selectbox("Wind Strength", wind_strength_opts, key="p2_wind")
        interior_lights = st.selectbox("Interior Lights", interior_lights_opts, key="p2_interior")

    with col2:
        active_reflection = st.selectbox("Active Reflection", active_reflection_opts, key="p2_reflection")
        render_style = st.selectbox("Render Style", render_style_opts, key="p2_renderstyle")
        site_context = st.selectbox("Site Context", site_context_opts, key="p2_sitecontext")
        mood_style = st.selectbox("Mood / Style", mood_style_opts, key="p2_mood")

    st.subheader("Concept Options")
    # Specific concept-oriented options, but still using same style controls
    concept_type = st.selectbox("Concept Type (what kind of building the image is)", [
        "Same Type As Input (auto-detect assumed)", "Cultural Center","Pavilion","House/Villa","Tower","Commercial Shop","Mixed-use Block",
        "Bridge / Infrastructure","Campus Building","Exhibition Space"
    ])
    concept_focus = st.multiselect("Concept Focus (choose multiple if needed)", [
        "Form Evolution","Massing & Proportion","Light & Shadow","Material Transformation","Adaptive Reuse",
        "Spatial Sequence","Landscape Integration","Sustainability Strategies","Circulation & Entrances"
    ], default=["Form Evolution", "Light & Shadow"])
    extra_keywords = st.text_input("Extra keywords (optional)", placeholder="e.g. vaulted roof, perforated facade, cross-ventilation")

    if st.button("Generate Concept Prompt"):
        # Build a detailed prompt that instructs the AI to "read" the (imagined) input image type
        prompt = "Only output prompts. Assume you have a single input image of an architectural work. " \
                 "Do NOT ask for an upload — analyze the building type, form, and visible design language and produce concept prompts that evolve from that image's type.\n\n"

        prompt += "Instruction to AI:\n"
        prompt += "- Identify the building category and dominant formal language in the (assumed) input image and keep the concept within that category.\n"
        prompt += "- Evolve the design language (do not convert to an unrelated building type).\n"
        prompt += "- Provide 3 distinct concept prompt variations (short titles + 2–3 detailed bullet sentences each) suitable for AI image generation.\n\n"

        prompt += "Context (from user controls):\n"
        prompt += f"- View / Camera Angle: {view_angle}. Depth of Field: {depth_of_field}. Motion Blur: {motion_blur}.\n"
        prompt += f"- Time of Day: {time_of_day}. Weather: {weather}. Wind Strength: {wind_strength}. Interior Lights: {interior_lights}.\n"
        prompt += f"- Reflections: {active_reflection}. Render Style: {render_style}. Site Context: {site_context_descriptions.get(site_context, site)}\n" if site in site_context_descriptions else ""
        # The previous line uses site variable; to ensure safety, we'll add a simpler context line instead:
        prompt += f"- Site Context: {site_context_descriptions.get(site_context, site_context)}.\n"
        prompt += f"- Mood / Style: {mood_style}.\n"
        prompt += f"- Material guidance: {material_description}.\n"
        if extra_keywords:
            prompt += f"- Extra keywords to include: {extra_keywords}.\n"
        if concept_focus:
            prompt += f"- Concept focus areas: {', '.join(concept_focus)}.\n\n"

        prompt += "Output format (strict):\n"
        prompt += "1) Concept Title — short descriptive name\n"
        prompt += "   - Prompt: One or two long sentences with explicit details for AI image generation. Include material specifics, lighting, scale, and composition. Make it vivid and prioritized for rendering tools (e.g., 'ultra-detailed, photoreal, lens info, lighting').\n"
        prompt += "   - Notes: 1-2 short design notes explaining the design intention and what to emphasize.\n\n"
        prompt += "Repeat for 3 variations with different design moves while keeping to the same building type inferred from the image.\n"
        prompt += "Do not add UI instructions, do not ask for image upload, and do not include analysis text beyond the 3 prompts and notes.\n\n"

        prompt += "End of instruction."

        st.text_area("Generated Concept Prompt (copy these into your LLM/image model)", prompt, height=520)
        st.success("Concept prompts generated! ✅ Copy manually to clipboard.")

# ----------------------------------------------------------
# PAGE 3: New Building Design Prompt (same variables used)
# ----------------------------------------------------------
elif page == "New Building Design Prompt":
    st.title("New Building Design Prompt Generator")

    # Use same controls (with different keys to avoid conflicts)
    col1, col2 = st.columns(2)
    with col1:
        view_angle = st.selectbox("View / Camera Angle", view_angles, key="p3_view")
        depth_of_field = st.selectbox("Depth of Field", depth_of_field_opts, key="p3_dof")
        motion_blur = st.selectbox("Motion Blur", motion_blur_opts, key="p3_mb")
        time_of_day = st.selectbox("Time of Day", time_of_day_opts, key="p3_time")
        weather = st.selectbox("Weather", weather_opts, key="p3_weather")
        wind_strength = st.selectbox("Wind Strength", wind_strength_opts, key="p3_wind")
        interior_lights = st.selectbox("Interior Lights", interior_lights_opts, key="p3_interior")

    with col2:
        active_reflection = st.selectbox("Active Reflection", active_reflection_opts, key="p3_reflection")
        render_style = st.selectbox("Render Style", render_style_opts, key="p3_renderstyle")
        site_context = st.selectbox("Site Context", site_context_opts, key="p3_sitecontext")
        mood_style = st.selectbox("Mood / Style", mood_style_opts, key="p3_mood")

    st.subheader("Design Specifics")
    building_types = st.selectbox("Building Type", [
        "Modern Villa","Luxury Resort","High-Rise Tower","Commercial Complex","Shop / Retail Unit","Apartment Block",
        "Cultural Center","Community Market","School / Educational","Hospital","Office Building","Mixed-use Complex"
    ])
    design_language = st.selectbox("Design Language", [
        "Modern Minimalist","Tropical Modern","Neo-Futuristic","Sustainable Green","Industrial Loft","Vernacular Khmer",
        "Brutalist","Scandinavian","Japanese Wabi-Sabi","Luxury Contemporary"
    ])
    material_focus = st.multiselect("Materials (choose multiple)", ["Concrete","Glass","Wood","Steel","Stone","Bamboo","Green Wall / Vegetation"], default=["Concrete","Glass"])
    scale_opts = st.selectbox("Scale", ["Small Residential","Medium Building","Large Complex","Skyscraper"])
    context = st.selectbox("Site Context (brief)", ["Urban City","Suburban Area","Coastal Zone","Mountain Area","Forest","Island","Riverside"])
    key_features = st.text_input("Key Features / Keywords", placeholder="e.g. infinity pool, vertical garden, perforated metal screen, courtyard")

    if st.button("Generate Design Prompt"):
        # Compose a long, detailed design & render prompt
        prompt = f"Design prompt for a {design_language.lower()} {building_types.lower()} sited in a {context.lower()} environment.\n\n"
        prompt += "Goals:\n"
        prompt += "- Produce a realistic, buildable architectural design with strong massing, clear circulation, and environmental responsiveness.\n"
        prompt += "- Provide detailed instructions for visual rendering (materials, lighting, camera, composition) and design rationale.\n\n"

        prompt += "Design Parameters (from controls):\n"
        prompt += f"- View / Camera Angle: {view_angle}. Depth of Field: {depth_of_field}. Motion Blur: {motion_blur}.\n"
        prompt += f"- Time of Day: {time_of_day}. Weather: {weather}. Wind Strength: {wind_strength}. Interior Lights: {interior_lights}.\n"
        prompt += f"- Active Reflection: {active_reflection}. Render Style: {render_style}. Mood: {mood_style}.\n"
        prompt += f"- Site Context (detailed): {site_context_descriptions.get(site_context, site_context)}\n"
        prompt += f"- Material focus: {', '.join(material_focus)}. Key features: {key_features if key_features else 'none specified'}.\n"
        prompt += f"- Scale: {scale_opts}.\n\n"

        prompt += "Output (structured):\n"
        prompt += "1) Short Title: e.g., 'Coastal Minimalist Villa with Cascading Terraces'\n\n"
        prompt += "2) Full Design Description (2-4 paragraphs):\n"
        prompt += "- Describe overall massing and form, facade strategy, and primary materials.\n"
        prompt += "- Explain circulation, main spatial sequences, relationship to landscape/site, and human scale considerations.\n"
        prompt += "- Include sustainable strategies (passive ventilation, shading, rainwater capture) if appropriate.\n\n"

        prompt += "3) Visual / Rendering Instructions (detailed):\n"
        prompt += "- Camera/Composition: specify camera height, lens (e.g., 35mm, 24mm), framing (wide, close-up), and POV (eye-level, aerial).\n"
        prompt += "- Lighting: time of day, sun position, HDRI/artificial lights, interior/exterior light balance, shadow crispness.\n"
        prompt += "- Materials & Textures: describe exact materials and texture behavior (exposed concrete with fine formwork lines, low-iron glass, aged teak wood planks, matte black metal). Mention wear, seams, tiles, grout, reflections.\n"
        prompt += "- Environmental detail: landscaping, trees, hardscape, human figures, vehicles, street furniture, water features.\n\n"

        prompt += "4) Key Scenes to Render (3 scenes):\n"
        prompt += "- Primary exterior perspective (show massing & context).\n"
        prompt += "- Secondary exterior detail (facade material and entry).\n"
        prompt += "- Interior / courtyard or rooftop view showing spatial quality and materiality.\n\n"

        prompt += "Finish with a concise sentence describing the architectural intent and mood.\n\n"
        prompt += "End of prompt."

        st.text_area("Generated Building Design Prompt (copy into your LLM/image model)", prompt, height=520)
        st.success("New building design prompt generated! ✅ Copy manually to clipboard.")
