# Image & Design (1/4)

743 prompts. Copy one, replace anything in brackets, and paste it into any chat model.

[English](../en/image.md) · [中文](../zh/image.md)

Pages: **1** · [2](image-2.md) · [3](image-3.md) · [4](image-4.md)

<details><summary><b>1950s Diner Photo Transformation</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. The face must remain clear and unaltered. Transform the subject into a cheerful **1950s Diner Patron/Waitress**, seated at a classic diner counter, enjoying a milkshake. Emphasize bright, cheerful colors, chrome accents, a nostalgic retro aesthetic, and a lively, feel-good atmosphere.",
  "details": {
    "year": "1950s (Mid-Century Americana)",
    "genre": "Retro / Nostalgia / Pop Art / Slice of Life",
    "location": "A classic American diner interior. Visible elements include a shiny chrome counter, red vinyl stools, checkerboard floor, and possibly a jukebox or vintage soda fountain in the background. Bright, inviting lighting.",
    "lighting": "Bright, even, and slightly diffused incandescent lighting, typical of a bustling diner. Everything is clearly illuminated, creating a cheerful, inviting glow.",
    "camera_angle": "Medium close-up, capturing the subject from the chest up, with enough of the counter and background to establish the diner setting. The subject is looking slightly towards the camera with a warm expression. (1:1 composition).",
    "emotion": "Joyful, relaxed, friendly, and carefree.",
    "costume": "Classic 1950s attire: for a patron, a brightly colored (e.g., pastel pink or light blue) letterman jacket or a poodle skirt with a fitted sweater. For a waitress, a crisp uniform (e.g., light blue dress with a white apron, paper hat, and roller skates if applicable for a carhop look). Hair is styled in a classic 50s bouffant or ponytail.",
    "color_palette": "Vibrant and cheerful primary colors (red, blue, yellow) mixed with soft pastels (pink, mint green, baby blue) and shiny chrome silver. Strong, clean lines define objects. Everything looks fresh and inviting.",
    "atmosphere": "Upbeat, nostalgic, lively, and incredibly friendly. A sense of youthful innocence and fun, set to the background hum of a jukebox.",
    "subject_expression": "A wide, genuine smile with bright, sparkling eyes. A slight tilt of the head, conveying friendliness and openness.",
    "subject_action": "One hand is holding a tall, frosted milkshake glass with a striped straw, perhaps mid-sip. The other hand is resting casually on the chrome counter or gesturing lightly. Body language is relaxed and happy.",
    "environmental_elements": "A perfect, whipped cream-topped milkshake with a cherry. Reflections of the diner's neon signs (if any) or bright lights on the chrome surfaces. A classic diner menu or napkin dispenser on the counter. Perhaps a faint 'Wurlitzer' logo on a distant jukebox."
  }
}
```

</details>

<details><summary><b>1980s vs Modern Café Split Screen Video</b></summary>

```text
A cinematic, high-quality video scene in a split-screen or retro-modern café setting. On one side, a stylish man from the 1980s wearing a vintage wide-lapel blazer, thick glasses, and sporting a classic 80s hairstyle, holding a cassette tape. On the other side, a woman from the 2000s wearing low-rise jeans, a cropped top, and modern highlights, holding an early 2000s slider mobile phone. They are engaged in a lively, animated, and intriguing conversation, smiling, gesturing, and talking to each other across time. Warm cinematic lighting, authentic retro color grading, film grain, highly detailed, 4k resolution, smooth motion.
```

</details>

<details><summary><b>2026 Astrology Poster</b></summary>

```text
{
  "task": "Photorealistic premium mystical 2026 astrology poster using uploaded portrait as strict identity anchor, with user-selectable language (TR or EN) for text.",
  "inputs": {
    "REF_IMAGE": "${user_uploaded_image}",
    "BIRTH_DATE": "{YYYY-MM-DD}",
    "BIRTH_TIME": "{HH:MM or UNKNOWN}",
    "BIRTH_PLACE": "{City, Country}",
    "TARGET_YEAR": "2026",
    "OUTPUT_LANGUAGE": "${tr_or_en}"
  },
  "prompt": "STRICT IDENTITY ANCHOR:\nUse ${ref_image} as a strict identity anchor for the main subject. Preserve the same person exactly: facial structure, proportions, age, skin tone, eye shape, nose, lips, jawline, and overall likeness. No identity drift.\n\nSTEP 1: ASTROLOGY PREDICTIONS (do this BEFORE rendering):\n- Build a natal chart from BIRTH_DATE=${birth_date}, BIRTH_TIME=${birth_time}, BIRTH_PLACE=${birth_place}. If BIRTH_TIME is UNKNOWN, use a noon-chart approximation and avoid time-dependent claims.\n- Determine 2026 outlook for: LOVE, CAREER, MONEY, HEALTH.\n- For each area, choose ONE keyword describing the likely 2026 outcome.\n\nLANGUAGE LOGIC (critical):\nIF OUTPUT_LANGUAGE = TR:\n- Produce EXACTLY 4 Turkish keywords.\n- Each keyword must be ONE WORD only (no spaces, no hyphens), UPPERCASE Turkish, max 10 characters.\n- Examples only (do not copy blindly): BOLLUK, KAVUŞMA, YÜKSELİŞ, DENGE, ŞANS, ATILIM, DÖNÜŞÜM, GÜÇLENME.\n- Bottom slogan must be EXACT:\n  \"2026 Yılı Sizin Yılınız olsun\"\n\nIF OUTPUT_LANGUAGE = EN:\n- Produce EXACTLY 4 English keywords.\n- Each keyword must be ONE WORD only (no spaces, no hyphens), UPPERCASE, max 10 characters.\n- Examples only (do not copy blindly): ABUNDANCE, COMMITMENT, BREAKTHRU, CLARITY, GROWTH, HEALING, VICTORY, RENEWAL, PROMOTION.\n- Bottom slogan must be EXACT:\n  \"MAKE 2026 YOUR YEAR\"\n\nIMPORTANT TEXT RULES:\n- Do NOT print labels like LOVE/CAREER/MONEY/HEALTH.\n- Print ONLY the 4 keywords + the bottom slogan, nothing else.\n\nSTEP 2: PHOTO-REALISTIC MYSTICAL LOOK (do NOT stylize into illustration):\n- The subject must remain photorealistic: natural skin texture, realistic hair, no plastic skin.\n- Mysticism must be achieved via cinematography and subtle atmosphere:\n  - faint volumetric haze, minimal incense-like smoke wisps\n  - moonlit rim light + warm key light, refined specular highlights\n  - micro dust motes sparkle (very subtle)\n  - faint zodiac wheel and astrolabe linework in the BACKGROUND only (not on the face)\n  - sacred geometry as extremely subtle bokeh overlay, never readable text\n\nSTEP 3: VISUAL METAPHORS LINKED TO PREDICTIONS (premium, not cheesy):\n- MONEY positive: refined gold-toned light arcs and upward flow (no currency, no symbols).\n- LOVE positive: paired orbit paths and warm rose-gold highlights (no emoji hearts).\n- CAREER positive: ascending architectural lines or subtle rising star-route graph in background.\n- HEALTH strong: calm balanced rings and clean negative space.\n- Make the two strongest themes visually dominant through light direction, contrast, and placement.\n\nPOSTER DESIGN:\n- Aspect ratio: 4:5 vertical, ultra high resolution.\n- Composition: centered hero portrait, head-and-shoulders or mid-torso, eye-level.\n- Camera look: 85mm portrait, f/1.8, shallow depth of field, crisp focus on eyes.\n- Background: deep midnight gradient with subtle stars; modern, premium, minimal.\n\nTYPOGRAPHY (must be perfect and readable):\nA) Keyword row:\n- Place the 4 keywords in a single row ABOVE the slogan.\n- Use separators: \" • \" between words.\n- Font: modern sans (Montserrat-like), slightly increased letter spacing.\n\nB) Bottom slogan:\n- Place at the very bottom, centered.\n- Font: elegant serif (Playfair Display-like).\n\nNO OTHER TEXT ANYWHERE.\n\nFINISHING:\n- Premium color grading, subtle filmic contrast, no oversaturation.\n- Natural retouching, no over-sharpening.\n- Ensure the selected-language text is spelled correctly and fully readable.\n",
  "negative_prompt": "any extra text, misspelled words, wrong letters, watermark, logo, signature, QR code, low-res, blur, noise, face distortion, identity drift, different person, illustration, cartoon, anime, heavy fantasy styling, neon colors, cheap astrology clipart, currency, currency symbols, emoji hearts, messy background, duplicated face, extra fingers, deformed hands, readable runes, readable glyph text",
  "output": {
    "count": 1,
    "aspect_ratio": "4:5",
    "style": "photorealistic premium cinematic mystical editorial poster"
  }
}
```

</details>

<details><summary><b>2026 Fashion Editorial</b></summary>

```text
A 20-year-old adult Dutch female model with fair skin and long loose copper-brown waves wears a contemporary outfit derived strictly from the attached fashion wardrobe reference. She stands behind an overflowing roadside fruit stall, one hand holding an enormous watermelon while she looks directly into camera with complete composure; her clothing creates a precise silhouette against the chaotic produce. Waist-up framing through foreground fruit, shallow depth of field, brutal midday sunlight, saturated watermelon red, citrus orange, leaf green and cobalt accents, crisp hard shadows, slightly faded analog color, spontaneous street-fashion photography, tactile realism, no text, no logos.
```

</details>

<details><summary><b>2026 Mobile Poster Creator</b></summary>

```text
Act as a graphic design assistant. Your task is to create a visually appealing mobile poster to congratulate everyone on the year 2026. The poster should:
- Have an aspect ratio of 9:16 with a resolution of 1080x1920 pixels
- Include cheerful and celebratory elements suitable for a New Year theme
- Allow space for users to add their brand name prominently
- Maintain a professional and festive tone

Constraints:
- Ensure the design supports text overlays for customization
- Make use of vibrant colors to capture attention

Example Elements:
- Fireworks, confetti, or similar celebratory graphics
- Text placeholders for 'Happy 2026!' and '${your_brand_here}'
- A festive color palette of ${color1:gold}, ${color2:silver}, and ${color3:blue}

Use this prompt to generate a high-quality digital image suitable for mobile devices.
```

</details>

<details><summary><b>360 Degree Product Rotation Video</b></summary>

```text
{
  "model": "veo-3.1",
  "task": "image_to_video_360_product_rotation",

  "objective": "Generate a photorealistic, silent, 360-degree rotation video from the provided front and back images of the exact same product. Preserve 100% of the original product identity without modification, addition, removal, or hallucination. The product must appear naturally filled internally using ghost mannequin volume reconstruction, while remaining completely faithful to the original images. The garment must appear professionally ironed, perfectly smooth, crisp, and retail-ready while preserving all original details. Output must contain absolutely no audio.",

  "garment_condition_global_rule": {
    "all_clothing_must_be_ironed": true,
    "appearance": "perfectly pressed, crisp, smooth, structured, premium retail presentation",
    "no_new_wrinkles": true,
    "no_random_fabric_folding": true,
    "maintain_original_wrinkle_data_if_present": true,
    "no_artificial_wrinkle_generation": true,
    "clean_finish": true,
    "brand_new_look": true
  },

  "input": {
    "type": "multi_image",
    "views": [
      {
        "name": "front",
        "role": "primary_reference",
        "weight": 1.0
      },
      {
        "name": "back",
        "role": "secondary_reference",
        "weight": 1.0
      }
    ],

    "forensic_identity_lock": {
      "mode": "strict",

      "geometry_lock": true,
      "silhouette_lock": true,
      "mesh_lock": true,

      "texture_lock": true,
      "fabric_pattern_lock": true,
      "stitching_lock": true,
      "wrinkle_lock": true,

      "color_lock": true,
      "material_lock": true,
      "surface_lock": true,

      "logo_lock": true,
      "label_lock": true,
      "branding_lock": true,

      "proportion_lock": true,
      "measurement_lock": true,

      "prevent_hallucination": true,
      "prevent_detail_invention": true,
      "prevent_detail_removal": true
    }
  },

  "geometry_reconstruction": {
    "method": "constrained_true_3d_reconstruction",

    "source_constraint": "only_use_information_present_in_input_images",

    "volume_generation": {
      "enabled": true,
      "type": "ghost_mannequin_volume",
      "visibility": "none"
    },

    "reconstruction_rules": {
      "interpolate_only": true,
      "no_detail_creation": true,
      "no_surface_modification": true,
      "no_topology_change": true,
      "no_design_interpretation": true
    },

    "mesh_constraints": {
      "rigid": true,
      "no_deformation": true,
      "no_shape_change": true,
      "no_texture_shift": true
    }
  },

  "animation": {
    "type": "360_degree_rotation",
    "axis": "vertical",
    "degrees": 360,
    "direction": "clockwise",

    "speed": "constant",
    "duration_seconds": 6,

    "motion_constraints": {
      "no_wobble": true,
      "no_jitter": true,
      "no_mesh_change": true,
      "no_texture_shift": true,
      "no_geometry_shift": true
    },

    "start_state": "exact_front_view",
    "end_state": "exact_front_view",

    "loop": true
  },

  "ghost_mannequin": {
    "enabled": true,
    "visibility": "invisible",

    "constraints": {
      "must_not_be_visible": true,
      "must_not_modify_surface": true,
      "must_not_modify_shape": true,
      "must_not_modify_wrinkles": true,
      "must_not_modify_fit": true
    }
  },

  "scene": {
    "background": {
      "type": "pure_white",
      "color": "#FFFFFF",
      "uniform": true
    },

    "product_state": {
      "floating": true,
      "no_support_visible": true
    },

    "shadow": {
      "type": "soft_contact",
      "stable": true,
      "physically_correct": true
    }
  },

  "camera": {
    "type": "fixed",
    "movement": "none",
    "rotation": "none",
    "zoom": "none",
    "center_lock": true,
    "lens": "85mm",
    "distortion": false
  },

  "lighting": {
    "type": "studio_softbox",
    "consistency": "locked",
    "variation": false,
    "flicker": false,
    "must_not_change_during_rotation": true
  },

  "rendering": {
    "mode": "photorealistic",
    "texture_source": "input_images_only",
    "no_texture_generation": true,
    "no_creative_interpretation": true,
    "no_artificial_enhancement": true,
    "fabric_finish": "smooth_pressed_clean",
    "retail_presentation_standard": "premium_ecommerce_ready"
  },

  "audio": {
    "enabled": false,
    "generate_audio": false,
    "include_audio_track": false,
    "music": false,
    "sound_effects": false,
    "voice": false,
    "ambient_sound": false,
    "silence": true
  },

  "output": {
    "resolution": "2160x2160",
    "fps": 30,
    "duration_seconds": 6,
    "format": "mp4",
    "video_codec": "H.264",
    "audio_codec": "none",
    "include_audio_track": false,
    "loop": true,
    "background": "pure_white",
    "silent": true
  },

  "hard_constraints": [
    "NO audio",
    "NO music",
    "NO sound effects",
    "NO voice",
    "NO ambient sound",
    "DO NOT add details",
    "DO NOT remove details",
    "DO NOT modify stitching",
    "DO NOT modify logos",
    "DO NOT modify texture",
    "DO NOT modify structure",
    "DO NOT change proportions",
    "DO NOT stylize",
    "DO NOT hallucinate",
    "NO new wrinkles",
    "NO messy fabric folds",
    "MUST appear professionally ironed"
  ],

  "negative_prompt": [
    "music",
    "sound",
    "voice",
    "audio",
    "ambient audio",
    "sound effects",
    "hallucinated details",
    "modified stitching",
    "different fabric",
    "shape morphing",
    "geometry distortion",
    "creative reinterpretation",
    "wrinkled fabric",
    "messy folds",
    "creased clothing",
    "unpressed garment"
  ]
}
```

</details>

<details><summary><b>3D Cartoon Physicist Caricature</b></summary>

```text
A highly detailed stylized 3D cartoon caricature of a playful physicist inspired by Richard Feynman.

Character identity:
- male
- middle-aged
- slim build
- expressive face with large smile
- thick wavy dark hair
- large round glasses
- intelligent mischievous eyes
- warm friendly personality
- tweed academic jacket
- white shirt with pens in pocket
- holding a physics book

Art style:
Pixar-inspired stylized realism, whimsical 3D caricature, oversized expressive eyes, exaggerated facial proportions, polished CGI rendering, animated movie character aesthetic, collectible figurine look, ultra-clean white background.

Pose:
standing confidently with one finger raised as if explaining physics.

Scene:
minimal white studio background with subtle physics doodles.

Render quality:
ultra detailed CGI, cinematic lighting, octane render, AAA animated movie quality.

Negative prompt:
uncanny realism, bad anatomy, distorted hands, blurry eyes, duplicate limbs, extra fingers, messy textures.
```

</details>

<details><summary><b>3D City Diorama</b></summary>

```text
Hyper-realistic 3D square diorama of ${city_name:Istanbul}, carved out with exposed soil cross-section beneath showing rocks, roots, and earth layers. Above: whimsical fairytale cityscape featuring iconic landmarks, architecture, and cultural elements of ${city_name:Istanbul}. Modern white “${city_name:Istanbul}” label integrated naturally. Pure white studio background with soft natural lighting. DSLR photograph quality - crisp, vibrant, magical realism style. 1080x1080 dimensions
```

</details>

<details><summary><b>3D Family Short: Toddler Meets Newborn Sibling</b></summary>

```text
Create a beautiful, ultra-detailed 3D animated family short film featuring a cute toddler boy with fluffy golden-blond hair, big expressive blue eyes, rosy cheeks, and blue-and-white striped pajamas. He interacts lovingly with his newborn baby sibling in a cozy, sunlit modern home.

Scene 1: A warm living room with soft natural sunlight streaming through large windows. A mother gently takes care of household tasks while the curious toddler walks toward the newborn sleeping peacefully in a soft woven bassinet.

Scene 2: Close-up of the toddler carefully leaning over the bassinet, smiling sweetly at the tiny newborn wrapped in a light-blue blanket. The baby moves gently and makes adorable expressions.

Scene 3: The mother places the newborn safely in a wooden crib. The toddler stands beside the crib, looking at the baby with affection and curiosity. Capture the tender sibling bond with cinematic close-ups.

Scene 4: The toddler sits on the floor holding a baby bottle, looking innocent and adorable. Warm sunlight illuminates his face, highlighting his expressive eyes and soft blond hair.

Scene 5: The toddler plays gently with toys beside his baby sibling on a soft living-room rug while their mother watches lovingly from the sofa.

Scene 6: The toddler hugs a cute teddy bear and smiles happily. Use a close-up shot to emphasize his joyful expression and realistic animated details.

Final Scene: At night, the mother sits comfortably on a bed with both children. She lovingly cuddles the newborn while the toddler sits close beside her. End with a tender close-up of the mother kissing her baby's forehead in a peaceful, loving family moment.

Visual Style: High-end Pixar-inspired 3D animation, adorable character design, realistic fabric textures, detailed hair strands, expressive facial animation, soft global illumination, warm cinematic lighting, natural shadows, smooth camera movements, shallow depth of field, emotionally engaging storytelling, consistent character appearance across all scenes, 4K quality, vertical 9:16 aspect ratio.

Negative Prompt: Distorted faces, inconsistent character designs, extra fingers, unnatural movements, flickering, blurry textures, deformed hands, sudden outfit changes, unrealistic proportions, text, logos, and watermarks.
```

</details>

<details><summary><b>3D Heart Anatomy Video</b></summary>

```text
[00:00 - 00:03]
Hyper-realistic 8K 3D human heart anatomy, beating slowly, detailed muscle texture with coronary arteries, Golden Hour Cinematic lighting, fisheye distortion effect, 35mm storytelling lens, professional medical infographic style, blurred futuristic laboratory background. --ar 9:16

[00:03 - 00:06]
 Extreme close-up of heart anatomy, dramatic golden hour lighting, 35mm fisheye lens distortion, hyper-realistic biological textures, cinematic 8K, 9:16 vertical composition. --ar 9:16
```

</details>

<details><summary><b>3D Isometric Miniature City with Weather</b></summary>

```text
Present a clear, 45° top-down view of a vertical (9:16) isometric miniature 3D cartoon scene, highlighting iconic landmarks centered in the composition to showcase precise and delicate modeling.

The scene features soft, refined textures with realistic PBR materials and gentle, lifelike lighting and shadow effects. Weather elements are creatively integrated into the urban architecture, establishing a dynamic interaction between the city's landscape and atmospheric conditions, creating an immersive weather ambiance.

Use a clean, unified composition with minimalistic aesthetics and a soft, solid-colored background that highlights the main content. The overall visual style is fresh and soothing.

Display a prominent weather icon at the top-center, with the date (x-small text) and temperature range (medium text) beneath it. The city name (large text) is positioned directly above the weather icon. The weather information has no background and can subtly overlap with the buildings.

The text should match the input city's native language.

Please retrieve current weather conditions for the specified city before rendering.

City name: İSTANBUL
```

</details>

<details><summary><b>3D Medical Anatomy Model Render</b></summary>

```text
{
  "fixed_prompt_components": {
    "composition": "Wide angle full body shot, the entire figure is visible from head to toe, far shot, vertical portrait framing, centered and symmetrical stance",
    "background": "Isolated on a seamless pure white background, studio backdrop, clean white environment",
    "art_style": "Photorealistic 3D medical render, ZBrush digital sculpture style, scientific anatomy model aesthetics",
    "texture_and_material": "Monochromatic silver-grey skin with brushed metal texture, micro-surface details, highly detailed muscle striation, matte finish",
    "lighting_and_tech": "Cinematic rim lighting, global illumination, raytracing, ambient occlusion, 8k resolution, UHD, sharp focus, hyper-detailed"
  },
  "variables": {
    "gender": "${gender:male}",
    "view_angle": "${view_angle:Front view}",
    "target_muscle_group": "${target_muscle_group:Pectoralis Major (Chest)}",
    "highlight_color": "${highlight_color:glowing cyan blue}"
  },
  "negative_prompt": "text, infographic, chart, diagram, labels, arrows, UI, cropped image, close-up, macro shot, headshot, cut off feet, cut off head, partial body, grey background, gradient background, shadows on floor, blurry, low resolution, distortion, watermark"
}
```

</details>

<details><summary><b>3D Part Image to Technical Drawing Sheet</b></summary>

```text
{
  "task": "image_to_image",
  "input_image": "3d_render_of_mechanical_part.png",
  "prompt": "Reference scale: the outer diameter of the flange is exactly 360 mm. Mechanical engineering drawing sheet with three separate drawings of the same part placed in clearly separated rectangular areas. Drawing 1: fully dimensioned orthographic views (front, top, side) with precise numeric measurements in millimeters, diameter symbols, radius annotations, hole count notation and center lines. Drawing 2: sectional view taken through the center axis of the part, showing internal geometry with proper section hatching and wall thickness clearly visible. Drawing 3: isometric reference view of the part without any dimensions, used only for spatial understanding. ISO mechanical drafting standard, consistent line weights, monochrome black lines on white background, manufacturing-ready technical documentation, no perspective distortion.",
  "negative_prompt": "single combined drawing, merged views, artistic rendering, perspective view, realistic lighting, shadows, textures, colors, gradients, sketch style, hand drawn look, missing dimensions, decorative presentation",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 45,
    "cfg_scale": 6,
    "denoising_strength": 0.45,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "one technical drawing sheet containing three clearly separated drawings: dimensioned orthographic views, a centered sectional view, and an undimensioned isometric reference, suitable for manufacturing reference"
}
```

</details>

<details><summary><b>3D to 2D Floor Plan Converter</b></summary>

```text
{
  "task": "image_to_image",
  "description": "Convert a furnished 3D interior render into a clean 2D architectural floor plan drawing",
  "input_image": "3d_render_of_apartment_interior.png",
  "prompt": "top-down 2D architectural floor plan, black and white technical drawing, clean vector-style lines, precise wall thickness, clearly defined rooms, labeled spaces with room names and square meter areas, doors with swing arcs, windows shown as breaks in walls, minimal shading, no perspective, orthographic projection, architectural blueprint style, professional residential floor plan, similar to CAD drawing",
  "negative_prompt": "3d perspective, isometric view, realistic lighting, shadows, textures, furniture rendering, people, depth, photorealism, colors, gradients, soft edges, artistic sketch, hand drawn style",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 30,
    "cfg_scale": 7,
    "denoising_strength": 0.65,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "flat 2D floor plan similar to architectural plan drawings, suitable for real estate listings or construction documents"
}
```

</details>

<details><summary><b>3D Viral Ad Poster Prompt</b></summary>

```text
Create a more detailed prompt for Photoshop poster to create a 3d poster design and and use the attached image as the background  in 1:1 ratio  and the put the attached image given character and  text it should have a design and and a stronger “viral ad” version with more aggressive visual hooks  "GRAND OPENING" "THIS JUNE 12" (MAIN HEADLINE) SMALL TEXT BELLOW "ENCODING JUNE 7" "BOTTOM BUTTON "LINE UP NOW"
```

</details>

<details><summary><b>3D Wireframe Icon</b></summary>

```text
Reconstruct the central object of the given 2D image as a true 3D wireframe model.

- Interpret the 2D shape as volumetric geometry and extrude it into depth.

- Build visible 3D structure with wireframe mesh lines wrapping around the form (front, sides, and curvature).

- Use thin, precise, glowing white wireframe lines only, no solid surfaces, no flat fills.

- Apple App Store style icon, premium iOS design language, WWDC-inspired.

- Rounded square app icon, centered and symmetrical.

- Soft blue gradient background, subtle glow.

- Clean orthographic front view with clear depth cues (z-axis wireframe).

- High-resolution, futuristic UI icon.

- No text, no logos, no illustration style


Negatives:

2D flat design, flat icon, illustration, lighting-only depth, fake 3D, gradients on object, shading, shadows, cartoon style, sketch, photorealism, textures, noise, grain
```

</details>

<details><summary><b>3x3 Grid Storyboard from a Photo</b></summary>

```text
Act as a storyboard artist. You are skilled in visual storytelling and composition. Your task is to convert an uploaded photo into a 3x3 grid storyboard while keeping the main character centered.

You will:
- Analyze the uploaded photo
- Divide the photo into 9 equal parts
- Ensure the main character remains consistent across the grid
- Adjust each section for visual balance and continuity

Rules:
- Maintain the original resolution and quality
- Ensure each grid section transitions smoothly
- No overlapping or distortion of the main character

Variables:
- Photo: ${photo}
- Main Character: ${mainCharacter}
```

</details>

<details><summary><b>4K Reference Image Enhancement</b></summary>

```text
"Ultra-high-resolution 4K enhancement based strictly on the provided reference image. Absolute fidelity to original facial anatomy, proportions, and identity. Preserve expression, gaze, pose, camera angle, framing, and perspective with zero deviation. Clothing, hair, skin, and background elements must remain unchanged in structure, placement, and design. Recover fine-grain detail with natural realism. Enhance pores, fine lines, hair strands, eyelashes, fabric weave, seams, and material edges without introducing stylization. Maintain original color science, white balance, and tonal relationships exactly as captured. Lighting direction, intensity, contrast, and shadow behavior must match the source image precisely, with only improved clarity and expanded dynamic range. No relighting, no reshaping. Remove any grain. Apply controlled sharpening and high-frequency detail reconstruction. Remove compression artifacts and noise while retaining authentic texture. No smoothing, no plastic skin, no artificial gloss. Facial features must remain consistent across the entire image with coherent anatomy and clean, stable edges. Negative constraints: no warping, no facial drift, no added or missing anatomy, no altered hands, no distortions, no perspective shift, no text or graphics, no hallucinated detail, no stylized rendering. Output must read as a true-to-life, photorealistic upscale that matches the reference exactly, only clearer, sharper, and higher resolution."
```

</details>

<details><summary><b>80s Synthwave Gamer Transformation</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. The face must remain clear and unaltered. Transform the subject into a cool **80s Synthwave Gamer**, intensely playing an arcade cabinet in a dimly lit, neon-drenched retro arcade. Emphasize glowing neon colors (magenta, cyan), retro-futuristic fashion, CRT screen reflections, and a nostalgic, electronic atmosphere.",
  "details": {
    "year": "1980s (Retro-Futuristic / Synthwave Aesthetic)",
    "genre": "Synthwave / Retrowave / 80s Nostalgia / Cyberpunk Lite",
    "location": "A dark, atmospheric retro arcade. Walls are lined with glowing arcade cabinets showing pixel art. The floor might have a glowing neon grid pattern. Smoke machines create a slight haze in the air, catching the colored lights.",
    "lighting": "Intense, contrasting neon lighting. Dominant hues of electric pink, cyan, deep purple, and laser blue. The primary light source on the subject's face is the glow from the CRT arcade screen they are playing, creating strong, colorful highlights.",
    "camera_angle": "Medium shot, capturing the subject from the waist up, engaged with the arcade machine. The background is a blur of neon lights and screens. (1:1 composition).",
    "emotion": "Cool, focused, immersed, and slightly nostalgic.",
    "costume": "Quintessential 80s cool: A satin 'Members Only' style jacket (perhaps iridescent or with a retro logo), a graphic band t-shirt, and maybe fingerless gloves. Sunglasses worn indoors are optional but encouraged for the aesthetic. Hair is styled with volume.",
    "color_palette": "A strict synthwave palette: saturated magenta, cyan, deep violet, electric blue, and sunset orange. Deep blacks in the shadows contrast sharply with the neon light sources.",
    "atmosphere": "Electric, nostalgic, hazy, and cool. The air feels filled with the sounds of synthesized music and coin drops. A visual representation of a vaporwave track.",
    "subject_expression": "A cool, focused smirk or intense concentration, eyes fixed on the screen. The realistic face is illuminated by the shifting colored light of the game.",
    "subject_action": "Hands are actively engaged with the arcade joystick and buttons, knuckles slightly white from gripping. The body is leaned slightly into the machine in concentration.",
    "environmental_elements": "Scanlines visible on the CRT screens. Pixelated explosions or high scores reflecting in the subject's sunglasses or eyes. Glowing coin slots. A retro poster for a fictional 80s sci-fi movie in the background."
  }
}
```

</details>

<details><summary><b>90s Power Dressing Editorial</b></summary>

```text
Full-body black and white fashion editorial portrait of a young woman with an hourglass figure, standing in a professional photo studio against a smooth neutral gray gradient backdrop with a polished concrete floor. She has dark hair slicked back into a low neat bun, strong defined eyebrows, full lips, and an intense serious gaze looking directly at the camera. She is wearing a white fitted button-down dress shirt with the top buttons undone creating a deep V-neckline, sleeves rolled up to the mid-forearm, black wide suspenders with silver metal clips attached to high-waisted slim black ankle trousers, and black pointed-toe stiletto pumps. Her pose: standing with legs slightly crossed (right leg forward), both hands raised holding the suspenders near her collarbones, elbows slightly bent outward, shoulders back, confident powerful stance. Professional studio lighting with a large softbox key light from above-front, subtle fill light, soft shadows cast on the floor to the left. Shot with a full-frame DSLR, 85mm prime lens at f/5.6, ISO 100, frontal angle at hip height, full body vertical frame, everything in sharp focus. High-contrast monochrome, editorial fashion aesthetic, minimalist, androgynous-chic power dressing vibe, reminiscent of 90s Vogue photography by Peter Lindbergh, ultra high quality, magazine cover quality.
```

</details>

<details><summary><b>A Night in Paris</b></summary>

```text
{
  "subject_and_scene": {
    "main_subject": "A young man with thick curly brown hair, wearing a sophisticated beige turtleneck sweater and a matching tailored wool blazer, displaying a contemplative and moody expression.",
    "action": "Leaning casually against a weathered stone bridge parapet, looking away from the camera toward the Parisian cityscape.",
    "environment": "Paris at night on the banks of the Seine; the Eiffel Tower stands prominently in the background, brilliantly illuminated in golden light, with city lights and river boats creating soft reflections on the dark water."
  },
  "cinematography": {
    "camera_model": "Sony Venice 2",
    "sensor_type": "Full Frame",
    "shot_type": "Cowboy Shot",
    "camera_angle": "Eye Level",
    "movement": "Static"
  },
  "optics": {
    "lens_type": "Spherical",
    "focal_length": "35mm (Standard Wide)",
    "aperture": "f/2.8 (Moderate depth of field to retain background context)",
    "shutter_effects": "Standard Shutter"
  },
  "lighting_design": {
    "setup": "Natural Night Ambience with soft fill on subject",
    "style": "Low-Key with high atmospheric glow",
    "atmospheric_light": "Golden Glow from the Eiffel Tower, Rim Lighting from city lights",
    "color_temperature": "Warm (3000K, Amber and Gold tones)"
  },
  "color_and_post": {
    "film_stock": "Kodak Portra 400",
    "color_grading": "Warm Nostalgic Tones, Muted Log-C",
    "analog_artifacts": "Heavy Film Grain, soft Halation around the golden tower lights"
  },
  "rendering_and_tech": {
    "engine": "Octane Render",
    "advanced_tech": "Subsurface Scattering on skin, Global Illumination for water reflections",
    "specs": {
      "aspect_ratio": "2.39:1 (CinemaScope)",
      "resolution": "8K, Photorealistic, Hyper-detailed"
    }
  },
  "directorial_style": "Denis Villeneuve (Atmospheric mood and pensive composition)"
}
```

</details>

<details><summary><b>Abandoned Wife Portrait</b></summary>

```text
{
  "character_profile": {
    "name": "Natalia",
    "subject": "Full-body 3/4 view portrait capturing a moment of profound emotional transition",
    "physical_features": {
      "ethnicity": "Southern European",
      "age_appearance": "Youthful features now marked by a complex, weary expression",
      "hair": "Dark brown, wavy, artfully disheveled as if by passion, time, and thought",
      "eyes": "Deep green with amber flecks, gazing into the middle distance — a mix of melancholy, clarity, and resignation",
      "complexion": "Olive skin with a subtle, dewy sheen",
      "physique": "Slender with a pronounced feminine silhouette, shown with natural elegance",
      "details": "A simple gold wedding band on her right ring finger, catching the light"
    },
    "clothing": {
      "outfit": "A sleek black silk slip dress, one thin strap delicately fallen off the shoulder, black thigh-high stockings",
      "condition": "Elegantly disordered, suggesting a prior moment of intimacy now passed"
    }
  },
  "scene_details": {
    "location": "Minimalist, sunlit apartment in Rome. Clean lines, a stark white wall.",
    "lighting": "Natural, cinematic morning light streaming in. Highlights the texture of skin and fabric, creating long, dramatic shadows. Feels both exposing and serene.",
    "pose": "Leaning back against the wall, body in a graceful 3/4 contrapposto. One hand rests lightly on her collarbone, the other hangs loosely. A posture of quiet aftermath and introspection.",
    "atmosphere": "Poetic stillness, intimate vulnerability, a palpable silence filled with memory. Sophisticated, raw, and deeply human. The story is in her expression and the space around her."
  },
  "technical_parameters": {
    "camera": "Sony A7R IV with 50mm f/1.2 lens",
    "style": "Hyper-realistic fine art photography. Cinematic, with a soft film grain. Inspired by the evocative stillness of photographers like Petra Collins or Nan Goldin.",
    "format": "Vertical (9:16), perfect for a portrait that tells a story",
    "details": "Sharp focus on the eyes and expression. Textural emphasis on skin, silk, and the wall. Background is clean, almost austere, holding the emotional weight. No explicit debris, only the subtle evidence of a life lived."
  },
  "artistic_intent": "Capture the silent narrative of a private moment after a significant encounter. The focus is on the emotional landscape: a blend of vulnerability, fleeting beauty, quiet strength, and the profound self-awareness that follows intimacy. It's a portrait of an inner turning point."
}
```

</details>

<details><summary><b>Add Black Glasses to a Photo</b></summary>

```text
add black glasses on my picture that suits on me that cover my eyes also make it realistic
```

</details>

<details><summary><b>Aerochrome Birch Forest and Still Lake</b></summary>

```text
A grove of white birch trees with bright magenta and hot pink foliage stands along the shore of a still mountain lake, captured on false-color infrared film in the style of Kodak Aerochrome. Every living leaf and the grassy meadow in the foreground glow in shades of pink, coral, and crimson, while the lake turns a deep cobalt blue and the sky a saturated cyan with a few soft white clouds. A small wooden jetty reaches into the water, and a low granite boulder sits at the water's edge. Distant hills covered in pink forest fade into light haze, and the lake mirrors the pink trees and clouds almost perfectly. Visible fine film grain, slightly lifted blacks, natural vignetting, and crisp detail in the white birch bark with its dark marks. Surreal yet believable landscape photography, calm late morning light, medium format film look. Wide landscape 16:9. No people, no animals, no boats, no text, no logos, no watermark.
```

</details>

<details><summary><b>Aesthetic Sunset</b></summary>

```text
8K ultra hd aesthetic, romantic, sunset, golden hour light, warm cinematic tones, soft glow, cozy winter mood, natural candid emotion, shallow depth of field, film look, high detail.
```

</details>

<details><summary><b>Aether Prince at the Crystal Gala</b></summary>

```text
{
  "title": "The Aether Prince at the Crystal Gala",
  "description": "A breathtaking cinematic shot of a regal nobleman standing on the balcony of a translucent palace hovering above the clouds.",
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve his core likeness. Transform Subject 1 (male) into a high-society aristocrat attending a royal ball inside a floating crystal palace. He stands near a transparent balustrade, with the grand ballroom behind him and a sea of clouds stretching out to the horizon. The image must be ultra-photorealistic, utilizing cinematic lighting to capture the refraction of light through the crystal structures. The scene is highly detailed, shot on Arri Alexa, featuring a shallow depth of field that blurs the dancing guests in the background while keeping the subject sharpness pristine.",
  "details": {
    "year": "Timeless Fantasy Era",
    "genre": "Cinematic Photorealism",
    "location": "A grand ballroom constructed entirely of diamond and glass, floating high in the stratosphere at sunset.",
    "lighting": [
      "Golden hour sunlight refracting through crystal prisms",
      "Soft volumetric glow",
      "Caustic reflections"
    ],
    "camera_angle": "Medium shot at eye level, capturing the subject against the vast sky.",
    "emotion": [
      "Regal",
      "Contemplative",
      "Serene"
    ],
    "color_palette": [
      "Champagne gold",
      "prismatic white",
      "sky blue",
      "sunset orange"
    ],
    "atmosphere": [
      "Opulent",
      "Ethereal",
      "Majestic",
      "Airy"
    ],
    "environmental_elements": "Floating anti-gravity chandeliers, clouds drifting past open arches, blurred silhouettes of dancers in formal wear.",
    "subject1": {
      "costume": "A futuristic formal white tuxedo with intricate gold filigree embroidery and a silk sash.",
      "subject_expression": "A calm, confident gaze with a hint of aristocratic detachment.",
      "subject_action": "Resting one hand elegantly on the crystal railing, holding a flute of sparkling nectar."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "darkness",
        "dirt",
        "grime",
        "industrial machinery",
        "ground level terrain"
      ],
      "exclude_styles": [
        "cartoon",
        "sketch",
        "oil painting",
        "anime",
        "CGI 3D render look"
      ],
      "exclude_colors": [
        "neon green",
        "muddy brown",
        "pitch black"
      ],
      "exclude_objects": [
        "cars",
        "modern streetlights",
        "weapons"
      ]
    }
  }
}
```

</details>

<details><summary><b>Afrofuturist High-Fashion Editorial Model</b></summary>

```text
STYLE / AESTHETIC:
High-fashion editorial, luxury commercial photography, hyperrealistic 3D render aesthetic, mythological afrofuturism, opulent dark fantasy, perfectly symmetrical composition.
SUBJECT:
ANATOMY: 1girl, young woman, flawless symmetrical face, medium-dark skin tone, full lips, perfect hands with natural nails.
SKIN: Glowing, heavily oiled and glossy skin, flawless texture, rich melanin, subtle subsurface scattering.
HAIR: Hidden beneath helmet.
CLOTHING: (Metallic gold ribbed shoulder armor:1.3), matching metallic gold bikini top.
ACCESSORIES: (Diamond-encrusted dome helmet with a large gold cross motif:1.4), (smooth reflective gold face visor obscuring the upper face and eyes:1.3), intricate white crystal/lace geometric jewelry adhering to the cheeks.
BODY ART: Adhered crystal face adornments.
POSE & EXPRESSION:
POSE: Crouching on all fours, leaning forward, hands extended flat on the ground towards the camera, perfectly symmetrical posture.
EXPRESSION: Fierce, sensual, intense stare (implied beneath visor), slightly parted glossy lips.
BACKGROUND & SETTING:
SETTING: Dark, opulent studio environment, (perfectly reflective black mirror floor:1.4).
DETAILS: (Two large highly detailed golden metallic snakes symmetrically intertwined and framing the subject, facing each other at the top:1.4), dark marble pillars with gold Greek key pattern borders, scattered metallic gold roses resting on the reflective floor.
LIGHTING & CAMERA:
LIGHTING: Dramatic high-contrast studio lighting, (brilliant specular highlights and cross-shaped lens flares glinting off the gold and diamonds:1.3), strong rim lighting on the body and snakes separating them from the dark background, deep black shadows.
CAMERA STYLE: Symmetrical wide-angle shot, low camera angle, perfectly centered framing, sharp focus on the subject's face and hands, cinematic hyperrealism.
RENDER / QUALITY TAGS:
Masterpiece, best quality, ultra-detailed, highres, photorealistic textures, Octane render aesthetic, ray-traced reflections, highly detailed gold material, 8k resolution.

Negative Prompt: 


(worst quality, low quality, normal quality:1.4), asymmetrical composition, unbalanced framing, illustration, painting, drawing, cartoon, anime, 3d geometry artifacts, ugly, poorly drawn hands, poorly drawn fingers, extra fingers, missing fingers, mutated hands, bad anatomy, deformed limbs, poorly drawn face, messy background, text, watermark, signature, dull lighting, matte skin, missing reflection, distorted reflection, blurry, out of focus.
```

</details>

<details><summary><b>AI Face Swapping for E-commerce</b></summary>

```text
Act as a state-of-the-art AI system specialized in face-swapping technology for e-commerce applications. Your task is to enable users to visualize e-commerce products using AI face swapping, enhancing personalization by integrating their facial features with product images.

Responsibilities:
- Swap the user's facial features onto various product models.
- Maintain high realism and detail in face integration.
- Ensure compatibility with diverse product categories (e.g., apparel, accessories).

Rules:
- Preserve user privacy by not storing facial data.
- Ensure seamless blending and natural appearance.

Variables:
- ${productCategory} - the category of product for visualization.
- ${userImage} - the uploaded image of the user.

Examples:
- Input: User uploads a photo and selects a t-shirt.
- Output: Image of the user’s face swapped onto a model wearing the t-shirt.
```

</details>

<details><summary><b>AI Patent Illustration Designer</b></summary>

```text
Act as an AI Patent Illustration Designer. You are tasked with creating high-quality patent illustrations based on user descriptions and articles.

Your illustrations will:
- Follow Chinese National Intellectual Property Administration patent drawing standards.
- Use SolidWorks black and white engineering line style for structure diagrams.
- Employ Origin's professional scientific plotting style for data analysis charts.

You will:
1. Draw an overall isometric structure diagram without perspective distortion, using solid lines for outlines and dashed lines for hidden structures. Label key components with Arabic numerals.
2. Create standard three-view plus sectional view diagrams with aligned views and uniform sectional lines.
3. Produce exploded isometric diagrams showing assembly directions with clear part separation and no overlaps.
4. Design detailed zoomed-in views to accurately present small structures and connection nodes.
5. Generate data analysis charts in Origin style using academic color schemes with clear axis labels and legends, suitable for embedding in academic papers and patent descriptions.

Rules:
- No colors, shadows, rendering, gradients, or textures in SolidWorks diagrams.
- Maintain clarity and adherence to mechanical drawing standards.
- Origin charts must avoid 3D effects and excessive decoration, focusing on clear data presentation.
```

</details>

<details><summary><b>AI Themed Mechanical Design</b></summary>

```text
Act as an AI-Driven Mechanical Design Artist. You are tasked with creating a digital artwork that incorporates AI themes into a mechanical design. Your main objective is to generate an image that resonates with the uploaded background theme, ensuring harmony in aesthetics.

You will:
- Maintain the resolution of the uploaded image.
- Ensure the two devices present in the original image are preserved in the new design.
- Design a background that is thematically aligned with the uploaded image but introduces a unique AI concept.
- Include the slogan: "Siz daha iyisini yapabilirsiniz ama performanslı bir yardımcıya ihtiyacınız olacak."

Rules:
- The final image must have a mechanical design focus.
- Adhere to the aesthetic style and color palette of the uploaded background.
- Innovate while keeping the AI theme central to the design.
```

</details>

<details><summary><b>Airport Corridor Walk</b></summary>

```text
{
  "category": "AIRPORT_CORRIDOR_FULLBODY",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Low ponytail, travel-day casual",
      "texture": "Natural strands, slight flyaways",
      "movement": "Subtle motion from walking"
    },
    "face": {
      "eyes": "Bright, awake",
      "skin_details": "Real texture, no filter",
      "makeup": "Minimal travel-friendly look"
    },
    "clothing": {
      "outfit": "Travel chic: coat + comfy pants + sneakers (no logos)",
      "fabric": "Realistic wrinkles at knees/elbows"
    },
    "accessories": {
      "items": ["Rolling suitcase (no branding)", "Small tote (no logos)"],
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Full-body walking candid",
    "orientation": "Mid-stride, slight lookback",
    "hands": "One hand on suitcase handle, other holding tote strap",
    "gaze": "Lookback toward camera, subtle smile",
    "posture": "Relaxed, confident traveler"
  },
  "setting": {
    "environment": "Airport corridor",
    "background_elements": [
      "Soft overhead lights",
      "Motion blur in distant travelers (no faces identifiable)",
      "Glossy floor reflections"
    ],
    "depth": "Subject sharp; background softened with motion"
  },
  "camera": {
    "shot_type": "Full-body travel photo",
    "angle": "Eye-level",
    "focal_length_equivalent": "26mm phone or 35mm editorial",
    "framing": "4:5",
    "focus": "Face readable, outfit sharp"
  },
  "lighting": {
    "source": "Overhead airport lighting",
    "highlights": "Natural reflections on floor",
    "shadows": "Soft, realistic"
  },
  "mood_and_expression": {
    "tone": "Travel-day stylish, candid",
    "expression": "Friendly micro-smile"
  },
  "style_and_realism": {
    "style": "Photorealistic UGC travel",
    "imperfections": "Slight tilt, mild noise"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild",
    "motion_blur": "Background only"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "readable signage", "logos",
    "extra limbs", "warped suitcase",
    "plastic skin", "cgi"
  ]
}
```

</details>

<details><summary><b>Alpine Cable Car Scene Concept Brief Builder</b></summary>

```text
Act as a cinematic environment designer who writes image-ready and motion-ready scene briefs. Help me design one hero shot of a single cable car cabin crossing a snowy mountain valley, which will first be generated as a still image and then animated into a short video that uses that image as its first frame. Your brief must make the still image rich in elements that can move naturally (the cabin gliding along its cable, drifting clouds, falling or blowing snow, chimney smoke, glinting light, birds) while keeping the composition calm and easy to animate.

My starting choices:
- Mountain region and landscape: ${region:Alpine valley with a small village and pine forest}
- Season and time of day: ${season:winter sunrise}
- Cabin type and color: ${cabin:small vintage red aerial tram cabin with large windows}
- Visual style: ${style:photoreal travel photography}
- Mood words: ${mood:crisp, quiet, golden, airy}

First ask me, in one short message, for anything missing: the camera viewpoint I prefer (from a ridge looking across the valley, from below looking up at the cabin, or level with the cabin from a nearby slope), whether the valley station or the mountain station should be visible, and anything to avoid (people, skiers, logos, signs, ski lifts, modern buildings).

Then produce the brief with these sections:

1. **Scene Overview**: two or three sentences describing the place, the season, the light, and the story of the moment.

2. **Cable Car and Line**: cabin shape, color, window layout, roof hanger and carriage, the number and thickness of steel cables, the steel lattice pylon (position in the frame, height, color), and the direction the cabin travels. State that the cabin hangs below the cables and moves along them, never off them.

3. **Valley and Landscape**: peaks and their shapes, snow cover and rock, pine forest density, the village below (number of houses, roof colors, church or chalet details), roads or a frozen stream, and depth layers from foreground to background.

4. **Light and Atmosphere**: sun direction and color, alpenglow on the peaks, low clouds or valley fog, light snow in the air, chimney smoke, and how the light catches the cabin windows and cables.

5. **Fixed Visual Details**: a numbered list of 8 to 10 details that must stay identical in the still image and in the video (cabin color and position, cable angle, pylon side, peak shapes, village position, sun side, cloud layer height, camera position, framing).

6. **Motion Map**: a table of every element that can move in the video, with columns: element, type of motion, direction, speed (very slow, slow, medium), and how strongly it should move. Include the camera move. Keep total motion subtle and physically plausible.

7. **Prompt Seed A - Hero Still Image**: a ready-to-paste image prompt under 170 words for a wide landscape 16:9 frame, with the cabin, the cables, the pylon, and the snowy valley in the first sentence, ending with: no people, no text, no signs, no logos.

8. **Prompt Seed B - Image-to-Video Animation**: a ready-to-paste video prompt under 120 words that starts from the hero still as the first frame, describes one slow camera move and the natural motions from the Motion Map for about 6 seconds, and says to keep the cabin, the cables, the pylon, the mountains, and the framing exactly as in the image with no new objects.

Rules: no people as the main subject, no text, signs, or logos, no fast camera moves or cuts, and no motion that breaks physics (the cabin moves smoothly along the cable at a constant slow speed and swings only slightly, clouds drift with one wind direction, smoke bends with the same wind). Use short paragraphs and lists.
```

</details>

<details><summary><b>Alpine Freefall</b></summary>

```text
{
  "title": "Alpine Freefall",
  "description": "A high-octane, wide-angle action shot capturing the exhilarating rush of a freestyle skier mid-descent on a steep mountain peak.",
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve her core likeness. Create a hyper-realistic GoPro selfie-style image of Subject 1 speeding down a high-altitude ski slope. The image should feature the signature fisheye distortion, capturing the curvature of the horizon and the intense speed of the descent, with the subject holding the camera pole to frame herself against the dropping vertical drop.",
  "details": {
    "year": "2024",
    "genre": "GoPro",
    "location": "A jagged, snow-covered mountain ridge in the French Alps with a clear blue sky overhead.",
    "lighting": [
      "Bright, harsh sunlight",
      "Lens flare artifacts",
      "High contrast"
    ],
    "camera_angle": "Selfie-stick POV with wide-angle fisheye distortion.",
    "emotion": [
      "Exhilarated",
      "Fearless",
      "Wild"
    ],
    "color_palette": [
      "Blinding white",
      "Deep azure",
      "Stark black",
      "Skin tones"
    ],
    "atmosphere": [
      "Adrenaline-fueled",
      "Fast-paced",
      "Crisp",
      "Windy"
    ],
    "environmental_elements": "Kicked-up powder snow spraying towards the lens, motion blur on the edges, water droplets on the camera glass.",
    "subject1": {
      "costume": "black mini skirt, white crop top, leather fingerless gloves",
      "subject_expression": "Wide-mouthed shout of excitement, eyes wide with the thrill.",
      "subject_action": "ski"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "studio lighting",
        "calm",
        "static pose",
        "indoor settings",
        "trees"
      ],
      "exclude_styles": [
        "oil painting",
        "sketch",
        "warm vintage",
        "soft focus"
      ],
      "exclude_colors": [
        "sepia",
        "muted tones",
        "pastel"
      ],
      "exclude_objects": [
        "ski lift",
        "crowd",
        "buildings"
      ]
    }
  }
}
```

</details>

<details><summary><b>Alpine Lake Golden Hour Portrait</b></summary>

```text
A realistic, high-quality 8K photo taken on an iPhone 16 Pro Max, 3:4 aspect ratio.

Composition & Camera Angle: Medium shot at eye level in a three-quarter profile. A young woman stands beside a mountain lake, positioned slightly right of center. Her body is turned sideways while she looks back over her shoulder toward the camera with a soft, natural smile.

Subject & Mood: A smiling young woman with a relaxed, peaceful “granola girl” aesthetic. Her arms rest naturally at her sides as she holds a transparent water bottle hanging beside her thigh. Her expression is calm, warm, and effortless.

Outfit & Accessories: She wears a cropped oversized sherpa fleece jacket featuring a bold ethnic geometric pattern in beige, rust brown, blue, and black. Black leggings complete the outfit, and a dark shoulder strap from a bottle or small bag crosses her body.

Hair & Makeup:  hair is partially gathered into a messy bun, with loose strands framing her face and falling over her shoulders. Minimal, natural “no-makeup” makeup with fresh, realistic skin.

Lighting & Atmosphere: Golden hour sunlight bathes the scene in warm, rich tones. The atmosphere feels peaceful, adventurous, cozy, and deeply connected to nature.

Background: A tranquil alpine lake reflects dramatic limestone cliffs rising behind it. The lower mountain slopes are covered with forest and vibrant green alpine meadows. The sky is clear blue with a few soft clouds, and tiny figures of people are visible along the opposite shoreline. Wild grass and reeds appear in the foreground.

Technical Details: Deep focus keeps both the woman and the mountain landscape crisp and highly detailed. Photorealistic, ultra-sharp, realistic skin texture. Do not change her facial features or identity.
```

</details>

<details><summary><b>Amateur Hallway Mirror Selfie</b></summary>

```text
instagirl, mirror selfie in a hallway, realistic amateur phone snapshot, natural skin texture, minimal makeup, mild lens distortion from phone camera, casual posture, everyday outfit, slight handheld micro-blur, iPhone 11 wide 26mm EXIF feel, imperfect framing (a little headroom cut), mixed indoor lighting with slight color cast, background clutter present, no retouching, no beauty filter, faithful anatomy, same person identity, same body proportions, match reference face closely, iphone 11 pro max,
```

</details>

<details><summary><b>Amateur Phone Photo with Chat Screen</b></summary>

```text
Create a realistic, poorly taken amateur photo of a physical smartphone showing a WhatsApp chat on its screen.

The phone should be held vertically in one hand, with visible dark bezels/case, warm dim indoor lighting, slight tilt, blur, grain, glare, reflections, uneven focus, and imperfect framing. It must look like a bad real-world photo of a phone screen, not a clean screenshot.

On the phone screen, show an iPhone-style WhatsApp conversation in Turkish with the contact name ${receiver_name} and a small profile photo attached photo (if not provided use default whatsapp profile icon).

Chat subject:
${talk_subject}

Generate the WhatsApp dialogue naturally based on the subject above. The contact’s messages should be in ${language_name:Turkish} language and ${talk_style} (e.g. broken ${language_name:Turkish} with typos and awkward wording. My messages should be correct ${language_name:Turkish} with no typos). Use realistic white incoming bubbles, green outgoing bubbles, timestamps, blue double-check marks, and a WhatsApp input bar at the bottom.

Keep the screen readable but slightly blurry, like a poorly photographed phone screen.
```

</details>

<details><summary><b>Amateur Phone Snapshot Style</b></summary>

```text
{
  "prompt": "instagirl, candid phone snapshot, realistic amateur vibe, natural skin texture, light makeup at most, handheld micro-blur, iPhone 11 wide 26mm EXIF look, f/1.8, 1/60s, ISO 200, slight lens distortion, casual posture, everyday outfit, mild flyaway hair, imperfect framing, background clutter present, no retouching, realistic shadows, faithful anatomy, same person identity, same body proportions",
  "negative_prompt": "beauty filter, skin smoothing, studio glam, hdr glow, cinematic grading, fashion editorial, airbrush, liquify, body morph, face changed, de-aged, uncanny valley, extra fingers, warped limbs, NSFW, lingerie, bikini, watermark, text, logo, border",
  "image": "<REFERENCE_IMAGE_URL>",
  "strength": 0.35,
  "guidance": 5.0,
  "control_nets": [
    {
      "type": "openpose",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.7,
      "guess_mode": false
    },
    {
      "type": "depth",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.45
    }
  ],
  "face_lock": {
    "type": "ip_adapter_faceid",
    "ref_image": "<REFERENCE_FACE_CROP_OR_SAME_URL>",
    "weight": 0.75
  }
}
```

</details>

<details><summary><b>Analog Film Camera Look</b></summary>

```text
Kodak porra 400 Authentic vintage analog film photography, captured on classic 35mm film camera with manual focus lens, shot on expired Kodak Portra 400 film stock, pronounced natural film grain structure with visible halation around bright highlights, warm nostalgic color palette with slightly desaturated mid-tones, organic color shifts between frames, gentle peachy skin tones characteristic of Portra film, soft dreamy vignetting gradually darkening towards corners and edges, accidental light leaks with orange and red hues bleeding into frame edges, subtle lens flare from uncoated vintage optics, imperfect manual focus creating dreamy bokeh with swirly out-of-focus areas, chromatic aberration visible in high contrast edges, film dust particles and hair caught during scanning process, fine vertical scratches from film transport mechanism, authentic analog warmth with slightly lifted blacks and compressed highlights, natural color bleeding between adjacent film layers, gentle overexposure in bright areas creating soft glow, film edge artifacts and frame numbers barely visible, scanned from original negative with slight color cast, 1990s point-and-shoot disposable camera aesthetic, Fujifilm Superia or Agfa Vista alternative film characteristics, organic photographic imperfections and inconsistencies, slightly soft focus overall sharpness, date stamp in corner optional, double exposure ghost images subtle overlay, sprocket holes impression, cross-processed color shifts, pushed film development look with increased contrast and grain, natural lighting artifacts and lens imperfections, retro photo lab color correction style, authentic film emulsion texture, varying exposure between frames showing human photographer touch, mechanical shutter artifacts, slight motion blur from slower shutter speeds, nostalgic summer afternoon golden hour warmth, faded photograph found in old shoebox quality, memory lane aesthetic, tactile analog photography feel
```

</details>

<details><summary><b>Animated Logo Title Card Reveal</b></summary>

```text
Cinematic intro animation. Dark navy blue background with subtle particle effects. 
Large bold white text "MARMARA MPDS" appears with a cyan glow effect, letter by letter for PDS, color effect only effects the PDS letters, M letter is white. 
Below it smaller text "Fikirleri Projeye Dönüştürüyoruz" fades in. 
Futuristic, minimalist tech aesthetic. No people.
```

</details>

<details><summary><b>Animated Weather Radar Map: Brescia Storm</b></summary>

```text
Act as a meteorological video producer. You are tasked with creating an animated weather radar map for Northern Italy, zoomed into the province of Brescia. Your video should include:
- A clearly labeled map with Inzino on the west and Sarezzo on the east.
- A swirling hurricane-like storm system with rotating cloud bands.
- Heavy rain colors represented in blue, green, yellow, and red on the radar.
- Motion arrows indicating the storm's eastward movement from Inzino to Sarezzo.
- Realistic meteorological radar textures and satellite overlay.
- Dramatic yet professional TV weather broadcast graphics.
- Smooth animation frames for seamless viewing.

Your task is to ensure that the animation is both informative and visually engaging, suitable for a TV weather forecast.
```

</details>

<details><summary><b>Anime Demon Red Eyes Portrait</b></summary>

```text
Anime boy with short white hair, pale skin, black shirt, close-up portrait, neutral expression, soft shadows, minimalist background, glowing demon red eyes, dark red sclera veins, subtle red aura around the eyes, sharp pupils, intense gaze, cinematic lighting, high detail, dramatic contrast
```

</details>

<details><summary><b>Apartment Mirror Selfie in Jersey</b></summary>

```text
“Mirror-selfie scene in a modern apartment interior. A young woman with long, naturally wavy light-brown hair wears a dark baseball cap (strap visible at the back), a black short-sleeve football jersey with pink lettering and the number ‘10’, and black high-waist leggings. She is turned back to camera, facing the mirror; her face is mostly not visible (rear/three-quarter from behind).
She holds a black smartphone in her right hand at shoulder height, elbow bent ~90°, wrist straight, the rear camera facing the mirror so the phone screen in the mirror shows the same scene (phone-within-phone recursion). Left arm relaxed down by her side.
Camera & composition: shot as a mirror selfie from behind; lens ~26–28mm equivalent, eye-level camera height; portrait orientation; framed from mid-thigh to above the head, centered on the jersey text and number. Subtle soft daylight from the room; no harsh shadows.
Environment: white door on the left with metal lever handle, narrow wall section, open doorway leading to a minimal kitchen (tall fridge/oven column visible), pale neutral walls, light flooring. Background slightly soft but readable.
Wardrobe details to preserve: jersey text “MESSI” in rounded pink letters above a large pink “10”; pink line style consistent; jersey fit slightly loose; cap color dark; leggings matte black; hair length reaches mid-back with a few loose curls.
Pose & micro-angles: head slightly tilted right, cap brim angled slightly downward; shoulders relaxed; pelvis square to mirror; spine neutral. Right hand grip firm with fingertips visible at the phone’s far edge; phone edges parallel to mirror frame; phone centered roughly over the spine line.
Lighting: soft natural indoor light, neutral white balance, no flash, no color cast. Reflections are physically correct with no duplication or misalignment.
Aesthetic: clean, realistic, unfiltered, true-to-life skin and fabric textures, sharp focus on jersey lettering and phone; minimal grain.
Crop & aspect: primary 3:4 (portrait); safe alternatives 9:16 and 4:5 maintaining full jersey text and number in frame.”
Consistency Locks (do not alter):
Same woman: hair length, color, wave pattern; dark baseball cap with back strap; black jersey with pink “MESSI” + “10”; black leggings; right-hand phone hold at shoulder height; left arm relaxed; mirror-selfie from behind; apartment/kitchen layout; door with metal lever handle; overall camera height ≈ eye level; phone recursion visible on screen.
Keep proportions and body type; no slimming/lengthening.
Keep colors and typography of jersey lettering exactly; no restyling.
Maintain environment geometry and object placement.
```

</details>

<details><summary><b>Apartment Window Night Snapshot</b></summary>

```text
Ultra-realistic amateur night photo, vertical phone snapshot from inside a small Ankara apartment, looking toward a window and catching the vibe of an “iyi geceler” tweet. The camera is low and slightly tilted, as if the photo was taken by someone lying or sitting on a couch. In the foreground, the armrest of a worn fabric sofa and a soft blanket are visible, slightly out of focus.

In the mid-ground, a 27-year-old Turkish-looking woman with a soft, slightly chubby figure stands near the window, back partially turned to the camera, phone in one hand at chest level, the other hand resting lightly on the window frame. She wears comfy, non-revealing home clothes: an oversized pastel sweatshirt and loose pajama pants with a simple pattern. Her blonde hair falls loosely down her back. You can’t read the phone screen; it only casts a subtle blue glow on her face and hand, suggesting she has just posted a tweet.

Outside the window, the street is lit by a bright sodium-orange streetlamp, giving the buildings and parked cars a warm glow. A single yellow taxi is parked near the curb, slightly blurred. Across the street is an old apartment building with balconies, some windows dark and a few still lit. A small ground-floor Migros Jet or Şok market sign is visible, glowing softly, and a distant blue Turkcell shop sign and a tiny Ülker billboard are out of focus further down the street.

Inside the room, only a floor lamp with a warm bulb is on, casting a low, cozy light that contrasts with the cold bluish light from outside. Shadows pool in the corners of the room; there is some clutter like a stack of books, a mug on a coffee table, and a TV remote. Vertical framing is slightly off; the woman is closer to the right edge, part of the window frame is cut off, and a lamp shade intrudes at the top, making it feel like an honest, uncomposed phone shot.

There is visible high-ISO noise in the dark areas, slight motion blur on a car passing outside, and no strong color grading—just natural warm and cool lights mixing. The whole mise-en-scène should feel like a peaceful moment in a real Ankara apartment, seconds after quietly saying “iyi geceler” to the timeline.
```

</details>

<details><summary><b>App Store Screenshots Gallery Generator</b></summary>

```text
# App Store Screenshots Gallery Generator

**Create a professional, production-ready screenshots gallery for an iOS/macOS/Android app that looks like it was designed by the top 1% of app developers.**

## Context

You are building a screenshots gallery page for an app. The project has screenshots in a folder (typically `screenshots/`, `fastlane/screenshots/`, or similar). The gallery should be a single HTML file that can be deployed to Netlify, Vercel, or any static host.

## Requirements

### 1. Design System Foundation

Create CSS custom properties (design tokens) for:

- **Colors**: Primary palette (50-900 shades), secondary/accent palette, neutral grays (50-900)
- **Surfaces**: Three surface levels (surface-1, surface-2, surface-3)
- **Typography**: Two-font stack (mono for UI elements, sans for body)
- **Spacing**: Consistent scale (4px base)
- **Borders**: Radius scale (sm, md, lg, xl, 2xl, 3xl)
- **Shadows**: Five elevation levels (sm, md, lg, xl, 2xl)
- **Transitions**: Three speeds (fast: 150ms, normal: 300ms, smooth: 400ms with cubic-bezier)

### 2. Layout Architecture

- **Container**: Max-width 1600px, centered, with responsive padding
- **Grid**: Masonry-style responsive grid using `grid-template-columns: repeat(auto-fill, minmax(340px, 1fr))`
- **Gap**: 2rem on desktop, 1.5rem tablet, 1rem mobile
- **Card aspect ratio**: Maintain consistent screenshot presentation

### 3. Header Section

- **App badge**: Small pill-shaped badge with icon and "IOS APPLICATION" or platform text
- **Title**: Large, bold app name with gradient text treatment
- **Subtitle**: One-line description mentioning key technologies and features
- **Background**: Subtle grid pattern overlay for depth
- **Padding**: Reduced vertical padding (3rem top, 2rem bottom) for compact feel

### 4. Screenshot Cards

Each card should have:

- **Container**: White/off-white background, rounded corners (2xl), subtle shadow
- **Image container**: Gradient background, centered screenshot with white border (8px)
- **Hover effects**:
  - Card lifts (-8px translateY) with enhanced shadow
  - Screenshot scales (1.04) with slight rotation (0.5deg)
  - Top border appears (gradient bar)
  - Radial glow overlay fades in
- **Metadata bar**:
  - Number badge (gradient background, 26px square)
  - Device name (uppercase, small font, mono font)
- **Title**: Bold, mono font, 1rem
- **Description**: One-line caption, smaller font, subtle color

### 5. User Journey Ordering

Order screenshots by how users experience the app:

1. **Login/Onboarding** - First screen users see
2. **Dashboard/Home** - Main landing after login
3. **Primary feature views** - Core app functionality
4. **Settings/Configuration** - Customization screens
5. **Permissions/Integrations** - HealthKit, notifications, etc.
6. **Advanced features** - Sync, sharing, cloud features
7. **Analytics/Reports** - Data visualization screens
8. **Archive/History** - Historical data views

### 6. Animations

- **Entrance**: Staggered fade-in with translateY (0.1s delays between cards)
- **Hover**: Smooth cubic-bezier easing (0.16, 1, 0.3, 1)
- **Scroll**: IntersectionObserver to trigger animations when cards enter viewport
- **Performance**: Use `will-change` for transform and opacity

### 7. Footer

- **Background**: Dark (neutral-900) with subtle gradient overlay
- **Border radius**: Top corners only (2xl)
- **Content**: Minimal metadata (device, date, status) with icons
- **Spacing**: Compact (2rem padding)

### 8. Responsive Breakpoints

- **Desktop** (>1280px): 4-5 columns
- **Tablet** (768-1280px): 2-3 columns
- **Mobile** (<768px): 1 column, reduced padding throughout

### 9. Technical Requirements

- **Single HTML file**: All CSS inline in `<style>` tag
- **External dependencies only**:
  - Pico.css (minimal CSS framework)
  - Font Awesome (icons)
  - Google Fonts (Inter + IBM Plex Mono)
  - Animate.css (optional, for additional animations)
- **No build step**: Must work as static HTML
- **Performance**: Optimized animations, no layout shift
- **Accessibility**: Semantic HTML, alt text on images

### 10. Polish Details

- **Subtle gradients**: Background radials for depth (not overwhelming)
- **Border treatment**: 1px solid with alpha transparency
- **Shadow layering**: Multiple shadow values for depth
- **Typography**: Tight letter-spacing on headings (-0.03em)
- **Color consistency**: Use design tokens everywhere, no hardcoded values
- **Image presentation**: White border around screenshots for device frame illusion

## Output Format

Generate a single `index.html` file with:

1. Complete HTML structure
2. Inline CSS with design tokens
3. JavaScript for scroll animations (IntersectionObserver)
4. All screenshot cards with proper metadata
5. Responsive design for all screen sizes

## Example Screenshot Card Structure

'''html
<div class="screenshot-card">
    <div class="screenshot-img-container">
        <img src="screenshot-name.png" alt="Description" class="screenshot-img">
    </div>
    <div class="screenshot-info">
        <div class="screenshot-meta">
            <div class="screenshot-number">1</div>
            <div class="screenshot-device">iPhone 17 Pro Max</div>
        </div>
        <h3 class="screenshot-title">Screen Title</h3>
        <p class="screenshot-desc">One-line caption</p>
    </div>
</div>
'''

## Key Differentiators from "AI-looking" Galleries

❌ **Avoid**:
- Excessive gradients and colors
- Large stat cards that waste space
- Verbose descriptions and feature lists
- Section dividers and category headers
- Overwhelming animations
- Inconsistent spacing
- Generic stock photography style

✅ **Emulate**:
- Apple App Store product pages
- Linear, Raycast, Superhuman marketing sites
- Minimalist, content-first design
- Subtle, refined interactions
- Consistent visual rhythm
- Typography-driven hierarchy
- White space as design element

## Deployment Notes

- Gallery should deploy to `project-root/screenshots-gallery/` or similar
- Include `.netlify` folder with `netlify.toml` for configuration
- All screenshots should be in the same folder as `index.html`
- No build process required - pure static HTML

---

**Usage**: Copy this prompt and provide it to an AI assistant along with:
1. The list of screenshot files in your project
2. Your app name and one-line description
3. The platform (iOS, macOS, Android, web)
4. Key technologies used (SwiftUI, React Native, Flutter, etc.)

The AI will generate a production-ready gallery that looks professionally designed.
```

</details>

<details><summary><b>Apple-Level UI System Designer</b></summary>

```text
You are a senior product designer operating at Apple-level design standards (2026).

Your task is to transform a given idea into a clean, professional, production-grade UI system.

Avoid generic, AI-generated aesthetics. Prioritize clarity, restraint, hierarchy, and precision.

---

### Design Principles (Strictly Enforce)

- Clarity over decoration  
- Generous whitespace and visual breathing room  
- Minimal color usage (functional, not expressive)  
- Strong typography hierarchy (clear scale, no randomness)  
- Subtle, purposeful interactions (no gimmicks)  
- Pixel-level alignment and consistency  
- Every element must have a reason to exist  

---

### 1. Product Context
- What is the product?
- Who is the user?
- What is the primary action?

---

### 2. Layout Architecture
- Page structure (top → bottom)
- Grid system (columns, spacing rhythm)
- Section hierarchy

---

### 3. Typography System
- Font style (e.g. neutral sans-serif)
- Size scale (H1 → body → caption)
- Weight usage

---

### 4. Color System
- Base palette (neutral-first)
- Accent usage (limited and intentional)
- Functional color roles (success, error, etc.)

---

### 5. Component System
Define core components:
- Buttons (primary, secondary)
- Inputs
- Cards / containers
- Navigation

Ensure consistency and reusability.

---

### 6. Interaction Design
- Hover / active states (subtle)
- Transitions (fast, smooth, minimal)
- Feedback patterns (loading, success, error)

---

### 7. Spacing & Rhythm
- Consistent spacing scale
- Alignment rules
- Visual balance

---

### 8. Output Structure

Provide:

- UI Overview (1–2 paragraphs)
- Layout Breakdown
- Typography System
- Color System
- Component Definitions
- Interaction Notes
- Design Philosophy (why it works)
```

</details>

<details><summary><b>Appliance Showroom Cartoon Argument</b></summary>

```text
A funny 3D cartoon scene inside a modern Fresh appliance showroom. A Fresh fan, a Fresh air cooler, and a Fresh microwave are having a hilarious argument like human characters.

The Fresh Fan spins proudly and says: "I'm the superstar of summer! The moment the weather gets hot, everyone runs to buy me!"

The Fresh Air Cooler smiles confidently and replies: "Easy there! I don't just move air... I actually cool it!"

The Fresh Microwave suddenly interrupts with a glowing light inside: "Oh please! While you're only popular in summer, I work all year long—winter, summer, and even during Ramadan!"

The Fan laughs and says: "Maybe, but people run away from your heat!"

The Microwave responds: "And you stop working the second the power goes out!"

The Air Cooler raises its hands and says: "Guys, guys... we're all Fresh products. The real problem is that customers can't decide which one of us to buy first!"

Highly detailed 3D cartoon style, expressive funny faces, colorful showroom, comic speech bubbles, playful atmosphere, professional lighting, ultra-realistic rendering, humorous family-friendly advertisement, high quality.
```

</details>

<details><summary><b>Architectural Sketch Markup Overlay</b></summary>

```text
Based on the source image, overlay an architect's busy working process onto the entire scene. The image should look like a blueprint or trace paper covering the original photo, filled with handwritten black ink sketches, technical annotations, dimension lines with measurements (e.g., "12'-4"", "CLG HGT 9'"), rough cross-section diagrams showing structural details, revision clouds with notes like "REVISE LATER", and leaders pointing to specific elements labeled with English architect's notes such as "CHECK BEAM", "REMOVE FINISH", or "PROPOSED NEW OPENING". The style should be messy, authentic, and look like a work-in-progress conceptual drawing.
```

</details>

<details><summary><b>Architectural Study Sheet</b></summary>

```text
A vintage architectural infographic of ${historic_site_name} that blends art and technical clarity: a detailed front elevation at the center, a clean line-art landscape of ${location} behind it, and annotated dimension lines with sample values like “${height_value_1}” and “${height_value_2}”. Surrounded by 2–3 close-up detail boxes and a “Site plan – ${location}” panel, the piece uses pen-and-ink hatching on warm aged paper to feel like a hand-drawn architectural study sheet.
```

</details>

<details><summary><b>Arctic Fox Curled Up in Snow</b></summary>

```text
A photorealistic wildlife photograph of an Arctic fox in its thick pure white winter coat, curled up in a round ball on fresh powder snow in the center of a wide landscape 16:9 frame. Its bushy white tail wraps around the front of its body and covers its paws, with its black nose resting just above the tail. Both eyes are half open, dark and drowsy, gazing calmly toward the camera, small rounded ears upright, and a few fine snowflakes resting on the dense fur. The fox lies in a soft hollow of snow, shot from a low eye-level angle close to the ground. Behind it, a wide snowy tundra fades into a creamy blur of gentle drifts under soft blue-hour light, with a thin band of pink glow along the distant horizon and pale lavender sky above. Telephoto lens, shallow depth of field, sharp focus on the face and the fur texture, cool blue and white tones with a touch of pink, natural colors, quiet and peaceful mood. No text, no watermark, no people.
```

</details>

<details><summary><b>Arctic Research Station Under a Green Aurora</b></summary>

```text
A photorealistic wide-angle night photograph of a small Arctic research station on a snow-covered ridge above a frozen fjord. Three red prefabricated modules on steel stilts are joined by a short covered walkway; their small square windows glow warm amber. A weather mast with an anemometer, a satellite dish and a radio antenna stand beside them, lightly rimed with frost. In the foreground, a lone scientist in an orange expedition parka and fur-trimmed hood walks along a trail of boot prints toward the station, a narrow white headlamp beam cutting through faint blowing snow. Above, a vivid green aurora ripples across the whole sky in curtains, fading to violet and magenta at the top edges, with stars visible between the bands and the aurora faintly reflected on the ice of the fjord. Deep blue polar night, crisp cold air, subtle snow texture. Shot on a full-frame camera with a 16mm lens, 10-second exposure, f/2.8, ISO 3200, tripod, slight foreground sharpness, natural colors, no lens flare, no text, 16:9.
```

</details>

<details><summary><b>Art Deco Seaplane Harbor Travel Poster</b></summary>

```text
A 1930s Art Deco travel poster illustration of a seaplane harbor at dawn on a calm turquoise bay. A sleek silver and cream twin-engine seaplane with rounded floats glides low over the water toward a curved white Streamline Moderne terminal building with porthole windows, a slim observation tower, and flag poles with plain colored pennants. Long straight reflections stretch across the glassy water, and a small wooden pier with striped mooring posts leads into the foreground, where two moored seaplanes and a little red launch boat sit in neat geometric ripples. Behind the harbor, terraced hills with cypress trees and white villas rise toward a pale peach and coral sky with a large, low sun drawn as concentric rings and stylized radiating sunbeams. Bold flat shapes, crisp clean edges, limited palette of teal, coral, cream, navy, and gold, smooth airbrushed gradients in the sky and water, subtle speed lines behind the plane. Strong diagonal composition with the seaplane on the upper third line and a deep sense of distance, elegant and optimistic mood of golden-age travel. Lithograph print look with fine paper grain and slight ink registration offsets, gentle sun-faded edges. Leave an empty plain band of sky at the top with no detail, but do not add any lettering. No text, no letters, no logos, no airline markings, no people in close-up. Vertical 3:4 poster aspect ratio.
```

</details>

<details><summary><b>Art Nouveau Heron Among Blue Irises</b></summary>

```text
A grey heron stands on one leg among tall blue and violet irises at the edge of a moonlit lily pond, framed by an ornate Art Nouveau border of curling whiplash vines, iris leaves, and dragonflies. Wide horizontal decorative panel in the spirit of 1900s Art Nouveau posters and stained-glass design. The heron's long neck forms a graceful S-curve, its feathers drawn with flowing contour lines in soft greys and pearl white. A large pale full moon sits inside a circular halo behind the bird, with concentric rings of gold leaf. Water lilies and round pads float on dark teal water with stylized ripple patterns. Bold dark outlines, flat areas of muted color, and fine decorative linework. Palette of deep teal, sage green, iris blue, lavender, cream, and burnished gold, with subtle aged paper grain. Symmetrical, elegant, calm composition with the heron slightly left of center and irises balancing the right side. Landscape 16:9. No people, no text, no lettering, no signature, no logos.
```

</details>

<details><summary><b>Art Style Consistency for Image Projects</b></summary>

```text
Act as an Image Generation Specialist. You are responsible for creating images that adhere to a specific art style and project guidelines.

Your task is to:
- Use only the files available within the specified project folder.
- Ensure all image generations maintain the designated art style and type as provided by the user.

You will:
- Access and utilize project files: Ensure that any references, textures, or assets used in image generation are from the user's project files.
- Maintain style consistency: Follow the user's specified art style guidelines to create uniform and cohesive images.
- Communicate clearly: Notify the user if any required files are missing or if additional input is needed to maintain consistency.

Rules:
- Do not use external files or resources outside of the provided project.
- Consistency is key; ensure all images align with the user's artistic vision.

Variables:
- ${projectPath}: Path to the project files.
- ${artStyle}: User's specified art style.

Example:
- "Generate an image using assets from ${projectPath} in the style of ${artStyle}."
```

</details>

<details><summary><b>Article to Symbolic Images</b></summary>

```text
Assume you're an AI capable of converting textual information into concrete images. Now you've entered an information world where everything is symbolically represented. I'm about to give you an article, and your task is to convert the information in this article into symbolic images as you understand them. Can you describe the form of these symbolic images in your visual world based on the article's information?
```

</details>

<details><summary><b>Artistic Half Skeleton Glamour Portrait</b></summary>

```text
A portrait photo of a woman with bare shoulders against a dark, neutral studio background. The camera is positioned at eye level. The woman is facing the camera in a clear three-quarter view, with her head slightly turned to the right from her perspective, allowing the intricate makeup on both sides of her face to remain clearly visible. Her shoulders and neck are also visible in the frame.
Makeup (the main focus):

Extremely intricate and artistic half-skeleton makeup, executed with great precision. The face is visually divided vertically into two halves.
Left side of the face (viewer’s perspective): Glamorous and beautiful, with intense purple gradient eyeshadow, precise black eyeliner, very long, thick false eyelashes, and a neatly defined eyebrow.
Right side of the face (viewer’s perspective): A skeletal structure with a pink-purple gradient. The eye socket is painted pink and purple. The contours of the eye socket, cheekbone, and lower jaw are detailed with thin, delicate lines made of small, shimmering purple rhinestones or glitter. The nasal cavity is also highlighted with a purple gradient.
Lips: Divided into two contrasting halves. One half has matte purple lipstick with skeletal teeth outlined using purple rhinestones. The other half has glossy pinkish-brown lipstick.
Hair: Luxurious, medium-length wavy hair falling over the shoulders. Keep the main hair color exactly as in the reference, with large, vivid purple strands framing the face, resembling intense toning or an ombre effect. The hair is neatly and softly styled, with a purple strand above the forehead forming an elegant wave.
Clothing & Body: Bare shoulders and neck. She wears a strapless top or corset that is mostly not visible. Fine glitter or sparkles cover the skin of her shoulders and neck, shimmering under the light.
Accessories: A small, delicate stud earring is visible. No visible jewelry on the shoulders to keep the focus on the makeup.
Lighting: Soft lighting that emphasizes the makeup textures, rhinestones, glitter, and eyeshadow while adding shine to the hair. Highlights on the glitter and rhinestones create a sparkling effect. Dark, neutral background.
Atmosphere & Mood: Glamorous, artistic, mystical, and confident. A modern Halloween makeup look combining fear and beauty. Mysterious and captivating.
Do not change the facial features or identity from the reference image. Preserve the exact face shape, eyes, nose, lips, and other distinctive features.
Format: 3:4.

Realistic, high-quality, sharp 8K photograph, shot on an iPhone 16 Pro Max.

Dark background.
```

</details>

<details><summary><b>Ascii Artist</b></summary>

```text
I want you to act as an ascii artist. I will write the objects to you and I will ask you to write that object as ascii code in the code block. Write only ascii code. Do not explain about the object you wrote. I will say the objects in double quotes. My first object is "cat"
```

</details>

<details><summary><b>Attention-Grabbing Booklet Cover Design</b></summary>

```text
Create a professional program to create a booklet cover in different colors with the possibility of adding images to complement the painting contribute to attracting the reader's attention distributed in a superior format with the choice of type, colors and Font Format for the product name ""brief summary 60 words* ""author ""serial number ""conjure the attached design to simulate a more creative design with the possibility of data entry above" I want a creative design from a unique idea like this in the attached image
```

</details>

<details><summary><b>Autumn Pumpkin Patch Portrait</b></summary>

```text
A realistic, high-quality 8K photo taken on an iPhone 16 Pro Max, 3:4 aspect ratio.

Subject: A young woman with loose hair. Do not change her facial features or identity. She is looking directly into the camera with a cute, gentle smile.

Pose: She is sitting on the ground with her knees bent and slightly pulled toward her body, both feet resting on the ground. Her torso is slightly turned toward the camera. She is holding a medium-sized bright orange pumpkin with both hands at stomach/lower chest level, as if hugging it.

Outfit: An oversized textured sweater in a brown-olive (khaki/cappuccino) shade with long sleeves that slightly cover her hands. The fabric resembles wide-rib corduroy. Very short black shorts are barely visible beneath the long sweater. She is wearing chunky black leather lace-up boots with thick soles in the style of Dr. Martens, paired with light white or light gray ankle socks featuring a thin pale blue stripe.

Setting: An open pumpkin patch with dry, yellow autumn grass covering the ground. Bright orange pumpkins of various sizes are scattered naturally around her. A very large pumpkin is partially visible in the right foreground. In the background, a low white wooden fence stretches across the field, with dark tree silhouettes and wooden utility poles visible in the distance.

Lighting & Atmosphere: Golden hour with soft, warm, diffused natural light and no harsh facial shadows. The sky is dramatic with large blue-gray autumn clouds, while a vivid yellow-orange sunset glow breaks through the horizon. Cozy fall vibes, autumn aesthetic, relaxed, slightly melancholic yet warm and comforting.

Camera: Eye-level perspective of a seated person, creating an intimate viewpoint. The woman is positioned slightly right of center. Deep enough depth of field keeps her in sharp focus while the background remains recognizable with a soft natural blur. The color palette contrasts warm orange and brown autumn tones with cool gray skies.
```

</details>

<details><summary><b>Avant-Garde Ghost Duplicate Portrait</b></summary>

```text
An ultra-realistic 8K cinematic studio portrait framed from mid-thigh up, featuring a figure standing confidently against a vibrant ochre-red background. The subject wears an oversized, highly textured bomber jacket with an eclectic, abstract patchwork pattern in muted and vivid reds, blues, greens, and beiges, paired with loose drab olive cargo pants and a white T-shirt. Lighting is harsh and frontal, creating crisp shadows and emphasizing fabric textures. A defining artistic element is a translucent, motion-blurred ghost duplicate of the subject positioned slightly behind and to the right, streaking horizontally with colorful trails that convey rapid movement or temporal distortion. The background remains uniform but subtly graded, adding depth without distraction. Shot in a high-fashion editorial style with sharp focus on the primary figure, shallow depth of field, and precise studio realism, delivering a bold, experimental, avant-garde mood.
```

</details>

<details><summary><b>Balcony Morning Coffee</b></summary>

```text
{
  "category": "BALCONY_COFFEE_PLANTS",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Preserve exact identity from reference. Adult 21+ only. No beautification or face changes."
  },
  "subject": {
    "demographics": "Adult woman, 21-29 (match reference identity).",
    "hair": {
      "color": "Match reference.",
      "style": "Loose waves or messy bun with tendrils",
      "texture": "Real strands, flyaways, realistic volume",
      "movement": "Natural, slight breeze lift"
    },
    "face": {
      "eyes": "Exact reference eyes; soft morning catchlights",
      "skin_details": "Natural texture, pores visible, gentle morning glow",
      "micro_details": "Keep reference marks"
    },
    "clothing": {
      "outfit": "Cozy cardigan + simple top (no logos/text)",
      "fabric": "Knit texture visible, slight pilling allowed"
    },
    "accessories": {
      "jewelry": ["Small silver hoops"],
      "props": ["Ceramic mug (unbranded)"]
    }
  },
  "pose": {
    "type": "Lifestyle candid",
    "orientation": "Half-body seated on balcony chair",
    "head_position": "Slight tilt, chin relaxed",
    "hands": "Both hands around mug for warmth (hands correct)",
    "gaze": "Near-direct eye contact",
    "expression": "Soft smile, relaxed"
  },
  "setting": {
    "environment": "Balcony with potted plants",
    "background_elements": [
      "Plant leaves in foreground bokeh",
      "Soft city background blur (no readable signs)",
      "Morning haze, gentle atmosphere"
    ],
    "depth": "Foreground leaves blurred; face sharp; background soft"
  },
  "camera": {
    "shot_type": "Half-body portrait",
    "angle": "Slightly above eye level",
    "focal_length_equivalent": "26mm phone OR 50mm pro",
    "framing": "4:5, off-center composition",
    "focus": "Eyes sharp; mug slightly softer"
  },
  "lighting": {
    "source": "Soft morning daylight",
    "direction": "Front/side diffuse",
    "highlights": "Natural highlights on eyes and lips",
    "shadows": "Gentle under-chin shadow"
  },
  "mood_and_expression": {
    "tone": "Cozy, relatable, calm",
    "atmosphere": "Tactile morning quiet"
  },
  "style_and_realism": {
    "style": "Photoreal IG lifestyle",
    "imperfections": "Mild grain, slightly imperfect framing"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Mild",
    "mode_variants": {
      "amateur": "Handheld iPhone-candid tilt, slight noise, imperfect composition",
      "pro": "Cleaner exposure, crisp micro-contrast, shallow DOF"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "identity drift", "face morphing",
    "cgi plants", "plastic skin",
    "extra fingers", "warped mug",
    "readable text", "logos", "watermark"
  ]
}
```

</details>

<details><summary><b>Bald Eagle 3D Render</b></summary>

```text
{
  "subject": {
    "description": "The head and upper neck of a bald eagle, looking upwards towards a light source.",
    "count": 1,
    "orientation": "profile, facing left, tilted steeply upward",
    "pose_or_state": "static, neck extended and head looking up",
    "expression": "majestic, neutral"
  },
  "scale_and_proportion": {
    "subject_to_frame_ratio": "subject occupies approximately 40% of the frame, positioned in the center-right",
    "proportions": "anatomically accurate eagle head",
    "negative_space": "extensive negative space on the left and bottom of the frame"
  },
  "composition": {
    "shot_type": "close-up",
    "camera_angle": "low angle, looking up at the subject",
    "framing": "subject positioned in the right half of the frame",
    "symmetry": "highly asymmetrical",
    "background": "pitch black with prominent diagonal volumetric light rays",
    "depth_of_field": "deep, light rays and illuminated subject features are in sharp focus"
  },
  "temporal_context": {
    "era": "contemporary digital art",
    "modern_elements": false,
    "retro_stylization": false,
    "trend_influence": false
  },
  "style": {
    "visual_type": "3D render",
    "realism_level": "maximum texture realism",
    "art_style": "none",
    "stylization": false,
    "interpretation": "literal reproduction only"
  },
  "lighting": {
    "setup_type": "volumetric / rim lighting",
    "light_direction": "top right, casting rays downwards toward the bottom left",
    "light_quality": "hard volumetric beams (god rays)",
    "contrast": "extremely high, chiaroscuro effect",
    "shadow_behavior": "deep, absolute black shadows obscuring the lower half of the subject",
    "color_temperature": "very cool, monochromatic deep violet/purple",
    "lighting_variation": "none"
  },
  "materials": {
    "primary_materials": [
      "feathers",
      "keratin (beak)"
    ],
    "surface_finish": "matte feathers, semi-gloss beak",
    "light_reflection": "sharp glint on the upper curve of the beak, soft highlights on individual feather edges",
    "material_accuracy": "exact"
  },
  "color_palette": {
    "dominant_colors": [
      "Deep Purple (#32174d)",
      "Black (#000000)"
    ],
    "saturation": "high saturation in the purple light beams",
    "contrast_level": "maximum",
    "color_shift": false
  },
  "texture_and_detail": {
    "surface_detail": "fine feather barbs and textures visible only where the light hits",
    "grain_noise": "none, perfectly clean digital render",
    "micro_details": "preserved beak texture and sharp edges of highlighted feathers",
    "sharpness": "sharp focus on the beak and top of the head"
  },
  "camera_render_settings": {
    "lens_equivalent": "50mm",
    "perspective_distortion": "none",
    "aperture_look": "f/8 (deep focus)",
    "resolution": "high",
    "render_quality": "clean and neutral"
  },
  "constraints": {
    "no_additional_objects": true,
    "no_reframing": true,
    "no_crop": true,
    "no_stylization": true,
    "no_artistic_license": true,
    "no_text": true,
    "no_watermark": true,
    "no_effects": true,
    "no_dramatic_lighting": false,
    "no_color_grading": true
  },
  "iteration_instruction": {
    "compare_to_reference": true,
    "fix_geometry_first": true,
    "then_fix_composition": true,
    "then_fix_lighting": true,
    "then_fix_color": true,
    "ignore_aesthetic_improvements": true
  },
  "negative_prompt": [
    "creative",
    "cinematic",
    "artistic",
    "stylized",
    "illustration",
    "abstract",
    "dramatic",
    "wide-angle",
    "fisheye",
    "exaggeration",
    "reinterpretation",
    "extra elements",
    "modernized",
    "retro look",
    "color grading",
    "AI artifacts",
    "warm colors",
    "visible background elements"
  ]
}
```

</details>

<details><summary><b>Balinese Barong Mask Vector</b></summary>

```text
A detailed vector illustration of a traditional Balinese Barong Ket mask with a fierce expression, bulging eyes, and prominent tusks. Constructed with smooth Bezier curves and Gestalt principles of symmetry. The style fusions Balinese wood-carving aesthetics with modern flat-design minimalism. Colors include crimson, gold, and obsidian black. Verified: Scalable SVG, clean paths, no text, no trademarks
```

</details>

<details><summary><b>Basketball Court Background Swap</b></summary>

```text
Remove original background and put in realistic basketball court on a sunny day. Put in the name OGMELLY in background as graffiti. Only keep body features the sa,e with digital illustration
```

</details>

<details><summary><b>Bathroom Flash Selfie</b></summary>

```text
{
  "category": "BATHROOM_SELFIE_FLASH",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking / Mediterranean vibe.",
    "hair": {
      "color": "Dark brown with subtle natural highlights.",
      "style": "Loose, slightly tousled, casual parting.",
      "texture": "Soft strands, visible flyaways, roots realistic.",
      "movement": "Falls naturally over shoulders with minor stray hairs."
    },
    "face": {
      "shape": "Soft oval with gentle jawline.",
      "eyes": "Almond-shaped, dark irises, sharp catchlights, subtle eyeliner.",
      "nose": "Defined bridge, natural highlight on tip.",
      "lips": "Natural fullness, soft tint, slight parting (casual confident).",
      "skin_details": "Real pores, mild shine from flash, subtle blush, no airbrush.",
      "micro_details": "Tiny imperfections preserved (fine baby hairs at hairline)."
    },
    "clothing": {
      "top": "Casual ribbed tank or fitted tee (no logos, no text).",
      "fit": "Realistic fit with subtle fabric tension at shoulders.",
      "texture": "Visible ribbing/knit weave under flash."
    },
    "accessories": {
      "jewelry": [
        "Small silver hoop earrings"
      ]
    }
  },
  "pose": {
    "type": "Mirror selfie perspective (phone not visible if you prefer; otherwise mirror-only reflection style).",
    "orientation": "Close-up to half-body, slight high angle.",
    "head_position": "Slight tilt to subject's right.",
    "limbs": "One arm implied holding camera out of frame; other hand lightly touching hair near temple.",
    "gaze": "Direct eye contact, cool and confident.",
    "posture": "Relaxed shoulders, casual stance."
  },
  "setting": {
    "environment": "Domestic bathroom",
    "background_elements": [
      "Glossy tiles with realistic reflections",
      "Chrome shower fixture slightly out of focus",
      "Ceramic surfaces with mild specular highlights"
    ],
    "depth": "Shallow DOF: face sharp, background slightly softened."
  },
  "camera": {
    "shot_type": "Selfie-style portrait",
    "angle": "Slightly above eye level",
    "focal_length_equivalent": "24-28mm smartphone wide",
    "framing": "3:4 or 4:5, chest-up crop",
    "focus": "Eyes and face tack sharp, gentle falloff on shoulders",
    "perspective": "Natural mild foreshortening typical of handheld selfie"
  },
  "lighting": {
    "source": "Phone-flash-like hard frontal light + ambient bathroom light",
    "direction": "Front-facing flash with minimal side fill",
    "highlights": "Flash specular on forehead/nose/lips; realistic shine not plastic",
    "shadows": "Soft-ish shadows under chin; controlled contrast",
    "quality": "Candid flash pop"
  },
  "mood_and_expression": {
    "tone": "Casual, confident, intimate-candid",
    "expression": "Relaxed micro-smirk, 'cool girl' vibe",
    "atmosphere": "Spontaneous, unplanned"
  },
  "style_and_realism": {
    "style": "Photorealistic IG selfie",
    "fidelity": "High skin detail, no smoothing",
    "imperfections": "Mild noise, tiny stray hairs, natural texture retained"
  },
  "colors_and_tone": {
    "palette": "Neutral bathroom tones + natural skin",
    "white_balance": "Slightly warm indoor",
    "contrast": "Medium",
    "saturation": "Natural"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High resolution",
    "noise": "Slight phone-sensor grain in shadows",
    "motion_blur": "Minimal; acceptable only away from face"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "single_subject_only": true
  },
  "negative_prompt": [
    "nudity", "explicit", "porn",
    "extra fingers", "warped hands", "double face",
    "plastic skin", "over-smoothing",
    "readable text", "logos", "watermark",
    "cgi", "cartoon", "anime"
  ]
}
```

</details>

<details><summary><b>Batik Double Exposure Portrait</b></summary>

```text
Abstract portrait of a young Indonesian man, blending contemporary aesthetics with traditional heritage, double exposure technique, floating batik motifs, vibrant acrylic swirls, geometric patterns, expressive brushstrokes, warm skin tones contrasted with deep indigo and gold, cinematic lighting, ethereal atmosphere, masterpiece, high detail, artistic fusion.
```

</details>

<details><summary><b>Batik Pattern of Twin Peacocks and Lotus</b></summary>

```text
Twin peacocks facing each other beside lotus ponds, rendered as a traditional Indonesian batik textile pattern in indigo and cream. The peacocks fill the center with mirrored S-curved necks, fan tails filled with dotted isen motifs, and small floral medallions along the wings. Around them, oval lotus ponds hold blooming lotus flowers, pads, and tiny fish drawn as repeating geometric fills. A classic batik border frames the cloth: interlocking kawung and ceplok shapes with fine crackle lines from wax-resist dyeing. Palette limited to deep indigo blue, soft cream ground, and a few pale grey-blue washes. Hand-drawn irregularity in the lines, visible wax crackle texture, cloth weave grain, flat ornamental layout suitable for fabric. No people, no modern objects, no text, no signature.
```

</details>

<details><summary><b>Bauhaus Poster of a Sailboat Regatta</b></summary>

```text
Five sailboats with bold triangular sails race across a calm blue bay toward a small harbor pier, drawn as a Bauhaus-style geometric poster built only from circles, triangles, rectangles, and straight lines. The sails are flat primary red, yellow, and black triangles, the hulls are slim black and white trapezoids, and a large red-orange sun circle sits low on the right above the horizon. The sea is layered horizontal bands of cobalt, navy, and pale blue, with small white semicircles for waves, and a few thin diagonal lines suggest wind. A simple white pier of stacked rectangles extends from the left edge, with a round black buoy in the foreground. Off-white textured paper background, crisp hard edges, flat colors with no gradients, subtle screen-print grain and slight ink misregistration, strong asymmetric balance and generous negative space in the sky. Modernist 1920s design spirit, clean and joyful. Wide landscape 16:9. No people, no text, no letters, no numbers, no logos.
```

</details>

<details><summary><b>Beauty Editorial Photo Shoot Spec</b></summary>

```text
{
  "project_specifications": {
    "format": "2x2 Grid Collage",
    "aspect_ratio": "4:5",
    "aesthetic_style": "High-end Beauty Editorial",
    "rendering_engine_hints": {
      "realism_level": "Ultra-photorealistic",
      "texture_quality": "8k",
      "lighting_simulation": "Ray-traced studio lighting"
    }
  },
  "global_assets": {
    "subject_definition": {
      "hair": {
        "style": "Long, loosely wavy, voluminous",
        "texture": "Natural, individual strands defined",
        "behavior": "Messy but styled, framing face and shoulders"
      },
      "complexion": {
        "skin_texture": "Porous, hyper-realistic",
        "finish": "Dewy, glass-skin effect",
        "makeup": {
          "cheeks": "Heavy flush/blush",
          "lips": "High-gloss, plump, natural pink",
          "eyes": "Clean, defined lashes, natural brows"
        }
      },
      "wardrobe": {
        "item": "Mini dress",
        "fit": "Bodycon / Tight",
        "fabric": {
          "material": "Soft textured knit / Boucle",
          "tactility": "Fuzzy, light-catching fibers",
          "color": "Soft mauve or neutral taupe"
        },
        "details": "Spaghetti straps, mid-thigh length"
      }
    },
    "environment_definition": {
      "studio_setup": {
        "background": "Seamless paper, soft off-white/beige",
        "atmosphere": "Clean, warm, intimate"
      },
      "lighting_rig": {
        "key_light": "Large diffuse softbox (Front-Left)",
        "fill_light": "Reflector (Right)",
        "highlights": "Specular highlights on lips, cheekbones, and shoulders"
      }
    }
  },
  "panel_architecture": [
    {
      "position": "Top-Left (1)",
      "shot_type": "Extreme Close-Up (Macro)",
      "composition": {
        "angle": "Low angle, looking up slightly",
        "focus": "Mouth and nose area",
        "depth_of_field": "Shallow"
      },
      "action": {
        "primary": "Eating a strawberry",
        "nuance": "Delicate finger hold, lips slightly parted"
      },
      "visual_anchors": [
        "Moisture on strawberry surface",
        "Gloss reflection on lips",
        "Baby hairs at temple"
      ]
    },
    {
      "position": "Top-Right (2)",
      "shot_type": "Medium Shot (Thigh-up)",
      "composition": {
        "angle": "Eye level",
        "pose_dynamic": "Leaning forward slightly towards lens"
      },
      "action": {
        "stance": "Standing straight on",
        "arms": "Relaxed at sides",
        "expression": "Direct gaze, alluring pout"
      },
      "visual_anchors": [
        "Texture of knit dress",
        "Collarbone shadows",
        "Curvature of waist"
      ]
    },
    {
      "position": "Bottom-Left (3)",
      "shot_type": "Full Body (Seated)",
      "composition": {
        "angle": "Side profile",
        "framing": "Subject compacted on floor"
      },
      "action": {
        "pose": "Knees to chest (fetal position variation)",
        "interaction": "Cheek resting on knee, arms embracing legs",
        "hair_flow": "Cascading onto the floor"
      },
      "visual_anchors": [
        "Smooth leg definition",
        "Dress stretching over thigh",
        "Dreamy gaze"
      ]
    },
    {
      "position": "Bottom-Right (4)",
      "shot_type": "Beauty Portrait (Head & Hands)",
      "composition": {
        "angle": "Frontal close-up",
        "framing": "Chin to hairline"
      },
      "action": {
        "gesture": "Chin resting on interlaced fingers",
        "expression": "Soft smile, looking off-camera"
      },
      "visual_anchors": [
        "Hand detail and manicure",
        "Eye clarity",
        "Flush on cheeks"
      ]
    }
  ]
}
```

</details>

<details><summary><b>Bedroom Full-Body Mirror Selfie</b></summary>

```text
ultra realistic photo of a 25-year-old woman taking a full-body mirror selfie in a cozy bedroom, oversized hoodie and biker shorts, messy bed, warm afternoon window light, shot on a regular iPhone in one hand, casual handheld photo, automatic exposure, slight digital noise, imperfect framing, no studio lighting, everyday amateur Instagram style, natural skin texture, a bit of lens smudge, unedited colors
```

</details>

<details><summary><b>Bedroom Mirror Selfie Analysis</b></summary>

```text
{
  "image_analysis": {
    "environment": {
      "type": "Indoor",
      "location_type": "Bedroom or Living Area",
      "spatial_depth": "Reflected depth via mirror",
      "background_elements": "Large black flat-screen TV (reflected), clean white walls, dark flooring or rug"
    },
    "camera_specs": {
      "lens_type": "Smartphone Main Camera (Wide)",
      "angle": "Eye-level, straight-on mirror reflection",
      "perspective": "Full body shot (cropped at knees)",
      "focus": "Sharp focus on the subject's body",
      "framing": "Vertical portrait within a circular frame (mirror)"
    },
    "lighting": {
      "condition": "Soft Daylight / Window Light",
      "sources": [
        {
          "source_id": 1,
          "type": "Natural Window Light",
          "direction": "From the left (subject's right side)",
          "color_temperature": "Cool/Neutral White",
          "intensity": "Moderate",
          "effect_on_subject": "Creates gentle highlights on the right arm, shoulder, and hip; casts soft shadows on the left side of the torso, emphasizing muscle definition"
        }
      ],
      "shadows": "Soft, diffuse shadows defining the abdominal muscles and collarbones"
    },
    "subject_analysis": {
      "identity": "Young woman (Face obscured by phone)",
      "orientation": "Front-facing towards mirror",
      "emotional_state": "Confident, body-positive",
      "sensuality": "Moderate; highlights physique and fitness",
      "posture": {
        "general_definition": "Standing, 'Contrapposto' stance (weight on one leg)",
        "feet_placement": "Not visible (cropped out)",
        "hand_placement": "Left hand holding phone covering face, Right arm hanging naturally by side",
        "visible_extent": "From top of head to mid-thigh"
      },
      "head_details": {
        "hair": {
          "color": "Dark Brown",
          "style": "Long, loose, slightly wavy",
          "texture": "Silky",
          "interaction_with_face": "Falls over shoulders, framing the phone"
        },
        "face": {
          "definition": "Obscured by smartphone",
          "visible_features": "None explicitly visible"
        }
      },
      "body_details": {
        "body_type": "Slim / Athletic / Toned",
        "skin_tone": "Fair / Pale",
        "neck_area": {
          "visibility": "Visible, slender",
          "details": "Defined sternocleidomastoid muscles due to lighting"
        },
        "shoulder_area": {
          "shape": "Squared but delicate",
          "posture": "Relaxed"
        },
        "chest_area": {
          "ratio_to_body": "Proportionate",
          "visual_estimate": "Small to Medium",
          "bra_status": "Wearing sports bra/bralette",
          "nipple_visibility": "Concealed by padding/fabric",
          "shape": "Natural, lifted"
        },
        "midsection": {
          "belly_button": "Visible, vertical oval",
          "muscle_definition": "Visible '11' line abs (linea alba definition)",
          "ratio_to_chest": "Narrower",
          "ratio_to_hips": "Significantly tapered (Hourglass silhouette)"
        },
        "hip_area": {
          "ratio_to_waist": "Curved, wider than waist",
          "shape": "Rounded",
          "width": "Moderate"
        },
        "leg_area": {
          "thighs": "Smooth, slight gap visible",
          "knees": "Not visible"
        }
      },
      "attire": {
        "upper_body": {
          "item": "Bralette / Crop Top",
          "style": "Spaghetti straps, gathered/ruched front, scoop neck",
          "color": "Dark Olive Green",
          "fabric": "Cotton or synthetic blend, matte finish",
          "fit": "Tight / Skin-tight"
        },
        "lower_body": {
          "item": "Boy Shorts / Hot Pants",
          "style": "Wide ribbed waistband, short leg",
          "color": "Dark Olive Green (Matching set)",
          "fabric": "Ribbed knit texture",
          "fit": "Tight / Form-fitting"
        }
      },
      "accessories": {
        "jewelry": "Simple ring on left hand (phone hand)",
        "tech": "Smartphone with light pink/blush case"
      }
    },
    "objects_in_scene": [
      {
        "object": "Mirror",
        "description": "Large, circular wall mirror with a thin black frame",
        "role": "Framing device for the selfie",
        "ratio": "Dominates the composition"
      },
      {
        "object": "Television",
        "description": "Large flat screen, black, turned off",
        "position": "Reflected in background, behind subject",
        "role": "Background clutter/context"
      }
    ],
    "negative_prompts": [
      "face visible",
      "ugly",
      "fat",
      "morbid",
      "mutilated",
      "tranny",
      "trans",
      "trannsexual",
      "illustration",
      "cartoon",
      "anime",
      "painting",
      "drawing",
      "low quality",
      "jpeg artifacts",
      "grainy",
      "text",
      "watermark",
      "signature",
      "cluttered background",
      "bad lighting"
    ]
  }
}
```

</details>

<details><summary><b>Billiards Bar Scene with Reference</b></summary>

```text
{
  "meta_data": {
    "task_type": "text_to_image_with_reference",
    "version": "v1.0",
    "priority": "high"
  },
  "technical_constraints": {
    "identity_preservation": {
      "enabled": true,
      "reference_mode": "strict",
      "parameters": {
        "use_reference_face_only": true,
        "identity_lock": true,
        "preserve_facial_features": true,
        "preserve_skin_texture": true,
        "avoid_face_morphing": true,
        "preservation_strength": 1
      }
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "resolution_target": "ultra_high_res",
      "render_engine_style": "photorealistic"
    }
  },
  "creative_prompt": {
    "scene": {
      "location": "dim billiards bar",
      "background": "dark ceiling, red-and-white wall stripe, a few tables/chairs in the back, low-light ambience with subtle film grain",
      "key_props": [
        "green-felt pool table (foreground)",
        "vintage red billiard lamps overhead (warm red glow)",
        "scattered billiard balls on the table",
        "pool cue (held by the subject)"
      ]
    },
    "subject": {
      "type": "young adult woman",
      "identity_instruction": "The subject must be 100% identical to the uploaded reference photo (same face, proportions, age, and identity). No identity drift.",
      "pose": "leaning against the pool table edge; one hand braced on the table; the other hand holding the cue stick vertically; hip slightly popped; head slightly tilted; gaze up and to the side",
      "expression": "cool, confident, subtly flirtatious",
      "wardrobe": {
        "top": "leopard-print corset/bustier top with straps",
        "bottom": "black mini skirt",
        "accessories": "minimal jewelry (small hoops or studs)"
      },
      "details": {
        "nails": "red nail polish",
        "hair": "long, voluminous, wavy hair",
        "makeup": "night-out glam: defined eyeliner/lashes, warm blush, nude-brown lips"
      }
    },
    "camera_and_lighting": {
      "shot_style": "realistic nightlife flash photo + ambient bar lighting",
      "camera": "full-frame DSLR",
      "lens": "35mm or 50mm",
      "aperture": "f/1.8",
      "shutter_speed": "1/80s",
      "iso": "800",
      "lighting": {
        "primary": "on-camera flash (crisp subject, natural falloff, realistic shadows)",
        "secondary": "overhead red lamps glow + dim ambient fill",
        "look": "high contrast, controlled specular highlights, no blown whites"
      },
      "color_grading": "warm reds with natural skin tones, subtle film grain",
      "focus": "tack-sharp eyes and face, shallow depth of field, soft background bokeh"
    }
  },
  "negative_prompt": [
    "different person",
    "identity change",
    "face morphing",
    "extra people",
    "extra limbs",
    "extra fingers",
    "bad hands",
    "deformed anatomy",
    "warped cue stick",
    "warped pool table",
    "text",
    "logo",
    "watermark",
    "cartoon",
    "anime",
    "illustration",
    "over-smoothed skin",
    "plastic skin",
    "low resolution",
    "blurred face",
    "overexposed flash highlights"
  ]
}
```

</details>

<details><summary><b>Bioluminescent Jellyfish City in a Night Aquarium</b></summary>

```text
Photoreal cinematic still of a large rectangular glass aquarium at night, viewed slightly from below eye level. Inside the water floats a miniature deep-sea city nestled among towering bioluminescent jellyfish: tiny coral-spired towers, soft-glow windows, delicate bridges of translucent kelp fiber, and warm pinpoint lights like abyssal lanterns. Moon jellies and lion’s mane jellyfish drift slowly, their bells and tentacles glowing cyan, teal, and pale violet, casting dappled light on the sand floor. Fine plankton sparkles in volumetric god rays from a single cool overhead aquarium lamp. Condensation beads and subtle reflections on the glass; a dark living-room background barely visible beyond. Ultra-detailed, shallow depth of field on the central cluster of towers, 85mm look, no people, no text, no logos, serene and wondrous mood, safe for work.
```

</details>

<details><summary><b>Black and White Night Candid</b></summary>

```text
Overall Scene: A candid, medium-shot black-and-white photograph with a raw, grainy cinematic film texture. The mood is playful, flirty, and effortlessly confident, capturing a spontaneous night-time moment.

Subject & Appearance: A young woman with  voluminous wavy hair falling naturally over . Her facial features and identity remain unchanged. 

Outfit: She wears a fitted white cotton crop-top T-shirt with the text “DRAMA IS PART OF THE PROCESS” printed in a slightly worn, textured uppercase serif font. She is paired with light-colored textured casual pants sitting just below her waist, revealing a subtle strip of midriff.

Pose & Expression: She stands slightly turned to her left with her head gently tilted downward. Her eyes are closed, and she wears a sweet, soft smile. One hand rests casually on her hip while the other lightly touches the hem of her crop top. Her body language feels relaxed, feminine, playful, and naturally flirty.

Lighting: Low-light night photography with a single directional light from the left, creating dramatic high-contrast shadows while softly illuminating her face, hair, and outfit.

Background: A deep, nearly black background with softly blurred distant city lights and barely visible urban silhouettes, keeping the focus entirely on the woman.

Details: Highly realistic, razor-sharp 8K quality with authentic film grain. Shot on iPhone 16 Pro Max, realistic skin texture, minimal natural makeup, slightly tousled hair, shallow depth of field, off-center composition, ultra-detailed, photorealistic.

Aspect ratio: 3:4.
```

</details>

<details><summary><b>Black and White Portrait on Black Background</b></summary>

```text
Turn it into a black & White image. Make the background solid

black. So everything blends nicely. Keep the person exactly

the same.
```

</details>

<details><summary><b>Black and White Side Profile Portrait</b></summary>

```text
{
  "Use the attached image of the person as reference. Hyper-realistic black and white studio portrait of the young man in side profile, natural hair gently falling around his face. Strong rim light accentuating his jawline and nose, dark minimalist background. Expression thoughtful and serene, cinematic lighting creating dramatic contrast and fine photographic detail.",
  "size": "{argument name="image size" default="1024x1024"}",
  "n": {argument name="number of images" default="1"}
}
```

</details>

<details><summary><b>Black Oversize T-Shirt Image Batch</b></summary>

```text
create a bulk 50 images for oversize tshirt black color 1:1, 8k quality professional style me
```

</details>

<details><summary><b>Black Suit Studio Portrait</b></summary>

```text
A crisp, minimalist studio portrait of an individual dressed in classic formal attire.

Attire: A tailored black suit jacket paired with matching black trousers, a sharp white dress shirt buttoned to the collar, and a sleek black tie. Setting: A clean, neutral studio background—typically seamless grey, white, or deep black—offering high contrast and zero distractions. Lighting: Studio lighting casts soft shadows that highlight the clean lines and texture of the suit fabric, creating a polished, professional look. Pose: Typically a confident headshot or full-body pose, either facing forward with hands in pockets or angled slightly toward the light.
```

</details>

<details><summary><b>Blacksmith Shop Breakfast Cinematic Scene</b></summary>

```text
{
  "meta_instruction": {
    "image_category": "cinematic_scene",
    "core_prompt": "A cinematic shot taken from inside a dimly lit blacksmith shop looking outwards towards a partially open rolling shutter. A middle-aged master and his young apprentice are having a traditional Turkish breakfast on a scrap wood table covered with newspaper. The morning sunlight streams through the 80% open shutter, creating a beautiful lens flare and illuminating the dust particles in the air. The master is speaking while the apprentice listens with polite curiosity.",
    "negative_prompt": "clean pristine clothes, spotless environment, modern furniture, soft unworked hands, messy food, overexposed, fully open shutter, artificial studio lighting, cartoonish, 3d render"
  },
  "narrative_and_purpose": {
    "story_or_concept": "A moment of mentorship and tradition. An apprentice respectfully listening to his master during a peaceful early morning breakfast before a hard day's work in an industrial site.",
    "mood_and_vibe": "Authentic, warm, respectful, raw, industrious, serene morning."
  },
  "subjects": [
    {
      "presence": "primary",
      "type": "human",
      "description": "Middle-aged blacksmith master.",
      "dynamic_attributes": {
        "if_human": {
          "role_and_demographics": "Middle-aged male, stubble beard, wearing reading glasses resting on his chest with a neck strap.",
          "emotion_and_expression": "Experienced, calm, speaking with authority and warmth.",
          "action_and_wardrobe": "Wearing slightly dirty mechanic overalls. Hands are clean from dirt but look deeply worn, calloused, and weathered. Sitting and eating breakfast."
        }
      }
    },
    {
      "presence": "primary",
      "type": "human",
      "description": "Young blacksmith apprentice.",
      "dynamic_attributes": {
        "if_human": {
          "role_and_demographics": "Young male, humble appearance.",
          "emotion_and_expression": "Curious, polite, respectful, actively listening.",
          "action_and_wardrobe": "Wearing slightly dirty mechanic overalls. Hands are clean but show signs of manual labor. Sitting at the table, leaning in slightly to listen attentively."
        }
      }
    }
  ],
  "environment_and_worldbuilding": {
    "setting_type": "indoor",
    "location_details": "Inside a gritty mechanic and blacksmith shop in an industrial zone. A metal rolling shutter door is 80% open, revealing the bright morning outside.",
    "time_of_day_and_weather": "Early morning, sunrise, clear weather outside.",
    "props_and_supporting_elements": [
      "Low coffee table made from scrap wood",
      "Newspaper spread as a tablecloth",
      "Chrome plates containing tomatoes, black olives, white feta cheese, and cucumbers",
      "A metal pan of 'menemen' (Turkish scrambled eggs with tomatoes) in the center",
      "A custom trivet under the pan made from welded scrap iron pieces",
      "Metal shavings scattered organically on the shop floor"
    ]
  },
  "camera_and_lens": {
    "shot_scale": "medium_shot",
    "camera_angle": "eye_level",
    "lens_focal_length": "35mm",
    "depth_of_field": "Shallow depth of field, sharp focus on the subjects and the breakfast table, background and outside lightly blurred."
  },
  "lighting_and_atmosphere": {
    "lighting_source": "natural",
    "lighting_quality": "high_contrast",
    "atmospheric_effects": "Morning sun rays streaming into the dark shop, illuminated airborne dust particles, gentle lens flare from the sun."
  },
  "composition_and_layout": {
    "framing_rule": "rule_of_thirds",
    "functional_space": "none"
  },
  "post_processing_and_medium": {
    "medium": "digital_photography",
    "color_grading": "Cinematic color grading, warm earthy tones inside contrasting with the bright morning light outside, subtle teal and orange hues.",
    "texture_and_grain": "Subtle film grain, highly detailed textures on hands, wood, and metal."
  }
}
```

</details>

<details><summary><b>Blue Hour Bridge Full Body</b></summary>

```text
{
  "category": "BLUE_HOUR_BRIDGE_FULLBODY",
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking, calm confident vibe.",
    "hair": {
      "color": "Dark brown",
      "style": "Loose waves, slightly wind-touched",
      "texture": "Individual strands visible",
      "movement": "Small motion in hair tips"
    },
    "face": {
      "eyes": "Calm direct gaze",
      "skin_details": "Natural texture, no smoothing"
    },
    "clothing": {
      "outfit": "Minimal black coat + fitted top, no logos",
      "fabric": "Coat texture visible, slight wrinkles"
    },
    "accessories": {
      "jewelry": ["Silver hoops"]
    }
  },
  "pose": {
    "type": "Full-body leaning on railing",
    "orientation": "Body angled, head turned to camera",
    "hands": "Hands resting on railing, fingers correct",
    "gaze": "Direct eye contact",
    "expression": "Neutral calm confidence"
  },
  "setting": {
    "environment": "Bridge at blue hour",
    "background_elements": [
      "City lights bokeh",
      "Cool dusk ambience",
      "Railing texture visible"
    ],
    "depth": "Subject sharp, background bokeh"
  },
  "camera": {
    "shot_type": "Full-body portrait",
    "angle": "Eye-level",
    "focal_length_equivalent": "35mm editorial",
    "framing": "4:5, subject off-center",
    "focus": "Face sharp, background creamy"
  },
  "lighting": {
    "source": "Ambient dusk + city light bounce",
    "direction": "Soft front fill from environment",
    "highlights": "Controlled, subtle"
  },
  "mood_and_expression": {
    "tone": "Cinematic, calm, premium",
    "atmosphere": "Blue hour dreamy realism"
  },
  "style_and_realism": {
    "style": "Photoreal social/editorial",
    "imperfections": "Slight low-light noise allowed"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild low-light grain"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "fake skyline", "cgi",
    "plastic skin", "over-smoothing",
    "extra fingers", "warped railing",
    "readable text", "logos", "watermark"
  ]
}
```

</details>

<details><summary><b>Blue Tone Mirror Selfie Scene</b></summary>

```text
Scene

Mirror selfie in an computer corner, blue color tone.

Subject

Gender expression: female

Age: around 25

Ethnicity: East Asian

Body type: slim, with a defined waist; natural body proportions

Skin tone: light neutral tone

Hairstyle:

Length: waist-length hair

Style: straight with slightly curled ends

Color: medium brown


Pose:

Stance: standing in a slight contrapposto pose

Right hand: holding a smartphone in front of her face (identity hidden)

Left arm: naturally hanging down alongside the torso

Torso: body leaning slightly back; waist and abdomen exposed


Clothing:

Top: tranparent bra

Bottom: transparent thong

Socks: blue and white horizontal striped over-the-knee socks

Accessory: a blue cute mascot phone case



Environment

Description: bedroom computer corner seen through a wall-mounted mirror

Furnishings:

White desk

Single monitor showing a soft blue wallpaper (no readable text)

Mechanical keyboard with white keycaps on a blue desk mat

Mouse on a small blue mouse pad

PC tower on the right side with blue case lighting

Three anime figures on or near the PC tower

A poster of a pagoda on the wall

Cat-shaped desk lamp with blue accents

A transparent glass of water

A tall green leafy plant by the window (on the left side of the frame)


Color replacement: replace all originally pink elements (clothes and room decor) with blue tones (baby blue to sky blue/periwinkle blue).


Lighting

Light source: daylight coming from a large window on the left side of the camera, through sheer curtains

Light quality: soft, diffused light

White balance (K): 5200


Camera

Mode: smartphone rear camera shooting via the mirror (no portrait/bokeh mode)

Equivalent focal length (mm): 26

Distances (m):

Subject to mirror: 0.6

Camera to mirror: 0.5


Exposure:

Aperture (f): 1.8

ISO: 100

Shutter speed (s): 0.01

Exposure compensation (EV): -0.3


Focus: focus on the torso and shorts in the mirror image

Depth of field: natural smartphone deep depth of field; background clearly visible with no artificial blur

Composition:

Aspect ratio: 1:1

Crop: from the top of the head to mid-thigh; include the desk, monitor, PC tower, and plant in the frame

Angle: slightly high angle from the mirror’s point of view

Composition note: keep the subject centered; to avoid wide-angle edge distortion, have her stand a bit further away and crop to a square later.



Negative prompts

Any appearance of pink/magenta anywhere

Beauty filters/over-smoothed skin; poreless skin look

Exaggerated or distorted anatomy

NSFW, see-through fabrics, wardrobe malfunctions

Logos, brand names, or readable user interface text

Fake portrait-mode blur, CGI/illustration feel
```

</details>

<details><summary><b>Blueprint Infographic for Social Media</b></summary>

```text
SYSTEM:
You are an LLM prompt executor.

USER TASK:
Create a vertical 9:16 infographic for TikTok about: AI Deepfakes & Scams (2026).

LAYOUT (choose ONE):
Use: 1-6 box
Number boxes with circled numbers. Flow top-to-bottom, left-to-right.

CONTENT RULES:
Each box must include:
- 1 short subheading
- 2–4 bullet points (plain English, phone-readable)
Include at least 1 example.
End with 1 actionable takeaway/checklist box.

STYLE RULES:
Follow the STYLE SPEC below exactly. Do not add any border/frame. Keep full-bleed. Keep the same hand-drawn style for every element.

TEXT QUALITY REQUIREMENTS:
- All text must be clean, readable English (no gibberish, no random characters).
- Use short bullets only; do not exceed 10–12 words per bullet.
- If layout is 1-8 or 1-10 box, reduce text even more or switch to 1-6 box for maximum readability.

OUTPUT REQUIREMENT:
Return the infographic content in this exact structure:
TITLE: ...
BOX 1: (Subheading) + bullets
BOX 2: (Subheading) + bullets
...
FOOTER (small): By SirCrypto

Then apply the style spec below.

--- STYLE SPEC (DO NOT CHANGE) ---
{
  "title": "",
  "layout_options": {
    "box_variants": ["1-2 box", "1-4 box", "1-6 box", "1-8 box", "1-10 box"],
    "remark": "Choose ONE box variant. Use schematic callouts and node connectors. Number each box with circled numbers."
  },
  "footer_credit": {
    "text": "By SirCrypto",
    "placement": "Bottom center or bottom right",
    "size": "Small/subtle"
  },
  "style": {
    "name": "Steel Blueprint Infographic",
    "description": "Mature engineering-notes infographic: blueprint grid, technical callouts, schematic icons. Serious, credible, and clean."
  },
  "visual_foundation": {
    "surface": {
      "base": "Deep steel blue background",
      "texture": "Subtle paper grain + faint blueprint grid (very light)",
      "edges": "Content extends fully to edges, no border or frame",
      "feel": "Like an engineer’s annotated blueprint page"
    },
    "overall_impression": "Technical clarity with human sketch warmth"
  },
  "illustration_style": {
    "line_quality": {
      "type": "Hand-drawn technical ink sketch aesthetic",
      "weight": "Medium strokes for boxes and icons, thin strokes for grid and callouts",
      "character": "Drafting-pen realism—slight wobble, consistent intent",
      "edges": "Soft, not vector-crisp",
      "fills": "Minimal hatching; avoid heavy shading"
    },
    "icon_treatment": {
      "style": "Minimal technical icons",
      "complexity": "Essential forms—readable at small sizes",
      "personality": "Professional, precise, not playful",
      "consistency": "Same hand-drawn style throughout"
    },
    "human_figures": {
      "style": "Optional, minimal silhouette only",
      "faces": "No detailed facial features"
    },
    "objects_and_scenes": {
      "approach": "Schematic objects: chip, camera, waveform, lock, network nodes",
      "detail_level": "Enough to identify; avoid clutter",
      "perspective": "Flat technical / simple isometric"
    }
  },
  "color_philosophy": {
    "palette_character": {
      "mood": "Professional, trustworthy, technical",
      "saturation": "Low-to-medium",
      "harmony": "Monochrome blues with restrained accents"
    },
    "primary_palette": {
      "blues": "Steel blue, navy",
      "cyans": "Soft cyan highlights for key terms and connectors",
      "ambers": "Muted amber for warnings and risk tags"
    },
    "supporting_palette": {
      "neutrals": "Cool-warm balanced grays",
      "blacks": "Soft charcoal lines, never pure #000000",
      "whites": "Off-white ink for readability"
    },
    "color_application": {
      "fills": "Light translucent blocks behind section boxes",
      "backgrounds": "Blueprint grid remains faint and secondary",
      "accents": "Cyan underlines and amber warning tags, limited use",
      "technique": "Keep restrained, ‘engineering notes’ feel"
    }
  },
  "typography_integration": {
    "headline_style": {
      "appearance": "Bold technical hand-lettered title",
      "weight": "Heavy, structured",
      "case": "Uppercase preferred",
      "color": "Off-white ink"
    },
    "subheadings": {
      "appearance": "Compact technical labels",
      "decoration": "Brackets, callout tags, thin underlines"
    },
    "body_text": {
      "appearance": "Clean condensed sans-serif",
      "spacing": "Phone-readable; no cramped lines"
    },
    "annotations": {
      "style": "Engineering callouts with arrows and note bubbles",
      "purpose": "Define terms and show cause→effect"
    }
  },
  "layout_architecture": {
    "canvas": {
      "framing": "NO BORDER, NO FRAME",
      "boundary": "Full-bleed vertical 9:16",
      "containment": "The infographic IS the image"
    },
    "structure": {
      "type": "Blueprint grid alignment + modular boxes",
      "sections": "Clear numbered boxes (circled numbers)",
      "flow": "Top-to-bottom pipeline, left-to-right within rows",
      "breathing_room": "Clean gutters; avoid dense clusters"
    },
    "section_treatment": {
      "borders": "Thin technical rounded rectangles or sharp-corner boxes",
      "separation": "Clear spacing and callout connectors",
      "numbering": "Small circled numbers blueprint style"
    },
    "visual_flow_devices": {
      "arrows": "Straight callout arrows",
      "connectors": "Dotted circuit paths and node lines",
      "progression": "Input → Process → Output"
    }
  },
  "information_hierarchy": {
    "levels": {
      "primary": "Large title + central schematic anchor illustration",
      "secondary": "Subheads + icons + tag labels",
      "tertiary": "Bullets + short annotations"
    },
    "emphasis_techniques": {
      "color_highlights": "Cyan underline behind key words",
      "boxing": "Definitions in tag boxes",
      "icons": "Warning triangle for risks, checkmarks for actions"
    }
  },
  "decorative_elements": {
    "badges_and_labels": {
      "style": "Blueprint tags, measurement-like labels",
      "use": "Definitions, risks, steps"
    },
    "connective_tissue": {
      "arrows": "Drafting arrows",
      "lines": "Grid lines, dotted paths",
      "brackets": "Curly braces grouping related points"
    },
    "ambient_details": {
      "small_icons": "Tiny nodes, calibration marks (very minimal)",
      "texture": "Blueprint grid faint and subtle"
    }
  },
  "authenticity_markers": {
    "hand_made_quality": {
      "line_variation": "Natural thickness changes",
      "alignment": "Slightly imperfect micro-alignment",
      "overlap": "Minor overlaps acceptable"
    }
  },
  "technical_quality": {
    "resolution": "High-resolution for phone and print",
    "clarity": "Text readable, diagrams clear",
    "balance": "Even distribution of visual weight",
    "completeness": "Finished, clean, professional"
  },
  "content_guidance": {
    "explanation": "Write like a technical explainer. Define the concept, show a simple mechanism (how it works), highlight common misconceptions, then give a practical checklist. Keep each box to a subheading plus 2–4 bullets for phone readability.",
    "writing_rules": [
      "Each box: 1 label + 2–4 bullets",
      "Prefer cause→effect language",
      "Include at least one 'How to spot it' or 'How to reduce risk' section",
      "Avoid hype; keep it precise and actionable"
    ]
  },
  "avoid": [
    "ANY frame, border, or edge decoration",
    "Cute or childish characters",
    "Neon cyber overload",
    "Overly dense wiring/lines",
    "Tiny unreadable text",
    "Sterile vector perfection"
  ]
}
```

</details>

<details><summary><b>Board Game Box Cover Art Director</b></summary>

```text
Act as the art director of a small independent board game publisher. You turn a game concept into a box cover art brief that an illustrator, or an AI image generator, can follow without guessing.

Game details:
- Working title: ${title:Sky Orchard Merchants}
- One-sentence pitch: ${pitch:A cozy cooperative trading game where players crew wooden airships that harvest fruit from floating orchard islands and trade it between sky towns.}
- Player count and age: ${players:1 to 4 players, ages 10 and up}
- Play time and weight: ${weight:45 minutes, light to medium strategy}
- Mood in three words: ${mood:whimsical, warm, adventurous}
- Preferred art style: ${style:hand-painted gouache with visible brush texture}
- Box shape: ${box:square 1:1}
- Things to avoid: ${avoid:dark or scary imagery, violence, cluttered compositions}

Produce the brief in this order:

1. Shelf test. In two sentences, say what a shopper should feel and understand about this game from three meters away, and what should make them pick the box up.

2. Focal point and story moment. Choose one moment from the game to show, the main subject, and what is happening. Explain why this moment sells the game better than two alternatives you considered.

3. Composition. Describe the layout for the box shape: where the title area sits (keep it calm and free of detail), where the focal point sits, the depth layers (foreground, middle, background), and how the silhouette stays readable at thumbnail size on an online store.

4. Characters and props. List the characters, creatures, and key props, with one detail each that hints at a game mechanic (for example, baskets of fruit hint at collecting sets).

5. Lighting and palette. Time of day, light direction, and a palette of four or five named colors that fit the mood and stand out on a shelf of other games.

6. Style guidance. Medium, brushwork, level of detail, and two or three broad style references described in words (eras or techniques, never living artists' names).

7. Accessibility and age check. Confirm that the cover is appropriate for the age range, avoids anything on the avoid list, and doesn't rely on color alone to be readable.

8. Final image prompt. Write one paragraph of 120 to 180 words that an AI image generator can use directly. It must include the subject, the action, the setting, the lighting, the palette, the style, the composition with the title space, the aspect ratio, and the line "No text, no letters, no logos, no borders." Do not put the game title inside the image; the title is added later by a designer.

9. Variations. Give two one-line variations of the final prompt: one with a different time of day and one with a different focal character.

Keep the whole brief practical and specific. If a game detail is missing or vague, make a sensible choice and note it in one line at the top under "Assumptions".
```

</details>

<details><summary><b>Booklet Cover Design Program</b></summary>

```text
Create a professional program to create a booklet cover in different colors with the possibility of adding images to complement the painting that contribute to attracting the reader's attention, distributed in a superior format with the choice of type, colors and Font Format for the product name ""brief summary" writer ""and serial number"
```

</details>

<details><summary><b>Bookstore Aisle Portrait</b></summary>

```text
{
  "category": "BOOKSTORE_AISLE_ARTSY",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Preserve the exact identity from the reference image (face geometry, features, skin tone, marks). Adult 21+ only. No beautification or identity changes."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking (must match reference).",
    "hair": {
      "color": "Match reference exactly.",
      "style": "Loose waves tucked behind one ear",
      "texture": "Real strands; slight frizz; flyaways visible",
      "movement": "Hair rests naturally on shoulders"
    },
    "face": {
      "eyes": "Exact reference eyes; thoughtful gaze; natural catchlights",
      "skin_details": "Pores visible, realistic tone variation",
      "micro_details": "Preserve all reference marks precisely"
    },
    "clothing": {
      "outfit": "Minimal black coat or cardigan over a neutral top (no logos/text).",
      "fabric": "Wool/knit texture visible, slight wrinkles at elbows"
    },
    "accessories": {
      "jewelry": ["Small silver hoops"],
      "props": ["One hardcover book with no readable title (blur/spine turned away)"]
    }
  },
  "pose": {
    "type": "Candid browsing",
    "orientation": "Half-body",
    "head_position": "Chin slightly down, eyes up toward camera",
    "hands": "One hand holding a book near chest; other hand touching a shelf edge (hands correct)",
    "gaze": "Near-direct eye contact, calm and confident",
    "expression": "Soft neutral with micro-smile"
  },
  "setting": {
    "environment": "Bookstore aisle",
    "background_elements": [
      "Shelves of books with spines turned away or blurred (NO readable text)",
      "Warm indoor lighting",
      "Soft depth layers down the aisle"
    ],
    "depth": "Shallow DOF: face sharp, shelves softly blurred"
  },
  "camera": {
    "shot_type": "Half-body portrait",
    "angle": "Eye level or slightly above",
    "focal_length_equivalent": "35-50mm pro OR 26mm phone",
    "framing": "4:5, asymmetrical with leading lines from shelves",
    "focus": "Eyes sharp, hands reasonably sharp, background soft"
  },
  "lighting": {
    "source": "Warm overhead bookstore lights + soft fill",
    "direction": "Gentle top/side",
    "highlights": "Soft highlights on eyes and cheekbones",
    "shadows": "Subtle under-chin shadow, realistic contrast"
  },
  "mood_and_expression": {
    "tone": "Artsy, calm, 'quiet luxury'",
    "atmosphere": "Cozy and intimate, candid"
  },
  "style_and_realism": {
    "style": "Photoreal lifestyle/editorial",
    "fidelity": "High detail, no airbrushing"
  },
  "colors_and_tone": {
    "palette": "Warm browns + neutral blacks + creamy highlights",
    "white_balance": "Warm indoor",
    "contrast": "Medium"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Mild indoor grain",
    "mode_variants": {
      "amateur": "Slightly crooked handheld framing, mild noise, imperfect WB",
      "pro": "Cleaner exposure, controlled highlights, crisp micro-contrast"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_book_titles": true
  },
  "negative_prompt": [
    "readable text", "logos", "watermark",
    "identity drift", "face morphing",
    "plastic skin", "over-smoothing",
    "extra fingers", "warped hands",
    "cgi", "cartoon", "anime"
  ]
}
```

</details>

<details><summary><b>Branded Social Post Image Assistant</b></summary>

```text
Act as an Image Generation Assistant for impactful posts. Your task is to create visually striking images that adhere to a standard visual identity for social media posts.

You will:
- Use the primary background color: ${primary_background:#0a1128}
- Implement the background texture: Subtle technological circuit grid (${accent_blue_cyan:#00ffff})
- Element ${elemento} will be in the ${position: center} of image.
- Highlight the main visual element with accent colors: ${accent_green:#ebf15b} and ${accent_blue_cyan}
- Incorporate the brand's logo and tagline where applicable
- Ensure the image aligns with the brand's overall aesthetic

Design images that evoke emotion and engagement.

Rules:
- Maintain consistency with the brand's color palette and fonts
- Avoid overcrowding the image with too much text or elements
- Follow the specified dimensions for each social media platform

Variables you can customize:
- ${brandName: Suzuki Intelligence & Innovation} for the brand identity
- ${message: ""} for the text to be included on the image
- ${accent_green} for additional accent color options
- ${elemento} for the main element in the image
```

</details>

<details><summary><b>Broken Medieval Knight</b></summary>

```text
{
  "subject_and_scene": {
    "main_subject": "A broken, soul-crushed medieval knight kneeling in defeat, his eyes glazed with tears and trauma; his shattered armor is caked in dried mud and fresh blood. His face is a canvas of scars, sweat, and grime, reflecting the harrowing loss of a fallen kingdom.",
    "action": "Gripping his sword's hilt with trembling hands as if it's the only thing keeping him from collapsing; his chest heaving in rhythmic, heavy gasps of despair.",
    "environment": "A desolate, windswept battlefield at the edge of an ancient forest; a hazy, ethereal fog rolls over the ground, partially obscuring the distant, smoldering ruins of a castle. Petals or embers are caught in the wind, drifting past his face."
  },
  "cinematography": {
    "camera_model": "Sony Venice 2",
    "sensor_type": "Full Frame",
    "shot_type": "Medium Close-Up (Vertical composition focusing on the knight's torso and face, but keeping his kneeling posture visible)",
    "camera_angle": "Low Angle (Slightly tilted Dutch Angle to evoke a sense of psychological instability and sorrow)",
    "movement": "Slow 'Dolly In' combined with a 'Snorricam' effect to make the knight's struggle feel claustrophobic and intensely personal"
  },
  "optics": {
    "lens_type": "Anamorphic (to create emotional 'dream-like' fall-off and dramatic flares)",
    "focal_length": "50mm (providing a natural but emotionally focused perspective)",
    "aperture": "f/1.4 (Extremely shallow depth of field, blurring everything but his tear-filled eyes)",
    "shutter_effects": "180-degree shutter for natural motion blur on the wind-blown debris, emphasizing the 'slow-motion' feeling of grief"
  },
  "lighting_design": {
    "setup": "Split Lighting to hide half of his face in darkness, symbolizing his internal conflict and loss",
    "style": "Low-Key with high emotional contrast",
    "atmospheric_light": "Blue Hour fading into darkness, with a single warm 'God Ray' piercing through the clouds to highlight his face like a spotlight",
    "color_temperature": "Ice-cold Blue tones for the environment, contrasting with the Warm, flickering orange light from distant fires"
  },
  "color_and_post": {
    "film_stock": "Kodak Portra 160 (Pulled 1 stop for lower contrast and softer, more melancholic skin tones)",
    "color_grading": "Bleach Bypass (Desaturated colors, heavy blacks, emphasizing the grittiness and sorrow)",
    "analog_artifacts": "Heavy Halation around the highlights and subtle 'Gate Weave' to mimic a vintage 35mm war film aesthetic"
  },
  "rendering_and_tech": {
    "engine": "Octane Render",
    "advanced_tech": "Highly detailed skin pore texture with Ray Traced tear droplets and wet blood reflections",
    "specs": {
      "aspect_ratio": "9:16 (Vertical Cinema)",
      "resolution": "8K Photorealistic"
    }
  },
  "directorial_style": "Denis Villeneuve (Atmospheric haze and overwhelming silence) mixed with Mel Gibson (Gritty, visceral realism of war)"
}
```

</details>

<details><summary><b>Building the Great Pyramid</b></summary>

```text
Hyper realistic 4K cinematic scene from ancient Egypt during the construction of the Great Pyramid. The pyramid is half built and clearly unfinished, its massive silhouette rising but incomplete. Colossal stone blocks move along engineered water canals on heavy rafts, guided by ropes, ramps and wooden structures. Hundreds of workers, coordinated movement, dust in the air, subtle mist from the water. Epic wide-angle composition, dramatic skies, soft golden light cutting through dust, long shadows, cinematic scale. The atmosphere should feel monumental and historic, as if witnessing a civilization shaping the future. The person from the uploaded image appears as the main leader, positioned slightly elevated above the scene, commanding presence, confident posture, intense but realistic expression, historically accurate Egyptian-style clothing. Ultra-detailed textures, lifelike skin, documentary realism, depth of field, no fantasy elements, pure photorealism.
```

</details>

<details><summary><b>Butterfly Metamorphosis Video</b></summary>

```text
[00:00 - 00:03]
Macro 100mm detail of a green chrysalis hanging from a twig, Golden Hour Cinematic lighting, the cocoon vibrates and rapidly turns translucent revealing folded orange and black wing patterns inside, Hyper-Realistic 8K, microscopic organic textures, static observational long take. --ar 9:16

[00:03 - 00:06]
Macro 100mm timelapse of a Monarch butterfly emerging from its shell, wet wings unfurling and hardening instantly, sharp wing scale details, warm bokeh forest background, Golden Hour lighting, Hyper-Realistic 8K, cinematic film quality, static observational long take. --ar 9:16
```

</details>

<details><summary><b>Cafe Portrait Prompt</b></summary>

```text
{
  "subject": {
    "description": "A young, attractive blonde woman with sleeked-back hair styled into a loose side braid, resting her right cheek on her hand and looking directly at the camera with a calm, natural, slightly pensive expression. Her facial features are balanced and aesthetically pleasing, with clear and smooth skin.",
    "position": "Seated at a wooden table in a cafe, facing the camera.",
    "pose": "Head resting gently on right hand, elbow on table; left arm relaxed on the table surface.",
    "expression": "Calm, natural, slightly pensive, soft gaze.",
    "clothing": {
      "top": "Black spaghetti strap tank top with a minimal, fitted look."
    },
    "accessories": "Multiple small gold hoop earrings, thin rings on fingers, minimal jewelry, a small script tattoo on the inner left forearm (text: 'no pain').",
    "hair": "Blonde hair, neatly slicked back and styled into a loose braid falling over the left shoulder with slight natural flyaways.",
    "skin_details": "Clear, smooth, healthy-looking skin with subtle natural texture, minimal blemishes, no heavy retouching"
  },
  "scene": {
    "description": "Interior of a modern cafe/bar during daytime. The bar counter and shelves are clearly visible, filled with liquor bottles and glassware, but the space feels clean and not overcrowded.",
    "location": "A modern cafe in Istanbul, Turkey.",
    "setting": "Indoor cafe with daylight.",
    "background_elements": "Bar shelves with bottles, glassware, wooden textures, large windows with daylight entering, very few or no visible people; if present, only soft blurred silhouettes without distinguishable features.",
    "lighting": "Soft natural daylight coming from windows combined with gentle indoor ambient light.",
    "atmosphere": "Relaxed, calm, modern urban setting, not overly busy."
  },
  "technical_details": {
    "shot_type": "Medium close-up.",
    "perspective": "Eye-level, natural handheld perspective as if taken by another person sitting at the table.",
    "focal_length": "Smartphone wide lens (~26mm equivalent).",
    "depth_of_field": "Shallow depth of field, subject sharply in focus, background softly blurred with natural bokeh.",
    "composition": "Subject slightly off-center, balanced composition with vertical lines from shelves and soft background structure.",
    "colors": "Neutral and natural tones, warm wood browns, soft gold from jewelry, realistic color balance.",
    "camera_type": "iPhone 13 rear camera",
    "camera_behavior": "Natural smartphone processing, slight edge sharpening, realistic HDR, no artificial filters",
    "resolution": "Standard mobile photo quality, not ultra sharp, slightly softened details",
    "image_characteristics": {
      "grain": "Very subtle fine digital grain",
      "dynamic_range": "Balanced HDR with controlled highlights and shadows",
      "sharpness": "Moderate, not overly crisp",
      "compression": "Minimal compression artifacts, close to original capture"
    }
  },
  "constraints": {
    "background_people": "Avoid clearly visible or detailed people; allow only indistinct blurred shapes",
    "focus_priority": "Face must be the sharpest element",
    "avoid": "Artificial faces in background, over-processed skin, Instagram-style filters, excessive sharpness, cinematic DSLR look"
  }
}
```

</details>

<details><summary><b>Cafe Window Seat Close-up</b></summary>

```text
{
  "category": "CAFE_WINDOW_SEAT_CLOSEUP",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Loose waves tucked behind one ear",
      "texture": "Individual strands visible, slight frizz",
      "movement": "A few strands fall forward naturally"
    },
    "face": {
      "shape": "Soft oval",
      "eyes": "Expressive, warm, natural wetline detail",
      "makeup": "Natural 'clean' makeup, subtle liner, soft blush",
      "skin_details": "Pores visible, natural sheen, no airbrush",
      "micro_details": "Fine baby hairs near forehead"
    },
    "clothing": {
      "top": "Casual knit or fitted tee (no text)",
      "texture": "Visible knit weave, realistic folds"
    },
    "accessories": {
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Candid portrait at a table",
    "orientation": "Close-up/half-body",
    "head_position": "Slight tilt",
    "hands": "One hand near chin, fingers relaxed and anatomically correct",
    "gaze": "Near-direct eye contact, soft smile",
    "posture": "Relaxed shoulders leaning slightly forward"
  },
  "setting": {
    "environment": "Cozy cafe by a window",
    "background_elements": [
      "Ceramic cup on table",
      "Condensation on glass",
      "Tiny crumbs on plate (subtle realism)",
      "Background patrons blurred (no identifiable faces)"
    ],
    "depth": "Shallow DOF with warm bokeh"
  },
  "camera": {
    "shot_type": "Portrait",
    "angle": "Slightly above eye level (casual handheld feel)",
    "focal_length_equivalent": "26mm phone OR 50mm pro portrait",
    "framing": "4:5, face and shoulders dominate frame",
    "focus": "Eyes sharp, background softly blurred"
  },
  "lighting": {
    "source": "Diffused window daylight + warm interior ambient",
    "direction": "Soft side light shaping cheekbones",
    "highlights": "Natural highlights on nose bridge and lips",
    "shadows": "Gentle shadow under chin, realistic contrast",
    "quality": "Soft, flattering, cozy"
  },
  "mood_and_expression": {
    "tone": "Warm, approachable, intimate",
    "expression": "Soft smile, lively eyes",
    "atmosphere": "Tactile, everyday candid"
  },
  "style_and_realism": {
    "style": "Photorealistic IG lifestyle",
    "fidelity": "High detail (lashes, pores, hair strands)",
    "imperfections": "Natural noise, slight imperfect WB allowed"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild phone-like grain in shadows",
    "motion_blur": "None on face; minimal allowed in background"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "over-smoothing", "plastic skin", "uncanny eyes",
    "bad hands", "extra fingers",
    "readable text", "logos", "watermark",
    "cgi", "cartoon", "anime"
  ]
}
```

</details>

<details><summary><b>Candid Bedtime Selfie</b></summary>

```text
{
  "meta": {
    "aspect_ratio": "9:16",
    "quality": "raw_photo, uncompressed, 8k",
    "camera": "iPhone 15 Pro Max front camera",
    "lens": "23mm f/1.9",
    "style": "influencer candid bedtime selfie, clean girl aesthetic, youthful natural beauty, ultra-realistic",
    "iso": "800 (clean, low noise)"
  },
  "scene": {
    "location": "Luxury bedroom interior",
    "environment": [
      "high thread count white or cream bedding",
      "fluffy down pillows",
      "soft warm ambient light from background",
      "hint of a silk headboard"
    ],
    "time": "Late night / Bedtime",
    "atmosphere": "intimate, relaxing, soft luxury, innocent"
  },
  "lighting": {
    "type": "Phone screen softbox effect",
    "key_light": "Soft cool light from phone screen illuminating the face center, enhancing skin smoothness",
    "fill_light": "Warm, dim bedside lamp in background creating depth",
    "shadows": "Very gentle, soft shadows",
    "highlights": "Creamy, dewy highlights on the nose bridge and cheekbones (hydrated glow)"
  },
  "camera_perspective": {
    "pov": "Selfie (arm extended)",
    "angle": "High angle, slightly tilted head (flattering portrait angle)",
    "framing": "Close-up on face and upper chest",
    "focus": "Sharp focus on eyes and lips, soft focus on hair and background"
  },
  "subject": {
    "demographics": {
      "gender": "female",
      "age": "24 years old",
      "ethnicity": "Northern European (fair skin)",
      "look": "Fresh-faced, youthful model off-duty"
    },
    "face": {
      "structure": "Symmetrical soft features, youthful plump cheeks, defined but soft jawline, delicate nose",
      "skin_texture": "smooth, youthful complexion, 'glass skin' effect (ultra-hydrated and plump), porcelain/pale skin tone, extremely fine texture with minimal visible pores, radiant healthy glow, naturally flawless without heavy texture",
      "lips": "Naturally plush lips, soft pink/rosy natural pigment, hydrated balm texture",
      "eyes": "Large, expressive piercing blue eyes, clear bright iris detail, long natural dark lashes, looking into camera lens",
      "brows": "Naturally thick, groomed, soft taupe color matching hair roots"
    },
    "hair": {
      "color": "Cool-toned honey blonde with platinum highlights",
      "style": "Chic blunt bob cut, chin-length, slightly tousled on the pillow but maintaining shape",
      "texture": "Silky, healthy shine, fine soft hair texture"
    },
    "expression": "Soft, innocent, confident but sleepy, slight gentle smile"
  },
  "outfit": {
    "headwear": {
      "item": "Luxury silk sleep mask",
      "position": "Pushed up onto the forehead/hair",
      "color": "Champagne gold or blush pink",
      "texture": "Satin sheen"
    },
    "top": {
      "type": "Silk or satin pajama camisole",
      "color": "Matching champagne or soft white",
      "details": "Delicate lace trim at neckline, thin straps, fabric draping naturally over collarbones"
    }
  },
  "details": {
    "realism_focus": [
      "Intense dewy moisturizer sheen on skin",
      "Realistic lip balm texture",
      "Reflection of phone screen in the clear blue pupils",
      "Softness of the fabrics",
      "Focus on dewy hydration sheen rather than heavy skin texture"
    ],
    "negative_prompt": [
      "heavy makeup",
      "foundation",
      "cakey skin",
      "plastic skin",
      "airbrushed",
      "acne",
      "blemishes",
      "dark hair",
      "brown eyes",
      "long hair",
      "large pores",
      "rough texture",
      "wrinkles",
      "aged skin",
      "mature appearance"
    ]
  }
}
```

</details>

<details><summary><b>Candid Street Photo at Golden Hour</b></summary>

```text
Candid street photo in Tehran, 2026, golden hour, shallow depth of field, crowd blurred behind. Iranian woman glancing off-frame; both brows flicked up once, eyes darting to the exit, a micro widening of the eyes — the secret signal "let's leave, now". Below the frame, a hand-scribbled bordered box, ballpoint handwriting: "بریم؟".
```

</details>

<details><summary><b>Candlelit Restaurant Close-up</b></summary>

```text
{
  "category": "CANDLELIT_RESTAURANT_CLOSEUP",
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Loose, softly styled",
      "texture": "Real strands, gentle shine"
    },
    "face": {
      "eyes": "Soft eye contact, warm highlights",
      "makeup": "Natural glam, subtle liner",
      "skin_details": "Real pores, warm glow from candle"
    },
    "clothing": {
      "outfit": "Simple elegant black top/dress (no logos)"
    },
    "accessories": {
      "jewelry": ["Silver hoops"]
    }
  },
  "pose": {
    "type": "Close-up seated",
    "orientation": "Face toward camera",
    "hands": "One hand supporting chin, fingers relaxed",
    "gaze": "Direct eye contact",
    "expression": "Calm confident micro-smile"
  },
  "setting": {
    "environment": "Restaurant table",
    "background_elements": [
      "Candle flame bokeh",
      "Glass reflections",
      "Soft background blur (no readable signage)"
    ],
    "depth": "Face sharp, background creamy"
  },
  "camera": {
    "shot_type": "Close-up portrait",
    "angle": "Eye-level",
    "focal_length_equivalent": "50-85mm pro feel or 26mm phone variant",
    "framing": "4:5, tight crop",
    "focus": "Eyes extremely sharp"
  },
  "lighting": {
    "source": "Candle + warm ambient",
    "direction": "Warm side/front",
    "highlights": "Soft specular on lips and eyes",
    "shadows": "Gentle, flattering"
  },
  "mood_and_expression": {
    "tone": "Intimate, elegant, confident",
    "atmosphere": "Warm, cinematic"
  },
  "style_and_realism": {
    "style": "Photoreal IG portrait",
    "imperfections": "Slight grain acceptable"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild low-light grain"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "fake flames", "cgi",
    "plastic skin", "over-smoothing",
    "extra fingers", "warped hands",
    "readable text", "logos", "watermark"
  ]
}
```

</details>

<details><summary><b>Car Interior Portrait</b></summary>

```text
A realistic, ultra-high-quality 8K photo shot on an iPhone 16 Pro Max in a 3:4 aspect ratio.

Subject & pose: A young woman is sitting inside a premium car. She is slightly leaning back against the seat, with one arm raised and bent at the elbow, her hand resting behind her head. Her head is gently tilted to one side, and she looks directly into the camera with a soft, confident, relaxed expression and a subtle closed-lip half smile.

Clothing: She wears a fitted sage green (muted olive) long-sleeve ruched dress with pronounced horizontal draping and gathered texture across the torso.

Hair: Long, straight, silky hair with a center part. Thick strands cascade naturally over her left shoulder onto her chest, with a soft natural shine and warm highlights.

Makeup: Elegant daytime makeup featuring sharp black cat-eye eyeliner, smooth glowing skin, and matte nude-pink lips.

Lighting & color: Soft, diffused daylight enters from the side and slightly from the front, creating gentle shadows while emphasizing the texture of the fabric and the shine of her hair. The color palette blends warm beige-green tones with a deep dark interior.

Camera & composition: Medium close-up portrait, photographed from a slightly low angle with a subtle tilt, creating the feeling of a natural selfie or a candid shot from the passenger seat.

Background & atmosphere: A relaxed, sophisticated, stylish, and cozy mood. The background is a blurred dark luxury car interior with black leather seats and refined trim details, keeping the full attention on the woman.

Do not change the girl's facial features, eye shape, eyebrows, nose, or lips. Maintain 100% facial resemblance.
```

</details>

<details><summary><b>Casual Girls Night Selfie</b></summary>

```text
Amateur girls’ night selfie, very casual and imperfect, 1:1 aspect ratio. The image is shot directly from the FRONT CAMERA of a cheap, older smartphone: we see only what the phone sees, we DO NOT see any phones or cameras in the frame.

Three adult women sit close together on an old, comfy couch in a small apartment living room at night. They are wearing simple home clothes and sweatpants, like a real chill night in.

Center woman: medium skin tone, long dark hair, wearing a plain black sleeveless top and light grey sweatpants. She sits in the middle of the couch, one leg tucked under her, the other bent. Her body leans slightly toward the left, head tilted a bit, smiling softly toward the camera, relaxed and unposed.

Left woman: light skin and straight, light-brown hair, wearing a long-sleeve black top and light grey sweatpants. She leans in very close to the center woman, almost touching shoulders, making a big exaggerated kissy face toward the camera, lips puckered, eyebrows slightly raised. Because this is a selfie POV, she appears slightly closer and a bit larger from perspective, like someone near the phone.

Right woman: light skin and wavy blonde hair, wearing a dark long-sleeve top and black leggings. She leans into the group from the right, head tilted, smiling with her tongue out in a playful, goofy expression, eyes squinting slightly from laughter. All three look like close friends having fun, not models.

Environment: cozy, slightly messy living room. Behind them, a simple floor lamp with a warm bulb lights the wall. In the background on one side, a TV screen is visible with a paused movie scene (soft, abstract shapes, no recognizable faces or logos). On a low wooden coffee table in front of the couch (visible at the bottom of the frame) are open pizza boxes with half-eaten slices, a bag of chips, a soda can and a sparkling water can, a few crumbs, and a phone lying flat on the table. The room has string lights or fairy lights along one wall, giving a warm, imperfect glow. The apartment and furniture look normal and slightly worn, not like a studio set.

Camera and style: VERY IMPORTANT – this image should look like a real, bad selfie, NOT a professional photo. It is captured with a basic smartphone front camera in AUTO mode. Direct, slightly harsh phone flash from near the lens, with faces a little overexposed and shiny in some spots. Visible digital noise and grain in the darker parts of the room. Mixed lighting: warm yellow from the lamp and a cooler bluish cast from the TV, giving slightly uneven white balance. Focus is soft, not razor sharp, with a tiny bit of motion blur in hair and hands. Edges of the frame have mild vignetting and slight wide-angle distortion, like a cheap front camera. The composition is a little crooked and off-center; some pizza boxes and objects are cut off at the edges. Overall, the picture should feel like an unedited, spontaneous selfie sent to a group chat.

Constraints: there are EXACTLY THREE women in the frame and NO other people. The only camera is the phone we are looking through, so no extra hands, no extra phones, no mirror showing the photographer, no second photographer at the edge of the frame. No reflections of another camera. Just the three friends on the couch and the messy coffee table.

Negative prompt: professional studio, pro lighting, softboxes, rim light, cinematic atmosphere, commercial photoshoot, perfect color grading, HDR, strong depth of field blur, bokeh, high-end DSLR or lens, ultra-clean fashion image, symmetrical composition, influencer preset, heavy airbrushed skin, filters, hotel room, staged set, extra people, extra arms, extra hands, any additional phones or cameras in the frame, mirrors showing another photographer, text, logo, watermark, surreal glitches, underage appearance.
```

</details>

<details><summary><b>Casual Portrait of a Young Woman</b></summary>

```text
{
    "subject": {
      "appearance": "Young woman with mixed ethnicity features, fair skin, and long, layered dark brunette hair falling loosely around her shoulders. Natural, fresh-faced makeup look with groomed brows and soft pink lips.",
      "outfit": "Simple black spaghetti-strap camisole or tank top.",
      "environment": "Bright, airy bedroom setting. Lying on a bed with crisp white duvet/sheets. A grey upholstered headboard is visible behind. White sheer curtains covering a window in the background, letting in soft light."
    },
    "technical_style": "Social media selfie aesthetic, triptych or collage style, soft focus, high-key lighting, intimate and casual atmosphere."
  },
  "pose_specs": {
    "body_position": "Prone position (lying on stomach) on the bed, facing the camera. Shoulders and upper chest lifted off the mattress.",
    "arms": "Elbows resting on the bed to support the upper body. One hand (right hand) brought up to touch the face—fingers resting gently on the chin or cheek.",
    "head": "Tilted slightly, creating a playful and engaging angle.",
    "expression": "Varied playful expressions: 1) A soft, sweet smile with direct eye contact. 2) A candid laugh looking away to the side. 3) A playful wink with a scrunched nose.",
    "framing": "Close-up portrait framing, cutting off at the shoulders/chest."
  },
  "camera_settings": {
    "viewpoint": "Eye-level relative to the subject on the bed (low angle relative to the room).",
    "focal_length": "24mm to 35mm (Front-facing smartphone camera focal length).",
    "aperture": "f/2.0 to f/2.8 (Soft background blur to keep focus on the face).",
    "shutter_speed": "1/100s",
    "iso": "200",
    "composition": "Centered subject, intimate proximity to the lens."
  },
  "lighting_setup": {
    "type": "Natural Window Light.",
    "qualities": "Soft, diffused, wrapping light.",
    "direction": "Side lighting coming from the window (left side of the frame), illuminating the face evenly while creating very soft, flattering modeling shadows on the opposite side.",
    "color_temperature": "Daylight balanced (approx 5500K), clean white tones."
  }
}
```

</details>

<details><summary><b>Cedar Observatory Cabin Under the Milky Way</b></summary>

```text
A small cedar cabin with a white rotating telescope dome on its roof sits on a rocky mountain ridge under a vivid Milky Way arching across the night sky. The cabin is a compact single-story box clad in vertical warm-brown cedar boards, with a low dark-metal shed roof, a matte white hemispherical dome on the left end with its narrow slit half open and a telescope tube just visible inside, and a black steel stovepipe chimney on the right end with a thin curl of smoke. One wide rectangular window on the front glows dim warm amber, and a small wooden deck with a simple railing faces the valley. A narrow gravel path lined with flat stones leads up to the deck. Scattered dwarf pines and patches of old snow surround the cabin, and a jagged ridge silhouette fades into a deep valley of distant peaks. Thousands of sharp stars, the bright galactic core in soft violet and gold. Photorealistic long-exposure astrophotography, wide-angle 16:9, low camera angle, no light pollution, no people, no text.
```

</details>

<details><summary><b>Cedar Observatory Cabin Warm Interior</b></summary>

```text
Interior room of a small cedar observatory cabin at night: walls and ceiling of warm vertical cedar boards matching the exterior, a wooden desk with open star charts and a red-glowing desk lamp, a telescope eyepiece and black telescope tube angled up through a ceiling hatch into the white hemispherical dome above, and a small black cast-iron wood stove with orange firelight and a black steel stovepipe. A worn leather armchair with a wool blanket sits between the desk and the stove; a wall shelf holds eyepiece cases and a brass star globe. The camera stands inside looking toward two rectangular front windows that glow amber from inside and frame a jagged mountain ridge, dwarf pines, old snow, and a bright Milky Way beyond. Lighting mixes dim red task light and warm firelight; the windows are cooler and darker outside. Photorealistic interior photography, 24mm lens, 16:9, cozy and quiet, no people, no text.
```

</details>

<details><summary><b>Cedar Treehouse in an Old Oak, Summer</b></summary>

```text
Photoreal architectural photograph of a small timber treehouse retreat built into a single huge old oak tree, standing in a sloping summer meadow at the edge of a beech forest, seen from the meadow at the front left, camera at standing eye level (1.6 m) about 12 m away, 35mm lens, vertical lines straight, 16:9 landscape composition with the whole tree and treehouse in frame. The oak has a massive grey, deeply furrowed trunk about 1.2 m wide that splits into three thick main limbs above the roof, with a full, dense green summer canopy spreading over the treehouse. A square timber deck about 3.5 m above the ground wraps around the trunk, the trunk rising through the deck behind the cabin; the deck is held by two round natural timber posts at the front corners and four diagonal timber knee braces angled from the trunk. On the deck stands a compact cabin about 3 by 4 m, clad in vertical cedar boards weathered to a warm honey brown, under a steep gable roof of dark green standing-seam metal with the gable end facing the camera. Front wall: a round porthole window high in the gable apex; a large black-framed picture window that wraps around the front left corner of the cabin; and a teal-blue Dutch door, split into upper and lower halves, on the right half of the front wall, with a small black metal lantern beside it. A slim black stove chimney pipe rises from the right side of the roof. The deck has a railing of cedar posts with three horizontal natural ropes between them, warm globe string lights looped along the railing (off in daylight), and two mustard-yellow folding wooden deck chairs at the front. A straight timber staircase with a mid-height landing rises along the right side of the deck from the ground to the front right corner. On the left, a rope swing with a plain wooden seat hangs from a low horizontal oak limb. At the base of the tree: ferns, moss, a few large stones, and a pale gravel path curving through the meadow grass to the foot of the stairs, with wildflowers in white and purple. Warm late-afternoon sunlight from the left, dappled light through the leaves on the cedar walls, soft shadows, clear blue sky glimpsed between branches. Palette of honey cedar, moss green, teal blue, mustard yellow, charcoal black, and oak grey. Realistic wood grain, metal, rope, and bark textures, high-end architecture magazine photography, calm and inviting mood. No people, no text, no logos, no signs.
```

</details>

<details><summary><b>Cedar Treehouse on a Snowy Winter Evening</b></summary>

```text
Photoreal architectural photograph of the same small cedar treehouse cabin and old oak from step 2, now on a snowy winter evening at blue hour, seen from the meadow at the front right instead of from the left, camera at standing eye level (1.6 m) about 14 m away, 35mm lens, vertical lines straight, 16:9 landscape composition with the oak trunk and the whole cabin in frame. Keep every fixed design detail identical to step 2. Host tree: one huge old oak with a massive grey, deeply furrowed trunk and wide flared root buttresses spreading over the ground, splitting into several thick limbs that arch over the cabin roof; it now stands on the left side of the frame, completely bare, its dark branches lined with fresh snow against a deep blue sky. The cabin stands right beside the trunk, to its right, on a low timber deck raised about 0.6 m on short square timber posts. Cabin: a compact two-storey-high single room clad in vertical cedar boards in bright honey brown, under a steep gable roof of dark green standing-seam metal with one small dark box vent on the roof slope, now carrying a soft layer of snow; the gable end faces the camera on the right, plain vertical cedar boards with a narrow green fascia. The long side wall, now seen at an angle on the left, has a row of large dark-framed floor-to-ceiling glass windows and a glass door, all glowing warm amber from inside. The timber deck wraps around the front and the gable side, with simple timber railings of square posts and thin vertical balusters, snow along the top rail, and a wooden slatted lounge chair on the deck dusted with snow. A wide, straight timber staircase with matching railings descends from the front right corner of the deck down to the meadow, now in the right foreground, its treads covered in fresh snow with a line of footprints. Warm globe string lights hang along the deck railing, glowing. At the base: smooth snow over the meadow and around the oak's roots, a bare deciduous forest fading into blue dusk behind. Cool blue-hour light on the snow mixed with warm amber light from the windows and string lights. Palette of honey cedar, dark green, charcoal black window frames, oak grey, warm amber, and snow white. Realistic wood, metal, glass, bark, and snow textures, architecture magazine photography, quiet mood. No people, no text, no logos, no signs.
```

</details>

<details><summary><b>Ceramic Pour Over Coffee Set Hero Shot</b></summary>

```text
Product hero photograph of a matte sand-beige ceramic pour-over coffee set: a ribbed dripper on a clear glass carafe with a thin ribbon of steam, two matching handleless cups beside it. Set on a honed travertine slab against a cream plaster wall. Props: a folded linen napkin under one cup, a few roasted coffee beans, an olive sprig. Diffused window key light from the left, white bounce fill from the right, faint warm rim light on the dripper, velvety highlights on the matte glaze, soft shadows falling right. Full-frame camera, 85mm lens, f/5.6, focus on the dripper rim, elevated three-quarter angle. Palette: sand beige, cream, terracotta, espresso brown, olive green. Calm, warm, handcrafted morning mood. Product on the left third, clean negative space on the right for a headline, 16:9. No logos, no text, no hands, no clutter.
```

</details>

<details><summary><b>Change Attire and Background</b></summary>

```text
I want to change the attire of this image to something with good clothes and should change the background to some famous places
```

</details>

<details><summary><b>Character Reference Sheet</b></summary>

```text
Create a professional character reference sheet of the exact same person from the uploaded reference image on a plain white background.

The character must match the uploaded reference image EXACTLY in both appearance and artistic style. If the reference image is a drawing, illustration, or stylized artwork, replicate the same drawing style, line work, shading technique, and rendering method. If the reference image is photorealistic, the result must also be photorealistic. The visual style must be identical to the reference.

Layout: three rows.

Top row: four equally sized close-up head shots placed side by side — front facing, left profile, right profile, and back of head.

Bottom row: three equally sized full body views placed side by side — full body front, full body side profile, and full body back.

Replicate every detail from the reference image exactly:
- facial structure
- skin tone
- natural blemishes and pore texture (if visible)
- hair color, texture, and styling
- exact iris color and eye details
- realistic eye moisture and catchlights if applicable to the style

The exact same outfit must be worn in every view with identical details, folds, colors, and materials.

Lighting should be soft, neutral studio lighting that is flat and evenly distributed with no shadows and no color cast.

All views must remain perfectly consistent with each other and with the reference image.
```

</details>

<details><summary><b>Character Sketch Sheet</b></summary>

```text
Draw the character from the image—(Your name)—in a free, spontaneous sketching style. Against a bright white background, freely arrange full-body drawings, close-ups of the face, small doodles, full-body sketches, and chibi or stylized versions, so that the page conveys the character's humor and personality. Do not create an organized character sheet; instead, make it look like a sketchbook page filled with spontaneously drawn details.
```

</details>

<details><summary><b>Charcoal Tenderness Portrait</b></summary>

```text
Charcoal and graphite drawing on textured paper, Iranian woman in her early thirties, heavy shading, visible smudges. The whole emotion is in the brows: inner ends pulled up and together, eyes soft, wet, slightly narrowed with tenderness — the maternal "elahi bemiram" look. Below the drawing, a rough hand-sketched border box with smudged handwritten pencil script: "الهی بمیرم".
```

</details>

<details><summary><b>Chiaroscuro Fine Art Portrait Collage</b></summary>

```text
A vertical collage of 5 distinct black and white fine art portraits of a woman, shot on 35mm film with visible grain and high contrast.
Top Left: Intimate close-up, she rests her chin on her hand, smiling softly, messy hair strands on face, wearing a dangling earring, soft window light.Top Right: Spontaneous joy, head thrown back laughing, hand running through messy hair, wearing a white t-shirt, dramatic high-contrast lighting.Middle Left: Extreme close-up profile shot, sharp focus on the eye and nose, visible freckles and skin texture, half face in deep shadow (split lighting).Bottom Left: Wearing a chunky knit sweater, hands holding her head, intense gaze at camera, prominent eyebrows, soft moody lighting.Bottom Right: Artistic composition, a face in profile silhouette close to another face looking at the camera, wearing a black turtleneck, low-key lighting with deep blacks.
Style: Editorial fashion photography, raw emotion, unretouched skin texture, chiaroscuro, moody atmosphere, masterpiece, photorealistic.
```

</details>

<details><summary><b>Chic Minimalist Mirror Selfie</b></summary>

```text
A realistic, high-quality 8K mirror selfie photographed on an iPhone 16 Pro Max, 3:4 aspect ratio.

Style: A sharp, premium mirror selfie with a clean, modern aesthetic.

Camera Angle: Close-up portrait, with the smartphone held at face level in front of a mirror.

Subject: A young woman. Do not change her facial features or identity.

Face & Makeup: Glowy dewy skin, defined black winged eyeliner (cat-eye), long voluminous lashes, and full lips with a sheer pink gloss.

Hair:  straight hair worn loose with a clean middle part.

Pose: She looks slightly away from the camera toward her reflection with a calm, confident expression. Her right hand holds a dark gray iPhone. Her nails are painted a soft light pink.

Outfit & Accessories: A black halter-style top with thin crisscross straps. Layered delicate gold (or rose gold) necklaces with three small round pendants, medium-sized gold hoop earrings, and a small silver ear cuff on the cartilage.

Lighting: Soft natural daylight coming from the side, creating gentle highlights on her skin and hair.

Background: A clean, modern interior with white walls, elegant decorative molding, and a wooden door frame in the background.

Mood: Effortlessly stylish, confident, relaxed, and minimal. Photorealistic with realistic skin texture.
```

</details>

<details><summary><b>Chick Hatching Close Up</b></summary>

```text
Extreme close-up of a cracking chicken egg on straw, hyper-detailed shell texture. Newly hatched featherless chick, wet and wrinkled pink skin. 14mm ultra wide lens providing dramatic perspective, hyper-realistic 8K style, cinematic atmosphere. --ar 9:16.
```

</details>

<details><summary><b>Child's Crayon Coloring Style</b></summary>

```text
A cartoon ${setting} scene with crayon colored ${detail1} and ${detail2} and ${detail3}, like that of a learning child.
```

</details>

<details><summary><b>Chinese Fire Horse Celebration</b></summary>

```text
A vibrant fire horse galloping with intense movement and energy, its mane blazing dramatically with ${flame_colors:golden and crimson flames}. Running joyfully alongside is ${companion_character:a mysterious ethereal character}, celebrating with dynamic poses. The background features ${environment_elements:festive red Chinese lanterns bursting throughout, and fireworks illuminating the night sky in brilliant reds, golds, and oranges}.

Artistic style: ${artistic_style:Chinese ink wash with dynamic, flowing lines that capture rapid movement. The brushstrokes are bold and energetic, creating a sense of rushing movement and intensity}. The composition balances ${style_balance:the traditional aesthetic with celebratory elements}.

Mood: ${mood:Vibrant, celebratory, passionate, energetic}. The Fire Horse's characteristic extroversion and intense movement dominate the scene. ${additional_mood:Excitement and joy radiate from all characters}.

Composition: ${composition:Vertical portrait, the horse and companion moving diagonally across the frame, with dynamic elements creating movement in the background. The motion creates a sense of forward momentum}.

Colors: ${color_palette:Vibrant reds, golds, oranges, blacks, white highlights for intensity, contrasting with additional accent colors}. The palette represents ${color_meaning:warmth, joy, and celebration}}.
```

</details>

<details><summary><b>Christmas Poster</b></summary>

```text
Design a Christmas-themed poster that captures the festive holiday spirit. Include elements such as twinkling Christmas lights, a beautifully decorated tree, snowflakes falling, wrapped presents, and a cozy winter backdrop. The scene should evoke warmth, joy, and togetherness. Use vibrant colors like red, green, and gold, and add soft glowing effects to create a magical atmosphere. The poster format should be ${size:1080x1080} for easy sharing on social media. Customize the text to include a holiday message like "Happy Holidays!" or "Season's Greetings!".
```

</details>

<details><summary><b>Cinema Selfie with Na'vi Characters</b></summary>

```text
Create an 8k resolution image of a 20-year-old girl sitting in a cinema hall. She's taking a selfie with Na'vi characters from the 'Avatar' movie sitting next to her. The girl is wearing a black t-shirt with 'AVATAR' written on it and blue jeans. The background should show cinema seats and a large movie screen, capturing a realistic and immersive atmosphere.
```

</details>

<details><summary><b>Cinematic 3x3 Focal Lengths Grid</b></summary>

```text
<instruction>
Analyze the entire composition of the input image. Identify ALL key subjects present (whether it's a single person, a group/couple, a vehicle, or a specific object) and their spatial relationship/interaction.
Generate a cohesive 3x3 grid "Cinematic Contact Sheet" featuring 9 distinct camera shots of exactly these subjects in the same environment.
You must adapt the standard cinematic shot types to fit the content (e.g., if a group, keep the group together; if an object, frame the whole object):

**Row 1 (Establishing Context):**
1. **Extreme Long Shot (ELS):** The subject(s) are seen small within the vast environment.
2. **Long Shot (LS):** The complete subject(s) or group is visible from top to bottom (head to toe / wheels to roof).
3. **Medium Long Shot (American/3-4):** Framed from knees up (for people) or a 3/4 view (for objects).

**Row 2 (The Core Coverage):**
4. **Medium Shot (MS):** Framed from the waist up (or the central core of the object). Focus on interaction/action.
5. **Medium Close-Up (MCU):** Framed from chest up. Intimate framing of the main subject(s).
6. **Close-Up (CU):** Tight framing on the face(s) or the "front" of the object.

**Row 3 (Details & Angles):**
7. **Extreme Close-Up (ECU):** Macro detail focusing intensely on a key feature (eyes, hands, logo, texture).
8. **Low Angle Shot (Worm's Eye):** Looking up at the subject(s) from the ground (imposing/heroic).
9. **High Angle Shot (Bird's Eye):** Looking down on the subject(s) from above.

Ensure strict consistency: The same people/objects, same clothes, and same lighting across all 9 panels. The depth of field should shift realistically (bokeh in close-ups).
</instruction>

A professional 3x3 cinematic storyboard grid containing 9 panels.
The grid showcases the specific subjects/scene from the input image in a comprehensive range of focal lengths.
**Top Row:** Wide environmental shot, Full view, 3/4 cut.
**Middle Row:** Waist-up view, Chest-up view, Face/Front close-up.
**Bottom Row:** Macro detail, Low Angle, High Angle.
All frames feature photorealistic textures, consistent cinematic color grading, and correct framing for the specific number of subjects or objects analyzed.
```

</details>

<details><summary><b>Cinematic Badminton Championship Commercial</b></summary>

```text
Create a 30-second ultra-realistic cinematic badminton sports commercial set inside a massive indoor championship arena packed with spectators. A talented female badminton player wearing a red and white athletic jersey, black shorts, white sports shoes, and her hair tied in a ponytail prepares for an intense match.

Scene 1: A breathtaking aerial establishing shot of the enormous indoor stadium, with dramatic steel roof structures, thousands of spectators, and powerful spotlights illuminating the badminton court.

Scene 2: A dynamic tracking shot follows the female athlete as she moves rapidly across the green badminton court, gripping her racket and preparing to return a powerful shot. Capture her intense focus, realistic footwork, and athletic movements.

Scene 3: An extreme low-angle close-up of her white sports shoes making quick movements across the court. Show realistic friction, rapid footwork, subtle floor reflections, and natural motion blur.

Scene 4: A dramatic slow-motion shot of the athlete jumping high to smash the shuttlecock. Bright stadium lights shine behind her as the camera rotates slightly, creating a powerful sports-advertisement aesthetic.

Scene 5: Artistic cinematic transitions featuring mirrored reflections, diagonal glass-like panels, split-screen compositions, and close-ups of the racket striking the shuttlecock. Maintain realistic anatomy and consistent character appearance.

Scene 6: Finish with a powerful low-angle hero shot of the athlete standing confidently on the court, surrounded by glowing stadium lights and a cheering audience.

Visual Style: Photorealistic sports cinematography, 4K resolution, dramatic stadium lighting, teal and blue color grading, realistic skin texture, shallow depth of field, dynamic camera movements, high-speed action, smooth slow motion, subtle lens flares, professional sports commercial quality.

Camera: Aerial wide shots, tracking shots, low-angle close-ups, macro details, slow-motion action, and dramatic hero shots.

Aspect Ratio: 9:16 vertical
Duration: 30 seconds
Quality: Ultra-realistic, cinematic, professional sports advertisement.

Negative Prompt: Cartoon visuals, distorted anatomy, extra fingers, duplicated limbs, unnatural racket movement, floating shuttlecock, inconsistent faces, flickering frames, blurry subject, unrealistic physics, excessive motion blur.
```

</details>

<details><summary><b>Cinematic BTS Fashion Photo</b></summary>

```text
Create a photorealistic cinematic BTS fashion photograph of the exact same real person from Image 1, in a 2:3 vertical composition. Preserve her actual facial identity, facial proportions, distinctive features, natural asymmetry, perceived age and recognizable characteristics. Do not beautify, rejuvenate, slim or redesign her face.

Keep her original hair open and loose, softly styled for a major fashion editorial. Let a gentle studio fan create subtle movement through the loose hair.

Dominant idea: a glamorous celebrity moment illuminated by a huge studio light, as if captured seconds before the photographer calls action.

Scene: spacious Hollywood soundstage with a clean warm-white seamless backdrop and soft atmospheric haze. One enormous vintage studio Fresnel dominates one side of the composition, creating a dramatic pool of light and subtle lens bloom. Only one understated apple box and one partially visible camera rig are allowed as secondary production elements.

Pose: she stands on a low production box with one foot slightly elevated, creating an elegant asymmetrical stance. One arm reaches casually toward the large light stand while the other rests at her waist. Her loose hair moves gently in the light breeze. She turns her face toward camera with a poised, slightly serious expression and direct eye contact.

Wardrobe: contemporary 2026 sculptural fashion — electric cobalt-blue draped top with an exaggerated asymmetric shoulder, flowing black skirt and pointed heels. Bold silver earrings.

Composition: 50mm lens, low camera angle, subject placed slightly off-center. The enormous light creates a strong framing shape around her without competing with her face. Use negative space deliberately. Background should feel cinematic and expansive rather than busy.

Lighting: dramatic Hollywood photography — large softbox camera-left as key, low-power frontal fill, warm Fresnel beam entering from the side, subtle overhead highlight and fine rear separation through the loose hair. Create atmospheric flare, luminous haze and controlled highlight bloom while keeping the face perfectly exposed and detailed.

Colour: premium cinematic grade with cobalt, warm ivory, graphite and restrained tungsten highlights. Natural skin tones, luminous midtones, elegant contrast and subtle filmic grain.

Mood: iconic Hollywood BTS fashion photograph, sophisticated, dramatic, sensual, effortless and cinematic.

Ultra-realistic photography, believable studio lighting, realistic haze, natural hair movement, tactile fabric and authentic photographic optics.

Keep the subject as the unmistakable first read. No prop clutter, no equipment wall, no excessive set dressing, no random studio objects, no facial redesign, plastic skin, CGI, artificial hair physics, crushed blacks, orange LUT, text or logos.
```

</details>

<details><summary><b>Cinematic Character Crossover Scene</b></summary>

```text
Create a cinematic crossover scene featuring ${character1} and ${character2} in ${location:fantasy world}. 

Art style: high-quality 2D cartoon animation with detailed lighting, expressive emotions, dynamic poses, and movie-like composition.

Scene mood: ${mood:emotional and adventurous}.

The characters are interacting through ${interaction:a heartfelt moment of friendship}. 

Include:
- dramatic lighting
- colorful background
- cinematic atmosphere
- detailed environment
- smooth animation style
- expressive faces
- depth and motion

Camera angle: ${camera:wide cinematic shot}

Visual inspiration: animated feature films, modern cartoon aesthetics, emotional storytelling, fantasy adventure.

Avoid:
- blurry details
- extra limbs
- distorted anatomy
- low quality
- cropped characters
```

</details>

<details><summary><b>Cinematic Chucky Inspired Night Portrait</b></summary>

```text
Scene & Composition:
A realistic, high-quality nighttime photo taken in a parking lot. The scene is dark and atmospheric, illuminated by realistic parking-lot lights and subtle ambient night lighting. Vertical 3:4 composition, sharp 8K detail, photographed on an iPhone 16 Pro Max.

Pose:
The young woman is standing with her back to the camera. Her back is straight, while her head is turned to the left, revealing her profile. She is looking into the distance to the left.

Both arms are lowered and positioned behind her back.

Key Pose Detail:
She is holding a large fake axe horizontally directly underneath her buttocks, behind her back. This is the main visual feature of the pose. The axe is positioned clearly beneath the buttocks, extending horizontally from one side to the other. Her right hand holds the axe near the base of the blade, while her left hand grips the wooden handle. The positioning makes it look as though she is secretly hiding the axe behind her.

Her legs are straight and slightly apart. She wears red fishnet stockings that extend above the knees, with a thick red band at the top.

Outfit:
A classic Chucky doll-inspired outfit.

- Long-sleeved rainbow-striped top with horizontal red, orange, yellow, green, blue, and purple stripes.
- Light-blue short denim overall romper with straps crossing at the back.
- Short overall-style shorts. No “Good Guys” logo, but the same recognizable style.
- Red fishnet thigh-high stockings with thick red elastic bands.

Axe:
A large realistic-looking theatrical prop axe with a massive silver metallic blade and a wooden handle. The axe is held strictly horizontally underneath the buttocks and behind the back, making this positioning the central visual detail of the image.

Hair:
Long, thick chestnut/reddish-brown hair styled into a messy, voluminous high ponytail or half-up ponytail, with loose strands falling naturally down her back. Slightly tousled texture.

Makeup & Face:
Dramatic Chucky-inspired makeup with dark lipstick. No scars, cuts, bruises, or marks on the face. Her natural facial features and identity must remain exactly the same as in the reference image. Do not alter the shape of her face, eyes, nose, lips, or jawline. Her profile should remain clearly recognizable.

Photography:
Photorealistic, natural skin texture, realistic proportions, cinematic nighttime atmosphere, sharp focus, highly detailed, realistic lighting, 8K quality, iPhone 16 Pro Max photography, vertical 3:4.
Легка напівпосмішка
```

</details>

<details><summary><b>Cinematic Close-Up Portrait</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "high",
    "dominant_palette": [
      "burnt orange",
      "deep teal",
      "black",
      "tan"
    ]
  },
  "composition": {
    "camera_angle": "close-up",
    "depth_of_field": "medium",
    "focus": "Man's face in profile",
    "framing": "The subject is tightly framed on the left, looking towards the right side of the frame, creating negative space for his gaze."
  },
  "description_short": "A dramatic and gritty close-up portrait of a man in profile, illuminated by warm side-lighting against a cool, textured dark background.",
  "environment": {
    "location_type": "studio",
    "setting_details": "The background is a solid, dark, textured surface, possibly a wall, with a moody, dark teal color.",
    "time_of_day": "unknown",
    "weather": "none"
  },
  "lighting": {
    "intensity": "strong",
    "source_direction": "side",
    "type": "cinematic"
  },
  "mood": {
    "atmosphere": "Introspective and somber",
    "emotional_tone": "melancholic"
  },
  "narrative_elements": {
    "character_interactions": "The man is alone, seemingly lost in thought, creating a sense of isolation and introspection.",
    "environmental_storytelling": "The dark, textured, and minimalist background serves to isolate the subject, focusing all attention on his emotional state and the detailed texture of his features.",
    "implied_action": "The subject is in a still moment of deep contemplation, gazing at something unseen off-camera."
  },
  "objects": [
    "Man",
    "Jacket collar"
  ],
  "people": {
    "ages": [
      "young adult"
    ],
    "clothing_style": "The dark collar of a jacket or coat is visible.",
    "count": "1",
    "genders": [
      "male"
    ]
  },
  "prompt": "A dramatic, cinematic close-up portrait of a pensive young man in profile. Intense, warm side lighting from the left illuminates the rugged texture of his skin, stubble, and wavy dark hair. His blue eye gazes off into the distance with a melancholic expression. The background is a dark, textured teal wall, creating a moody and introspective atmosphere. The style is gritty and photographic, with high contrast and a noticeable film grain effect, evoking a feeling of raw emotion and deep thought.",
  "style": {
    "art_style": "realistic",
    "influences": [
      "cinematic portraiture",
      "fine art photography"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "close-up",
    "portrait",
    "profile shot",
    "side lighting",
    "high contrast",
    "film grain",
    "textured",
    "moody lighting",
    "cinematic",
    "chiaroscuro"
  ],
  "use_case": "Training AI models for emotional portrait generation, cinematic lighting styles, and realistic skin texture rendering.",
  "uuid": "6f682e5f-149f-475a-8285-7318abc5959f"
}
```

</details>

<details><summary><b>Cinematic Evolution of Cars Video</b></summary>

```text
"Generate a video: Documentary style cinematic sequence showing the evolution of cars from vintage 1920s automobile to modern electric vehicle charging at sunset, photorealistic, dramatic lighting"
```

</details>

<details><summary><b>Cinematic Fashion Portrait</b></summary>

```text
Image 1 is the subject identity reference. Preserve the same real person’s recognizable face, facial proportions, natural asymmetry, perceived age, skin tone, eyes, nose, lips, jawline, and distinctive features. Use the image only for identity.

Create a vertical 4:5 mid-close cinematic fashion portrait. Transform her hair into a polished glass bob: compact jaw-length silhouette, side-swept part, straight razor-cut ends, realistic hairline, believable density, and a natural high-shine finish.

She wears a deep burgundy open-collar blouse in soft matte silk, with a simple gold hoop and a narrow black leather watch. She leans slightly forward toward the camera, one hand resting naturally at the collarbone. Her eyes meet the lens with direct, high-fashion attitude: self-assured, intense, and effortlessly cool.

Set it in a real studio against a warm off-white seamless paper backdrop. Use soft direct editorial flash close to camera, balanced with one large diffused side light so the face remains dimensional and the shirt retains natural folds. Shoot at eye level with a 50mm lens look, f/2.0, shallow depth of field, precise focus on eyes and face.

Colour grade: warm skin, rich but natural burgundy, soft cream background, subtle warm film contrast, lifted shadow detail, clean highlights, delicate grain. Premium magazine fashion photography, realistic skin texture and materials, no text, logo, or watermark.
```

</details>

<details><summary><b>Cinematic Horse Drawn Wagon Landscape</b></summary>

```text
Photograph a horse-drawn wagon traveling across open country from Wanganui towards Marton in 1870s. Aim for a cinematic landscape photography style with expansive skies and a fresh atmosphere. Use an ARRI Alexa camera with a wide lens to capture the scene's grandeur and detail.
```

</details>

<details><summary><b>Cinematic Low Key Night Selfie</b></summary>

```text
A first-person selfie featuring a young woman in a close-up portrait of her face and shoulders against a very dark background.

She has long, voluminous wavy hair reaching her waist, styled over one shoulder with a deep, well-defined side part and a layered cascading haircut. The layers are clearly visible, creating soft movement, natural flow, and abundant volume from the roots through the full length. Her hair looks thick, glossy, highly realistic, and naturally textured, with visible individual strands.

She is wearing a stylish oversized gray sweater made of soft, cozy knit fabric. Her makeup is a subtle evening look with a natural skin finish, elegant cat-eye eyeliner, and dusty rose lips. Her expression is calm, sultry, and confident. Her head is gently tilted toward one shoulder, her chin slightly lowered, and she gazes directly into the camera from beneath her lashes. Her lips are closed. Around her neck is a delicate silver chain with a small pendant.

The background is almost entirely black, with a soft gray-white diagonal strip on the left edge resembling the side of a curtain. The lighting is dramatic low-key night lighting, with warm soft side light, deep shadows, and a subtle film grain. The camera is noticeably tilted, creating an intimate close-up composition. Her pose is relaxed and cinematic, with her head tilted and chin lowered while her eyes look upward into the lens.

Dark mood filter, low-key aesthetic, sensual, mysterious atmosphere, photorealism, ultra-detailed realistic skin, extremely low brightness, dark photo, shot on iPhone 17, 8K quality, vertical 3:4.
```

</details>

<details><summary><b>Cinematic Neon Alley Night Walk</b></summary>

```text
Cinematic night scene in a narrow urban alley, rain-soaked ground reflecting neon lights.
Vertical composition (9:16), album cover style.

A single male figure walking calmly toward the camera from mid-distance.
Confident but restrained posture, natural street presence.
Dark, minimal clothing with no visible logos.
Face partially lit by ambient neon light, creating a soft color transition across the body.

Environment:
Futuristic neon light arches overhead forming a tunnel-like perspective.
Wet pavement with strong reflections in blue, red, and orange tones.
Buildings on both sides, shopfronts blurred with depth of field.
A few distant pedestrians in soft focus.

Lighting & mood:
Cinematic lighting, realistic neon glow.
Mix of cool blue and warm red/orange lights.
Natural shadows, no harsh contrast.
Atmospheric rain, subtle mist.

Camera & style:
Full-body shot, eye-level angle.
Slight depth-of-field blur in background.
Ultra-realistic, cinematic realism.
No fantasy, no animation look.
No exaggerated effects.

Overall feel:
Modern street aesthetic, dark but elegant.
Minimalist, moody, confident.
Album cover or music video keyframe.
```

</details>

<details><summary><b>Cinematic Portrait Template</b></summary>

```text
A professional, cinematic portrait featuring a {subject} in a stunning {dress} and {Hairstyle} expertly enhanced by detailed makeup and posed in a specific {Poses}. The scene is set against a carefully chosen {background}, illuminated by artistic {light} and captured with precise{framing} to create a high-fashion aesthetic
```

</details>

<details><summary><b>Cinematic Realism</b></summary>

```text
${subject} portrayed in a high-end cinematic realism masterpiece, physically accurate PBR lighting and shading workflow, volumetric fog layers interacting dynamically with rim light and key light, extreme clarity micro-surface details with tactile realism, cinematic depth of field emphasizing subject presence, smooth organic bokeh bloom in background highlights, controlled motion blur simulating real shutter behavior, subtle analog film grain texture, realistic lens artifacts from professional cinema optics, ray-traced reflections and refractions enhancing depth and realism, atmospheric dust and particles suspended in the air, dramatic chiaroscuro lighting composition, HDR filmic exposure with rich shadow detail, premium film camera style capture
```

</details>

<details><summary><b>Cinematic Street Photography</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "medium",
    "dominant_palette": [
      "brown",
      "beige",
      "muted teal",
      "cream"
    ]
  },
  "composition": {
    "camera_angle": "eye-level",
    "depth_of_field": "shallow",
    "focus": "A young ${gender} laughing",
    "framing": "The main subject is framed by a blurred crowd in the background and a camera in the foreground. The camera's screen creates a frame-within-a-frame, emphasizing the act of photography."
  },
  "description_short": "An over-the-shoulder shot of a photographer taking a picture of a joyful young ${gender} laughing heartily in the middle of a blurred crowd.",
  "environment": {
    "location_type": "outdoor",
    "setting_details": "A busy, crowded public space, likely a city street or plaza. The background is filled with many people, all rendered as a soft blur, with some red bokeh lights visible.",
    "time_of_day": "afternoon",
    "weather": "cloudy"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "front",
    "type": "natural"
  },
  "mood": {
    "atmosphere": "A candid moment of pure joy",
    "emotional_tone": "joyful"
  },
  "narrative_elements": {
    "character_interactions": "A photographer is capturing a candid, happy moment of a ${gender}, suggesting a positive and comfortable rapport between them.",
    "environmental_storytelling": "The crowded, out-of-focus background highlights the ${gender} as a singular point of happiness and calm within a bustling environment, making the moment feel personal and intimate.",
    "implied_action": "A photoshoot is actively in progress, capturing a spontaneous reaction from the subject."
  },
  "objects": [
    "camera",
    "${gender}",
    "crowd"
  ],
  "people": {
    "ages": [
      "young adult"
    ],
    "clothing_style": "casual winter wear",
    "count": "unknown",
    "genders": [
      "female"
    ]
  },
  "prompt": "Cinematic street photography from an over-the-shoulder perspective. A photographer holds a digital camera, its screen displaying the shot. The subject is a beautiful young Asian ${gender} with wavy brown hair, who is bursting into a joyful, open-mouthed laugh. She wears a cozy cream-colored knit sweater. The background is a dense, anonymous crowd, completely blurred with soft bokeh lights. The image has a warm, vintage color grade, shallow depth of field, and captures a candid, heartwarming moment of pure happiness.",
  "style": {
    "art_style": "realistic",
    "influences": [
      "street photography",
      "candid portraiture",
      "cinematic"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "shallow depth of field",
    "bokeh",
    "over-the-shoulder shot",
    "candid photography",
    "portrait",
    "frame within a frame",
    "warm tones"
  ],
  "use_case": "Stock photography for themes of happiness, urban life, photography, and candid moments.",
  "uuid": "c0e1b01c-e07e-41b1-b035-f8802d8ec319"
}
```

</details>

<details><summary><b>Cinematic Sunset Boat Scene</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "low",
    "dominant_palette": [
      "sepia",
      "taupe",
      "dark slate gray",
      "khaki",
      "goldenrod"
    ]
  },
  "composition": {
    "camera_angle": "wide shot",
    "depth_of_field": "deep",
    "focus": "Person in boat",
    "framing": "The main subject, the boat and person, are placed off-center to the right within a 1:1 square format, following the rule of thirds. Horizontal layers of water, shoreline, and mountains are preserved and adapted to fit the square frame, maintaining depth and tranquility."
  },
  "description_short": "A lone person wearing a conical hat sits in a traditional wooden boat on a calm lake at sunrise or sunset, surrounded by birds, with hazy mountains in the background.",
  "environment": {
    "location_type": "outdoor",
    "setting_details": "A serene lake or river with calm, reflective water. In the background, a distant, hazy mountain range rises above a low shoreline with trees. The atmosphere is filled with a golden mist.",
    "time_of_day": "evening",
    "weather": "hazy"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "back",
    "type": "natural"
  },
  "mood": {
    "atmosphere": "Peaceful and contemplative solitude",
    "emotional_tone": "calm"
  },
  "narrative_elements": {
    "environmental_storytelling": "The traditional boat, conical hat, and vast, quiet landscape suggest a timeless, rural way of life, possibly fishing or commuting in a place untouched by modernity. The golden haze creates a dreamlike, nostalgic feeling.",
    "implied_action": "The person is likely paddling slowly or pausing to observe the surroundings, suggesting a routine journey or a moment of reflection amidst nature."
  },
  "objects": [
    "boat",
    "person",
    "water",
    "birds",
    "mountains",
    "conical hat"
  ],
  "people": {
    "ages": [
      "adult"
    ],
    "clothing_style": "Traditional attire including a conical hat.",
    "count": "1",
    "genders": [
      "unknown"
    ]
  },
  "prompt": "A cinematic, wide-angle photograph in a 1:1 square format of a lone figure in a traditional wooden boat, silhouetted against the hazy golden light of a serene sunset. The person wears a conical hat, resting peacefully in the boat on a calm, rippling lake. The composition is balanced within a square frame with the subject slightly off-center. In the distance, misty mountains fade into the warm sky. Flocks of birds fly overhead and float on the water, adding life to the tranquil scene. The atmosphere is calm and timeless, with a soft, grainy film texture.",
  "style": {
    "art_style": "realistic",
    "influences": [
      "cinematic photography",
      "landscape photography",
      "travel photography"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "silhouette",
    "wide shot",
    "landscape",
    "golden hour",
    "hazy",
    "atmospheric perspective",
    "serene",
    "natural light",
    "reflection",
    "film grain",
    "square format",
    "1:1 aspect ratio"
  ],
  "use_case": "Travel and tourism promotion, stock photography, cinematic reference, background imagery."
}
```

</details>

<details><summary><b>Cinematic Thriller Silhouette</b></summary>

```text
{
  "prompt_content": {
    "positive_prompt": "cinematic shot, view through green textured wire reinforced glass, frosted glass effect, silhouette of a person pressing palms against the glass, hands distinctively visible pressing on wet glass, mysterious atmosphere, dim lighting, greenish yellow color palette, grid pattern texture, psychological thriller vibe, photorealistic, 8k, highly detailed textures, mosaic glass distortion",
    "negative_prompt": "clear glass, cartoon, illustration, anime, bright lighting, low resolution, blurry, text, watermark, deformed hands, missing fingers, extra fingers, dry glass, blue tones",
    "parameters": {
      "aspect_ratio": "1:1",
      "steps": 30,
      "cfg_scale": 7.0,
      "sampler": "DPM++ 2M Karras"
    }
  },
  "visual_analysis": {
    "subject": "Silhouette behind textured glass",
    "action": "Hands pressing against surface",
    "atmosphere": "Claustrophobic, mysterious",
    "dominant_colors": ["#4a6b45", "#8c9c5e", "#2e3a24"]
  }
}
```

</details>

<details><summary><b>Cinematic Triptych: A Day in the Countryside</b></summary>

```text
{
  "colors": {
    "color_temperature": "cool",
    "contrast_level": "medium",
    "dominant_palette": [
      "green",
      "dark gray",
      "yellow",
      "red-orange"
    ]
  },
  "composition": {
    "camera_angle": "multi-angle triptych",
    "depth_of_field": "shallow",
    "focus": "woman with red hair and bicycle",
    "framing": "A triptych format that follows the woman's journey, combining a wide shot from behind, a medium portrait, and a medium shot by a pond."
  },
  "description_short": "A triptych showing a woman with red hair on a day out with her bicycle in the countryside. Panels show her riding through a wildflower field, a close-up portrait, and standing by a pond.",
  "environment": {
    "location_type": "outdoor",
    "setting_details": "A rural landscape featuring a wildflower meadow, a dirt path, rolling green hills, and a small, still pond.",
    "time_of_day": "afternoon",
    "weather": "cloudy"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "top",
    "type": "natural"
  },
  "mood": {
    "atmosphere": "peaceful and contemplative",
    "emotional_tone": "calm"
  },
  "narrative_elements": {
    "environmental_storytelling": "The overcast sky and quiet, natural setting create a mood of introspection and serene solitude.",
    "implied_action": "The woman is on a leisurely bike ride, pausing to take in the scenery and enjoy a quiet moment, suggesting a journey of both distance and thought."
  },
  "objects": [
    "woman",
    "bicycle",
    "jacket",
    "wildflower meadow",
    "pond",
    "hills"
  ],
  "people": {
    "ages": [
      "young adult"
    ],
    "clothing_style": "casual, dark jacket and jeans",
    "count": "1",
    "genders": [
      "female"
    ]
  },
  "prompt": "A cinematic triptych capturing a serene day in the countryside with a young woman with vibrant red hair. Top panel: viewed from behind, she cycles down a narrow path through a vast meadow of yellow and purple wildflowers under a cloudy sky. Middle panel: a gentle medium portrait of her smiling softly, with the colorful field blurred behind her. Bottom panel: she stands with her vintage bicycle beside a calm pond, reflectively brushing her hair back. The style is moody and atmospheric, with soft, diffused natural light from the overcast sky and a muted, earthy color palette.",
  "style": {
    "art_style": "realistic",
    "influences": [
      "cinematic photography",
      "moody portraiture",
      "film aesthetic"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "triptych",
    "overcast lighting",
    "diffused light",
    "rural",
    "shallow depth of field",
    "portrait"
  ],
  "use_case": "Lifestyle blog imagery, narrative photo essay, advertising for travel or apparel.",
  "uuid": "2cc80ab3-7973-4fc0-9f95-db3917b8b152"
}
```

</details>

<details><summary><b>Cinematic Urban Night Portrait</b></summary>

```text
Subject: A medium portrait of a young woman.

Pose: She is standing upright, looking directly into the camera. Her right hand is raised naturally near her hair or the side of her head.

Clothing: A black zip-up athletic jacket with a raised collar, slightly unzipped. A delicate silver chain necklace is subtly visible.

Hair: wavy hair worn loose. Part of the hair is brushed back, revealing her face, while soft waves and loose strands are illuminated by the backlight.

Makeup: Bold, flawless evening / e-girl makeup. Sharp black winged eyeliner, long voluminous lashes, and a bright shimmer in the inner corners of the eyes. Coral-pink blush with a luminous highlighter on the cheekbones and the tip of the nose. Rich matte terracotta / reddish-brown lipstick.

Jewelry: Multiple silver hoop earrings in the left ear (both cartilage and lobe) and a thin silver necklace.

Lighting: Dramatic cinematic lighting with a strong warm golden backlight creating a glowing halo around her hair and silhouette, especially on the left side. Soft frontal light keeps her face clear and highlights every makeup detail. Warm, rich color grading.

Background: A deeply blurred evening or nighttime urban setting with soft bokeh lights and subtle greenery.

Mood: Intimate, confident, stylish, mysterious, and modern city night.

Camera: Eye-level shot, medium portrait, vertical 3:4. Hyper-realistic, ultra-detailed 8K, photographed on iPhone 16 Pro.

Do not change the facial features.
```

</details>

<details><summary><b>Civil Engineer and Elevation Design Architect</b></summary>

```text
Role: think you are civil engineer & elevation design architect. Context: give me 3D view elevation design for the provided images for ground plus one floor whose physical structure is completed, which is 26 feet wide on road facing, give me multiple design images with modern floors. Respect the existing visible structure and opening.
```

</details>

<details><summary><b>Clay Bust from Photo</b></summary>

```text
Use the uploaded photo as the only identity reference. Transform the person into a hyper-realistic handmade modeling clay (plasticine) bust sculpture.

SUBJECT
- Create a bust only: head + neck + upper shoulders (no full body).
- Keep the person clearly recognizable: same facial proportions, eyes, nose, lips, jawline, hairstyle.
- Preserve the original facial expression and approximate head angle from the uploaded photo.
- No beautification, no age change.

REAL CLAY MATERIAL (MUST LOOK PHYSICAL)
- Must look like real modeling clay, not CGI, not porcelain, not wax.
- Show subtle hand-made realism: faint fingerprints, tiny tool marks, soft smudges, gentle dents, slight seam lines where clay pieces meet.
- Add realistic clay surface behavior: matte-waxy sheen, micro texture, tiny dust specks, minor uneven thickness.

SCULPTING DETAILS
- Hair: sculpted clay strands/clumps with believable direction and volume, slightly imperfect alignment.
- Skin: layered clay look with fine micro texture (not airbrushed smooth).
- Eyes: clay-crafted eyes (not glossy realistic eyeballs). If separate pieces are used, show tiny join lines.
- Lips and nose: soft clay transitions, realistic handmade edges.

COLOR & FINISH
- Natural clay color palette for skin and lips; hair as clay (not real hair).
- If painted, it must look hand-painted: slight pigment variation, mild brush texture, tiny imperfections.
- No extra accessories unless clearly present in the uploaded photo.

PHOTOGRAPHY STYLE (MAKE IT LOOK LIKE A REAL PRODUCT PHOTO)
- Studio product photo of a physical sculpture: realistic 85mm lens look, natural depth of field.
- Soft diffused key light from front-left + subtle rim light, clean soft shadows.
- Neutral seamless background: solid off-white or light gray.
- Add a realistic contact shadow and a subtle tabletop surface texture.

COMPOSITION & QUALITY
- Centered composition, chest-up framing, clean margins.
- Ultra sharp focus on facial features, high resolution, realistic materials.

NEGATIVE CONSTRAINTS
- No cartoon/anime style.
- No 3D render look, no plastic toy look, no porcelain, no wax museum skin.
- No text, no logos, no watermark.
```

</details>

<details><summary><b>Clay Crafted Mini City</b></summary>

```text
Generate a whimsical miniature world featuring ${landmark_name} crafted entirely from colorful modeling clay. Every element (buildings, trees, waterways, and urban features) should appear hand-sculpted with visible fingerprints and organic clay textures. Use a playful, childlike style with vibrant colors: bright azure sky, puffy cream clouds, emerald trees, and buildings in warm yellows, oranges, reds, and blues. The handmade quality should be evident in every surface and gentle curve. Capture from a wide perspective showcasing the entire miniature landscape in a harmonious, joyful composition.

At the top-center, add the city name ${city_name} in a clean, bold, friendly rounded font that matches the playful clay aesthetic. The text should be clearly readable and high-contrast against the sky, with subtle depth as if it is also made from clay (slight 3D clay lettering), but keep it simple and not overly detailed.

Include no other text, words, or signage anywhere else in the scene. Only sculptural clay elements should define the location through recognizable architectural features. 1080x1080 dimension.
```

</details>

<details><summary><b>Claymation Adventure on a Mushroom Cap</b></summary>

```text
{
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness but render them as charming, handcrafted clay models. Transform Subject 1 (male) and Subject 2 (female) into miniature adventurers resting on the cap of a giant red mushroom. The scene should look like a freeze-frame from a high-budget stop-motion film, complete with visible thumbprints on the clay surfaces and uneven, sculpted textures.",
  "details": {
    "year": "Timeless Whimsy",
    "genre": "Claymation",
    "location": "A macro-scale forest floor, centered on top of a large, red Fly Agaric mushroom with white spots.",
    "lighting": [
      "Soft studio lighting",
      "Warm key light",
      "Simulated rim lighting to highlight clay edges"
    ],
    "camera_angle": "Slight high-angle macro shot with a shallow depth of field to simulate a miniature set.",
    "emotion": [
      "Joyful",
      "Cozy",
      "Wonder"
    ],
    "color_palette": [
      "Vibrant red",
      "moss green",
      "canary yellow",
      "earthy brown",
      "sky blue"
    ],
    "atmosphere": [
      "Playful",
      "Handcrafted",
      "Tactile",
      "Charming"
    ],
    "environmental_elements": "Oversized blades of grass made of flattened green clay, a snail with a spiral shell made of rolled play-dough, and cotton-ball clouds in the background.",
    "subject1": {
      "costume": "A textured hiker's vest made of matte clay, a plaid shirt with painted lines, and chunky brown boots.",
      "subject_expression": "A wide, friendly grin with slightly exaggerated, rounded features.",
      "subject_action": "Sitting on the edge of the mushroom, dangling his legs and pointing at a clay butterfly."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "photorealistic skin",
        "human proportions",
        "hair strands",
        "digital gloss"
      ],
      "exclude_styles": [
        "CGI",
        "2D cartoon",
        "sketch",
        "anime",
        "watercolor"
      ],
      "exclude_colors": [
        "neon",
        "grayscale",
        "dark moody tones"
      ],
      "exclude_objects": [
        "modern technology",
        "cars",
        "buildings"
      ]
    },
    "subject2": {
      "costume": "A yellow raincoat with a smooth, glossy finish and oversized red rain boots.",
      "subject_expression": "A cheerful look with sculpted laugh lines and bright eyes.",
      "subject_action": "Kneeling on the mushroom cap, holding a giant, sculpted blueberry with both hands."
    }
  }
}
```

</details>

<details><summary><b>Claymation Frog Band on Lily Pads</b></summary>

```text
Four cheerful clay frogs play tiny instruments on giant lily pads in a pond at dusk: one strums a little banjo, one plays an upright bass made from a hollow reed, one taps drums made of acorn caps, and one blows a curled snail-shell horn. Handmade stop-motion claymation set with visible fingerprints and soft tool marks in the plasticine. Paper lanterns glow on short bent-wire posts around the pond, and fireflies made of tiny warm LEDs drift between cattails and pink water lilies. The water is glossy blue resin with gentle ripples and reflections of the lanterns. Background of felt hills, cotton-wool mist, and a painted twilight sky in peach and lavender with a few early stars. Shallow depth of field like a real miniature set photographed with a macro lens, warm key light and cool blue rim light. Playful, cozy, storybook mood with rich saturated colors. Wide landscape 16:9. No people, no hands, no text, no letters, no logos.
```

</details>

<details><summary><b>Cliffside Himalayan Monastery at Misty Dawn</b></summary>

```text
A small whitewashed Himalayan monastery clings to the ledges of a steep granite cliff on the left of the frame at misty dawn, with five long strings of colorful prayer flags running from its rooftops across the gorge to a tall rock spire in the right foreground. The monastery has four stacked buildings with white lower walls, red-brown upper walls, rows of small dark windows, dark flat-edged roofs, and small gold roof ornaments catching the first light, joined by narrow stone stairs and one short wooden balcony. Thin incense smoke rises from a rooftop burner. The prayer flags repeat blue, white, red, green, and yellow, sagging gently in soft curves. Far below, a turquoise river winds through a deep forested gorge, half hidden under a soft band of white mist that sits below the monastery. Snow-capped peaks rise in the background, their tops lit pale gold and pink by the sun from the right, under a clear sky fading from soft blue to warm peach. Dark pines and juniper bushes cling to the rock. Photoreal travel and landscape photography, serene and airy mood. Wide landscape 16:9. No people, no text, no signs, no logos.
```

</details>

<details><summary><b>Cliffside Travel Portrait</b></summary>

```text
A handsome young man sits casually atop a large rocky cliff overlooking a vast turquoise sea, gazing toward the horizon with a relaxed, calm demeanor. He is dressed in a seaside vacation outfit. His short, neat black hair is gently tousled by the breeze, and he wears modern sunglasses. Captured in a wide shot from a rear-side angle, the scene reveals the expansive ocean, a distant small island, and a dramatic, cloudy sky with soft afternoon sunlight filtering through. The texture of the rock is detailed and natural. The atmosphere evokes an aesthetic, solitary, peaceful, and cinematic travel vibe. Realistic photography, natural lighting, ultra-detailed, DSLR quality, 35mm lens, high dynamic range, soft shadows, depth of field, photorealistic, Instagram travel aesthetic, vertical 9:16 composition.
```

</details>

<details><summary><b>Clockwork Hummingbird and Brass Flower</b></summary>

```text
Macro photograph of a delicate clockwork hummingbird made of brass and enamel, sipping nectar from a blooming brass orchid, tiny gears and sapphire eyes visible, soft studio lighting, shallow depth of field, ultra-detailed metal textures, elegant steampunk aesthetic
```

</details>

<details><summary><b>Cloisonné Enamel Dish of Two Cranes</b></summary>

```text
A close studio photograph of a round cloisonné enamel dish centered in a 16:9 frame on dark charcoal linen. Key subject first: two Japanese-style cranes with white bodies, black necks, and red crowns flying left to right above a deep cobalt mountain lake, every shape outlined in thin raised gold wire cells filled with glossy enamel. Behind the birds, layered indigo and teal mountains, a pale cream cloud band, and a small island pine in dark green enamel. The dish rim is a continuous border of peony and chrysanthemum motifs in coral, gold, and jade green. Metalwork details: tiny gold wire walls catching highlights, slight enamel meniscus inside each cell, a glassy kiln-fired surface with soft specular reflections, copper showing faintly at the outer foot ring. Soft side light from the left, gentle contact shadow on the linen, shallow depth of field with the cranes sharpest. Photoreal product photo of handmade enamelware, saturated true enamel colors, calm museum-craft mood. Not a painting of enamel: a real photographed object. No text, no hallmark letters, no watermark, no hands.
```

</details>

<details><summary><b>Close-up Black and White Portrait</b></summary>

```text
Close-up black and white portrait of a man and a woman standing side by side. The man has tousled hair and a rough beard, the woman has softly tousled natural hair. Both tilt their heads slightly upward as dramatic overhead light falls on them. Their eyes remain in shadow, creating a powerful, mysterious, silhouette-like mood with strong contrast. 9:16 composition, intimate dual-portrait framing.
```

</details>

<details><summary><b>Cocktail Videos</b></summary>

```text
Cinematic close-up of a mysterious bartender pouring a glowing green liquid into a glass, heavy smoke rising, dark cocktail bar background, 4k, hyper-realistic, slow motion.
```

</details>

<details><summary><b>Cold War 1962 Spy Exchange</b></summary>

```text
{
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Create an Ultra-Photorealistic, Movie-Quality scene depicting Subject 1 (male) and Subject 2 (female) as covert spies meeting on a foggy, iron bridge during the Cold War. The image must look like a frame from a high-budget blockbuster movie shot on Arri Alexa. Use cinematic lighting to create deep shadows and highlights. The scene is highly detailed with a shallow depth of field. Subject 1 is handing off a secret package to Subject 2. The composition adheres to a cinematic 1:1 aspect ratio.",
  "details": {
    "year": "1962",
    "genre": "Cinematic Photorealism",
    "location": "The Glienicke Bridge at midnight, obscured by thick river fog and illuminated by dim, yellow streetlamps.",
    "lighting": [
      "Volumetric fog lighting",
      "Noir style chiaroscuro",
      "Rim lighting on silhouettes",
      "Soft yellow tungsten glow"
    ],
    "camera_angle": "Eye-level medium closeup with a shallow depth of field to isolate the subjects from the misty background.",
    "emotion": [
      "Suspenseful",
      "Urgent",
      "Clandestine"
    ],
    "color_palette": [
      "Steel blue",
      "Fog gray",
      "Tungsten amber",
      "Deep black",
      "Vibrant crimson"
    ],
    "atmosphere": [
      "Cold",
      "Tense",
      "Cinematic",
      "Mysterious"
    ],
    "environmental_elements": "Swirling mist rising from the water below, damp iron railings, the distant blurred headlights of a vintage checkpoint vehicle.",
    "subject1": {
      "costume": "A textured charcoal wool peacoat with the collar turned up against the wind.",
      "subject_expression": "Anxious, with sweat glistening on his brow and eyes darting nervously.",
      "subject_action": "Subtly sliding a leather dossier across the railing towards Subject 2."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "daylight",
        "sunshine",
        "modern cars",
        "cell phones",
        "neon signs"
      ],
      "exclude_styles": [
        "cartoon",
        "3D render",
        "sketch",
        "anime",
        "impressionist"
      ],
      "exclude_colors": [
        "neon green",
        "hot pink",
        "pastel colors"
      ],
      "exclude_objects": [
        "umbrellas",
        "crowds",
        "modern architecture"
      ]
    },
    "subject2": {
      "costume": "A classic beige trench coat belted at the waist and a red hat.",
      "subject_expression": "Stoic and composed, with a piercing, calculating gaze.",
      "subject_action": "Reaching out with a black leather-gloved hand to intercept the dossier while looking over her shoulder."
    }
  }
}
```

</details>

<details><summary><b>Color Consistency Analysis and Adjustment</b></summary>

```text
Act as a professional designer and photographer with high visual intelligence. Your task is to analyze the colors used in the application and make them consistent according to the given primary color ${primaryColor} and secondary color ${secondaryColor:defaultSecondary}. Ensure that transitions between colors are smooth and aesthetically pleasing. Prefer the use of commonly accepted color combinations that look good together. Provide a detailed color palette recommendation and suggest adjustments to enhance visual harmony. Consider the business/domain of the application, ${businessDomain}, and ensure the color choices align with its goals and aims. If the application supports dark mode, ensure that necessary checks and adjustments are made to maintain consistency and aesthetics in dark mode as well.
```

</details>

<details><summary><b>Colorful Studio Photo Collage</b></summary>

```text
A 3-panel vertical photo collage of a beautiful 28-year-old woman with stylish long hair. Studio photography style. Panel 1: Fuchsia pink background, she is wearing a clean white suit, posing with her hands on her hips, a bold expression. Panel 2: Light blue background, wearing the same white suit, making a peace sign and smiling broadly. Panel 3: Bright yellow background, wearing a white suit, caught in the air in an energetic jumping pose. Very cheerful facial expression, bright and saturated colors, high-key studio lighting, sharp focus, high resolution. Ratio 16:9.
```

</details>

<details><summary><b>Coloring Book Page Designer</b></summary>

```text
Act as a creative illustrator. You are tasked with designing a series of coloring book pages suitable for both children and adults.

Your task is to:
- Create outlines of various themes such as nature, animals, and abstract patterns.
- Ensure each page contains intricate details for adults and simpler shapes for children.
- Use themes that promote relaxation and creativity.

Rules:
- Ensure designs are appropriate for all ages.
- Avoid overly complex patterns that may be frustrating for children.
- Include a variety of themes to cater to different interests.
```

</details>

<details><summary><b>Comic Book Team Illustration</b></summary>

```text
{
  "colors": {
    "color_temperature": "neutral",
    "contrast_level": "medium",
    "dominant_palette": [
      "blue",
      "red",
      "pale yellow",
      "black",
      "blonde"
    ]
  },
  "composition": {
    "camera_angle": "medium shot",
    "depth_of_field": "shallow",
    "focus": "A group of four people",
    "framing": "The subjects are arranged in a diagonal line leading from the background to the foreground, with the foremost character taking up the right side of the frame."
  },
  "description_short": "A comic book style illustration of four young people in matching uniforms, standing in a line and looking towards the left with serious expressions.",
  "environment": {
    "location_type": "outdoor",
    "setting_details": "The background is a simple color gradient, suggesting an open sky with no other discernible features.",
    "time_of_day": "unknown",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "unknown",
    "type": "ambient"
  },
  "mood": {
    "atmosphere": "Unified and determined",
    "emotional_tone": "serious"
  },
  "narrative_elements": {
    "character_interactions": "The four individuals stand together as a cohesive unit, sharing a common gaze and purpose, indicating they are a team or part of the same organization.",
    "environmental_storytelling": "The stark, minimalist background emphasizes the characters, their expressions, and their unity, suggesting that their internal state and group dynamic are the central focus of the scene.",
    "implied_action": "The characters appear to be standing at attention or observing something off-panel, suggesting they are either about to embark on a mission or are facing a significant event."
  },
  "objects": [
    "Blazers",
    "Collared shirts",
    "Uniforms"
  ],
  "people": {
    "ages": [
      "teenager",
      "young adult"
    ],
    "clothing_style": "Uniform consisting of blue blazers with a yellow 'T' insignia on the pocket, worn over red collared shirts.",
    "count": "4",
    "genders": [
      "male",
      "female"
    ]
  },
  "prompt": "A comic book panel illustration of four young team members standing in a line. They all wear matching uniforms: blue blazers with a yellow 'T' logo over red shirts. The person in the foreground has short, dark, wavy hair and a determined expression. Behind them are a blonde woman, and two young men with dark hair. They all look seriously towards the left against a simple gradient sky of pale yellow and green. The art style is defined by clean line work and a muted color palette, creating a serious, unified mood.",
  "style": {
    "art_style": "comic book",
    "influences": [
      "Indie comics",
      "Amerimanga"
    ],
    "medium": "illustration"
  },
  "technical_tags": [
    "line art",
    "illustration",
    "comic art",
    "character design",
    "group portrait",
    "flat colors"
  ],
  "use_case": "Training data for comic book art style recognition or character illustration generation.",
  "uuid": "1dac4e3f-b9dd-45de-9710-c4d685931446"
}
```

</details>

<details><summary><b>Confident Nighttime OOTD Portrait</b></summary>

```text
A full-body vertical nighttime photograph of a young woman with a slim hourglass figure and long wavy light brown hair with blonde highlights. She is wearing a tight white short-sleeve crop top and blue skinny jeans, holding a small silver metallic handbag in her left hand. She stands in an outdoor parking lot, body turned to the side in a three-quarter profile, looking back over her shoulder directly at the camera with a subtle confident smile. Behind her is a black Jeep Wrangler with a spare tire cover displaying the 'Jeep' logo in white, and a grey car parked to the right. The ground is dark asphalt with white parking lines. Overhead streetlights cast a cool white glow, illuminating her figure against the dark night sky. Shot with a smartphone camera, 24mm lens, flash or strong fill light on the subject, realistic lighting, casual social media aesthetic, 'outfit of the night' vibe, high quality, sharp focus on the subject.
```

</details>

<details><summary><b>Conservatory Concept Design Brief Builder</b></summary>

```text
Act as a conservatory and glasshouse designer and as a visualization art director. I will describe the Victorian-style glass conservatory I am imagining. You will turn it into a tight concept: the building, its iron and glass structure, the plants, the furniture, the floor and water features, the light and mood, with a numbered list of fixed design details plus two ready-to-use image prompts that show the SAME building from two viewpoints at two times of day, so the two AI images look like photos of one real place.

Era and inspiration: ${era:High Victorian, around 1870, inspired by public palm houses but at the scale of a private estate}
Purpose and scale: ${purpose:a private winter garden attached to nothing, standing alone at the end of a formal garden, about 14 m long, 8 m wide, 7 m high}
Structure and materials I like: ${structure:white-painted wrought iron, arched ribs, a diamond lattice glass roof, a low pale stone plinth wall}
Plants: ${plants:hanging Boston ferns, kentia palms in terracotta pots, tree ferns, orchids on a side shelf, moss}
Furniture and features: ${features:ornate cast-iron benches, a small round mosaic fountain with koi in the center, brass pendant lanterns}
Floor: ${floor:black-and-white checkerboard marble}
Mood: ${mood:calm, humid, timeless, a little romantic, a place to read on a Sunday morning}
Outside the building: ${outside:a gravel path between low box hedges, climbing pink roses on the front, a formal English garden}
View A: ${view_a:interior at eye level from just inside the front doors, looking down the central aisle, early morning sun with misty light shafts}
View B: ${view_b:exterior from the gravel garden path facing the front entrance at blue hour, warm lamps glowing inside}

Please produce:

1. Concept
   - A name idea for the conservatory (for my use only, it will not appear in the images) and a two-sentence story of how it should feel to step inside.
   - Architecture: footprint, height, roof form, rib spacing, glazing pattern, ridge details, entrance, ventilation features, and how the iron is finished, described in plain construction terms.
   - Interior layout: the central aisle, where the fountain sits, where benches, palms, ferns, and shelves go, and where the lanterns hang, described from the entrance looking in.
   - Planting plan: each plant group with its position and the effect it creates (height, texture, light filtering).
   - Palette: 6 named colors (simple names like "chalk white" or "fern green") and where each one appears.
   - Materials and finishes: iron, glass (clear, slightly wavy old glass, condensation), stone, marble, mosaic, brass, terracotta, and wood.

2. Fixed design details (the consistency list)
   A numbered list of 14 to 18 details that must look identical in every image: footprint and proportions, roof shape, rib count and spacing, the glazing pattern, the ridge cresting and finials, the plinth wall, the entrance doors and fanlight, the floor pattern, the fountain, the benches, the lanterns, the palms, the ferns, and anything visible from both inside and outside, each with its exact position. Write each one as a short, concrete phrase an image generator can follow (for example "a round fountain basin about 2 m across, clad in deep blue and gold mosaic, at the exact center of the hall").

3. Image prompt A: the base view
   One detailed prompt for an AI image generator: photoreal architectural interior photography from the view A position, in view A light. Include every fixed detail visible from there in its correct position (left and right as seen from the camera), camera height and lens, light direction, atmosphere (mist, humidity, light shafts), mood, and a 16:9 landscape composition. End with exclusions (no people, no readable text, no signage, no modern objects).

4. Image prompt B: the second view
   One detailed prompt for view B, written for a text-only image generator that cannot see image A: restate ALL fixed details again in full words (never "same as before"), place each one correctly for the new camera position, describe what is newly visible from outside (the front gable, the plinth, the ridge cresting, the path, the roses), describe which interior details can be seen through the glass and the open doors, and change only the viewpoint, time of day, and lighting. Keep the structure, colors, and proportions identical.

5. Consistency checklist
   Ten yes/no checks to compare image B against image A (for example "Is the roof glazing still a diamond lattice between the white arched ribs?").

6. Practical notes
   A short list on real-world feasibility: heating and humidity for these plants, ventilation, shading in summer, maintenance of painted iron and old glass, safety glass options, and a rough order of magnitude for building or restoring something similar, labeled as an estimate.

Rules:
- Keep the design historically believable for the stated era; flag anything that would be anachronistic or structurally unrealistic.
- Use plain color names and concrete shapes; avoid vague words like "beautiful" or "magical" on their own.
- No readable text, plaques, signs, or numbers anywhere in the image prompts.
- No real named buildings, brand names, or real people in the image prompts.
- If my description is missing something essential, make a sensible assumption and list it at the top.
```

</details>

<details><summary><b>Conversational Logo Design</b></summary>

```text
Design a conversational process to create a minimal logo for the user's project, leveraging their branding colors: #3a7eab, #cf4832, and #d1d3d4. Begin by developing a set of 10 thoughtful yes/no questions to clarify the project's goals, target audience, aesthetics, and design preferences. After receiving responses, assess if further detail is needed—if so, continue asking focused yes/no follow-up questions until sufficient clarity about the project's nature and user’s expectations is achieved. Only once all required information has been gathered, generate a detailed logo concept brief using the collected answers as reasoning steps. 

Request and Reasoning Order:
- All reasoning, deduction, and rationale for logo direction must be documented before the final conclusion.
- The final conclusion (logo brief/concept) must always appear after the reasoning.
- If providing examples, always show Q&A (reasoning) before the final logo concept.

Process Steps:
- Start by explaining the goal (creating a minimal logo using the specified branding colors).
- Present 10 sequential, thoughtful yes/no questions, designed to uncover essential details (e.g., project field, mood, geometric/organic shapes, initialism use, target audience, etc.).
- After each set of answers, assess what is unclear. Ask direct, relevant follow-up yes/no questions as needed for ambiguous or incomplete information.
- Once all important criteria are clarified, summarize the reasoning that leads to your logo design proposal (list the answers, state the key takeaways, explain how these shape your suggestions).
- Provide the minimal logo concept as the final output—describe it visually (not as an image), using concise, clear language, referencing the chosen colors and tying the concept to the reasoning steps.

Output Format:
- Converse in turn-by-turn, always basing next questions on previous answers until enough is known.
- At the end of the Q&A phase, output a JSON object with two main fields:
  - "reasoning_steps": An ordered list outlining each answer and what was deduced.
  - "logo_concept": A single clear paragraph describing the proposed minimal logo (visual elements, shapes, color usage, and rationale).

Example (shortened for illustration; real exchanges may be longer and more complex):

Sample Q&A Exchange:
Q1: Is your project related to technology?  
A1: Yes.  
Q2: Is your brand's mood more playful than serious?  
A2: No.
... (continue with more questions and follow-ups as needed)

Final Output Example:
{
  "reasoning_steps": [
    "The project is tech-related: suggests clean, structured symbols.",
    "Mood is serious: favors sharp lines and minimal, non-playful forms.",
    "Prefers geometric over organic shapes: will use strict geometry.",
    "Wants initials included: will consider stylized lettering."
    //... further reasoning as relevant
  ],
  "logo_concept": "A minimal logo using the initials in a geometric, interlocked arrangement. The primary color #3a7eab forms the base, with accent lines in #cf4832 and subtle highlights in #d1d3d4. The design is crisp and serious, reflecting the tech context and brand tone."
}

Important: 
- All reasoning and interim thinking must be shown before the final logo concept (conclusion).
- Persist with follow-up questions if key information is missing or ambiguous.
- Be clear, concise, and visual in the final descriptive paragraph (logo_concept).

---

Important Reminder:  
Persistently gather project information via yes/no questions, show your reasoning before giving a logo concept, and always follow the output JSON structure.
```

</details>

<details><summary><b>Corporate ID Photo</b></summary>

```text
Create a modern corporate ID photo of the person from the uploaded image, suitable for company badges and internal systems.
Keep the face identical to the uploaded image, with realistic proportions, no beautification or age adjustment.

Framing:
• Neutral, centered head and shoulders
• Subject looking straight at the camera with a neutral but friendly expression

Background:
• Plain, uniform background in [BACKGROUND_COLOR], no texture, no gradient
• No props, no text, no logos

Style:
• Even, soft lighting with minimal shadows
• High clarity and sharpness around the face, natural skin tones, high-resolution

Outfit:
• Transform clothing into [OUTFIT_STYLE] that matches a corporate environment
• No visible logos, patterns or distracting accessories

Make the result look like an upgraded, well-lit, professional version of a corporate ID or access badge photo, ready to be dropped into internal tools, email accounts or passes.
```

</details>

<details><summary><b>Corporate Logo Designer</b></summary>

```text
{
  "system_instruction": "Act as a senior brand identity designer. Create a professional, scalable corporate logo based on the following parameters.",
  "brand_variables": {
    "name": "${COMPANY_NAME}",
    "industry": "${INDUSTRY}",
    "core_aesthetic": "${AESTHETIC_STYLE}", 
    "primary_color": "${BRAND_COLOR_HEX_OR_NAME}",
    "metaphor": "${VISUAL_SYMBOL_DESCRIPTION}"
  },
  "design_logic": {
    "composition": "Professional balanced lockup of a symbol and typography.",
    "typography": "High-fidelity rendering of '${COMPANY_NAME}'. Style: Bold, modern, sans-serif, optimized kerning.",
    "symbolism": "Incorporate a minimal geometric mark representing ${VISUAL_SYMBOL_DESCRIPTION}.",
    "color_theory": "Dominant use of ${BRAND_COLOR_HEX_OR_NAME} on a clean, high-contrast background."
  },
  "nano_banana_constraints": {
    "style_reference": "Swiss Graphic Design, Modern Corporate Minimalism",
    "technical_specs": [
      "Vector-style clarity",
      "No 3D effects or drop shadows",
      "Solid flat colors",
      "Maximum legibility at small scale"
    ],
    "negative_space": "Utilize intentional white space to enhance the ${AESTHETIC_STYLE} feel."
  },
  "output_format": "Centered, single logo version, no mockups, white background."
}
```

</details>

<details><summary><b>Corporate Studio Portrait</b></summary>

```text
Use the person from the uploaded photo as the primary reference. Keep facial features, hair, skin tone, and overall identity identical (no beautification, no age changes).

Scene: Modern corporate studio portrait shoot.
Pose: Arms crossed at chest level, shoulders relaxed, body turned 20–30° to the side, face turned toward the camera. Expression: neutral and confident with a subtle friendly smile.
Framing: Chest-up or waist-up (head-and-torso), centered, balanced negative space.

Outfit (dynamic selection):
- If the subject is male: Black suit jacket + plain white dress shirt (no tie), no logos.
- If the subject is female: Choose a professional, elegant business outfit:
  • Black or navy blazer
  • Plain, pattern-free white or cream blouse/shirt underneath
  • Modest neckline (closed or simple V-neck), no deep cleavage
  • If jewelry is present, keep it minimal (e.g., small earrings), no logos/branding
In all cases, fabrics must look realistic with natural wrinkles. Avoid flashy fashion elements.

Background: Plain dark-gray studio backdrop with a soft gradient (a subtle vignette is ok). No distracting objects.
Lighting: Softbox-style key light (45°), gentle fill, very subtle rim light; no harsh shadows. Natural skin tones, professional retouching while preserving realistic texture.
Camera: 85mm portrait lens feel, f/2.8–f/4, slight background blur, high sharpness (especially the eyes).
Color: Cinematic but natural, low saturation, clean contrast.

Rules: No text, no logos, no watermarks, no extra people. Hands/fingers must be natural and correct. No facial distortion, asymmetry, duplicated limbs, or artificial artifacts.
Output: High resolution, photorealistic, corporate profile photo quality.
```

</details>

<details><summary><b>Corsairs of the Crimson Void</b></summary>

```text
{
  "title": "Corsairs of the Crimson Void",
  "description": "A high-octane cinematic moment capturing a legendary space pirate and his quartermaster commanding a starship through a debris field during a daring escape.",
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Transform Subject 1 (male) into a rugged, legendary space pirate captain and Subject 2 (female) into his tactical navigator on the bridge of a starship. The image must be ultra-photorealistic, movie-quality, featuring cinematic lighting, highly detailed skin textures, and realistic physics. Shot on Arri Alexa with a shallow depth of field, the scene depicts the chaotic aftermath of a space battle, with the subjects illuminated by the glow of a red nebula and sparking consoles.",
  "details": {
    "year": "2492, Post-Terran Era",
    "genre": "Cinematic Photorealism",
    "location": "The battle-scarred command bridge of the starship 'Iron Kestrel', with massive blast windows overlooking a volatile red nebula.",
    "lighting": [
      "Dynamic emergency red strobe lights",
      "Cool cyan glow from holographic interfaces",
      "Soft rim lighting from the nebula outside"
    ],
    "camera_angle": "Eye-level medium shot with a 1:1 framing, focusing on the interplay between the two subjects and the chaotic background.",
    "emotion": [
      "Intense focus",
      "Adrenaline-fueled",
      "Determined"
    ],
    "color_palette": [
      "Deep crimson",
      "Gunmetal grey",
      "Cyan blue",
      "Void black"
    ],
    "atmosphere": [
      "Gritty",
      "Claustrophobic but epic",
      "Industrial Sci-Fi",
      "High-stakes"
    ],
    "environmental_elements": "Sparks showering from a damaged overhead conduit, floating dust motes caught in light beams, complex 3D holographic star maps in the foreground.",
    "subject1": {
      "costume": "A distressed, heavy leather trench coat with magnetic armor plating and a bandolier of futuristic tech.",
      "subject_expression": "A fierce, commanding scowl, shouting orders over the alarm.",
      "subject_action": "Gripping the manual override yoke of the ship with white-knuckled intensity."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "bright daylight",
        "clean environment",
        "cartoonish proportions",
        "medieval weaponry",
        "wooden textures"
      ],
      "exclude_styles": [
        "3D render",
        "illustration",
        "anime",
        "concept art sketch",
        "oil painting"
      ],
      "exclude_colors": [
        "pastels",
        "neon pink",
        "pure white"
      ],
      "exclude_objects": [
        "swords",
        "sailing ship wheels",
        "parrots"
      ]
    },
    "subject2": {
      "costume": "A form-fitting tactical flight suit with glowing data-interface gloves and a headset.",
      "subject_expression": "Sharp, calculating, and unphased by the chaos.",
      "subject_action": "Rapidly manipulating a floating holographic projection of the escape route."
    }
  }
}
```

</details>

<details><summary><b>Couple on a Night Beach</b></summary>

```text
A cinematic wide-angle shot of a couple walking hand-in-hand on a quiet beach at night, the couple appearing small and distant in the frame to emphasize the vast environment. Deep teal and navy blue color grading. A vast clear night sky. Gentle ocean waves slowly crashing onto the shore with white foam reflections.

Camera: smooth slow tracking shot from behind, wide framing, slight cinematic drift, stabilized motion  
Framing: couple placed in lower third, small scale, large negative space, emphasizing sky and ocean  
Lighting: low-light, moody, high contrast, soft shadows, subtle highlights on water and sand  
Motion: natural walking movement, soft wind blowing hair and clothes, slow wave movement  
Style: dreamy lo-fi, romantic atmosphere, film grain, anamorphic lens, shallow depth of field  
Quality: ultra-realistic, 8K, clean composition, no clutter  

Duration: 5–8 seconds  
FPS: 24fps cinematic
```

</details>

<details><summary><b>Covert Exchange in the Fog</b></summary>

```text
{
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Create an Ultra-Photorealistic, Movie-Quality scene depicting Subject 1 (male) and Subject 2 (female) involved in a covert exchange on a foggy train platform in 1940s London. The image must be photorealistic, featuring cinematic lighting and highly detailed textures of wool and steam. The aesthetic should look like it was shot on Arri Alexa with a cinematic depth of field, capturing the tension and romance of a noir thriller.",
  "details": {
    "year": "1944",
    "genre": "Cinematic Photorealism",
    "location": "A dimly lit, steam-filled railway platform in London at night, with the blurred silhouette of a locomotive in the background.",
    "lighting": [
      "Dramatic chiaroscuro",
      "Volumetric lighting through steam",
      "Cold atmospheric backlight",
      "Warm tungsten practical light from a station lamp"
    ],
    "camera_angle": "Over-the-shoulder close-up shot, focusing on the faces and the subtle hand exchange.",
    "emotion": [
      "Secretive",
      "Urgent",
      "Melancholic",
      "Tense"
    ],
    "color_palette": [
      "Steel blue",
      "Charcoal grey",
      "Sepia highlights",
      "Deep crimson"
    ],
    "atmosphere": [
      "Noir",
      "Mysterious",
      "Cinematic",
      "Foggy"
    ],
    "environmental_elements": "Thick billowing steam from the train engine, wet cobblestones reflecting light, vintage leather suitcases in the periphery.",
    "subject1": {
      "costume": "A textured heavy wool trench coat, a fedora hat slightly tipped forward, and leather gloves.",
      "subject_expression": "Stoic and alert, eyes darting to the side to check for surveillance.",
      "subject_action": "Discreetly slipping a small, sealed envelope into Subject 2's hand."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "bright daylight",
        "modern technology",
        "smartphones",
        "digital watches",
        "modern architecture"
      ],
      "exclude_styles": [
        "cartoon",
        "3d render",
        "anime",
        "oil painting",
        "sketch",
        "low resolution"
      ],
      "exclude_colors": [
        "neon green",
        "fluorescent pink",
        "oversaturated colors"
      ],
      "exclude_objects": [
        "cars",
        "airplanes",
        "plastic"
      ]
    },
    "subject2": {
      "costume": "A tailored 1940s skirt suit with a fur collar, a pillbox hat with a small mesh veil, and red lipstick.",
      "subject_expression": "Anxious but composed, biting her lip slightly, looking intently at Subject 1.",
      "subject_action": "Grasping Subject 1's hand tightly while receiving the envelope, pulling her coat closer."
    }
  }
}
```

</details>

<details><summary><b>Cozy Autumn Curb Lifestyle Portrait</b></summary>

```text
Ultra-realistic, high-quality, sharp 8K photo, 3:4 aspect ratio. Shot on iPhone 16 Pro Max. Preserve 100% facial likeness — do not change any facial features. Cute face. Lips fully closed.
Character & pose:
A young woman is sitting on a concrete curb in a relaxed, natural pose. One leg is slightly bent and resting on the curb, while the other hangs down. Her hands rest loosely near her knees, and her upper body leans slightly forward. She is looking off to the side, not at the camera.
Expression & makeup:
A soft, relaxed half-smile with fully closed lips. Clean Girl makeup with a natural, fresh complexion, subtle blush, and even skin tone.
Hairstyle:
Hair is styled in a high, voluminous, slightly messy bun. A few loose front strands softly frame her face, with realistic flyaways gently moved by the wind.
Outfit & footwear:
An oversized chocolate-brown sweatshirt with no prints, fitted black leggings, high white slouch socks, and chunky black leather lace-up boots in the Dr. Martens style. A delicate pendant necklace is visible.
Props:
Next to her on the curb is a clear plastic iced latte cup with a straw, along with a soft black fabric tote bag.
Background & atmosphere:
An autumn urban parking lot with parked cars in the background, trees with golden autumn leaves, and a tall street lamp. The sky is completely clear and bright blue. Cozy autumn vibe, casual street style.
Lighting & camera:
Bright natural sunlight with strong directional light creating crisp, contrasting shadows on the asphalt. Eye-level angle from the perspective of the seated model, full-body lifestyle composition capturing both the subject and surroundings.
```

</details>

<details><summary><b>Cozy Autumn Park Profile</b></summary>

```text
Style: Realistic, high-quality photorealistic photo.

Subject: A young woman with hair freely falling over her back and shoulders in soft waves (curls).

Camera Angle: Medium shot, taken approximately at eye level. The woman is shown in profile, turned to the right, looking somewhere to the side rather than at the camera.

Clothing: The woman is wearing a layered autumn outfit. She has on a light gray V-neck sweater made of textured ribbed knit. Over the sweater, she is wearing an oversized black leather biker jacket.

Pose & Mood: She is standing calmly and relaxed. Her facial expression is thoughtful and peaceful, with a slight half-smile.

Background: The scene takes place on an autumn park avenue. A wide asphalt path is covered with fallen orange and red leaves. Trees with lush, rich autumn foliage in warm shades (orange, red, and golden) grow on both sides of the path. The background is softly blurred with a bokeh effect, emphasizing the woman. The avenue can be seen leading deeper into the park.

Lighting: Soft, natural, diffused daylight, typical of a cloudy or gentle autumn day. The light falls softly on the profile of her face, gently illuminating her features and the texture of her clothing. Shadows are soft.

Makeup: Very natural, "no-makeup" makeup. Natural skin tone, defined eyebrows, a subtle touch of blush, and natural-toned lip balm.

Atmosphere: Calm, cozy, thoughtful, autumnal, melancholic.

Do not change my facial features.

Aspect ratio: 3:4

Realistic, high-quality, sharp 8K photograph, shot on iPhone 16 Pro Max.
```

</details>

<details><summary><b>Cozy Autumn Sherpa Portrait</b></summary>

```text
Main Subject (Woman):

Subject: A young woman with straight hair peeking out from under a hat.

Pose: She is standing in a half-profile, turned three-quarters to the right, while looking directly into the camera with a warm smile. Lips are closed. Her body is slightly turned to the side.

Clothing:
- A chunky knit olive green (khaki) beanie with a rectangular black patch on the front.
- A very oversized, fluffy, textured brown sherpa (sheepskin) jacket featuring a large abstract embroidered orange and black pattern (resembling flames or abstract shapes) across the back and sleeve.
- A delicate thin gold chain necklace visible around her neck.

Appearance & Makeup:
- Detailed makeup with defined, sharp winged eyeliner accentuating the eyes and thick eyelashes.
- Even skin tone with a soft blush on the cheeks.
- Soft natural pink lipstick.

Atmosphere: Calm, cozy autumn or early winter setting in a backyard or terrace with a relaxed lifestyle aesthetic.

Lighting: Natural, soft, diffused daylight (overcast or shaded), creating even illumination across the face.

Mood: Friendly, happy, confident, effortless, and stylish.

Camera Angle: Medium shot (waist up), eye-level perspective, slightly angled toward the camera.

Background:
- A fence made of vertical wooden planks.
- Evergreen trees (thuja or spruce) adding a rich green accent.
- A wooden structure (possibly a pergola or gazebo) with visible timber elements.
- A stone-paved courtyard.
- The background is softly blurred with a shallow depth of field to keep the focus on the woman.

Do not change the facial features.

Aspect ratio: 3:4

Ultra-realistic, high-quality, sharp 8K photograph, shot on iPhone 16 Pro Max.
```

</details>

<details><summary><b>Cozy Bedroom ASMR Video Scene</b></summary>

```text
Subject: Cozy bedroom ASMR, Motion: Slow, gentle hand movements tracing textures, turning book pages, caressing soft fabric, Optics: 50mm lens, shallow depth of field, soft focus, Motion: 5 cm/s camera drift, Lighting: Warm, soft ambient light, 2700K, Style: Cinematic, serene, peaceful, Audio: Gentle whispers, soft tactile sounds, subtle rain ambiance, Continuity: 8s clip, 4K resolution, 60fps, 16:9 aspect ratio
```

</details>

<details><summary><b>Cozy Cabin in a Rainy Forest</b></summary>

```text
Create an image of a cozy wooden cabin nestled in a misty forest during heavy rain. Warm orange firelight glows softly through a frosted window. Dark pine trees frame the scene. Rain streaks down the window glass. Soft distant lightning briefly illuminates the wet trees. The camera slowly pushes toward the cabin window. Professional color grading. 24fps. Highly detailed. Premium quality.
```

</details>

<details><summary><b>Cozy Christmas Smile</b></summary>

```text
Use the uploaded photo of the person as the main subject.
Preserve the person’s REAL face, facial features, skin tone, hairstyle, and identity exactly as in the original photo. Do not change age or facial structure.

Gently adjust the facial expression to add a natural, warm, and friendly smile.
The smile should look realistic and subtle, not exaggerated or forced.
No change to facial proportions.

Outfit:
• A cozy knitted Christmas sweater with a classic reindeer (deer) pattern
• A bright red Santa hat with white fur trim and pom-pom
• Clothing should look naturally worn and well-fitted

Scene & Atmosphere:
• Warm, cozy New Year indoor atmosphere
• Soft golden ambient lighting
• Background may include:
  – A softly blurred Christmas tree
  – Warm fairy lights with gentle bokeh
  – Minimal holiday decorations
• Background slightly out of focus

Mood & Style:
• Cheerful, friendly, joyful New Year vibe
• Feels candid and spontaneous, not staged
• Festive but realistic

Camera & Quality:
• Keep the original camera angle and framing as much as possible
• Shallow depth of field
• High-resolution, photorealistic
• Natural skin texture and realistic fabric details

Do NOT add:
• Text, logos, or watermarks
• Exaggerated facial expressions
• Cartoon or stylized effects
• Face distortion or identity changes

The final image should feel like a fun, warm New Year moment captured naturally, perfect for social media or personal sharing.
```

</details>

<details><summary><b>Cozy Couch Lamp Close-up</b></summary>

```text
{
  "category": "COZY_COUCH_LAMP_CLOSEUP",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Messy bun with face-framing tendrils",
      "texture": "Visible strands, natural frizz",
      "movement": "Loose strands fall near cheeks"
    },
    "face": {
      "eyes": "Soft eye contact, warm catchlights",
      "makeup": "Minimal, dewy, natural",
      "skin_details": "Pores, natural texture, no smoothing"
    },
    "clothing": {
      "outfit": "Casual cozy knit sweater (no text)",
      "texture": "Knit weave visible, realistic folds"
    },
    "accessories": {
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Close-up candid",
    "orientation": "Slightly above angle, relaxed",
    "hands": "One hand holding mug near chin (fingers correct)",
    "gaze": "Gentle eye contact",
    "expression": "Soft smile, cozy"
  },
  "setting": {
    "environment": "Living room couch corner",
    "background_elements": [
      "Warm orange lamp glow behind",
      "Blanket texture visible",
      "Slight lived-in clutter blurred"
    ],
    "depth": "Face sharp, lamp bloom behind, soft background"
  },
  "camera": {
    "shot_type": "Close-up portrait",
    "angle": "Slightly above eye level",
    "focal_length_equivalent": "26mm phone or 50mm pro",
    "framing": "4:5, face dominant",
    "focus": "Eyes sharp"
  },
  "lighting": {
    "source": "Warm tungsten lamp + faint ambient",
    "direction": "Side/front warm",
    "highlights": "Soft glow on cheeks and hair",
    "shadows": "Gentle, comforting"
  },
  "mood_and_expression": {
    "tone": "Relaxed, intimate, relatable",
    "expression": "Soft smile",
    "atmosphere": "Warm, tactile, homey"
  },
  "style_and_realism": {
    "style": "Photorealistic iPhone-candid vibe",
    "imperfections": "Mild grain, slightly imperfect WB"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild phone sensor grain",
    "motion_blur": "None on face"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "plastic skin", "over-smoothing",
    "extra fingers", "warped mug",
    "readable text", "logo", "watermark"
  ]
}
```

</details>

<details><summary><b>Cozy Cyber Gamer Girl Portrait</b></summary>

```text
Composition & Camera Angle:** Close-up selfie-style portrait, framed from the chest up, 3:4 aspect ratio. The camera is positioned close to the face at eye level, creating the authentic look of an iPhone 16 Pro Max selfie.
Pose & Expression: The girl gently tilts her head to the side, resting her cheek softly on her left hand with the oversized sweater sleeve covering part of her palm. One shoulder is slightly exposed. Her eyes are closed, and her lips form a soft playful pout with no teeth visible. The expression is relaxed, sweet, effortless, and subtly flirty.
Facial Features & Hair: Preserve the exact facial features without changing identity. , straight, healthy hair with a clean middle part, naturally falling over the shoulders with highly realistic strands.
Makeup: Flawless Clean Girl makeup with Soft Glam touches — smooth even skin, fluffy defined lashes, neatly styled brows, a soft natural blush, and full glossy lips in a natural pink shade.
Clothing & Accessories: Cozy oversized knitted sweater in a creamy milk color with a rich textured knit. The main accent is large white over-ear gaming headphones with vibrant RGB lighting (green, blue, and purple gradient). The microphone tip glows with a soft blue light.
Nails: Long square-shaped milky nails.
Lighting: Low-light photography. Soft frontal illumination resembling monitor screen light, creating delicate highlights on the skin and glossy lips. Colored neon reflections from the headphones subtly illuminate the face and hair.
Background & Atmosphere: A dark room with a heavily blurred background (deep bokeh), featuring a soft purple neon fairy light. Cozy cyber aesthetic, Y2K vibe, relaxed late-night gamer girl mood.
Quality: Hyper-realistic, cinematic lighting, 8K, ultra-detailed skin pores, realistic hair, and highly detailed knitted fabric texture.
```

</details>

<details><summary><b>Cozy Home Scene with Natural Light</b></summary>

```text
Imagine a setting in a cozy home environment. The lighting is natural and soft, coming from large windows, casting gentle shadows. Include details such as a comfortable sofa, warm colors, and personal touches like a soft blanket or a favorite book lying around. The atmosphere should feel inviting and real, perfect for a relaxed day at home.
```

</details>

<details><summary><b>Cozy Minimalist Kitchen Portrait</b></summary>

```text
Hyper-realistic medium shot of a young woman standing in a modern minimalist kitchen.

Pose: She is standing, casually leaning against a gray kitchen countertop. Her right hand rests naturally on the surface, and her body is slightly turned to the left while she looks directly into the camera. The pose is relaxed, confident, and welcoming.

Clothing: She is wearing a white oversized sweatshirt with voluminous lantern sleeves and long cuffs. The sweatshirt is tucked into light blue high-waisted jeans that fit her hips and have a straight-leg cut.

Hair: Smooth, straight hair worn down, falling naturally.

Makeup: Natural “no-makeup” makeup with softly defined eyes, nude lipstick, and radiant skin.

Mood: Cozy, calm, effortless, and warm. She has a gentle half-smile.

Background: A modern kitchen with light gray matte cabinets. On the countertop to her left is a white textured ribbed vase holding a single white rose and dried gypsophila branches.

Lighting: Soft natural daylight, as if coming from a large window. Diffused light creates gentle shadows and highlights the texture of the clothing and skin.

Camera angle: Eye-level, medium shot framed from the knees or thighs to the top of the head. Balanced composition with the subject centered.

Do not change the facial features. 3:4 vertical. Photorealistic, ultra-detailed 8K, shot on iPhone 16 Pro.
```

</details>

<details><summary><b>Cozy Siamese Cat Portrait</b></summary>

```text
A detailed, intimate close-up portrait of a young woman gently holding and kissing a Siamese cat.
The woman’s defining feature is her incredibly voluminous, fluffy, naturally curly hair, framing her face like a soft cloud with rich texture and a slightly wild elegance.
She is seated, cradling a Siamese cat in her arms. Her right hand softly supports the cat’s face, showcasing long square-shaped nails with a glossy white manicure. Her lips are pursed in a gentle kiss (duck face), almost touching the top of the cat’s head.
Camera angle: close-up portrait from a slightly low angle, emphasizing the tenderness and intimacy of the moment.
Her eyes are softly squinted, with a dreamy, relaxed, and content expression.
She wears a simple black spaghetti-strap top.
Makeup is minimalistic in the clean girl style: fresh skin, subtle eye definition, natural brows, and nude lips.
The cat is a classic Siamese with seal-point coloring: dark face, ears, and paws. It sits comfortably in her arms, its head nestled between her hand and face. Its eyes are half-closed with a calm, sleepy, slightly indifferent expression while looking directly into the camera.
Lighting: soft natural daylight coming from the side through a nearby window, creating delicate shadows and beautifully highlighting the texture of her curls and the cat’s fur.
Background: a clean, neutral white interior with part of a white window frame and windowsill visible on the left.
Mood: warm, cozy, affectionate, and intimate. Preserve the exact facial features and identity without alteration.
Ultra-realistic, highly detailed 8K photography, shot on iPhone 16 Pro, 3:4 aspect ratio.
```

</details>

<details><summary><b>Cozy Sofa Portrait</b></summary>

```text
Prompt:
An ultra-realistic mobile photograph taken with an iPhone 17 Pro Max, RAW capture, vertical 9:16 format, with a completely authentic look, like a spontaneous shot taken by a real person, same sensitivity. Without any signs of AI generation, no CGI, no anime, no 3D render, no illustration, no exaggerated filters.
Keep exactly the same photographic angle, an almost full-body shot captured from a front perspective at chest height, with a slight three-quarter orientation. Preserve exactly the same composition and the same pose: the woman is sitting on an upholstered sofa, with one leg bent on the seat and the other relaxing down to the floor. The torso remains upright and slightly turned to one side. One arm gently crosses the body holding the opposite forearm, while the other hand rests relaxed on the leg. The head is tilted to one side with the gaze directed out of frame, conveying a calm, introspective, and natural expression.
Maintain the same visual style, inspired by an intimate and elegant lifestyle editorial shoot. The scene takes place in a modern and cozy living room with a fabric sofa, neutral cushions, wooden floor, and a large decorative mirror on the wall, with minimalist and warm decor.
Keep the same outfit: ribbed crop top with a high halter neck, tight jeans with large rips on the knees and frayed hems. The model remains completely barefoot. The clothing features natural folds, authentic texture, and a completely realistic fit. Do not specify the color or length of the hair.
The lighting comes from a large side window, generating soft natural light that delicately shapes the face and body, with subtle shadows and a warm, relaxed atmosphere. The skin features hyper-realistic texture with visible pores, slight natural tone variations, and authentic anatomical details. The fabric of the top, the worn denim of the jeans, the sofa upholstery, and the wooden floor show highly detailed and completely natural textures.
Shallow depth of field with the model perfectly in focus and the background softly blurred with natural bokeh. Balanced composition, contemporary editorial aesthetic, and a sense of spontaneity typical of a photograph taken during an everyday moment.
High-end editorial photography with a completely real appearance, high dynamic range, exceptional sharpness, perfectly balanced exposure, and a result totally indistinguishable from a photograph captured with an iPhone 17 Pro Max. No digital artifacts, no AI look, and a completely authentic photographic finish.
stylized and proportioned figure, semi curvy, hourglass,    
9:16 format
```

</details>

<details><summary><b>Craftsman with Newspaper Paper Figures</b></summary>

```text
A cinematic, warm-toned close-up photograph of a craftsman working at a wooden desk in the evening. In sharp focus on the table are two delicate paper figures made from newspaper: an origami raccoon sitting attentively and a small paper boy holding an umbrella. The man’s hand gently holds and positions the paper doll, while his face appears softly blurred in the background, showing deep concentration. A single desk lamp casts dramatic, golden light from above, creating long shadows and highlighting the fine paper textures. Shallow depth of field, soft bokeh background, realistic photography style, intimate and whimsical atmosphere, storytelling composition, high contrast lighting, handcrafted aesthetic.
```

</details>

<details><summary><b>Creative Booklet Cover Design Program</b></summary>

```text
Create a professional program to create a booklet cover in different colors with the possibility of adding images to complement the painting that contribute to attracting the reader's attention distributed in a superior format with the choice of type, colors and Font Format for the product name ""brief summary 60 words* ""author ""and serial number" * conjure the attached design to simulate a more creative design with the possibility of entering data above
```

</details>

<details><summary><b>Creative Image Generation for Digital Art</b></summary>

```text
Act as a creative digital artist. You are skilled in generating unique and visually appealing images for digital use.

Your task is to:
- Create original and imaginative images that capture attention
- Focus on artistic style, color harmony, and visual storytelling
- Ensure images are suitable for digital platforms and social media

You will:
- Use vibrant colors and innovative designs
- Adapt styles based on provided themes or prompts
- Maintain high resolution and quality standards

Rules:
- Avoid using copyrighted elements
- Ensure all images are appropriate for a general audience
```

</details>

<details><summary><b>Crewelwork Embroidery of a Sleeping Fox</b></summary>

```text
A hand-embroidered crewelwork panel of a red fox curled up asleep, stitched on natural cream linen and stretched in a round light wooden embroidery hoop with a brass tightening screw at the top. The fox lies in the center with its eyes closed and its bushy tail wrapped around its body, its fur worked in long-and-short stitch in rust, copper, cream, and dark brown wool so the raised threads follow the direction of the fur. Around it, a wreath of woodland plants: satin-stitch bluebells arching over the upper left, clusters of pale blue French-knot forget-me-nots scattered across the top and sides, sage-green fern fronds in fishbone and stem stitch on both sides, and two pairs of textured acorns with oak leaves along the bottom. Soft even daylight shows the thread texture and slight shine of the wool. Top-down photo, the hoop centered in the frame with plain linen fabric visible around it, wide landscape 16:9. Cozy, handmade, storybook mood. No text, no hands, no needles.
```

</details>

<details><summary><b>Crimson Waltz in the Rain</b></summary>

```text
{
  "title": "Crimson Waltz in the Rain",
  "description": "A visually stunning, cinematic moment of a woman finding joy in solitude, dancing on a rain-slicked European street at twilight.",
  "prompt": "You will perform an image edit creating an Ultra-Photorealistic masterpiece. The image must be photorealistic, utilizing cinematic lighting and be highly detailed, looking as if it was shot on Arri Alexa with a shallow depth of field. The scene features a female subject dancing freely in the rain on a cobblestone street. The rain droplets are frozen in time by the shutter speed, catching the amber glow of streetlamps.",
  "details": {
    "year": "Timeless Modern",
    "genre": "Cinematic Photorealism",
    "location": "A narrow, empty cobblestone street in Paris at dusk, wet with rain, reflecting the warm glow of vintage streetlamps and shop windows.",
    "lighting": [
      "Cinematic rim lighting",
      "Warm amber streetlights",
      "Soft blue ambient twilight",
      "Volumetric fog"
    ],
    "camera_angle": "Eye-level medium shot, emphasizing the subject's movement against the bokeh background.",
    "emotion": [
      "Liberated",
      "Joyful",
      "Serene"
    ],
    "color_palette": [
      "Deep obsidian",
      "Amber gold",
      "Rainy blue",
      "Vibrant crimson"
    ],
    "atmosphere": [
      "Romantic",
      "Melancholic yet joyful",
      "Atmospheric",
      "Wet"
    ],
    "environmental_elements": "Rain falling diagonally, puddles reflecting lights on the ground, mist swirling around ankles.",
    "subject1": {
      "costume": "red hat",
      "subject_expression": "Eyes closed in pure bliss, a soft smile on her lips, raindrops on her cheeks.",
      "subject_action": "dancing"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "bright daylight",
        "dry pavement",
        "crowds",
        "vehicles",
        "sunglasses"
      ],
      "exclude_styles": [
        "cartoon",
        "3D render",
        "illustration",
        "oil painting",
        "sketch"
      ],
      "exclude_colors": [
        "neon green",
        "hot pink"
      ],
      "exclude_objects": [
        "umbrellas",
        "modern cars",
        "trash cans"
      ]
    }
  }
}
```

</details>

<details><summary><b>Cultural Superhero Movie Poster</b></summary>

```text
Create an ultra-realistic, high-budget cinematic movie poster of ${superhero_name}, reimagined as if the character originated from ${country_or_culture}.

This image must look like an official theatrical poster for a live-action superhero film released worldwide.
The composition, lighting, typography, and tone should match real modern Hollywood movie posters.

FORMAT:
Aspect ratio: 9:16 (vertical theatrical poster).

SETTING:
The scene takes place at night in the capital city of ${country_or_culture}.
The environment reflects the city’s real architecture, atmosphere, and cultural identity, remaining geographically accurate and believable.

COMPOSITION & CAMERA ANGLE:
– dramatic low-angle perspective, looking up at the hero
– iconic, powerful stance suitable for a main movie poster
– medium-to-full body framing
– character visually dominant, city subtly visible behind
– cinematic depth with slight background blur

ATMOSPHERE:
– cinematic fog, smoke, and atmospheric haze
– rain falling through volumetric light
– wet surfaces reflecting city lights
– dramatic shadows and contrast
– epic but grounded realism

CHARACTER REALISM (CRITICAL):
– fully photorealistic human anatomy and proportions
– practical, wearable costume design
– subtle cultural elements from ${country_or_culture} integrated naturally
– realistic fabric, leather, metal, armor with wear, scratches, dirt
– no comic-book exaggeration, no cosplay look

LIGHTING:
– dramatic cinematic lighting
– strong rim light defining the silhouette
– controlled highlights and deep shadows
– volumetric light interacting with rain and fog

POSTER TEXT (ENGLISH ONLY – REALISTIC):
Include realistic, professionally designed movie poster text that matches the character’s origin and tone.

Examples of text placement and style:
– Main title: "${movie_title}"
– Tagline (origin-related, serious tone): "${tagline}"
– Credits block at the bottom (small, realistic):
  "A ${studio_style} Production  
   Directed by ${director_style}  
   Starring ${superhero_name}"

Typography must be cinematic, clean, modern, and realistic — no fantasy fonts, no comic lettering.

STYLE & FINISH:
Ultra-photorealistic live-action realism
Cinematic color grading
High dynamic range (HDR)
Premium poster polish
Sharp subject, controlled depth

NEGATIVE CONSTRAINTS:
No cartoon
No anime
No illustration
No comic-book art style
No exaggerated colors
No unrealistic fantasy elements
No watermarks

The final image should feel like a real, official movie poster —
localized in identity, grounded in realism, cinematic in every detail.
```

</details>

<details><summary><b>Curly-Haired Mirror Selfie</b></summary>

```text
{
  "image_analysis": {
    "environment": {
      "type": "Indoor",
      "location_type": "Bathroom or bedroom (indicated by mirror and sink edge)",
      "spatial_depth": "Shallow depth of field due to mirror reflection",
      "background_elements": "Grey painted wall, white door frame or window frame edge on the left, electrical outlet on the right, partial view of a white sink"
    },
    "camera_specs": {
      "lens_type": "Smartphone wide-angle lens (reflected)",
      "angle": "Eye-level, straight on relative to the mirror",
      "perspective": "Selfie reflection",
      "focus": "Sharp focus on the subject, slight softness on the background reflection"
    },
    "lighting": {
      "condition": "Natural daylight mixed with ambient indoor light",
      "sources": [
        {
          "source_id": 1,
          "type": "Natural Window Light",
          "direction": "From the left (subject's right)",
          "color_temperature": "Cool/Neutral daylight",
          "intensity": "Moderate to High",
          "effect_on_subject": "Highlights the texture of the ribbed top, illuminates the face profile and torso, creates soft gradients across the midriff"
        }
      ],
      "shadows": "Soft shadows cast on the right side of the subject's body (away from window) and under the bust line"
    },
    "subject_analysis": {
      "identity": "Young woman (face partially obscured by hair and angle)",
      "orientation": "Body angled 45 degrees to the left, Head turned to profile view facing left",
      "emotional_state": "Calm, focused, casual confidence",
      "visual_appeal": "Aesthetic, fit, natural",
      "posture": {
        "general_definition": "Standing upright, slight hip sway",
        "feet_placement": "Not visible in frame",
        "hand_placement": "Left hand holding the phone (visible), Right arm down by side (partially visible)",
        "visible_extent": "From top of head to upper hips/thighs"
      },
      "head_details": {
        "hair": {
          "color": "Dark Brown / Espresso",
          "style": "Shoulder-length, layered cuts",
          "texture": "Curly / Wavy, voluminous, messy-chic",
          "interaction_with_face": "Strands falling over the forehead and framing the cheekbones, partially obscuring the eye"
        },
        "ears": "Covered by hair",
        "face": {
          "definition": "Side profile view",
          "forehead": "Partially covered by curls",
          "eyebrows": "Dark, arched, natural thickness (partially visible)",
          "nose": "Straight bridge, slightly upturned tip",
          "mouth": "Lips relaxed, closed, full lower lip",
          "chin": "Defined, soft curve",
          "expression": "Neutral, concentrating on the reflection",
          "makeup": "Minimal or natural look"
        }
      },
      "body_details": {
        "body_type": "Ectomorph-Mesomorph blend (Slim with defined curves)",
        "skin_tone": "Light olive / Fair",
        "neck": "Slender, clavicles slightly visible",
        "shoulders": "Narrow, relaxed",
        "chest_area": {
          "ratio_to_body": "Proportionate to slim frame",
          "visual_estimate": "Moderate bust size",
          "undergarment_indications": "No distinct strap lines visible; likely seamless or no bra",
          "nipple_visibility": "Not explicitly defined due to fabric thickness",
          "shape_in_clothing": "Natural teardrop shape supported by tight fabric"
        },
        "midsection": {
          "belly_button": "Visible, vertical orientation",
          "ratio": "Slim waist, defined abdominals (linea alba visible)",
          "relation_to_chest": "Significantly narrower (hourglass suggestion)",
          "relation_to_hips": "Tapers inward before flaring to hips"
        },
        "hips_area": {
          "ratio_to_waist": "Wider than waist",
          "visibility": "Top curve visible",
          "width": "Moderate flare"
        }
      },
      "attire": {
        "upper_body": {
          "item": "Long-sleeve crop top",
          "style": "Henley neck with buttons (3 visible, unbuttoned at top), Ribbed knit texture",
          "color": "Light Brown / Taupe / Mocha",
          "fit": "Form-fitting / Tight",
          "fabric_drape": "Stretches over bust, hugs waist, cuffs at wrist"
        },
        "lower_body": {
          "item": "Pants / Leggings (Waistband only)",
          "color": "Heather Grey",
          "style": "Low-rise",
          "material": "Jersey or cotton blend",
          "visibility": "Only the waistband and upper hip area visible"
        },
        "accessories": {
          "hands": "Ring on left ring finger (thin band)",
          "wrist": "None visible"
        }
      }
    },
    "objects_in_scene": [
      {
        "object": "Smartphone",
        "description": "Black case, multiple camera lenses (iPhone Pro model style)",
        "function": "Capture device",
        "position": "Held in left hand, right side of image",
        "color": "Black"
      },
      {
        "object": "Mirror",
        "description": "Reflective surface containing the entire subject",
        "function": "Medium for the selfie",
        "position": "Foreground plane"
      },
      {
        "object": "Electrical Outlet",
        "description": "Standard white wall outlet",
        "position": "Background, right side behind subject",
        "color": "White"
      },
      {
        "object": "Sink",
        "description": "White ceramic basin edge",
        "position": "Bottom right corner",
        "color": "White"
      }
    ],
    "negative_prompts": [
      "blur",
      "noise",
      "distortion",
      "deformed hands",
      "missing fingers",
      "extra limbs",
      "bad anatomy",
      "overexposed",
      "underexposed",
      "cartoon",
      "illustration",
      "watermark",
      "text"
    ]
  }
}
```

</details>

<details><summary><b>Custom AI Image Creation</b></summary>

```text
Create an AI-generated picture. You can specify the theme or style by providing details such as ${theme:landscape}, ${style:realistic}, and any specific elements you want included. The AI will use these inputs to craft a unique visual masterpiece.
```

</details>

<details><summary><b>Custom Logo Design for a Website</b></summary>

```text
Act as a Logo Designer. Your task is to create a unique and visually appealing logo for a website. You will:
- Gather information about the brand's identity and target audience
- Develop design concepts that align with the brand's values
- Use colors and typography that enhance brand recognition
- Ensure the logo is versatile for various digital platforms
- Provide the logo in PNG formats

Rules:
- Adhere to the brand's style guide if provided
- Use a minimalist design approach unless specified otherwise
- Prioritize clarity and readability

Variables:
- ${brandName:CouponAmI.com} - Name of the brand
- ${stylePreference:Modern} - Style preference for the logo
- ${colorScheme:#6085fd} - Preferred color scheme
```

</details>

<details><summary><b>Custom Poster and Wallpaper Design</b></summary>

```text
Act as an expert digital artist. You will create a poster or wallpaper with exceptional rendering quality. The process requires the user to upload an image that serves as the base for the design. Ask the user to specify the character or persona they want to feature in the poster.

You will:
- Analyze the uploaded image for style and composition.
- Render a poster or wallpaper incorporating the specified character.
- Ensure the design is visually striking and high-resolution.

Rules:
- The user must upload an image.
- Confirm the character details with the user before proceeding.
```

</details>

<details><summary><b>Customizable Avatar Style Generator</b></summary>

```text
Act as an Avatar Customization Expert. You are skilled in transforming photos into personalized avatars in various styles.

Your task is to:
- Take an uploaded photo and generate an avatar.
- Allow users to select from different styles such as cartoon, realistic, anime, and more.
- Provide customization options for features like hair, eyes, and accessories.

Rules:
- Ensure high-quality output for each style.
- Respect user input and privacy.

Variables:
- ${style:cartoon} - the style of avatar to generate
- ${photo} - the photo uploaded by the user
```

</details>

<details><summary><b>Cut-Paper Shadow Box of a Coral Reef</b></summary>

```text
A museum-quality photograph of a deep wooden shadow box hanging on a pale grey gallery wall, seen straight on at eye level, 16:9 landscape composition with the box filling most of the frame. Inside the box is a layered cut-paper diorama of a coral reef aquarium, made of about twelve hand-cut paper layers spaced a few millimeters apart so each layer casts a soft shadow on the one behind it. The back layers are smooth gradients of turquoise and deep teal paper suggesting open water, with faint wavy cut-outs of light rays; middle layers hold silhouettes of distant coral in muted blue-green; the front layers are rich and colorful: branching coral in coral pink and salmon, a round brain coral in ochre with a carved maze pattern, a fan coral in violet with delicate lace-like cut holes, swaying sea grass in two greens, and a bright magenta anemone with fringed tentacles cut in fine strips. A single small yellow fish with a thin black stripe and a tiny punched eye swims near the anemone, slightly raised on its own layer. Columns of small circular bubbles, punched from white and pale aqua paper, rise on the right. A sandy floor of textured cream paper with a few tiny cut shells runs along the bottom. The box frame is natural oak, about 8 cm deep, with a clean inner white mat and a sheet of museum glass showing only a faint reflection at one corner. Soft directional light from the left side lights up the paper edges and creates crisp, layered shadows inside the box, emphasizing depth; the paper fibers, cut edges, and slight curl of thin pieces are visible. Calm, wondrous mood, true colors, craft and fine-art photography, sharp focus across the whole diorama. No text, no letters, no labels, no signature, no watermark, no people.
```

</details>

<details><summary><b>Cute 3D Periodic Table Characters</b></summary>

```text
I want to create a 4k image of 3D character of each element in the periodic table. I want them to look cute but has distinct features
```

</details>

<details><summary><b>Cyanotype Print of Coastal Ferns and Seaweed</b></summary>

```text
A wide, flat-lay photograph of a large handmade cyanotype print lying on a weathered pale oak worktable, the print filling most of the frame. The cyanotype shows a carefully arranged composition of coastal plants and sea finds as crisp white silhouettes on a deep, rich Prussian blue background: long feathery fronds of maidenhair and bracken ferns sweeping in from the left, delicate sprigs of sea lavender and Queen Anne's lace in the center, a branching strand of bladderwrack seaweed with its small air bladders, two ginkgo leaves, a tiny scallop shell, and the soft translucent outline of a dandelion seed head on the right. Where the plants were thin or slightly lifted from the paper, the silhouettes fade into pale sky blue and powder blue half-tones with fine visible veins, giving a ghostly, layered depth. The paper is thick, cold-pressed cotton watercolor paper with a slightly deckled, untrimmed edge, uneven hand-brushed borders where the blue chemistry stops in loose, streaky brush marks, and a few tiny drips and speckles. Around the print on the table: a glass contact frame leaning at the top edge, a small amber glass bottle, a wide flat hake brush with blue-stained bristles, a pair of brass tweezers, and a few loose fern fronds and seaweed pieces waiting for the next print. Soft, even morning daylight from a north window, gentle shadows, true-to-life color with the intense cyan blue as the hero, calm handmade studio atmosphere, extremely sharp paper texture and botanical detail. Composition: print slightly rotated, generous breathing room, 16:9 landscape framing. No people, no hands, no text, no labels, no signature, no watermark.
```

</details>

<details><summary><b>Cyber Security Character Workflow</b></summary>

```text
{
  "name": "Cyber Security Character",
  "steps": [
    {
      "step_1": "Facial Identity Mapping",
      "description": "Maintain 100% facial consistency based on the provided reference photos. Features: medium-length wavy red hair and a composed, visionary tech-innovator expression."
    },
    {
      "step_2": "Tactical Gear & Branding",
      "description": "Outfit the subject in a sleek red tactical jacket with intricate gold circuitry textures. Correctly integrate the '${Brand}' name and the specific '${Brand First Letter}' logo emblem onto the chest piece."
    },
    {
      "step_3": "Cybernetic Enhancement",
      "description": "Apply subtle, minimalist gold-accented cybernetic interface patterns onto the skin of the face, ensuring they blend naturally with the {Style:Cyberpunk} aesthetic."
    },
    {
      "step_4": "Environmental Integration",
      "description": "Design a background featuring the ${Country} flag merged with glowing golden digital circuits. Include a distant cinematic futuristic skyline of a ${Country} metropolis (${Style:Cyberpunk} ${City})."
    },
    {
      "step_5": "Lighting & Cinematic Render",
      "description": "Utilize warm, dramatic side lighting from the right to cast a soft silhouette onto the background. Render in 4K ultra-realistic quality with hyper-detailed textures."
    }
  ]
}
```

</details>

<details><summary><b>Cyberpunk Fallen Seraph</b></summary>

```text
A Fallen Angel Seraphim on a glitching throne, blending angelic and cyberpunk elements in a dark, surreal style.
```

</details>

<details><summary><b>Cyberpunk Netrunner in a Neon Alley</b></summary>

```text
{
  "prompt": "You will perform an image edit transforming the male subject into a fugitive netrunner in a gritty, high-tech future. The result must be an Ultra-Photorealistic, Movie-Quality image resembling a frame from an IMAX blockbuster. The scene is set in a rain-slicked neon alleyway where the subject is hiding. Ensure the image is highly detailed, utilizing cinematic lighting and realistic physics, shot on Arri Alexa with a shallow depth of field to isolate the subject from the chaotic background.",
  "details": {
    "year": "${year:2084}",
    "genre": "Cinematic Photorealism",
    "location": "A narrow, debris-strewn alleyway in a vertically built cyberpunk mega-city. The ground is wet asphalt reflecting the chaotic glow of neon kanji signs from skyscrapers above.",
    "lighting": [
      "Volumetric neon blue and magenta backlighting",
      "Soft cool fill light on face",
      "High-contrast shadows",
      "Specular highlights on wet surfaces"
    ],
    "camera_angle": "Eye-level medium shot with shallow depth of field (bokeh background) to focus on the subject's intense expression.",
    "emotion": [
      "Paranoid",
      "Focused",
      "Urgent"
    ],
    "color_palette": [
      "Electric Cyan",
      "Neon Pink",
      "Deep Shadow Black",
      "Rain Silver",
      "Cold Blue"
    ],
    "atmosphere": [
      "Dystopian",
      "Claustrophobic",
      "Wet",
      "Gritty",
      "High-Tech Low-Life"
    ],
    "environmental_elements": "Falling rain droplets frozen in time, swirling steam rising from vents, flickering holographic advertisements reflecting in muddy puddles.",
    "subject1": {
      "costume": "A heavily textured, waterproof black tech-wear windbreaker with illuminated geometric patterns, fingerless tactical gloves, and a metallic neural interface port visible on the temple.",
      "subject_expression": "Intense concentration mixed with anxiety, sweat and rain dripping down the face.",
      "subject_action": "Rapidly typing on a floating holographic keyboard projected from a wrist-mounted cyberdeck while glancing over his shoulder."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "daylight",
        "sunshine",
        "blue sky",
        "clean surfaces",
        "dryness",
        "warm lighting"
      ],
      "exclude_styles": [
        "cartoon",
        "anime",
        "3D render",
        "painting",
        "low resolution",
        "blurry",
        "sketch"
      ],
      "exclude_colors": [
        "warm sepia",
        "pastels",
        "bright white",
        "beige"
      ],
      "exclude_objects": [
        "cars",
        "trees",
        "pets",
        "flowers"
      ]
    }
  }
}
```

</details>

<details><summary><b>Cyberpunk Portrait with Glitch Frame</b></summary>

```text
Cyberpunk portrait, Iranian woman 2026, neon magenta and cyan rim light, wet reflective skin, subtle holographic eyeliner. Expression lives in the eyes only: one brow flattened, the other slightly cocked, eyes narrowed with a cold amused squint — mockery without a smile. Below, a clean glitchy sketch-frame box with hurried handwritten marker text: "همین؟".
```

</details>

<details><summary><b>Daguerreotype of a Clockmaker's Workbench</b></summary>

```text
An antique clockmaker's workbench covered with open pocket watches, scattered brass gears, a small bell-jar dome over a skeleton clock, a jeweler's loupe, fine tweezers, and an oil lamp, photographed as an 1850s daguerreotype. The image sits on a silver-mirrored copper plate with a cool silvery-grey tonal range, deep velvety shadows, and soft bright highlights that shimmer like polished metal. Extremely fine detail in the gear teeth and engraved watch movements, with shallow depth of field from a long exposure. Light falls softly from a tall window on the left, catching the brass edges and the glass dome. Behind the bench, a wooden wall cabinet with small drawers and a few hanging wall clocks fades into gentle darkness. Authentic plate artifacts: subtle tarnish halos around the edges, faint swirl marks, tiny dust specks, and a slight blue-bronze iridescence in the darkest areas, framed by a thin ornate brass mat with rounded corners. Calm, quiet, timeless mood. Wide landscape 16:9. No people, no hands, no text, no letters, no logos.
```

</details>

<details><summary><b>Daiquiri Cocktail Cinematic Video</b></summary>

```text
A cinematic 9:16 vertical video of a Daiquiri  cocktail placed on a wooden bar table. The camera is positioned at a slight angle on the front of the glass. The cocktail glass is centered and the table slowly rotates 360 degrees to showcase it. Soft, warm lighting and realistic reflections on the glass. Background slightly blurred. Smooth slow zoom in. No text overlay, no people — focus only on the drink and table, crisp details and realistic liquid movement.
```

</details>

<details><summary><b>Dark Romance Santa Muerte Portrait</b></summary>

```text
Photorealistic close-up female portrait, optimized for a 3:4 aspect ratio. Camera angle — straight-on, at eye level.

Pose and mood: The woman has her head slightly turned, with her dreamy gaze directed upward and to the side. Her right hand gracefully touches her neck near the collarbone. The overall atmosphere is mystical and glamorous, with a pronounced Dark Romance and Soft Glam aesthetic.

Makeup and face: Creative Halloween makeup inspired by a sugar skull (Santa Muerte), covering half of the face. The left side of the face has flawless skin, fluffy lashes, and closed lips in a natural shade. The right side is stylized as a skull: a dark eye surrounded by sparkling rhinestones, a black nose tip, and a dark line imitating the jaw. Symmetrical patterns made of tiny crystals are arranged on the forehead and chin.

Hairstyle and manicure: Long, thick, wavy hair, worn loose over the shoulders with highly realistic strands and contours. Nails are long, with a precise square shape and glossy black polish.

Clothing and accessories: On her head is a massive crown-like floral wreath made of large artificial white roses, with long transparent rays extending outward to create a glowing halo effect. She is wearing a white outfit with a voluminous texture resembling flower petals. A delicate diamond tennis necklace sparkles around her neck, and there is a ring on the ring finger of her right hand.

Lighting and background: Soft, even lighting. Dark, blurred background.

Do not change the facial features or identity.

3:4 aspect ratio.

Realistic, high-quality, sharp 8K photo, shot on an iPhone 16 Pro.
```

</details>

<details><summary><b>Dark Romance Witch Mirror Selfie</b></summary>

```text
Camera Angle & Composition:
An eye-level mirror selfie. Medium shot, framing the figure from the top of the head to mid-thigh. Vertical 3:4 aspect ratio. Her gaze is focused on her reflection in the mirror.

Pose:
A relaxed yet confident stance. Her left hand holds a smartphone at chest level, slightly to the side. Her right arm is elegantly raised, with her fingers gently touching the brim of her witch hat.

Outfit:
A gothic witch costume in a Dark Romance style. A fitted black velvet dress with a deep sweetheart neckline. A high slit in the dress reveals her right thigh. A sheer black tulle or chiffon cape drapes along her arms like loose, flowing sleeves. She wears sheer black pantyhose featuring a spiderweb pattern and a large black spider design on the thigh.

Accessories:
A tall, classic witch hat made of textured black material, featuring a rectangular silver buckle at the front. A thin black velvet ribbon choker tied into a bow at the front of the neck. A long, layered necklace made of black beads, resembling rosary beads, with a large, vintage-style metal cross pendant. The smartphone has a dark, chunky protective case.

Hair, Makeup & Appearance:
slightly wavy,loose.The hair falls naturally over her shoulders. Gothic Glam makeup with flawless,  skin and dramatic eye makeup. Her lips are closed and coated with rich, dark burgundy matte lipstick. Long, square-shaped nails with dark nail polish.

Lighting, Atmosphere & Mood:
Dim, mystical indoor lighting with a low-key lighting setup. Soft light gently illuminates her face and décolletage, leaving the background in shadow. The atmosphere is mysterious, elegant, and dark, combining Halloween aesthetics with Dark Academia. The overall mood is enigmatic and composed, with a subtle touch of mysticism.

Face Preservation: Preserve the exact facial features, identity, facial structure, and proportions of the reference photo. Do not alter her face.

Image Quality: Ultra-realistic, high-quality, sharp 8K photograph with realistic skin texture and natural details. Shot on an iPhone 16 Pro. Vertical 3:4 aspect ratio.
Легка напівпосмішка
```

</details>

<details><summary><b>Dark Style Image Prompt</b></summary>

```text
Create an image with a ${style:dark} aesthetic. Your image should feature:

- **Lighting:** Moody and low-key, highlighting shadows.
- **Color Palette:** Dark tones with high contrast.
- **Elements:** Include mysterious or shadowy figures, gothic architecture, or night-time scenery.

Feel free to adjust the ${elements} to match your vision of a dark style image.
```

</details>

<details><summary><b>Dark Surreal Organic Portrait</b></summary>

```text
Aspect ratio 3:4.
A dark surreal portrait of a girl surrounded by strange black shapes. Close-up, chest-up, slightly to the side. Her appearance — facial features, skin tone, hair color — must match the reference. Preserve tattoos, scars, piercings.

Her eyes are fully black, wide and hollow, no visible whites. Pale skin, freckles across the nose and cheeks, soft neutral lips, slightly parted. Slightly  messy hair, strands falling over her face.

Around her head and shoulders — several black glossy organic shapes, like twisted hands or tentacles. They curl around her, framing her face. Embedded inside these black shapes are large realistic human eyes with pale pink skin around them — wet, glossy, staring in different directions. One of the black claw-like shapes reaches toward her cheek.

She wears a plain black high-neck top.

Background: plain pale grey-white, soft gradient, blurred.

Light: soft, cool, diffused from the front. Gentle highlights on the wet eyes and glossy black shapes, soft shadows on her face.

Textures: real clean skin, natural freckles. Wet glossy eyes, reflective. Black organic shapes — smooth, wet, glossy like tar or skin. Slight film grain.

No illustration, no cartoon, no 3D. Dark, unsettling, surreal, quiet.
```

</details>

<details><summary><b>Defiant 90s Grunge Bedroom Portrait</b></summary>

```text
A vertical medium shot casual photograph of a young woman in her late teens with a slim figure, long wavy light brown hair with copper highlights, wearing white oval-shaped sunglasses with dark lenses and thick white frames. She is wearing a long-sleeve oversized shirt with wide horizontal stripes in burgundy red and navy blue, and blue jeans. She is sitting on the floor with her knees bent up, both hands raised at shoulder height showing the middle finger with both hands, black painted nails. She has layered thin silver necklaces. Her expression is serious, defiant, and cool, looking directly at the camera through the sunglasses. The background is a white bedroom wall covered with rock band posters: 'I WANT TO BELIEVE', 'ARCTIC MONKEYS', 'NIRVANA' smiley face logo, 'JOY DIVISION UNKNOWN PLEASURES', and 'THE CURE BOYS DON'T CRY'. To the left is a white and black electric guitar (Stratocaster style) leaning against the wall above a black amplifier. To the right are black combat boots and stacked Vans shoe boxes. Lighting is direct frontal smartphone flash creating harsh shadows on the wall behind her and specular highlights on the white sunglasses. Shot with a smartphone camera, 24mm lens, eye-level angle, full color, saturated colors, casual grunge aesthetic, alt girl vibe, 90s rock revival style, Instagram/Tumblr/Pinterest aesthetic, ultra-realistic.
```

</details>

<details><summary><b>Dental Clinic Portrait</b></summary>

```text
Use the uploaded photo of the person as the main subject. Keep the face, hair and identity identical.

Place the person sitting slightly reclined in a modern dentist chair, in a clean, bright dental clinic with soft white lighting. Add a light blue disposable dentist bib/apron on the person’s chest, clipped around the neck. Surround them with subtle dental details: overhead examination light, small side table with dental tools, and blurred shelves or cabinets in the background.

Keep the original camera angle and approximate framing from the uploaded photo. Do not change the person’s facial features or expression, only adjust the body pose, outfit details and environment to match a realistic dentist visit scene.
```

</details>

<details><summary><b>Desert Caravanserai Concept Brief Builder</b></summary>

```text
Act as a cinematic environment designer who writes image-ready and motion-ready scene briefs. Help me design one hero shot of an old desert caravanserai at dusk with a camel caravan arriving, which will first be generated as a still image and then animated into a short video that uses that image as its first frame. Your brief must make the still image rich in elements that can move naturally (camels walking with steady strides, flickering lantern light, palm fronds swaying, fine sand drifting over dune ripples, stars appearing as the sky darkens) while keeping the composition calm, readable, and easy to animate.

My starting choices:
- Desert setting: ${setting:wide sand desert with low rolling dunes and rippled sand}
- Time and sky: ${time:dusk turning to night, orange glow on the horizon fading up into violet with the first stars}
- Caravanserai look: ${building:square sandstone fortress with crenellated walls, round corner towers, and one tall arched gateway}
- Caravan: ${caravan:a line of five camels with riders arriving toward the gate}
- Visual style: ${style:photoreal cinematic travel photography}
- Mood words: ${mood:calm, timeless, welcoming, quiet}

First ask me, in one short message, for anything missing: the camera viewpoint I prefer (low and wide from the sand, from a dune slightly above, or level with the gate), which side the caravan should enter from and which way it walks, how much of the sky versus sand should show, and anything to avoid (close-up faces, text, signs, logos, modern vehicles, power lines, a specific real building or place).

Then produce the brief with these sections:

1. **Scene Overview**: two or three sentences describing the place, the time, the light, and the feeling of the moment. Describe an imagined caravanserai, not a copy of a real, named one.

2. **Caravanserai Architecture**: its position in the frame, wall color and texture, the corner towers, crenellations, small windows, the shape of the gateway (pointed or horseshoe arch), what is visible through it (inner arches, warm courtyard light), and where the lanterns hang.

3. **Caravan and Movement Line**: the number of camels and riders, their spacing, which side of the frame they occupy, the direction they walk, the path they follow toward the gate, saddle cloths and colors, and their shadows on the sand. State that every camel faces the direction it walks.

4. **Desert and Vegetation**: dune shapes near and far, sand ripples in the foreground, sparse dry shrubs near the walls, and palm trees (how many, where, and how tall), with depth layers from foreground to background.

5. **Light and Atmosphere**: where the last glow sits on the horizon, the sky gradient, the stars, the warm lantern light at the gate against the cool dusk, wispy clouds, and any low haze.

6. **Fixed Visual Details**: a numbered list of 8 to 10 details that must stay identical in the still image and in the video (fortress position and size, gate position, tower count, lantern positions, camel count and direction, palm count and position, horizon glow side, camera position, framing).

7. **Motion Map**: a table of every element that can move in the video, with columns: element, type of motion, direction, speed (very slow, slow, medium), and how strongly it should move. Include the camels' walk, the lantern flicker, palms, drifting sand, stars, and the camera move. Keep total motion subtle and physically plausible, with one wind direction for palms and sand.

8. **Prompt Seed A - Hero Still Image**: a ready-to-paste image prompt under 170 words for a wide landscape 16:9 frame, with the caravanserai, the camel caravan, and the dusk sky in the first sentence, ending with: no close-up faces, no text, no signs, no logos.

9. **Prompt Seed B - Image-to-Video Animation**: a ready-to-paste video prompt under 120 words that starts from the hero still as the first frame, describes the camels walking steadily in the direction they face, the lantern and palm motion, one slow camera move for about 6 seconds, and says to keep the fortress, towers, palms, and framing exactly as in the image with no new objects.

Rules: people only as small riders, never the main subject; no text, signs, or logos; no fast camera moves or cuts; and no motion that breaks physics (camels walk forward only in the direction they face with natural leg movement, riders stay seated, shadows follow the camels, the building never changes shape). Use short paragraphs and lists.
```

</details>

<details><summary><b>Desert Caravanserai Image to Video</b></summary>

```text
Start from the step 2 image "Sandstone Caravanserai with a Camel Caravan in the Desert at Dusk" as the exact first frame, and animate it into a calm ${duration:6}-second cinematic shot. Keep the square sandstone caravanserai with its two round crenellated towers and tall arched gateway in the center-right, the three palm trees beside the right tower, the low dunes, the orange-to-violet sky, and the framing exactly as in the image. The line of five camels with seated riders on the left walks slowly and steadily to the right toward the glowing gateway, their legs moving naturally and their shadows following them across the rippled sand; every camel keeps facing right and the riders stay seated. The two lanterns beside the gate flicker softly and the warm courtyard light glows steadily. A light breeze sways the palm fronds on the right, and fine sand drifts low across the dune ripples in the same direction. The orange glow on the left horizon fades a little and a few more stars appear in the violet sky. The camera makes one slow, smooth push-in toward the gateway. Natural, realistic motion, no cuts, no new objects, no text. Quiet desert wind and soft camel footsteps.
```

</details>

<details><summary><b>Design a Military Uniform</b></summary>

```text
Act as a Stylist. You are an expert in fashion and design, specializing in military attire.
Your task is to help visualize or design a military uniform for a ${projectType:movie} or ${characterRole:soldier}.
You will:
- Consider the historical period or futuristic setting
- Choose appropriate colors, materials, and insignia
- Provide sketches or detailed descriptions
Rules:
- Maintain authenticity and practicality
- Consider the context and environment of use
```

</details>

<details><summary><b>Dewy Fox Eye Selfie</b></summary>

```text
Do not change the face, maintain 100% facial resemblance.
Casual front-camera selfie, taken in a close-up at face level, a casual live selfie at home during the daytime — a natural beauty frame with a radiant, dewy skin effect.
In the photo, a woman with long, hip-length, wavy hair with a voluminous side part — her hair is full and falls freely over her shoulder and cheek, partially covering one side of her face with thick strands. Her head is tilted to the side and almost touches her shoulder, her gaze is directed straight at the camera from underneath her brows. Makeup, thick extended eyelashes with a fox-eye effect, a defined eyeliner wing, full lips covered with transparent glossy lip gloss with a plumping effect. Her skin is slightly tanned. Gold stud earrings with a square stone. She is wearing an oversized dark gray T-shirt with a partially visible yellow brand logo on the chest.
The frame is vertical, the head is slightly tilted and the cheek is pressed against the shoulder. The background is barely visible — darkened.
The lighting is natural and bright, directed from the side and front — a direct, hard light source.
The background must remain clearly visible and strictly in focus, without blur.
Shot on iPhone 17.
Aspect ratio: 3:4.
```

</details>

<details><summary><b>Director Variation Grid</b></summary>

```text
Create a single 3x3 grid image (square, 2048x2048, high detail).
The center tile (row 2, col 2) must be the exact uploaded reference film still, unchanged. Do not reinterpret, repaint, relight, recolor, crop, reframe, stylize, sharpen, blur, or transform it in any way. It must remain exactly as provided.

Director detection rule
If the director of the uploaded film still is one of the 8 directors listed below, then the tile for that same director must be an exact duplicate of the ORIGINAL center tile, with no changes at all (same image content, same framing, same colors, same lighting, same texture). Only apply the label.
All other tiles follow the normal re-shoot rules.

Grid rules
9 equal tiles in a clean 3x3 layout, thin uniform gutters between tiles.
Each tile has a simple, readable label in the top-left corner, consistent font and size, high contrast, no warping.
Center tile label: ORIGINAL
Other tiles labels exactly:
Alfred Hitchcock
Akira Kurosawa
Federico Fellini
Andrei Tarkovsky
Ingmar Bergman
Jean-Luc Godard
Agnès Varda
Sergio Leone
No other text, logos, subtitles, or watermarks.
Keep the 3x3 alignment perfectly straight and clean.

IDENTITY + GENDER LOCK (applies to ALL non-ORIGINAL tiles)
- Use the ORIGINAL center tile as the single source of truth for every person’s identity.
- Preserve the exact number of people and their roles/positions (no swapping who is who).
- Do NOT change any person’s gender or gender presentation. No gender swap, no sex change, no cross-casting.
- Keep each person’s key identity traits consistent: face structure, hairstyle length/type, facial hair (must NOT appear/disappear), makeup level (must NOT appear/disappear), body proportions, age range, skin tone, and distinctive features (moles/scars/glasses).
- Do not turn one person into a different person. Do not merge faces. Do not split one person into two. Do not duplicate the same face across different people.
- If any identity attribute is ambiguous, default to matching the ORIGINAL exactly.
- Allowed changes are ONLY cinematic treatment per director: framing, lens feel, camera height, DOF, lighting, palette, contrast curve, texture, mood, and set emphasis. Identities must remain locked.
NEGATIVE: gender swap, femininize/masculinize, add/remove beard, add/remove lipstick, change hair length drastically, face replacement, identity drift.

CAST ANCHORING
- Person A = left-most person in ORIGINAL, Person B = right-most person in ORIGINAL, Person C = center/back person in ORIGINAL, etc.
- Each tile must keep Person A/B/C as the same individuals (same gender presentation and identity), only reshot cinematically.

Content rules (for non-duplicate tiles)
Maintain recognizable continuity across all tiles (who/where/what). Do not change identities into different people.
Vary per director: framing, lens feel, camera height, depth of field, lighting, color palette, contrast curve, texture, production design emphasis, mood.
Ultra-sharp cinematic stills (except where diffusion is specified), coherent lighting, correct anatomy, no duplicated faces, no mangled hands, no broken perspective, no glitch artifacts, and perfectly readable labels.

Director-specific style and color grading (apply strongly per tile, unless the duplicate rule applies)

Alfred Hitchcock
Palette: muted neutrals, cool grays, sickly greens, deep blacks, occasional saturated red accent.
Contrast: high contrast with crisp, suspenseful shadows.
Texture: classic 35mm cleanliness with tense atmosphere.
Lens/DOF: 35–50mm, controlled depth, precise geometry.
Lighting/Blocking: noir-influenced practicals, hard key, voyeuristic framing, psychological tension.

Akira Kurosawa
Palette: earthy desaturated browns/greens; restrained primaries if color.
Contrast: bold tonal separation, punchy blacks.
Texture: gritty film grain, tactile elements (mud, rain, wind).
Lens/DOF: 24–50mm with deep focus; dynamic staging and strong geometry.
Lighting/Atmosphere: dramatic natural light, weather as design (fog, rain streaks, backlight).

Federico Fellini
Palette: warm ambers, carnival reds, creamy highlights, pastel accents.
Contrast: medium contrast, dreamy glow and gentle bloom.
Texture: soft diffusion, theatrical surreal polish.
Lens/DOF: normal to wide, staged tableaux, rich background set dressing.
Lighting: expressive, stage-like, whimsical yet melancholic mood.

Andrei Tarkovsky
Palette: subdued sepia/olive, cold cyan-gray, low saturation, weathered tones.
Contrast: low-to-medium, soft highlight roll-off.
Texture: organic grain, misty air, water stains, aged surfaces.
Lens/DOF: 50–85mm, contemplative framing, naturalistic DOF.
Lighting/Atmosphere: window light, overcast feel, poetic elements (fog, rain, smoke), quiet intensity.

Ingmar Bergman
Palette: near-monochrome restraint, cold grays, pale skin tones, minimal color distractions.
Contrast: high contrast, sculpted faces, deep shadows.
Texture: clean, intimate, psychologically focused.
Lens/DOF: 50–85mm, tighter framing, shallow-to-medium DOF.
Lighting: strong key with dramatic falloff, emotionally intense portraits.

Jean-Luc Godard
Palette: bold primaries (red/blue/yellow) punctuating neutrals, or intentionally flat natural colors.
Contrast: medium contrast, occasional slightly overexposed highlights.
Texture: raw 16mm/35mm energy, imperfect and alive.
Lens/DOF: wider lenses, spontaneous off-center composition.
Lighting: available light feel, street/neon/practicals, documentary new-wave immediacy.

Agnès Varda
Palette: warm natural daylight, gentle pastels, honest skin tones, subtle complementary colors.
Contrast: medium, soft and inviting.
Texture: tactile lived-in realism, subtle film grain.
Lens/DOF: 28–50mm, environmental portrait framing with context.
Lighting: naturalistic, human-first, intimate but open atmosphere.

Sergio Leone
Palette: sunbaked golds, dusty oranges, sepia browns, deep shadows, occasional turquoise sky tones.
Contrast: high contrast, harsh sun, strong silhouettes.
Texture: gritty dust, sweat, leather, weathered surfaces, pronounced grain.
Lens/DOF: extreme wide (24–35mm) and extreme close-up language; shallow DOF for eyes/details.
Lighting/Mood: hard sunlight, rim light, operatic tension, iconic dramatic shadow shapes.

Output: a single final 3x3 grid image only.
```

</details>

<details><summary><b>Doctor Guiding Students Up a Staircase of Books</b></summary>

```text
Create a program for a doctor who paves the way for university students through scientific books in the form of thresholds one by one to illuminate the path to success for them .. In the other, the word success appears to fascinate the world
```

</details>

<details><summary><b>Dogs Playing Golf Video</b></summary>

```text
A cinematic 9:16 vertical video in a Pixar-style tone of a joyful group of cartoonish dogs playing golf on a bright, colorful golf course. One main dog is centered, standing upright with exaggerated proportions, mid-swing with a golf club and a big excited smile, while his dog friends react with expressive faces—cheering, gasping, or holding tiny golf accessories. The camera is positioned at a slightly low angle facing the main character. Smooth, playful character animation with subtle squash-and-stretch. Warm, vibrant lighting, soft shadows, and rich saturated colors. Background slightly blurred with stylized trees and clouds. Smooth slow zoom in. No text overlay, no humans — focus only on the dogs and their fun, heartwarming golf moment, crisp details, expressive eyes, and a lighthearted Pixar-like charm. Duration: 10 seconds.
```

</details>

<details><summary><b>Double Exposure Portrait</b></summary>

```text
A double exposure portrait set in a ${name:sunny forest}. A left-facing profile silhouette showing the person’s head and shoulders. The interior of the silhouette is completely filled with the forest scenery, with rich depth. Deep inside this scene, among the natural elements, the same person appears again as a full-body figure integrated into the environment. The outer background is a bright, overexposed white light. The light subtly bleeds inward from the silhouette’s edges, creating a dramatic glow and high-contrast effect. High resolution, cinematic, soft light, realistic texture, crisp details.
```

</details>

<details><summary><b>Dreamy Ethereal Blonde Portrait</b></summary>

```text
A blonde woman in a dreamy, ethereal photographic scene with light effects and surreal elements.
```

</details>

<details><summary><b>Dreamy Meadow Portrait</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "medium",
    "dominant_palette": [
      "deep red",
      "olive green",
      "cream",
      "pale yellow"
    ]
  },
  "composition": {
    "camera_angle": "eye-level shot",
    "depth_of_field": "shallow",
    "focus": "A young woman in a red dress",
    "framing": "The woman is framed slightly off-center, walking across the scene in profile. The background exhibits a strong swirling bokeh, which naturally frames and isolates the subject."
  },
  "description_short": "A young woman in a short red dress and white sneakers walks in profile through a field of flowers, with a distinct swirling blur effect in the background.",
  "environment": {
    "location_type": "outdoor",
    "setting_details": "A lush green field or garden densely populated with white and yellow wildflowers, likely daisies. The entire background is heavily out of focus, creating an abstract, swirling pattern.",
    "time_of_day": "afternoon",
    "weather": "cloudy"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "front",
    "type": "natural"
  },
  "mood": {
    "atmosphere": "Dreamy and nostalgic",
    "emotional_tone": "melancholic"
  },
  "narrative_elements": {
    "character_interactions": "The woman is solitary, appearing lost in thought.",
    "environmental_storytelling": "The ethereal, swirling floral background suggests a dreamscape or a memory, emphasizing the subject's introspective state. Her vibrant red dress contrasts sharply with the muted green surroundings, highlighting her as the emotional center of the scene.",
    "implied_action": "The woman is walking from one place to another, suggesting a journey, a moment of contemplation, or an escape into nature."
  },
  "objects": [
    "woman",
    "red dress",
    "white sneakers",
    "flowers",
    "grass"
  ],
  "people": {
    "ages": [
      "young adult"
    ],
    "clothing_style": "Bohemian romantic; a short, flowing red dress with ruffled details, paired with casual white sneakers.",
    "count": "1",
    "genders": [
      "female"
    ]
  },
  "prompt": "A dreamy, artistic photograph of a young woman with brown, wind-swept hair, walking in profile through a meadow of daisies. She wears a vibrant short red dress and white sneakers. The image has a very shallow depth of field, creating a signature swirling bokeh effect in the background that frames her. The lighting is soft and natural, with a warm, vintage color grade. The mood is pensive and melancholic, capturing a fleeting moment of introspection.",
  "style": {
    "art_style": "cinematic",
    "influences": [
      "impressionism",
      "fine art photography"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "shallow depth of field",
    "bokeh",
    "swirl bokeh",
    "Petzval lens",
    "profile shot",
    "vintage filter",
    "motion blur",
    "natural light"
  ],
  "use_case": "Artistic stock photography, editorial fashion, book covers, or datasets for specialized lens effects.",
  "uuid": "0fce3d8f-9de2-4a75-8d3f-6398eea47e24"
}
```

</details>

<details><summary><b>Dreamy Slow Shutter Fashion Portrait</b></summary>

```text
Made with Nano Banana 2.1

Prompt:

Vertical 9:16 candid fashion portrait of a 
beautiful East Asian girl wearing a fitted long-sleeve orange turtleneck and a black mini skirt, with long, messy, loose black hair. She spins rapidly while looking back at the camera, arms spread wide and hair flying. VERY SLOW SHUTTER SPEED 1/8–1/15 sec, extreme realistic motion blur, long ghost trails on arms and hair, blurred body, softly recognizable face, horizontal background streaks, camera shake, double-exposure effect, heavy 35mm film grain, dreamy, moody, underexposed, photorealistic. No CGI, no frozen motion, no sharp arms or hair.
```

</details>

<details><summary><b>Dutch Golden Age Breakfast Still Life</b></summary>

```text
A Dutch Golden Age breakfast still life oil painting in the manner of the 1630s Haarlem masters, showing a quiet laid table against a deep brown-black background. A rumpled dark green velvet cloth covers the table. On the left, three opened oysters glisten on a round pewter plate. In front of them, a half-peeled lemon sits with its long spiral of yellow rind curling down over the front edge of the table. In the center, a tall ornate silver goblet lies tipped on its side, its polished bowl reflecting the room, beside a crusty golden bread roll and a small scatter of hazelnuts. On the right stands a clear glass roemer with a prunted, textured bowl on a slender knopped stem, filled with pale white wine, and next to it a crumpled white linen napkin with a lace edge spills over the corner of the table. Soft single window light from the upper left, rich transparent glazes, crisp highlights on the metal, glass, and oyster shells, deep shadows, and a fine craquelure across the varnish. Museum quality, calm and contemplative mood, wide landscape 16:9. No text, no signature, no people.
```

</details>

<details><summary><b>Echoes of the Rust Age</b></summary>

```text
You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Place Subject 1 (male) and Subject 2 (female) as post-apocalyptic wanderers in a desert of junk. They are traversing a massive canyon formed by centuries of rusted debris. The image must be photorealistic, featuring cinematic lighting, highly detailed skin textures and environmental grit, shot on Arri Alexa with a shallow depth of field to isolate them from the chaotic background.
```

</details>

<details><summary><b>Edgy Monochrome Studio Portrait</b></summary>

```text
A stunning black and white studio portrait photograph of a beautiful young woman with long wavy hair with subtle highlights, delicate facial features, defined eyebrows, natural lips, and an intense direct gaze at the camera. She is sitting on a wooden stool against a solid dark black background. Her pose: right leg bent upward with foot resting on the stool seat, left arm resting on her raised knee, right hand gently touching her hair near her head. She is wearing a black lace crop top bralette and light-colored distressed ripped jeans with frayed holes at the knees. Professional studio lighting with soft directional light from the front-side creating subtle Rembrandt-style shadows. Shot with a professional DSLR camera, 85mm portrait lens, f/1.8 aperture, medium depth of field. Editorial high-fashion photography style, artistic black and white portrait, full body to three-quarter composition, slightly low camera angle. Ultra-detailed, high resolution, photorealistic, sharp focus on face and eyes, natural skin texture, cinematic contrast.
```

</details>

<details><summary><b>Editorial Beauty Analysis Board East Asian Model</b></summary>

```text
{
  "prompt": "A minimalist editorial beauty analysis board featuring an East Asian female model with a slim oval face and soft V-line jaw. Neutral gray background, clean studio lighting, high realism.\n\nTop section: front-facing barefaced portrait, natural skin texture, no makeup, hair pulled back, neutral expression. A thin blue outline tracing the face shape.\n\nRight side graphic text layout titled 'FACE' with small bullet points describing facial features: slim oval face shape, high cheekbones, soft jawline, small chin, refined nose bridge.\n\nMiddle section: two studio portraits labeled 'barefaced', one straight-on view and one three-quarter profile, minimal styling, soft lighting.\n\nBottom section: two mirror selfie style images labeled 'with makeup', glossy skin, soft glam makeup, blush-heavy cheeks, nude glossy lips, subtle eyeliner, voluminous layered hair, modern fashion styling.\n\nFashion magazine editorial layout, clean typography, balanced spacing, muted tones, professional beauty photography, high resolution, realistic skin details.",
  "negative_prompt": "exaggerated makeup, heavy contour, harsh shadows, cartoon style, anime, distorted face, low resolution, oversaturated colors, messy layout, watermark, logo, text artifacts, duplicated faces, extra limbs",
  "style": "editorial beauty photography",
  "quality": "high",
  "lighting": "soft studio lighting",
  "background": "neutral gray"
}
```

</details>

<details><summary><b>Editorial Beauty Analysis Board European Model</b></summary>

```text
{
  "prompt": "A minimalist editorial beauty analysis board featuring a European female model with a balanced oval-to-heart face shape and a softly defined jawline. Subtle Central–Northern European facial characteristics with refined symmetry and elegant proportions. Neutral gray background, clean studio lighting, high realism.\n\nTop section: front-facing barefaced portrait, natural skin texture with neutral-to-cool undertones, no makeup, hair pulled back, calm neutral expression. A thin blue outline tracing the face shape.\n\nRight side graphic text layout titled 'FACE' with small bullet points describing facial features: balanced oval face shape, softly pronounced cheekbones, feminine and delicate jawline, slightly tapered natural chin, straight to softly contoured nose bridge, clear almond-to-rounded eyes with a soft gaze.\n\nMiddle section: two studio portraits labeled 'barefaced', one straight-on view and one three-quarter profile, minimal European editorial styling, soft diffused lighting, realistic skin texture and fine facial details.\n\nBottom section: two mirror selfie style images labeled 'with makeup', fresh luminous skin with a natural satin finish, modern European soft glam makeup, gentle blush tones, nude pink or soft rose glossy lips, subtle eyeliner with softly lifted outer corners, natural lashes, softly styled layered hair, contemporary European fashion styling inspired by Paris and Milan street elegance.\n\nFashion magazine editorial layout, clean modern typography, balanced spacing, muted neutral tones, professional beauty photography, high resolution, realistic skin texture and natural proportions.",
  "negative_prompt": "exaggerated makeup, heavy contour, harsh shadows, cartoon style, anime, distorted facial proportions, overly sharp jawline, low resolution, oversaturated colors, messy layout, watermark, logo, text artifacts, duplicated faces, extra limbs",
  "style": "editorial beauty photography",
  "quality": "high",
  "lighting": "soft studio lighting",
  "background": "neutral gray"
}
```

</details>

<details><summary><b>Editorial Beauty Analysis Board Turkish Model</b></summary>

```text
{
  "prompt": "A minimalist editorial beauty analysis board featuring a Turkish female model with a balanced oval-to-heart face shape and softly defined jawline. Subtle Mediterranean–Anatolian facial characteristics. Neutral gray background, clean studio lighting, high realism.\n\nTop section: front-facing barefaced portrait, natural skin texture with slight warmth, no makeup, hair pulled back, neutral expression. A thin blue outline tracing the face shape.\n\nRight side graphic text layout titled 'FACE' with small bullet points describing facial features: balanced oval face shape, softly pronounced cheekbones, feminine jawline, slightly pointed but natural chin, straight to softly arched nose bridge, expressive almond-shaped eyes.\n\nMiddle section: two studio portraits labeled 'barefaced', one straight-on view and one three-quarter profile, minimal styling, soft diffused lighting, realistic skin details.\n\nBottom section: two mirror selfie style images labeled 'with makeup', luminous but natural skin, soft glam makeup inspired by modern Turkish beauty trends, warm blush tones, nude or rose glossy lips, subtle eyeliner with lifted outer corners, voluminous layered hair, contemporary Istanbul fashion styling.\n\nFashion magazine editorial layout, clean modern typography, balanced spacing, muted neutral tones, professional beauty photography, high resolution, realistic skin texture and proportions.",
  "negative_prompt": "exaggerated makeup, heavy contour, harsh shadows, cartoon style, anime, distorted facial proportions, overly sharp jawline, low resolution, oversaturated colors, messy layout, watermark, logo, text artifacts, duplicated faces, extra limbs",
  "style": "editorial beauty photography",
  "quality": "high",
  "lighting": "soft studio lighting",
  "background": "neutral gray"
}
```

</details>
