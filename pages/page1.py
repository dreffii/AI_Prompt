import streamlit as st
from animated_title import show_animated_title

def show_prompt_page():
    st.set_page_config(page_title="🏛️ AI Prompt Generator ✨", layout="wide")

    # Show animated title
    show_animated_title()

    # --- Variables for dropdowns ---
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
        "Suburban Neighborhood": "Located in a calm suburban area, featuring low-rise houses, tree-lined streets, parked cars, and soft natural light.",
        "Historic European Street": "Placed on a cobblestone street with historic buildings, ornate facades, traditional street lamps, and light pedestrian traffic.",
        "Japanese Zen Garden": "Embedded in a tranquil Japanese garden, with stone pathways, koi ponds, bamboo, bonsai trees, and natural soft lighting.",
        "Coastal Town": "Situated in a small seaside town, with low-rise houses, boardwalks, boats in the harbor, and gentle sunlight reflecting on water.",
        "Mountain Valley": "Set in a valley surrounded by mountains, with scattered rural houses, rivers or streams, lush vegetation, and realistic daylight.",
        "Lush Forest": "Embedded in a dense forest, with tall trees, filtered sunlight, moss-covered ground, and natural textures dominating the surroundings.",
        "Tropical Island Beach": "Located on a tropical beach with palm trees, white sand, turquoise water, and natural sunlight. Subtle vegetation can be included.",
        "Desert Landscape": "Set in a realistic desert with sand dunes, rocky outcrops, sparse shrubs, and clear blue sky or realistic atmospheric haze.",
        "Upscale Plaza": "Placed in an urban plaza with paved areas, modern benches, minimalistic sculptures, and surrounding buildings reflecting sunlight naturally.",
        "Golf Course Sunrise": "Situated on a landscaped golf course at sunrise, with dew on grass, rolling greens, scattered trees, and soft morning light.",
        "Waterfront Promenade": "Located along a riverfront or marina, with yachts or boats docked, modern buildings nearby, and realistic reflections on water surfaces.",
        "Street Food Market": "Set in an urban market with vendor stalls, subtle human activity, steam or smoke effects from cooking, and realistic lighting.",
        "Botanical Garden": "Placed in a curated garden with walking paths, diverse plant species, small water features, and soft natural light.",
        "Highway Interchange Night": "Set beside a highway junction at night, with moving traffic, light streaks, overpasses, and urban lighting in the background.",
        "Glaciated Mountain Pass": "Situated on a remote snowy or glaciated mountain pass, with realistic snow textures, rocky formations, and overcast or diffused lighting.",
        "Luxury Resort": "Set in a high-end resort environment, featuring pools, landscaped gardens, palm trees, villas or buildings, and natural daylight.",
        "Financial District": "Placed in a modern business district with glass skyscrapers, paved streets, sparse pedestrian or vehicle activity, realistic reflections.",
        "Abandoned Industrial": "Situated in an industrial area with old factories, rusted metal structures, weathered concrete, and subtle overgrown vegetation.",
        "University Campus Quad": "Academic buildings, open quad areas, pathways, trees, students walking, benches, and natural daylight.",
        "Historic Cathedral Square": "Placed in front of a historic cathedral or plaza, featuring stone pavement, ornate architecture, light pedestrian activity, and natural daylight.",
        "Data Center Park": "Situated in a modern tech campus with low-rise uniform buildings, controlled landscaping, paved service roads, and realistic outdoor lighting.",
        "Volcanic Sand Beach": "Located on a black sand beach with volcanic rocks, waves realistically interacting with the shoreline, and cloudy or dramatic sky.",
        "Train Station Concourse": "Set inside or in front of a realistic train station concourse, with high ceilings, structural details, commuters, and subtle natural or artificial lighting.",
        "High-Tech Agricultural": "Placed in a modern farm environment with controlled crop rows, greenhouses or automated structures, and daylight illuminating the scene.",
        "Temperate River": "Situated alongside a flowing river in a temperate forest, with realistic rocks, trees, water reflections, and natural sunlight.",
        "Exclusive Residential": "Set in a gated or exclusive neighborhood, with architecturally distinct houses, private gardens, and tree-lined streets.",
        "Art District": "Located in a creative urban neighborhood, with murals, small galleries, street furniture, and subtle pedestrian activity.",
        "Reflective Salt Flat": "Set on a flat reflective surface, like a salt flat, with water or reflective ground, distant horizon, and natural sky lighting.",
        # Extended + new contexts
        "Residential Area – Suburban":"Calm suburban streets with detached houses, gardens, tree-lined roads, parked cars, and soft daylight.",
        "Residential Area – Urban":"High-density apartment blocks or townhouses, narrow streets, sidewalks, light pedestrian activity, realistic urban lighting.",
        "Riverside Residential":"Houses or low-rise apartments along a riverbank, trees lining the shore, calm water reflections, and natural daylight.",
        "Urban Market / Street Market":"Busy city market with stalls, colorful canopies, light pedestrian activity, realistic street materials, and soft shadows.",
        "Supermarket / Retail Complex":"Modern supermarket or retail plaza, with surrounding parking, signage, pedestrian access, and realistic urban lighting.",
        "Urban Street / Downtown":"City street with mixed-use buildings, sidewalks, streetlights, sparse traffic, and natural daylight.",
        "Hospital / Medical Campus":"Modern hospital or clinic complex, structured building layout, surrounding pathways, parking areas, and realistic lighting.",
        "School Campus":"Primary or secondary school campus, playgrounds, low-rise buildings, trees, sidewalks, and daylight illumination.",
        "University Campus":"Academic buildings, open quad areas, pathways, trees, students walking, benches, and natural daylight.",
        "Office / Company Campus":"Modern office buildings, structured outdoor areas, parking lots, landscaped areas, and soft daylight.",
        "Urban Green Park":"City park with lawns, walking paths, benches, trees, small water features, and light pedestrian activity.",
        "Public Parking Lot":"Open or multi-story parking area with vehicles, painted lines, pedestrian walkways, and realistic urban lighting.",
        "Riverside / Waterfront Urban":"Buildings along a river or canal, boardwalks, small boats, landscaped pathways, and natural reflections.",
        "Mixed-use Urban Development":"Combination of residential, commercial, and leisure buildings in a city block, streets, pedestrian areas, and realistic urban materials.",
        "Industrial / Warehouse Area":"Functional industrial buildings, loading docks, paved roads, vehicles, and realistic daylight or artificial lighting.",
        "Transport Hub – Bus / Train Station":"Busy station with platforms, benches, signage, people walking, and realistic artificial lighting.",
        "Community Center / Civic Plaza":"Public open space surrounded by civic buildings, benches, fountains, trees, and soft daylight.",
        "Riverside Park / Recreation Area":"Park along a river, landscaped lawns, walking paths, small bridges, trees, and calm water reflections.",
        "Urban Intersection / Street Network":"City streets intersecting, traffic signals, pedestrian crossings, vehicles, and street furniture in realistic daylight.",
        "Hospital Rooftop / Helipad Area":"Rooftop of a modern hospital with helipad, safety barriers, mechanical structures, and realistic light/shadow play.",
        # Additional 20 general render types
        "Pedestrian Street / Promenade":"A lively walkway with shops and cafés, light foot traffic, benches, street lamps, and urban greenery.",
        "Urban Plaza / Square":"Open city square with paving, surrounding buildings, fountains or sculptures, pedestrians, and realistic daylight.",
        "Residential Courtyard":"Inner courtyard of apartment buildings or townhouses, landscaped with plants, seating areas, and soft sunlight.",
        "Riverside Walkway":"Promenade along a calm river with benches, small trees, pathways, and reflections on the water.",
        "Parking Garage / Multilevel Parking":"Structured parking area with vehicles, ramps, signage, and artificial lighting.",
        "Suburban Shopping Street":"Low-rise retail buildings, sidewalks, cars, pedestrians, and trees along the street.",
        "Industrial Park / Logistics Area":"Cluster of warehouses and factories with loading docks, service roads, trucks, and minimal greenery.",
        "University Library Area":"Modern library building with outdoor study areas, pathways, benches, and students walking.",
        "Hospital Entrance / Ambulance Area":"Hospital main entrance with drop-off lanes, landscaped areas, signage, and realistic lighting.",
        "School Playground / Sports Area":"Outdoor school yard with sports facilities, trees, walkways, and children or people in daylight.",
        "Botanical Conservatory / Greenhouse":"Glass-enclosed botanical structure, plants inside, surrounding walkways, and filtered sunlight.",
        "Corporate Office Plaza":"Open plaza in front of office towers, paved areas, water features, landscaping, and soft urban lighting.",
        "Mixed Residential & Retail Street":"Street with ground-level shops and upper-floor apartments, pedestrians, vehicles, and urban materials.",
        "Community Park with Playground":"Green park with playground equipment, walking paths, trees, benches, and daylight illumination.",
        "Harbor / Marina":"Small marina with moored boats, piers, low-rise buildings nearby, and calm water reflections.",
        "Mountain Lodge / Resort Area":"Low-rise lodge in mountain setting, surrounding trees, pathways, and realistic daylight.",
        "Urban Rooftop Garden":"Green rooftop space with seating, planters, solar panels, and surrounding urban skyline.",
        "Bus Terminal / Transit Hub":"Bus terminal with platforms, waiting areas, vehicles, signage, and realistic pedestrian activity.",
        "City Intersection with Roundabout":"Urban intersection with roundabout, vehicles, street signs, crosswalks, and moderate pedestrian activity.",
        "Waterfront Park / Pier":"Public park along waterfront, with piers, benches, pathways, trees, and reflections on calm water."
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
