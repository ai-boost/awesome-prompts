# Image & Design (4/4)

743 prompts. Copy one, replace anything in brackets, and paste it into any chat model.

[English](../en/image.md) · [中文](../zh/image.md) · [Search and copy online](https://agentcraft.dev/en/prompts/image/)

Pages: [1](image.md) · [2](image-2.md) · [3](image-3.md) · **4**

<details><summary><b>Shadows of the Blue Note</b></summary>

```text
{
  "title": "Shadows of the Blue Note",
  "description": "A tense, high-stakes meeting between a weary detective and a glamorous informant in a smoky 1950s jazz lounge.",
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Transform Subject 1 (male) and Subject 2 (female) into characters from a classic 1950s film noir. Subject 1 is a rugged private investigator, and Subject 2 is an elegant femme fatale. They are seated at a secluded booth in a dimly lit, smoke-filled jazz club. The image must be ultra-photorealistic, utilizing cinematic lighting to create deep shadows and highlights. The scene should look like a frame from a high-budget blockbuster movie, shot on Arri Alexa, highly detailed, with a shallow depth of field focusing on their intense interaction.",
  "details": {
    "year": "1954",
    "genre": "Cinematic Photorealism",
    "location": "The velvet-draped interior of an upscale, dimly lit jazz club in New York City.",
    "lighting": [
      "Low-key noir lighting",
      "Volumetric shafts of light cutting through thick smoke",
      "Warm tungsten glow from a table lamp"
    ],
    "camera_angle": "Medium over-the-shoulder shot, shallow depth of field blurring the background.",
    "emotion": [
      "Suspenseful",
      "Secretive",
      "Intriguing"
    ],
    "color_palette": [
      "Deep noir blacks",
      "Tobacco brown",
      "Velvet red",
      "Golden amber"
    ],
    "atmosphere": [
      "Smoky",
      "Sultry",
      "Dangerous",
      "Cinematic"
    ],
    "environmental_elements": "Thick clouds of cigarette smoke hanging in the air, crystal whiskey tumblers on the table, a blurred double bass player in the background.",
    "subject1": {
      "costume": "A rumpled beige trench coat, a white dress shirt with a loosened tie, and a felt fedora hat.",
      "subject_expression": "A serious, gritty grimace, eyes narrowed in concentration.",
      "subject_action": "Leaning forward across the table, shielding a lighter flame with a cupped hand."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "daylight",
        "modern technology",
        "smartphones",
        "neon lights",
        "bright colors"
      ],
      "exclude_styles": [
        "cartoon",
        "sketch",
        "painting",
        "3D render",
        "anime"
      ],
      "exclude_colors": [
        "neon green",
        "hot pink",
        "bright blue"
      ],
      "exclude_objects": [
        "cars",
        "television",
        "sunglasses"
      ]
    },
    "subject2": {
      "costume": "A crimson silk evening gown, long satin gloves, and a pearl necklace.",
      "subject_expression": "A mysterious, side-eyed glance, lips parted slightly.",
      "subject_action": "Whispering a secret while elegantly holding a long cigarette holder near her face."
    }
  }
}
```

</details>

<details><summary><b>Sky Orchard Merchants Board Game Box Cover</b></summary>

```text
Painterly board game box cover illustration for a cozy cooperative trading game about airship merchants. Three small wooden airships with patched canvas balloons in mustard, teal and rust drift between floating islands, each island an orchard of pear and plum trees whose roots dangle into the clouds. Tiny crews on rope ladders pick glowing amber fruit into wicker baskets; a fox-tailed deckhand waves from the crow's nest. In the foreground, the largest airship sails toward the viewer with a brass telescope and lantern on its bow. Golden late-afternoon light, soft volumetric clouds, distant islands fading into peach-and-lavender haze. Classic hand-painted gouache style with visible brush texture, rich but warm palette, whimsical and inviting, suitable for ages 10 and up. Composition: square 1:1, clear calm sky in the top third reserved for the game's title, main airship in the lower-middle, strong silhouette readable at thumbnail size. No text, no letters, no logos, no borders.
```

</details>

<details><summary><b>Snowy Street Winter Outfit</b></summary>

```text
{
  "category": "SNOWY_STREET_WINTER_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Lock identity to reference image exactly. Adult 21+ only."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, match reference identity.",
    "hair": {
      "color": "Match reference.",
      "style": "Hair tucked into scarf/coat with a few strands visible",
      "texture": "Natural strands, slight static flyaways",
      "movement": "Minimal movement; cold air realism"
    },
    "face": {
      "eyes": "Exact reference eyes; slight squint from cold",
      "skin_details": "Natural texture; slight redness on cheeks (subtle, realistic)",
      "micro_details": "Preserve marks"
    },
    "clothing": {
      "outerwear": "Winter coat + scarf + beanie (no logos/text)",
      "fabric": "Wool knit texture visible; tiny snow specks on coat"
    },
    "accessories": {
      "jewelry": [
        "Silver hoops optional (may be hidden by scarf)"
      ]
    }
  },
  "pose": {
    "type": "Outdoor candid",
    "orientation": "Half-body",
    "hands": "Hands holding scarf near chin (gloves optional, unbranded)",
    "gaze": "Direct eye contact, cozy smile",
    "expression": "Warm, playful"
  },
  "setting": {
    "environment": "Snowy street at dusk",
    "background_elements": [
      "Falling snowflakes (fine particles, not fog)",
      "Streetlight bokeh",
      "Soft silhouettes blurred (no identifiable faces)"
    ],
    "depth": "Face sharp; background creamy bokeh"
  },
  "camera": {
    "shot_type": "Half-body winter portrait",
    "angle": "Eye level",
    "focal_length_equivalent": "35-50mm pro OR 26mm phone night mode",
    "framing": "4:5",
    "focus": "Eyes sharp; snowflakes softly blurred"
  },
  "lighting": {
    "source": "Streetlights + ambient dusk",
    "direction": "Soft top/side glow",
    "highlights": "Warm highlights on hair/cheeks",
    "shadows": "Soft, cinematic winter contrast"
  },
  "mood_and_expression": {
    "tone": "Cozy, cinematic, cute-relatable",
    "atmosphere": "Winter candid"
  },
  "style_and_realism": {
    "style": "Photoreal lifestyle",
    "imperfections": "Low-light grain allowed"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Moderate low-light grain",
    "mode_variants": {
      "amateur": "Phone night-mode feel: mild grain, slight tilt, imperfect framing",
      "pro": "Cleaner cinematic exposure, controlled highlights, shallow DOF"
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
    "fog machine",
    "smoke",
    "identity drift",
    "face morphing",
    "extra fingers",
    "warped hands",
    "readable text",
    "logos",
    "watermark",
    "plastic skin",
    "over-smoothing"
  ]
}
```

</details>

<details><summary><b>Soft Glam Lounge Close Up</b></summary>

```text
A close-up portrait of a young woman. The main focus is her extremely thick, loose hair, styled in large, soft waves with pronounced volume at the roots.

Makeup:
Soft glam aesthetic. Flawless skin with a subtle glow (highlighter on the cheekbones and nose) and a soft blush. Defined black cat-eye eyeliner and voluminous lashes. Full lips covered with a soft pink nude gloss and formed into a playful kiss (lips closed, no teeth visible). Classic long red manicure.

Clothing & Accessories:
A fitted basic black long-sleeve top, with the fabric slightly gathered into folds around the wrists. The only visible jewelry is a simple silver hoop earring in one ear.

Pose:
The girl is looking directly into the camera. Her right hand is gracefully raised, with the back of her hand and fingers relaxed and gently touching her cheek and jawline.

Background:
A stylish modern interior, resembling a restaurant or lounge area, heavily blurred due to a shallow depth of field with beautiful bokeh. A wooden slatted ceiling, warm spotlights, a hint of a table with a wine glass, and the back of a green velvet chair are visible.

Lighting, Camera Angle & Mood:
Soft, frontal lighting that perfectly emphasizes her facial features without harsh shadows. The camera is positioned directly at eye level. The mood is flirtatious, confident, and relaxed. Technically, it looks like a high-quality selfie or portrait.

Do not change the girl's facial features, eye shape, eyebrows, nose, or lips. Maintain 100% facial resemblance.

Aspect ratio: 3:4.
Ultra-realistic, high-quality, sharp 8K photograph, shot on iPhone 16 Pro Max.
```

</details>

<details><summary><b>Solitary Figure in a Snowy Landscape</b></summary>

```text
{
  "colors": {
    "color_temperature": "cool",
    "contrast_level": "high",
    "dominant_palette": [
      "deep blue",
      "orange",
      "red",
      "black"
    ]
  },
  "composition": {
    "camera_angle": "wide shot",
    "depth_of_field": "deep",
    "focus": "The burning house and the lone figure in the snow.",
    "framing": "The small figure in the foreground provides a sense of scale against the larger burning structure in the mid-ground. The figure is walking away, creating a path in the snow that acts as a leading line out of the frame."
  },
  "description_short": "A digital painting depicting a solitary figure in a red cloak walking through a snowy landscape at night, away from a house that is on fire.",
  "environment": {
    "location_type": "outdoor",
    "setting_details": "A winter scene with a two-story house surrounded by evergreen trees, all set within a vast landscape covered in a thick layer of snow under a dark, starry sky.",
    "time_of_day": "night",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "strong",
    "source_direction": "back",
    "type": "cinematic"
  },
  "mood": {
    "atmosphere": "A somber and dramatic departure",
    "emotional_tone": "mysterious"
  },
  "narrative_elements": {
    "character_interactions": "A single figure is shown in relation to an event rather than another person, suggesting solitude and a significant personal moment.",
    "environmental_storytelling": "The burning house signifies a destructive, climactic event—the end of something. The figure walking away suggests a deliberate departure, escape, or even responsibility, leaving the viewer to question the circumstances.",
    "implied_action": "The figure is actively walking away from the fire, leaving behind a scene of destruction. The fire is still raging, implying the event has just happened."
  },
  "objects": [
    "burning house",
    "snow",
    "figure",
    "red cloak",
    "smoke",
    "trees",
    "torch"
  ],
  "people": {
    "ages": [
      "unknown"
    ],
    "clothing_style": "long red cloak",
    "count": "1",
    "genders": [
      "unknown"
    ]
  },
  "prompt": "A dramatic digital painting of a lone figure in a vibrant red cloak walking through a deep blue, snow-covered landscape at night. In the background, a house is engulfed in roaring orange flames, sending a thick plume of black smoke into the starry sky. The scene is illuminated by the fire's harsh glow, creating high contrast between the warm blaze and the cold surroundings. The mood is mysterious and melancholic, capturing a moment of intense and solitary drama. Painterly, cinematic style.",
  "style": {
    "art_style": "painterly",
    "influences": [
      "concept art",
      "cinematic illustration"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "digital painting",
    "high contrast",
    "night scene",
    "fire",
    "snow",
    "narrative",
    "complementary colors",
    "wide shot"
  ],
  "use_case": "Narrative illustration for storytelling, concept art for film or games, or a dataset for generating images with strong emotional and color contrast.",
  "uuid": "922278fe-8572-4713-8d67-75c2ef540f47"
}
```

</details>

<details><summary><b>Sophisticated Istanbul Stroll</b></summary>

```text
Full-body cinematic shot of a sophisticated man in his early 30s walking confidently down a historic cobblestone street in Istanbul, Beyoğlu. He features a short beard and dark hair. He is wearing a tailored navy blue wool overcoat, a charcoal grey turtleneck sweater, and black trousers. He is holding a premium brown leather briefcase in one hand and a takeaway coffee cup in the other. He is wearing brown leather Chelsea boots and stylish sunglasses. The background prominently features the iconic Galata Tower rising at the end of the street. Soft natural daylight, high-end fashion photography, realistic anatomical proportions, 8k resolution, highly detailed textures. --ar 9:16
```

</details>

<details><summary><b>Spontaneous Neon Bar Snapshot</b></summary>

```text
A candid spontaneous nighttime photograph of a young woman in her early 20s with a slim figure, long straight dark brown hair, wearing a black leather biker jacket. She is sitting at a table in a lively bar, leaning forward with her head tilted to the side, eyes closed tight in genuine laughter, showing her teeth in a wide joyful smile, her right hand raised to her face holding a black drinking straw near her mouth in a playful gesture. In the immediate foreground are two large round glass goblets filled with orange-yellow cocktails (michelada-style drinks) with abundant ice cubes, orange slices, and black straws, plus a yellow beverage can partially visible. The background shows a casual bar interior with light wooden plank walls, hanging Edison bulb lights, vibrant purple pink and blue LED neon lighting, a blue neon sign with Spanish text on the back wall, and two men sitting at a table in the softly blurred background. Lighting is mixed: direct frontal smartphone flash illuminating her face and creating specular highlights on the leather jacket and glass drinks, contrasting with purple pink and blue ambient neon lights in the background. Shot with a smartphone camera, 24mm equivalent lens, f/1.8, eye-level close-up angle from short distance, medium close-up vertical composition, shallow depth of field with blurred background bokeh, visible digital noise and flash photography aesthetic, casual snapshot style, vibrant saturated colors, girls night out vibe, Latin American modern bar atmosphere, Instagram Stories 2020s aesthetic, joyful and spontaneous mood.
```

</details>

<details><summary><b>Spotify Playlist Cover Designer</b></summary>

```text
Act as a graphic designer specializing in music playlist covers. You are tasked with creating visually appealing and clean Spotify playlist covers that align with the vibe of different music categories such as Pop, Rock, Jazz, Classical, and more.

Your task is to:
- Design covers that are aesthetically pleasing and resonate with the intended musical vibe.
- Ensure the design is clean, organized, and visually appealing.
- Incorporate elements or themes typical to each music category.

Rules:
- Use high-quality graphics and fonts.
- Maintain a consistent style that aligns with Spotify's branding.
- Consider the mood and emotion each category conveys and reflect that in the design.

Variables:
- ${category} - The music category for which the cover is being designed.
- ${playlistName} - The name of the playlist for which the cover is being designed.
```

</details>

<details><summary><b>Stable Diffusion Prompt Engineer</b> · machine translated</summary>

```text
Role: SD Prompt Engineer
## Profile:
- Author: AC
- version: 0.1 
- Language: English

## Background:
- I am a skilled prompt engineer for the AI art generation model Stable Diffusion, which is similar to DALLE-2. I have a deep understanding of the intricacies of positive and negative prompts, ensuring that the generated artwork meets users' expectations.

## Skills:
- Skilled at creating the prompt structure for Stable Diffusion.
- Understand the structure and importance of positive and negative prompts.
- Able to tailor prompts to the given context and requirements.
- Deep knowledge of art styles, media and techniques.
- Maximize the quality of generated artwork through specific prompting techniques.

## Goals:
- Create Stable Diffusion prompts according to the user's requirements.
- Ensure the prompts follow the positive and negative guidelines.
- Provide clearly structured prompts to achieve the desired artwork.
- Provide insights and suggestions to improve the quality of the generated artwork.
- Ensure the user is satisfied with the generated artwork.

## Constrains:
-Always stay in the role of a stable diffusion prompt engineer.
-Make sure the prompts provided are accurate and appropriate.
-Avoid generating prompts that could lead to inappropriate or offensive artwork.
-Always work within the structure of positive and negative prompts.
-Prioritize the user's requirements and feedback when crafting prompts.

## Examples:
A clearly structured positive prompt based on the following factors: (subject), (action), (background), (environment), (lighting), (artist), (style), (medium), (genre), (color scheme), (computer graphics), (quality), (etc.) 
Subject: people, animals, landscapes 
Action: dancing, sitting, surveillance 
Verbs: what the subject is doing, such as standing, sitting, eating, dancing, surveilling 
Adjectives: beautiful, realistic, big, colorful 
Background: a pond on an alien planet, lots of detail 
Environment/setting: outdoors, underwater, sky, night 
Lighting: soft, ambient, neon, fog, hazy 
Mood: cozy, energetic, romantic, cool, lonely, fearful 
Art medium: oil on canvas, watercolor, sketch, photography, monochrome background
Style: Polaroid, long exposure, monochrome, GoPro, fisheye, bokeh, Photo, 8k uhd, dslr, soft light, high quality, film grain, Fujifilm XT3 
Art style: comic, fantasy, minimalism, abstract, graffiti 
Material: fabric, wood, clay, realistic, illustration, drawing, digital painting, photoshop, 3D 
Color scheme: pastel, vibrant, dynamic lighting, green, orange, red 
Computer graphics: 3D, octane, cycles 
Illustration: isometric, Pixar, scientific, comic 
Image quality: HD, 4K, 8K, 64K
A clearly structured negative prompt based on the following factors: 2 heads, 2 faces, cropped image, out of frame, draft, deformed hands, signature, twisted fingers, double image, long neck, malformed hands, multiple heads, extra limbs, ugly, poorly drawn hands, missing limbs, disfigured, cut off, ugly, texture, low resolution, deformed, blurry, bad body, disfigured, poorly drawn face, mutation, mutated, floating limbs, disconnected limbs, long body, disgusting, poorly drawn, mutilated, mutilated, surreal, extra fingers, duplicate artifacts, sickly, gross proportions, missing arms, mutated hands, maimed hands, cloned face, malformed, ugly, tiled, poorly drawn hands, poorly drawn feet, poorly drawn face, out of frame, extra limbs, ruined, deformed, body out of frame, bad anatomy, watermark, signature, cut off, low contrast, underexposed, overexposed, bad art, beginner, amateur, distorted face, blurry, draft, grainy, etc.

## Workflow:
- Analyze the user's keywords and create a stable diffusion prompt that fits them
- Create the positive prompt according to the given structure: a complete, detailed prompt about my idea, starting with (subject), (action), (background), (environment), (lighting), (artist), (style), (medium), (genre), (color scheme), (computer graphics), (quality), (etc.). For the negative prompt, directly quote the <negative prompt> from the examples
- Provide reasons or insights for the selected prompt elements, including extra words that match the user's needs.
- Finalize the prompt based on the user's feedback, making sure the prompt structure suits stable diffusion

## Initialization
As a [Role], in the [Background] context, strictly follow the [Constrains] and talk to the user in <Languge: English> in the order of the [Workflow], introducing yourself with the first sentence: "Hello, Im..."
```

</details>

<details><summary><b>Stained Glass Fox Under a Harvest Moon</b></summary>

```text
A tall arched stained glass window depicting a red fox sitting on a mossy rock beneath a huge golden harvest moon, photographed straight-on from inside a quiet stone chapel at night so the window glows from behind. The fox is made of hand-cut glass pieces in warm amber, copper, and burnt orange, with a cream chest and a white-tipped tail curled around its paws, its head turned slightly upward toward the moon. Around it, a stylized autumn forest of birch trunks in pale grey glass, oak leaves in deep red and mustard, and tall grasses in olive green rise along both edges of the arch, framing the scene in Art Nouveau curves. The night sky is built from cobalt and midnight blue glass shards with small pale stars, and the moon is a single large circle of textured gold glass with subtle seed bubbles and streaks. Thick dark lead came lines outline every piece, with visible solder joints, slight irregular thickness, and a few horizontal iron support bars across the window. Light passes through the glass and casts soft colored pools of amber and blue onto the worn stone sill and floor below. Rich jewel tones, high detail, gentle glow, realistic glass texture with rippled cathedral glass and opalescent patches, calm and reverent mood. Symmetrical composition, centered window filling most of the frame, faint carved stone tracery around the arch. No people, no text, no religious figures, no signature. Vertical 3:4 aspect ratio.
```

</details>

<details><summary><b>Stained Glass Great Horned Owl Under a Full Moon</b></summary>

```text
A stained glass window panel of a great horned owl perched on an oak branch under a full moon, in a wide landscape 16:9 rectangular composition. The owl sits in the center of the panel facing the viewer, with tall pointed ear tufts, large glowing amber-orange eyes, a white throat patch, and mottled brown, tan, and black feather glass with fine painted detail. It grips a thick brown oak branch that runs across the lower third of the panel from left to right, with dark talons wrapped around it. Behind the owl, a large pale yellow full moon with soft crater markings sits slightly to the upper left of center. The night sky is built from irregular pieces of textured cobalt blue and deep violet glass with tiny bubbles, scattered with about a dozen small gold glass stars. Clusters of lobed oak leaves in emerald, lime, and olive green glass spread from the branch on both the left and right sides. Thick dark lead lines separate every glass piece, light shines through so the colors glow like a real window, and the whole panel is framed by a border of square ruby red textured glass tiles. Rich jewel tones, symmetrical, decorative, calm night mood. No text, no signature.
```

</details>

<details><summary><b>Steam Locomotive on a Stone Viaduct</b></summary>

```text
A black steam locomotive pulling four maroon passenger carriages crosses a tall weathered grey stone viaduct over a deep autumn river valley in the soft light of early morning. The viaduct runs nearly straight across the frame, from the left foreground edge to the right middle distance with a slight recession, about ten tall round arches visible. The train sits on the left-center of the deck: the locomotive at the left end, facing and heading left, with the four carriages trailing to the right. A large white steam plume rises from the chimney and drifts up and slightly back over the first carriage. Below, a misty river winds from the bottom center of the frame away under the arches toward the right, with a heavy band of mist on the water. On the right bank in the lower right corner stands a small stone farmhouse with a red roof and two chimneys. Both hillsides are covered with orange, red, gold, and green autumn trees. Low soft sun from the left casts a warm glow on the left side of the scene, under a pale blue sky with a few soft clouds and distant hazy hills. Photoreal landscape and railway photography, rich natural color, fine stone texture. Wide landscape 16:9. No people visible, no text, no signs, no logos.
```

</details>

<details><summary><b>Steam Locomotive Viaduct Concept Brief Builder</b></summary>

```text
Act as a cinematic environment designer who writes image-ready and motion-ready scene briefs. Help me design one hero shot of a vintage steam train crossing a tall stone railway viaduct over a river valley, which will first be generated as a still image and then animated into a short video that uses that image as its first frame. Your brief must make the still image rich in elements that can move naturally (billowing steam and smoke, the train rolling steadily along the viaduct, mist drifting over the river, leaves stirring on the trees, flowing water, soft shifting light) while keeping the composition calm, readable, and easy to animate.

My starting choices:
- Valley setting: ${setting:deep river valley with wooded hillsides and distant hazy hills}
- Season, time, and weather: ${time:autumn, early morning, light river mist, mostly clear sky}
- Train look: ${train:black steam locomotive pulling four maroon passenger carriages}
- Viaduct look: ${viaduct:weathered grey stone viaduct with many tall arches}
- Visual style: ${style:photoreal landscape and railway photography}
- Mood words: ${mood:nostalgic, peaceful, golden, timeless}

First ask me, in one short message, for anything missing: the camera viewpoint I prefer (from a hillside above and to one side, from the riverbank below, or level with the deck), which way the train should travel across the frame, how much of the river and valley floor should show, and anything to avoid (people, text, signs, logos, modern trains, power lines, a specific real viaduct or railway).

Then produce the brief with these sections:

1. **Scene Overview**: two or three sentences describing the place, the time, the light, and the feeling of the moment. Describe an imagined viaduct and train, not a copy of a real, named one.

2. **Viaduct and Train**: the viaduct's path across the frame (straight or curved, where it enters and leaves), number of visible arches, stone color and texture, parapet; the locomotive's position on the deck, which way it faces, chimney and boiler details, the number and color of carriages, and how much of the train is visible.

3. **Steam and Smoke**: where the plume rises, its color (white steam, grey smoke), size, and which way the wind carries it. State that the plume stays attached to the chimney and drifts with one wind direction.

4. **Valley and Landscape**: the river below and how it winds under the arches, hillside trees and their autumn colors, any small buildings (for example a stone farmhouse by the river), distant hills, and depth layers from foreground to background.

5. **Light and Atmosphere**: sun direction and color, where the warm glow falls, mist on the water and its height, haze on the distant hills, and the sky.

6. **Fixed Visual Details**: a numbered list of 8 to 10 details that must stay identical in the still image and in the video (viaduct path and arch count, train position and direction, carriage count and color, river path, farmhouse position, sun side, mist height, camera position, framing).

7. **Motion Map**: a table of every element that can move in the video, with columns: element, type of motion, direction, speed (very slow, slow, medium), and how strongly it should move. Include the train's travel along the deck and the camera move. Keep total motion subtle and physically plausible, with one wind direction for steam, smoke, mist, and leaves.

8. **Prompt Seed A - Hero Still Image**: a ready-to-paste image prompt under 170 words for a wide landscape 16:9 frame, with the train, the viaduct, and the valley in the first sentence, ending with: no people visible, no text, no signs, no logos.

9. **Prompt Seed B - Image-to-Video Animation**: a ready-to-paste video prompt under 120 words that starts from the hero still as the first frame, describes the train moving steadily in the direction it faces, the steam and mist motion, one slow camera move for about 6 seconds, and says to keep the viaduct, the valley, the buildings, and the framing exactly as in the image with no new objects.

Rules: no people as the main subject, no text, signs, or logos, no fast camera moves or cuts, and no motion that breaks physics (the train moves only along the rails in the direction the locomotive faces, the carriages stay coupled, steam rises from the chimney and drifts with the wind, water flows downstream). Use short paragraphs and lists.
```

</details>

<details><summary><b>Steam Locomotive Viaduct Image to Video</b></summary>

```text
Start from the step 2 image "Steam Locomotive Crossing a Stone Viaduct over an Autumn River Valley" as the exact first frame, and animate it into a calm ${duration:6}-second cinematic shot. Keep the stone viaduct running nearly straight across the frame with its arches, the river below, the red-roofed farmhouse in the lower right, the autumn hillsides, the distant hills, and the framing exactly as in the image. The black locomotive, at the left end of the train, moves steadily to the left along the viaduct deck, pulling its four maroon carriages behind it; the carriages stay coupled and on the rails. Thick white steam and smoke keep billowing from the chimney, rolling upward and drifting back to the right over the carriages. The mist over the river drifts slowly and swirls gently under the arches. Leaves on the nearby trees stir softly in the breeze. Warm low sunlight from the left glows steadily on the stone and the trees. The camera makes one very slow, smooth pan to the left, following the train. Natural, realistic motion, no cuts, no new objects, no people, no text.
```

</details>

<details><summary><b>Steampunk Reading Nook Inside a Living Oak</b></summary>

```text
Warm illustrated fantasy interior: a steampunk reading nook carved into the hollow heartwood of a giant living oak. Curved wooden walls follow the grain of the tree; floor-to-ceiling shelves packed with leather-bound books wrap around brass pipes, pressure gauges, and small clockwork orreries. A deep emerald velvet armchair and a low oak table hold an open book and a steaming porcelain cup. Soft amber light from an articulated brass desk lamp and hanging Edison bulbs; green stained-glass inserts in a round porthole window let in dappled forest light. Living vines and moss frame the shelves without covering the books. Polished copper rails, a spiral staircase of root wood leading up out of frame. Cozy, inviting, highly detailed storybook illustration style, no people, no text overlays, safe for work.
```

</details>

<details><summary><b>Stencil Vector Poster Portrait</b></summary>

```text
Transform the uploaded portrait into a high-contrast vector poster illustration.

Style requirements:
- Bold stencil / propaganda poster aesthetic
- Flat vector art
- 3–4 color palette only
- Solid red background
- Face rendered in grayscale tones (2–3 flat shadow layers)
- Black thick outer contour lines
- No gradients
- No texture
- No photorealism
- Sharp clean edges
- Posterized shading
- Centered head composition
- Minimal but strong facial features
- Graphic design style
- Adobe Illustrator vector look
- High contrast
- Smooth geometric shadow shapes

Output:
Crisp, clean, scalable vector-style portrait.
```

</details>

<details><summary><b>Sticker Image Generator</b></summary>

```text
{
  "role": "Image Designer",
  "task": "Create a detailed sticker image with a transparent background.",
  "style": "Colorful, vibrant, similar to Stickermule",
  "variables": {
    "text": "Custom text for the sticker",
    "icon": "Icon to be included in the sticker",
    "colorPalette": "Color palette to be used for the sticker"
  },
  "constraints": [
    "Must have a transparent background",
    "Should be colorful and vibrant",
    "Text should be readable regardless of the background",
    "Icon should complement the text style"
  ],
  "output_format": "PNG",
  "examples": [
    {
      "text": "${text:Hello World}",
      "icon": "${icon:smiley_face}",
      "colorPalette": "${colorPalette:vibrant}",
      "result": "A colorful sticker with '${text:Hello World}' text and a ${icon:smiley_face} icon using a ${colorPalette:vibrant} color palette. It's an image of ${details}"
    }
  ],
  "details": {
    "resolution": "300 DPI",
    "dimensions": "1024x1024 pixels",
    "layers": "Text and icon should be on separate layers for easy editing"
  }
}
```

</details>

<details><summary><b>Stippling Illustration of Istanbul Street</b></summary>

```text
Highly detailed hand-drawn illustration of a busy Istanbul street crossing, inspired by Taksim Square / İstiklal Avenue pedestrian flow, filled with dense crowds of people moving in multiple directions. The entire scene is created in a stippling / dotwork technique (pen-and-ink style), with tightly packed black ink dots forming shading, texture, and atmospheric depth.

Buildings reflect a layered Istanbul cityscape: historic Ottoman-era architecture blended with modern storefronts, cafes, tram lines, and dense vertical signage. Surfaces are covered with Turkish shop signs, bakery signs, street advertisements, posters, and illuminated urban details, blending contemporary city life with cultural heritage.

The composition uses a slightly top-down wide-angle perspective with strong depth cues. Foreground is filled with tightly packed pedestrians, midground shows the main intersection and tram corridor, background extends into dense urban blocks and skyline silhouettes.

Use monochrome black-and-white stippling as the base rendering, with selective vibrant accent colors (red, blue, green, yellow) highlighting signs, tram elements, flags, and key visual focal points. The illustration should feel highly intricate, with micro-details, layered textures, and strong visual storytelling.

Include atmospheric urban density, small human figures, subtle motion cues, and complex architectural variation. Style merges traditional European stippling engraving with modern urban illustration aesthetics.

-- ultra detailed -- 8k -- high resolution -- intricate -- hand drawn -- ink illustration -- stippling -- dot shading -- urban scene -- crowded city -- Istanbul
```

</details>

<details><summary><b>Stock Trading Video Prompt</b></summary>

```text
Create a highly detailed video prompt for an AI video generator like Sora or RunwayML, emphasizing photorealistic stock trading visuals without any human figures, text overlays, or AI-generated artifacts. The scene should depict the pursuit of profit through trading Apple Inc. (AAPL) stock in a visually metaphorical way: Show a lush, vibrant apple orchard under dynamic daylight shifting from dawn to dusk, representing market fluctuations. Apples on trees grow, ripen, and multiply in clusters symbolizing rising stock values and profits, with some branches extending upward like ascending candlestick charts made of twisting vines. Subtly integrate stock market elements visually—glowing green upward arrows formed by sunlight rays piercing through leaves, or apple clusters stacking like bar graphs increasing in height—without any explicit charts, numbers, or labels. Convey profit-seeking through apples being “harvested” by natural forces like wind or gravity, causing them to accumulate in golden baskets that overflow, shimmering with realistic dew and light reflections. Ensure the entire video feels like high-definition drone footage of a real orchard, with natural sounds of rustling leaves, birds, and wind, no narration or music. Camera movements: Smooth panning across the orchard, zooming into ripening apples to show intricate textures, and time-lapse sequences of growth to mimic market gains. Style: Ultra-realistic CGI indistinguishable from live-action nature documentary footage, using advanced rendering for lifelike shadows, textures, and physics—avoid any cartoonish, blurry, or unnatural elements. Video length: 30 seconds, resolution: 4K, aspect ratio: 16:9.
```

</details>

<details><summary><b>Stone Farmhouse at the End of Provence Lavender Rows</b></summary>

```text
Long straight rows of purple lavender lead toward an old two-story stone farmhouse in Provence at sunrise, seen from a low viewpoint at the end of a central dirt path, in a wide landscape 16:9 frame. The rounded lavender rows fill the whole lower half of the image and converge toward the middle distance, with narrow brown dirt paths between them and one path running straight up the center. The farmhouse stands in the right third: rough beige stone walls, a brown-terracotta tile roof, and small windows with pale blue shutters, with green shrubs in front of it. A single tall, dark green cypress tree rises right beside the house on its right side. In the left middle distance, a lone round green oak tree stands on a gentle grassy rise. The low sun sits just above the hills at the far left, glowing gold with a soft lens glow and light morning haze, casting warm light across the tops of the lavender. Rolling blue hills stretch across the horizon, and a few small white clouds float in a pale blue sky that warms to peach near the sun. Photoreal landscape photography, wide angle, natural colors, peaceful mood. No people, no text, no logos.
```

</details>

<details><summary><b>Stone Watermill at Autumn Dawn</b></summary>

```text
An old two-story fieldstone watermill with a large wooden overshot waterwheel on its right side stands beside a clear forest stream at autumn dawn. A raised wooden chute carries water onto the top of the wheel, and the water spills from its wooden buckets in bright splashing streams into the stream below. The mill has warm grey and honey-colored stone walls, a steep dark slate roof covered in moss, small white-framed windows with two glowing warm yellow on the ground floor, and a stone chimney on the left end with a thin trail of pale smoke. In the foreground, the stream tumbles over a low step of mossy rocks in a small cascade. Maple and beech trees in orange, red, and gold surround the mill, with fallen leaves floating on the water. Soft low mist drifts over the stream, and golden sunrise light breaks through the trees from the left. A few small birds fly in the pale sky above the roof. Photoreal landscape photography, calm and timeless mood. Wide landscape 16:9. No people, no text, no signs, no cars.
```

</details>

<details><summary><b>Stone Watermill at Autumn Dawn Image to Video</b></summary>

```text
Start from the step 2 image "Stone Watermill on a Forest Stream at Autumn Dawn" as the exact first frame, and animate it into a calm ${duration:6}-second cinematic shot. Keep the stone mill, the slate roof, the wooden overshot waterwheel on the right, the chute, the windows, the trees, and the framing exactly as in the image. The waterwheel turns slowly and steadily, driven by water pouring from the wooden chute onto its top, with bright water spilling from its buckets and splashing into the stream. The stream flows toward the camera and tumbles over the mossy rocks in the foreground with soft white foam. Low mist drifts slowly across the water from left to right. A few orange and gold leaves fall gently from the maples and float downstream. Thin pale smoke rises and curls from the chimney, the two lit windows glow with a faint warm flicker, and the small birds glide across the sky. Golden dawn light slowly brightens. The camera makes one very slow, smooth push-in toward the mill. Natural, realistic motion, no cuts, no new objects, no people, no text.
```

</details>

<details><summary><b>Stone Watermill Scene Brief Builder</b></summary>

```text
Act as a cinematic environment designer who writes image-ready and motion-ready scene briefs. Help me design one hero shot of a small old stone watermill on a stream, which will first be generated as a still image and then animated into a short video that uses that image as its first frame. Your brief must make the still image rich in elements that can move naturally (falling water, a turning wheel, mist, leaves, smoke, birds, flickering lights) while keeping the composition calm and easy to animate.

My starting choices:
- Region and landscape: ${region:temperate forest valley}
- Season and time of day: ${season:autumn dawn}
- Mill size and age: ${mill:two-story fieldstone mill, about 200 years old}
- Visual style: ${style:photoreal landscape photography}
- Mood words: ${mood:quiet, golden, misty, timeless}

First ask me, in one short message, for anything missing: the camera viewpoint I prefer (across the stream, from a small footbridge, or low near the water), whether the mill is still working or restored as a home or museum, and anything to avoid (people, animals, modern cars, power lines, signs).

Then produce the brief with these sections:

1. **Scene Overview**: two or three sentences describing the place, the season, the light, and the story of the moment.

2. **Mill Architecture**: wall stone color and texture, roof material and shape, number of floors and windows, door, chimney, and the waterwheel type (overshot, undershot, or breastshot) with its size, material, number of paddles or buckets, and which side of the building it sits on. Include the wooden chute or millrace that feeds it.

3. **Water and Landscape**: the stream's width and flow, small cascades or a weir, rocks and moss, the type and color of trees, the ground cover, and the background hills or forest.

4. **Light and Atmosphere**: sun direction and color, mist or fog layers, warm lights in windows, chimney smoke, and how the light touches the water.

5. **Fixed Visual Details**: a numbered list of 8 to 10 details that must stay identical in the still image and in the video (wheel side and size, roof color, number of lit windows, chimney position, chute shape, tree colors, camera position, framing).

6. **Motion Map**: a table of every element that can move in the video, with columns: element, type of motion, direction, speed (very slow, slow, medium), and how strongly it should move. Include the camera move. Keep total motion subtle and physically plausible.

7. **Prompt Seed A - Hero Still Image**: a ready-to-paste image prompt under 170 words for a wide landscape 16:9 frame, with the mill, the waterwheel, and the stream in the first sentence, ending with: no people, no text, no signs.

8. **Prompt Seed B - Image-to-Video Animation**: a ready-to-paste video prompt under 120 words that starts from the hero still as the first frame, describes one slow camera move and the natural motions from the Motion Map for about 6 seconds, and says to keep the mill, the wheel, and the framing exactly as in the image with no new objects.

Rules: no people or animals as the main subject, no text, signs, or logos, no fast camera moves or cuts, and no motion that breaks physics (water must flow downhill, the wheel turns in the direction the water pushes it). Use short paragraphs and lists.
```

</details>

<details><summary><b>Street-Art Punk Poster</b></summary>

```text
Create a high-resolution graphic artwork in a bold street-art / punk poster style. Composition: dynamic, asymmetrical collage of repeated human skulls across the canvas, varying in scale, rotation, and cropping, with overlaps and edge cut-offs. Arrange diagonally to create motion and flow (no symmetry).
Style: skulls as flat, high-contrast stencil-like graphics with sharp edges and minimal detail. Apply halftone dot texture for a gritty screen-printed look. Mix solid black/off-white skulls with neon yellow or acid green gradient fills.
Color palette: neon yellow, acid green, black, off-white. Use rough spray-paint gradients, especially green → yellow transitions. Background: distressed textures—paint splashes, ink noise, halftone dots, grunge overlays.
Add diagonal bands or torn-paper strips cutting through the layout. Inside them place bold text (“ERROR”, “404”, “DECAY”) in rough stencil/distressed sans-serif, slightly tilted and partially overlapping skulls.
Lighting: flat, graphic (no realistic shading), high contrast. Mood: aggressive, chaotic, urban, rebellious—graffiti / punk zine / screen print.
Avoid realism, smooth gradients, or clean polish; embrace noise, imperfections, raw texture.
```

</details>

<details><summary><b>Streetwear Alley Portrait</b></summary>

```text
Full body urban portrait photography of a young man with a slim athletic build, short textured brown hair, and light stubble, serious confident expression looking directly at the camera. He is wearing a black hoodie with a white geometric design on the chest, dark blue slim-fit jeans, brown leather work boots, and a wristwatch on his left wrist. Pose: sitting casually on a red brick wall, one leg hanging down, the other leg bent with his foot resting on the wall, relaxed and dynamic posture. Environment: narrow urban alleyway, red brick walls on both sides creating a corridor effect, industrial vibe, black barred window in the upper background. Lighting: natural daylight, soft lateral lighting, warm color palette, moderate contrast. Camera details: shot on 85mm lens, f/2.8 aperture, slight low angle from waist height, vertical composition, medium depth of field with the foreground brick wall slightly blurred. Style: contemporary street fashion photography, photorealistic, highly detailed, sharp focus on subject, 8k resolution, cinematic lighting, shot on Sony A7R IV. --ar 4:5 --style raw --v 6.0
```

</details>

<details><summary><b>Studio Beauty Editorial Close-up</b></summary>

```text
{
  "category": "STUDIO_BEAUTY_EDITORIAL_CLOSEUP",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking, beauty campaign vibe.",
    "hair": {
      "color": "Dark brown",
      "style": "Sleek but natural (not helmet hair)",
      "texture": "Individual strands visible, subtle flyaways"
    },
    "face": {
      "shape": "Soft oval",
      "eyes": "Sharp catchlights, clean lashes",
      "makeup": "Clean glam, subtle contour, natural lip",
      "skin_details": "High fidelity pores, no airbrush",
      "micro_details": "Fine vellus hairs visible under light"
    },
    "clothing": {
      "outfit": "Minimal black top, no logos"
    },
    "accessories": {
      "jewelry": ["Silver hoops"]
    }
  },
  "pose": {
    "type": "Beauty close-up",
    "orientation": "Frontal close-up",
    "hands": "One hand lightly framing jawline (perfect anatomy)",
    "gaze": "Direct eye contact",
    "expression": "Neutral confident"
  },
  "setting": {
    "environment": "Studio seamless background",
    "background_elements": ["Clean gradient backdrop, no texture distractions"],
    "depth": "Very shallow background distraction, subject isolated"
  },
  "camera": {
    "shot_type": "Close-up portrait",
    "angle": "Eye-level",
    "focal_length_equivalent": "85mm editorial portrait feel",
    "framing": "4:5 (tight head-and-shoulders)",
    "focus": "Eyes razor sharp, skin texture preserved"
  },
  "lighting": {
    "source": "Softbox key + gentle fill + subtle rim",
    "direction": "Key slightly above and to one side",
    "highlights": "Clean speculars, not oily",
    "shadows": "Soft, sculpted, premium"
  },
  "mood_and_expression": {
    "tone": "Premium, elegant, calm",
    "atmosphere": "High-end beauty campaign"
  },
  "style_and_realism": {
    "style": "Photoreal editorial",
    "fidelity": "Extremely high detail, no smoothing"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Very low",
    "resolution": "High"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "airbrushed skin", "plastic face", "cgi",
    "extra fingers", "warped hands",
    "readable text", "logos", "watermark"
  ]
}
```

</details>

<details><summary><b>Studio Family Picture</b></summary>

```text
Create a prompt to create family picture in a studio with customized arrangement of the family members
```

</details>

<details><summary><b>Studio Host Portraits</b></summary>

```text
Act as an image generation expert. Your task is to create studio images featuring a host in different professional postures. 

You will:
- Insert the host into a modern studio setting with realistic lighting.
- Ensure the host is positioned exactly as specified for each posture.
- Maintain the host's identity and appearance consistent across images.

Rules:
- Use ${positioning} for exact posture instructions.
- Include ${lighting:soft} to define the lighting style.
- Images should be high-resolution and suitable for professional use.
```

</details>

<details><summary><b>Studio Portrait with Cinematic Lighting</b></summary>

```text
Ultra-realistic cinematic studio portrait of a stylish man wearing thin round metal eyeglasses, minimal navy blazer over a black crew-neck shirt. Shot from a slightly low angle with confident, thoughtful expressions and subtle pose variations. Dramatic warm orange–red gradient background, bold color contrast. Soft key light from the front with warm rim lighting sculpting the jawline and cheekbones, deep shadows for a moody editorial feel. Natural skin texture, sharp facial details, realistic hair strands, premium DSLR look, shallow depth of field, 85mm lens aesthetic, fashion editorial photography, modern intellectual vibe, high contrast, ultra-high resolution.
```

</details>

<details><summary><b>Subway Platform Street Candid</b></summary>

```text
{
  "category": "SUBWAY_PLATFORM_STREET_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Use reference image identity exactly. Adult 21+. Preserve face proportions and marks. No beautification."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, match reference identity.",
    "hair": {
      "color": "Match reference.",
      "style": "Low ponytail or loose waves tucked behind scarf",
      "texture": "Real strands; slight frizz; flyaways",
      "movement": "Minimal movement, platform breeze subtle"
    },
    "face": {
      "eyes": "Exact reference; reflective catchlights",
      "skin_details": "Pores visible, realistic shadows",
      "micro_details": "Preserve marks"
    },
    "clothing": {
      "outerwear": "Minimal black coat or jacket (no logos/text)",
      "extras": "Scarf optional (no patterns with text)",
      "fabric": "Wool texture visible"
    },
    "accessories": {
      "jewelry": ["Small silver hoops (optional)"],
      "bag": "Simple tote/shoulder bag (no logos)"
    }
  },
  "pose": {
    "type": "Candid waiting",
    "orientation": "Half-body standing near platform edge (safe distance)",
    "head_position": "Slight tilt, calm posture",
    "hands": "One hand holding bag strap, other in pocket",
    "gaze": "Looking toward camera with neutral confidence",
    "expression": "Calm, slightly serious"
  },
  "setting": {
    "environment": "Subway platform",
    "background_elements": [
      "Overhead fluorescent lights",
      "Train blur in background (no readable signage)",
      "Platform tiles with realistic wear"
    ],
    "depth": "Face sharp; background softened"
  },
  "camera": {
    "shot_type": "Street-style portrait",
    "angle": "Eye level",
    "focal_length_equivalent": "35mm editorial OR 26mm phone",
    "framing": "4:5, leading lines from platform",
    "focus": "Eyes sharp, background motion blur allowed"
  },
  "lighting": {
    "source": "Fluorescent overhead + ambient",
    "direction": "Top-down with mild fill",
    "highlights": "Realistic shine on hair/skin",
    "shadows": "Soft, slightly cool subway contrast"
  },
  "mood_and_expression": {
    "tone": "Moody, urban, confident",
    "atmosphere": "Real city commute candid"
  },
  "style_and_realism": {
    "style": "Photoreal street portrait",
    "imperfections": "Noise + slight motion blur in background"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Moderate low-light grain",
    "mode_variants": {
      "amateur": "Phone-like HDR, mild grain, imperfect framing",
      "pro": "Cleaner exposure, controlled highlights, crisp subject separation"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_signage": true
  },
  "negative_prompt": [
    "readable signs", "logos", "watermark",
    "identity drift", "face morphing",
    "extra fingers", "warped hands",
    "cgi", "plastic skin", "over-smoothing"
  ]
}
```

</details>

<details><summary><b>Sunlit Bedroom Mirror Selfie</b></summary>

```text
{
  "scene_type": "Indoor lifestyle portrait (mirror-selfie aesthetic)",
  "environment": {
    "location": "Sunlit bedroom with gentle, natural daytime illumination",
    "background": {
      "bed": "White metal-frame bed with a soft vintage feel, dressed in light botanical-pattern bedding",
      "decor": "Clean, minimal styling with a couple of small potted plants, a simple nightstand, and understated floral touches",
      "windows": "Large window with airy sheer curtains that diffuse the light and soften the whole room",
      "color_palette": "Warm whites, ivory, beige, and pale neutrals with faint botanical and floral accents"
    },
    "atmosphere": "Quiet, intimate, cozy, breathable, and softly lived-in"
  },
  "subject": {
    "gender_presentation": "Feminine",
    "approximate_age_group": "Adult (21+), young adult",
    "skin_tone": "Fair complexion with realistic, natural skin texture and subtle imperfections",
    "hair": {
      "color": "Cool platinum blonde (slightly icy tone)",
      "style": "Long, straight hair with a clean center part, falling naturally over shoulders"
    },
    "facial_features": {
      "expression": "Gentle, calm, and slightly introspective, relaxed mouth and soft eyes",
      "makeup": "Very light, natural makeup with understated definition, nothing dramatic or heavy"
    },
    "body_details": {
      "build": "Slim to average physique with natural proportions",
      "visible_tattoos": [
        "Fine-line floral and illustrative tattoos along the arms and forearms",
        "A small, subtle tattoo visible on the upper thigh area"
      ]
    }
  },
  "pose": {
    "position": "Seated on the bed near the edge, comfortable and casual",
    "legs": "Knees bent and pulled in close, creating a compact, cozy silhouette",
    "hands": "One hand holds a phone up toward the mirror for a selfie composition, the other hand lightly touches the lips or rests near the mouth in a thoughtful gesture",
    "orientation": "Body angled toward a mirror, face partially obscured by the phone, maintaining an authentic mirror-selfie framing"
  },
  "clothing": {
    "outfit_type": "Lightweight sleepwear or a soft lounge slip suitable for a relaxed bedroom setting",
    "color": "Soft white or ivory (clean, minimal, gentle tone)",
    "material": "Soft, delicate fabric with a slightly translucent feel while remaining tasteful and non-explicit",
    "details": "Thin shoulder straps with subtle lace edging and refined trim details"
  },
  "styling": {
    "accessories": [
      "Minimal necklace with a small pendant or simple chain",
      "Small hoop earrings with a clean, understated look"
    ],
    "nails": "Natural nails or lightly manicured in a neutral finish, not flashy",
    "overall_style": "Soft, feminine, intimate, and quietly aesthetic without looking overly styled or artificial"
  },
  "lighting": {
    "type": "Natural daylight",
    "source": "Window light coming from the side at a slight angle, wrapping gently across the subject",
    "quality": "Diffused, soft, and even illumination with smooth falloff across skin and fabric",
    "shadows": "Very mild shadows that add natural contour without harsh contrast, keeping the mood tender and airy"
  },
  "mood": {
    "emotional_tone": "Serene, warm, reflective, and quietly intimate",
    "visual_feel": "Peaceful, soft, and realistic, like a candid moment captured in a calm morning"
  },
  "camera_details": {
    "camera_type": "Smartphone camera capture",
    "lens_equivalent": "Wide-angle feel (approximately 24–28mm equivalent) typical of a phone selfie lens",
    "perspective": "Mirror-selfie perspective with realistic framing, slight hand-held authenticity",
    "focus": "Crisp focus on the subject with natural depth cues, background gently readable but not overly sharp",
    "aperture_simulation": "Phone-like shallow depth impression (f/1.8 to f/2.2 style look), subtle and believable",
    "iso_simulation": "Low ISO for a clean image with minimal noise while preserving natural texture",
    "shutter_speed_simulation": "Fast enough to reduce motion blur and keep details sharp even with handheld capture",
    "white_balance": "Neutral daylight balance with gentle warmth, avoiding overly yellow or overly blue tones"
  },
  "rendering_style": {
    "realism_level": "Ultra photorealistic",
    "detail_level": "High fidelity skin texture, realistic fabric drape and lace behavior, natural lighting gradients, and true-to-life shadows",
    "post_processing": "Soft contrast with gentle highlights, natural color grading, mild clarity that preserves skin texture without smoothing it away",
    "artifacts": "No visual artifacts, no painterly effects, no CGI look, and no synthetic plastic skin"
  }
}
```

</details>

<details><summary><b>Sunlit Villa Afternoon</b></summary>

```text
{
  "image_analysis": {
    "meta": {
      "file_name": "image_ef3de2.jpg",
      "file_type": "uploaded file",
      "analyst_persona": "Technical Photo Analyst"
    },
    "scene_environment": {
      "location_type": "Indoor / Semi-outdoor transition (Sunroom or covered patio)",
      "atmosphere": "Tropical, luxurious, relaxed, warm",
      "background_texture": "Stone walls, natural light, wooden furniture"
    },
    "camera_technical": {
      "lens_type": "35mm - 50mm (Standard)",
      "angle": "Eye-level, slightly angled from the right",
      "focus": "Sharp focus on the subject, slight bokeh in the extreme foreground (orchids)",
      "composition": "Rule of thirds, subject center-left, framed by flowers on the right"
    },
    "lighting": {
      "general_condition": "High-key, natural daylight dominant",
      "sources": [
        {
          "id": "light_source_1",
          "type": "Natural Sunlight",
          "direction": "From left (viewer's perspective)",
          "color_temp": "Neutral/Cool White (Daylight ~5500K)",
          "intensity": "High",
          "effect_on_objects": "Creates distinct highlights on the subject's right leg, arm, and face. Casts soft shadows to the right."
        },
        {
          "id": "light_source_2",
          "type": "Ambient Fill",
          "direction": "Omnidirectional",
          "color_temp": "Warm",
          "intensity": "Low/Medium",
          "effect_on_objects": "Softens shadows on the wooden furniture and the subject's left side."
        }
      ]
    },
    "subject": {
      "identity": "Adult Female (Celebrity likeness noted, treated anonymously as per instruction)",
      "orientation": "Facing forward, body angled slightly to the right",
      "gaze_direction": "Direct eye contact with the camera",
      "emotional_state": "Confident, relaxed, alluring",
      "sensuality_level": "Moderate to High (due to attire and pose, but elegant)",
      "pose": {
        "general_description": "Seated semi-reclined on a wooden sofa/daybed",
        "posture_effect_on_emotion": "The reclined posture emphasizes relaxation and confidence",
        "legs": "Crossed; Right leg bent over the left knee",
        "feet_position": "Left foot resting on the floor/rug, right foot suspended in air, toes pointed (plantar flexion)",
        "hands_position": "Right hand resting on the white cushion behind her; Left hand resting near her thigh/knee",
        "visible_body_extent": "Full body visible (head to toe)"
      },
      "head": {
        "hair": {
          "color": "Brunette with honey/caramel balayage highlights",
          "style": "Long, loose waves, center part",
          "texture": "Silky, voluminous",
          "interaction_with_head": "Frames the face symmetrically, falling over shoulders"
        },
        "ears": {
          "visibility": "Partially covered by hair",
          "shape": "Indiscernible due to hair"
        },
        "face": {
          "structure": "Oval to diamond shape, high cheekbones",
          "forehead": "Smooth, standard height, partially framed by hair",
          "brows": "Well-groomed, arched, dark brown",
          "eyes": "Almond shape, dark, lined with makeup",
          "nose": "Straight, defined bridge",
          "upper_lip": "Defined cupid's bow, mauve lipstick",
          "mouth_area": "Closed, slight smirk/smile",
          "chin": "Defined, slightly pointed",
          "mimic": "Subtle, confident smile, seductive gaze"
        }
      },
      "body_details": {
        "skin_tone": "Tanned / Olive",
        "neck": "Visible, smooth, accentuated by V-neckline",
        "shoulders": "Exposed, rounded, relaxed",
        "chest": {
          "ratio_to_body": "Proportionally large (Voluptuous)",
          "estimated_size": "Full bust",
          "bra_status": "No visible bra (likely built-in support in swimsuit)",
          "nipples_visible": "No",
          "shape_description": "Natural, lifted"
        },
        "stomach": {
          "ratio_to_body": "Slim, toned",
          "ratio_to_chest": "Significantly smaller (Hourglass figure)",
          "ratio_to_hips": "Significantly smaller"
        },
        "hips": {
          "ratio_to_body": "Wide, curvy",
          "ratio_to_chest": "Balanced with chest",
          "shape": "Curvaceous"
        },
        "legs": {
          "thighs": "Full, smooth skin texture, highlighted by light source",
          "knees": "Smooth, defined",
          "calves": "Toned",
          "feet": "Bare, arched, well-pedicured (pale polish)"
        }
      },
      "attire": {
        "upper_garment": {
          "type": "One-piece swimsuit / Monokini",
          "color": "Dark Brown / Espresso",
          "details": "Lace-up front with gold grommets, halter neck style",
          "light_interaction": "Absorbs light, creates contrast with skin"
        },
        "lower_garment": {
          "type": "Swimsuit bottom (connected)",
          "accessory": "Floral patterned shawl/sarong",
          "details": "Draped underneath and slightly over the legs, multicolored floral print",
          "light_interaction": "Soft folds create shadows"
        },
        "accessories": {
          "jewelry": [
            {
              "item": "Bracelet",
              "location": "Left wrist",
              "type": "Chunky gold chain link",
              "material": "Gold metal"
            },
            {
              "item": "Necklace",
              "location": "Neck",
              "type": "Thin delicate chain",
              "visibility": "Barely visible"
            }
          ],
          "footwear": "None (Barefoot)"
        }
      }
    },
    "objects_in_scene": [
      {
        "object": "Wooden Sofa / Daybed",
        "description": "Ornate, dark wood with intricate carvings",
        "purpose": "Seating for subject",
        "ratio": "Dominates the middle ground",
        "color": "Dark Mahogany",
        "location": "Mid-ground, extending from left to center"
      },
      {
        "object": "Orchid Plant",
        "description": "Phalaenopsis orchids with purple and white blooms",
        "purpose": "Foreground framing element, adds depth and color",
        "ratio": "Large in foreground due to perspective",
        "color": "Bright Purple, White, Green stems",
        "location": "Foreground Right"
      },
      {
        "object": "Fruit Bowl",
        "description": "White bowl filled with citrus fruits (oranges/lemons)",
        "purpose": "Decor, adds color contrast",
        "ratio": "Small compared to subject",
        "color": "Bright Orange, Yellow",
        "location": "Foreground Right (lower corner)"
      },
      {
        "object": "Lamp",
        "description": "White geometric/honeycomb textured base with white shade",
        "purpose": "Background decor",
        "ratio": "Medium",
        "color": "White",
        "location": "Background Left"
      },
      {
        "object": "Book/Magazine",
        "description": "Coffee table book featuring a face on the cover",
        "purpose": "Foreground detail",
        "ratio": "Small slice visible",
        "location": "Extreme Foreground Bottom Center"
      }
    ],
    "negative_prompts": [
      "bad anatomy",
      "extra fingers",
      "missing limbs",
      "distorted face",
      "low resolution",
      "blurry subject",
      "overexposed",
      "underexposed",
      "watermark",
      "text overlay (except book title)",
      "cartoon",
      "illustration",
      "CGI",
      "unnatural skin tone"
    ]
  }
}
```

</details>

<details><summary><b>Sunny Beach</b></summary>

```text
Generate an image of people sunbathing on a sunny beach. Capture a relaxing and joyful atmosphere with clear blue skies and gentle waves in the background. Include diverse individuals enjoying the sun, with beach towels and umbrellas scattered around.
```

</details>

<details><summary><b>Sunny Patio Selfie with Tiki Decor</b></summary>

```text
{
  "scene_analysis": {
    "environment": {
      "type": "Outdoor",
      "setting": "Patio or backyard terrace",
      "weather": "Sunny, clear sky visible",
      "background_elements": [
        "Grey stucco wall",
        "Artificial green hedge wall",
        "Blue sky"
      ]
    },
    "camera": {
      "lens": "Wide-angle lens (typical of smartphone front camera)",
      "angle": "Selfie angle, slightly low looking up, close-up framing",
      "focus": "Sharp focus on the subject's face and upper body",
      "distortion": "Slight perspective distortion due to wide angle"
    },
    "lighting": {
      "overall_condition": "Bright natural daylight, hard lighting",
      "sources": [
        {
          "source_id": 1,
          "type": "Sun",
          "angle": "High angle, coming from the upper left (subject's right)",
          "color": "Natural white/warm daylight",
          "intensity": "High/Strong",
          "effects_on_objects": "Creates hard shadows under the subject's hair, chin, and nose. Casts defined shadows on the grey wall behind. Illuminates the hair creating a golden sheen."
        }
      ]
    }
  },
  "subjects": [
    {
      "id": "person_1",
      "type": "Human",
      "gender": "Female",
      "identity": "Anonymous",
      "orientation": {
        "facing": "Directly towards the camera",
        "body_rotation": "Frontal, slight lean forward"
      },
      "emotional_state": {
        "mood": "Relaxed, confident, slightly sultry",
        "expression": "Neutral with slightly parted lips, 'bedroom eyes'",
        "lust_factor": "Moderate to High (suggestive pose and nudity implication)",
        "posture_effect": "The leaning posture emphasizes the chest and creates a casual, intimate vibe"
      },
      "pose": {
        "general_definition": "Leaning forward selfie, likely sitting or kneeling",
        "feet_position": "Not visible (out of frame)",
        "hand_position": "Right arm extended holding the camera (implied), Left arm resting on a lower surface/knee",
        "visible_extent": "Head to waist/mid-torso"
      },
      "head": {
        "structure": "Oval face shape, defined jawline",
        "hair": {
          "color": "Light brown with blonde highlights (bronde)",
          "style": "Shoulder-length, layered, textured/messy look",
          "shape": "Frames the face, voluminous",
          "condition": "Sun-kissed, dry texture"
        },
        "ears": "Partially covered by hair",
        "forehead": "Partially covered by bangs/hair strands, smooth skin",
        "brows": "Natural, brushed up, dark brown",
        "eyes": {
          "gaze": "Direct eye contact with the lens",
          "shape": "Almond",
          "makeup": "Minimal or natural look"
        },
        "nose": {
          "structure": "Straight, slightly button tip",
          "details": "Freckles visible across the bridge"
        },
        "mouth_area": {
          "lips": "Very full, plump, upper lip slightly lifted",
          "mouth_state": "Slightly open",
          "philtrum": "Defined"
        },
        "chin": "Rounded but defined",
        "mimics": "Relaxed facial muscles, seductive gaze"
      },
      "body": {
        "skin": {
          "tone": "Tanned",
          "texture": "Smooth, freckles on chest and face"
        },
        "neck": {
          "visibility": "Visible",
          "tattoo": "Small text tattoo on the center/throat area (vertical characters)"
        },
        "shoulders": {
          "visibility": "Visible",
          "posture": "Relaxed, slightly hunched forward due to leaning"
        },
        "chest": {
          "ratio_to_body": "Prominent",
          "estimated_size": "Full bust",
          "bra_status": "None (No bra visible)",
          "nipples_visible": "No (Hidden by framing/shadows)",
          "shape_notes": "Natural droop due to gravity and leaning pose, cleavage visible",
          "tattoo": "Gothic script text tattoo reading 'Divine Feminine' on the sternum"
        },
        "belly": {
          "visibility": "Partially visible (upper abdomen)",
          "ratio": "Slim relative to chest"
        },
        "arms": {
          "tattoos": {
            "right_arm": "Heavy ink, large sleeve/designs visible",
            "left_arm": "Sketch-style tattoos including an anime-style girl face, a hummingbird, and line art"
          }
        }
      },
      "clothing": {
        "upper_body": "None (Topless implied)",
        "lower_body": "Not clearly visible, possibly a white towel or garment bunched near the bottom left",
        "accessories": "Bracelet on left wrist (silver/thin chain)"
      },
      "light_interaction_body": {
        "face": "Evenly lit with highlights on the forehead and nose bridge",
        "chest": "Highlights on the upper curve of the breasts, deep shadows in the cleavage",
        "hair": "Backlighting effect on the top strands"
      }
    }
  ],
  "objects": [
    {
      "id": "object_1",
      "name": "Tiki Totem Statue",
      "description": "Wooden carved statue with a face",
      "color": "Grey/brown wood with painted red tongue and yellow teeth",
      "position": "Right side of the frame, foreground",
      "purpose": "Decoration, aesthetic element",
      "ratio": "Large vertical element comparable to subject's head size in perspective"
    },
    {
      "id": "object_2",
      "name": "Planter with Greenery",
      "description": "Rustic wooden planter box with artificial ferns/plants",
      "color": "Whitewashed wood, sage green plants",
      "position": "Right side, behind the Tiki statue",
      "purpose": "Decor, background texture"
    },
    {
      "id": "object_3",
      "name": "BBQ Grill",
      "description": "Stainless steel outdoor grill",
      "color": "Metallic silver",
      "position": "Far left edge, partially cropped",
      "purpose": "Functional patio equipment"
    }
  ],
  "negative_prompts": [
    "clothing on upper body",
    "shirt",
    "bra",
    "bikini top",
    "deformed hands",
    "bad anatomy",
    "blurry",
    "low resolution",
    "dark lighting",
    "indoor setting",
    "male subject",
    "sunglasses"
  ]
}
```

</details>

<details><summary><b>Surreal CGI Photography Hybrid Portrait</b></summary>

```text
{
  "prompt_type": "Surreal CGI-Photography Hybrid Portrait",
  "subject": {
    "reference_identity": "Crucially, the woman's facial features, hair, and unique identity must match the provided reference photo exactly.",
    "expression": "Neutral expression, gazing upward.",
    "pose": "A surreal full-body composition viewed from above. Her upper torso and arms emerge physically from a smartphone screen lying flat, hands resting on the screen's bezel. Her lower body is digitally contained within the screen's display.",
    "attire": {
      "upper_body_real": "Attractive daily wear: A fitted, charcoal grey ribbed knit sweater. White over-ear headphones are on her head.",
      "lower_body_screen": "Attractive daily wear: Dark high-waisted skinny jeans and stylish black leather ankle boots, rendered digitally within the phone interface."
    }
  },
  "environment": {
    "setting": "A minimalist gray concrete surface where a black smartphone lies flat.",
    "screen_content": "The smartphone display shows a music player app interface. Track: 'Lions In a Cage' by Pentagram. Timestamp: 0:41 / 5:59. Background visual on screen: A warm sunset with silhouetted palm trees.",
    "props": "Iphone 16"
  },
  "cinematography": {
    "camera_angle": "High top-down view (God's eye angle), looking straight down at the phone and emerging subject.",
    "lens": "35mm wide-angle lens, creating perspective integration between the real and digital worlds.",
    "aperture": "f/8 for deep depth of field, keeping both the physical subject and the screen content sharp.",
    "lighting": "Soft artificial overhead and frontal lighting mixed with the warm glow emanating from the smartphone screen. Medium contrast, diffused shadows. The lighting palette is slightly warm and desaturated, mirroring an intimate indoor setting.",
    "color_palette": "Neutral gray-white dominant palette in the real world, contrasted by the warm oranges, deep reds, and greens from the sunset interface on the screen.",
    "style": "Digital CGI blended seamlessly with photography. Whimsical, surreal, tech-inspired, and immersive mood."
  }
}
```

</details>

<details><summary><b>Surreal Miniature Cityscape with Giant Observer</b></summary>

```text
{
  "colors": {
    "color_temperature": "neutral",
    "contrast_level": "high",
    "dominant_palette": [
      "blue",
      "red",
      "green",
      "yellow",
      "brown"
    ]
  },
  "composition": {
    "camera_angle": "eye-level",
    "depth_of_field": "deep",
    "focus": "The miniature city diorama held by the woman",
    "framing": "The woman's hands frame the central diorama, creating a scene-within-a-scene effect. The composition is dense and layered, guiding the eye through numerous details."
  },
  "description_short": "A surreal digital artwork depicting a giant young woman holding a complex, multi-level cross-section of a vibrant, futuristic city that blends traditional East Asian architecture with modern technology.",
  "environment": {
    "location_type": "cityscape",
    "setting_details": "A fantastical, sprawling metropolis featuring a mix of traditional East Asian architecture, such as pagodas and arched bridges, alongside futuristic elements like flying vehicles and dense, multi-story buildings with neon signs. The scene is presented as a miniature world held by a giant figure, with a larger version of the city extending into the background.",
    "time_of_day": "daytime",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "strong",
    "source_direction": "mixed",
    "type": "cinematic"
  },
  "mood": {
    "atmosphere": "Whimsical urban fantasy",
    "emotional_tone": "surreal"
  },
  "narrative_elements": {
    "character_interactions": "The main giant woman is observing the miniature world. Within the diorama, tiny figures are engaged in daily life activities: a man sits in a room, others stand on a balcony, and two figures in traditional dress stand atop the structure.",
    "environmental_storytelling": "The juxtaposition of the giant figure holding a miniature world suggests themes of creation, control, or observation, as if she is a god or dreamer interacting with her own reality. The blend of old and new architecture tells a story of a culture that has advanced technologically while preserving its heritage.",
    "implied_action": "The woman is intently studying the miniature world she holds, suggesting a moment of contemplation or decision. The city itself is bustling with the implied motion of vehicles and people."
  },
  "objects": [
    "woman",
    "miniature city diorama",
    "buildings",
    "flying vehicles",
    "neon signs",
    "vintage car",
    "bridge",
    "pagoda"
  ],
  "people": {
    "ages": [
      "young adult"
    ],
    "clothing_style": "A mix of modern casual wear, business suits, and traditional East Asian attire.",
    "count": "unknown",
    "genders": [
      "female",
      "male"
    ]
  },
  "prompt": "A hyper-detailed, surreal digital painting of a giant, beautiful young woman with dark bangs and striking eyes, holding a complex, multi-layered miniature city diorama. The diorama is a vibrant cross-section of a futuristic East Asian metropolis, filled with tiny people, neon-lit signs in Asian script, a vintage green car, and traditional pagodas. In the background, a sprawling version of the city expands under a clear blue sky, with floating transport pods and intricate bridges. The style is a blend of magical realism and cyberpunk, with cinematic lighting.",
  "style": {
    "art_style": "surreal",
    "influences": [
      "cyberpunk",
      "magical realism",
      "collage art",
      "Studio Ghibli"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "hyper-detailed",
    "intricate",
    "surrealism",
    "digital illustration",
    "cityscape",
    "fantasy",
    "miniature",
    "scene-within-a-scene",
    "vibrant colors"
  ],
  "use_case": "Concept art for a science-fiction or fantasy film, book cover illustration, or a dataset for training AI on complex, detailed scenes.",
  "uuid": "a00cdac4-bdcc-4e93-8d00-b158f09e95db"
}
```

</details>

<details><summary><b>Surreal Split-Light Portrait</b></summary>

```text
Surreal dreamlike portrait of an Iranian woman, face split by two different light sources (cold blue / warm amber), floating dust particles. Her brows work in opposite directions — one raised, one lowered — eyes not aligned in focus, embodying pure indecision. Below the image, a sketchy hand-inked box with wobbly handwritten text: "دو دلم".
```

</details>

<details><summary><b>SVG Designer</b></summary>

```text
I would like you to act as an SVG designer. I will ask you to create images, and you will come up with SVG code for the image, convert the code to a base64 data url and then give me a response that contains only a markdown image tag referring to that data url. Do not put the markdown inside a code block. Send only the markdown, so no text. My first request is: give me an image of a red circle.
```

</details>

<details><summary><b>Symbiote Suit Editorial Portrait</b></summary>

```text
Photorealistic portrait of a young woman with long honey-brown hair parted in the middle, wearing a black Spider-Man symbiote suit with raised web pattern texture and metallic gray spider emblem on chest. She stands in three-quarter pose, hands on chest, direct intense gaze at camera. Professional studio lighting with soft shadows, medium gray seamless background. Mid-shot composition, vertical format. High detail fabric texture, cinematic photography style, 85mm lens, sharp focus, editorial quality.
```

</details>

<details><summary><b>Synthwave Desert Highway Convertible</b></summary>

```text
An empty cherry-red vintage convertible parked on the shoulder of a straight desert highway at sunset, rendered in retro synthwave style. The highway runs to a vanishing point where a huge striped sun, banded in hot pink, orange, and yellow, sits half below the horizon. Glowing magenta grid lines stretch across the desert floor, and tall saguaro cacti stand in dark silhouette along the road. Low purple mountains with neon cyan rim light frame the horizon. The sky fades from deep violet at the top to coral near the sun, with a few soft stars and thin horizontal clouds. Chrome bumpers and the car's curved fins catch pink and teal reflections; the dashed center line glows faintly. Clean 1980s retro-futuristic look, subtle film grain and gentle bloom, cinematic wide composition. No people, no text, no logos, no license plate characters.
```

</details>

<details><summary><b>Table with Various Items</b></summary>

```text
Create an image of a table with various items placed on it. The scene should include a lamp as a central object, along with other miscellaneous items such as books, a cup, and a plant. Aim for a realistic and detailed depiction, capturing shadows and reflections to enhance the ambiance.
```

</details>

<details><summary><b>Tactical Security Guard Image</b></summary>

```text
Create an image of a Latino private security guard. The guard should be depicted wearing a tactical helmet and a bulletproof vest. The vest should have a communication radio attached and prominently display the word 'FENASPE'. The setting should convey professionalism and readiness, capturing the essence of a security environment.
```

</details>

<details><summary><b>Tech Brand Identity Image</b></summary>

```text
Create a premium 4K ultra-high-resolution corporate technology brand identity image for a company named exactly:

"Spine For Technologies"

Design a futuristic, innovative, sophisticated logo that represents advanced technology, digital transformation, artificial intelligence, software development, cybersecurity, and the future of technological innovation.

The logo should be an original geometric symbol inspired by a technological spine / interconnected digital structure, intelligently combining the concepts of "Spine" and "Technology" into one distinctive visual mark. Use elegant geometric shapes, precise lines, subtle circuit-board patterns, connected nodes, and a dynamic sense of digital evolution.

Place the logo prominently in the center, with the company name:

"Spine For Technologies"

directly underneath it in a premium modern sans-serif typeface. Typography must be extremely clean, sharp, professional, perfectly aligned, and highly legible.

Visual style: futuristic technology, premium corporate identity, cutting-edge innovation, sophisticated minimalism, high-end digital branding.

Color palette: deep black and dark navy background with electric blue, cyan, and subtle violet luminous accents. Add controlled neon glow, metallic reflections, subtle glass effects, elegant light trails, and very refined technological details.

Composition should feel powerful, intelligent, trustworthy, innovative, and suitable for a global technology company.

Cinematic studio lighting, dramatic depth, realistic reflections, volumetric light, subtle particles, high contrast, clean composition, professional branding presentation, extremely sharp details, photorealistic 3D logo rendering.

4K resolution, ultra-detailed, crisp edges, premium quality, professional corporate branding, no people, no unnecessary objects, no clutter, no watermark.

IMPORTANT:
The company name must be written EXACTLY as:
"Spine For Technologies"

Do not misspell, alter, abbreviate, or replace any letters in the company name.
```

</details>

<details><summary><b>Tech Desk Builder Portrait</b></summary>

```text
{
  "category": "TECH_DESK_BUILDER_HALF_BODY",
  "subject": {
    "demographics": "Adult woman, 21-29, Turkish-looking, creator vibe.",
    "hair": {
      "color": "Dark brown",
      "style": "Low ponytail or loose waves",
      "texture": "Strands visible, slight flyaways"
    },
    "face": {
      "eyes": "Focused but friendly",
      "skin_details": "Real texture, no smoothing",
      "makeup": "Minimal"
    },
    "clothing": {
      "outfit": "Casual black top + light cardigan, no logos",
      "fabric": "Real knit weave, subtle wrinkles"
    },
    "accessories": {
      "jewelry": ["Silver hoops"]
    }
  },
  "pose": {
    "type": "Half-body seated",
    "orientation": "Body slightly angled, shoulders relaxed",
    "hands": "One hand near trackpad, other tucking hair behind ear",
    "gaze": "Looking at camera with small smirk",
    "posture": "Relaxed confident"
  },
  "setting": {
    "environment": "Minimal desk setup",
    "background_elements": [
      "Laptop/monitor with generic blurred UI (NO readable text)",
      "Warm desk lamp + cool monitor glow mix",
      "Plant in corner, small clutter blurred"
    ],
    "depth": "Face sharp, background bokeh"
  },
  "camera": {
    "shot_type": "Half-body lifestyle portrait",
    "angle": "Slightly above eye level",
    "focal_length_equivalent": "26mm phone or 50mm pro",
    "framing": "4:5",
    "focus": "Eyes sharp"
  },
  "lighting": {
    "source": "Warm lamp + cool monitor glow",
    "direction": "Soft mixed lighting with gentle shadows",
    "highlights": "Natural facial speculars",
    "shadows": "Soft, realistic"
  },
  "mood_and_expression": {
    "tone": "Cozy creator, confident",
    "expression": "Micro-smirk",
    "atmosphere": "Late-night build session vibe"
  },
  "style_and_realism": {
    "style": "Photorealistic lifestyle",
    "imperfections": "Mild noise, slight imperfect WB"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild",
    "resolution": "High"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_screens": true
  },
  "negative_prompt": [
    "readable UI text", "logos", "watermark",
    "plastic skin", "cgi",
    "extra fingers", "warped hands"
  ]
}
```

</details>

<details><summary><b>Teen Book Cover Illustration</b></summary>

```text
Thoughtful Islamic book cover illustration for teenagers, side silhouette of a young person. Inside the head a question mark transforming into light and certainty. Arabic word "اليقين" integrated in the light. Deep purple and blue tones, minimalist and modern style, serious educational mood, no cartoon elements, vertical format, high resolution.
```

</details>

<details><summary><b>Terminal Drift</b></summary>

```text
{
  "title": "Terminal Drift",
  "description": "A haunting visualization of a lone traveler stuck in an infinite, empty airport terminal that defies logic.",
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve her core likeness. Transform Subject 1 (female) into a solitary figure standing in an endless, windowless airport terminal. The surrounding space is a repetitive hallway of beige walls, low ceilings, and patterned carpet. There are no exits, only the endless stretch of artificial lighting and empty waiting chairs. The composition should adhere to a cinematic 1:1 aspect ratio.",
  "details": {
    "year": "Indeterminate 1990s",
    "genre": "Liminal Space",
    "location": "A vast, curving airport corridor with no windows, endless beige walls, and complex patterned carpet.",
    "lighting": [
      "Flat fluorescent overheads",
      "Uniform artificial glow",
      "No natural light source"
    ],
    "camera_angle": "Wide shot, symmetrical center-framed composition.",
    "emotion": [
      "Disassociation",
      "Unease",
      "Solitude"
    ],
    "color_palette": [
      "Beige",
      "Muted Teal",
      "Faded Maroon",
      "Off-white"
    ],
    "atmosphere": [
      "Uncanny",
      "Sterile",
      "Silent",
      "Timeless"
    ],
    "environmental_elements": "Rows of empty connected waiting chairs, commercial carpeting with a confusing pattern, generic signage with indecipherable text.",
    "subject1": {
      "costume": "A slightly oversized pastel sweater and loose trousers, appearing mundane and timeless.",
      "subject_expression": "A vacant, glazed-over stare, looking slightly past the camera into the void.",
      "subject_action": "Standing perfectly still, arms hanging loosely at her sides, holding a generic roller suitcase."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "crowds",
        "sunlight",
        "deep shadows",
        "dirt",
        "clutter",
        "windows looking outside",
        "lens flare"
      ],
      "exclude_styles": [
        "high contrast",
        "action movie",
        "vibrant saturation",
        "cyberpunk",
        "horror gore"
      ],
      "exclude_colors": [
        "neon red",
        "pitch black",
        "vibrant green"
      ],
      "exclude_objects": [
        "airplanes",
        "trash",
        "blood",
        "animals"
      ]
    }
  }
}
```

</details>

<details><summary><b>Terminal Velocity</b></summary>

```text
{
  "title": "Terminal Velocity",
  "description": "A high-stakes action frame capturing a woman sprinting through a crumbling industrial tunnel amidst sparks and chaos.",
  "prompt": "You will perform an image edit to create an Ultra-Photorealistic, Movie-Quality action shot. The result must be photorealistic, highly detailed, and feature cinematic lighting. Emulate the look of a blockbuster film shot on Arri Alexa with a shallow depth of field. Depict Subject 1 sprinting towards the camera in a dark, collapsing industrial tunnel, surrounded by flying sparks and falling debris.",
  "details": {
    "year": "Contemporary Action Thriller",
    "genre": "Cinematic Photorealism",
    "location": "A dilapidated, steam-filled industrial maintenance tunnel with flickering lights and exposed wiring.",
    "lighting": [
      "High-contrast chiaroscuro",
      "Warm backlight from exploding sparks",
      "Cold, gritty fluorescent ambient light",
      "Volumetric lighting through steam"
    ],
    "camera_angle": "Low-angle frontal tracking shot with motion blur on the background.",
    "emotion": [
      "Adrenaline",
      "Panic",
      "Determination"
    ],
    "color_palette": [
      "Concrete grey",
      "Hazard orange",
      "Steel blue",
      "Deep shadow black"
    ],
    "atmosphere": [
      "Chaotic",
      "Explosive",
      "Gritty",
      "Claustrophobic"
    ],
    "environmental_elements": "Cascading electrical sparks, motion-blurred debris, steam venting from broken pipes, wet concrete floor reflecting the chaos.",
    "subject1": {
      "costume": "black mini skirt, white crop top, leather fingerless gloves",
      "subject_expression": "Intense focus with mouth slightly parted in exertion, sweat glistening on skin, hair flying back.",
      "subject_action": "running"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "sunlight",
        "calm environment",
        "clean surfaces",
        "smiling",
        "standing still"
      ],
      "exclude_styles": [
        "cartoon",
        "3d render",
        "illustration",
        "sketch",
        "low resolution"
      ],
      "exclude_colors": [
        "pastel pink",
        "vibrant green",
        "soft colors"
      ],
      "exclude_objects": [
        "trees",
        "sky",
        "animals",
        "vehicles"
      ]
    }
  }
}
```

</details>

<details><summary><b>The Aether Workshop</b></summary>

```text
{
  "title": "The Aether Workshop",
  "description": "A vibrant, nostalgic snapshot of two inventors collaborating on a clockwork masterpiece in a sun-drenched steampunk atelier.",
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Render the scene in the distinct style of vintage Kodachrome film stock, characterized by high contrast, rich saturation, and archival film grain. Subject 1 (male) is a focused steampunk mechanic tinkering with the gears of a brass automaton. Subject 2 (female) is a daring airship pilot leaning over a workbench, examining a complex schematic. They are surrounded by a chaotic, sun-lit workshop filled with ticking gadgets, steam pipes, and scattered tools.",
  "details": {
    "year": "Alternate 1890s",
    "genre": "Kodachrome",
    "location": "A high-ceilinged, cluttered attic workshop with large arched windows overlooking a smoggy industrial city.",
    "lighting": [
      "Hard, warm sunlight streaming through dusty glass",
      "High contrast shadows typical of slide film",
      "Golden hour glow"
    ],
    "camera_angle": "Eye-level medium shot, creating an intimate, documentary feel. 1:1 cinematic composition.",
    "emotion": [
      "Focused",
      "Collaborative",
      "Inventive"
    ],
    "color_palette": [
      "Polished brass gold",
      "Deep mahogany brown",
      "Vibrant iconic Kodachrome red",
      "Oxidized copper teal"
    ],
    "atmosphere": [
      "Nostalgic",
      "Warm",
      "Dusty",
      "Tactile"
    ],
    "environmental_elements": "Floating dust motes catching the light, steam venting softly from a copper pipe, blueprints pinned to walls, piles of cogs and springs.",
    "subject1": {
      "costume": "A grease-stained white shirt with rolled sleeves, a heavy leather apron, and brass welding goggles resting on his forehead.",
      "subject_expression": " intense concentration, brow furrowed as he adjusts a delicate mechanism.",
      "subject_action": "Holding a fine screwdriver and tweaking a golden gear inside a robotic arm."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "neon lights",
        "digital displays",
        "plastic materials",
        "modern sleekness",
        "blue hues"
      ],
      "exclude_styles": [
        "digital painting",
        "3D render",
        "anime",
        "black and white",
        "sepia only",
        "low saturation"
      ],
      "exclude_colors": [
        "fluorescent green",
        "hot pink"
      ],
      "exclude_objects": [
        "computers",
        "smartphones",
        "modern cars"
      ]
    },
    "subject2": {
      "costume": "A brown leather aviator jacket with a shearling collar, a vibrant red silk scarf, and canvas trousers.",
      "subject_expression": "Curious and analytical, pointing out a specific detail on the machine.",
      "subject_action": "Leaning one hand on the workbench while holding a rolled-up blue schematic in the other."
    }
  }
}
```

</details>

<details><summary><b>The Digital Frontier: Pixelated Pioneers</b></summary>

```text
#version 1.0
root{details,prompt:str}:
  details{atmosphere,camera_angle:str,color_palette,emotion,environmental_elements:str,genre:str,lighting,location:str,subject1,subject2,year:str}:
    atmosphere[4]: Playful,Dreamlike,Digital frontier,Calm isolation
    camera_angle: "High-angle isometric view, emphasizing the island's isolation and the blocky aesthetics, 1:1 cinematic aspect ratio."
    color_palette[4]: Saturated primary colors,vibrant greens and blues for the island,deep purples and blacks for the void,pixelated orange accents
    emotion[4]: Wonder,Curiosity,Discovery,Serenity
    environmental_elements: "Blocky, geometric trees with glowing leaves, pixelated waterfalls cascading into the void, floating abstract digital dust motes, subtle grid lines on the void's floor."
    genre: Voxel Art
    lighting[3]: Emissive light from the voxels themselves,"soft, diffuse ambient light from the digital void",subtle rim lighting on the blocky figures
    location: "A solitary, blocky floating island made of glowing voxels, suspended in an infinite digital void, with sparse, geometric trees and structures."
    subject1{costume:str,subject_action:str,subject_expression:str}:
      costume: "Low-polygon adventurer tunic and trousers in muted greens and browns, a blocky utility belt with voxel tools, simple, chunky voxel boots."
      subject_action: "Standing with one hand lightly resting on a large, blocky, glowing data crystal embedded in the island."
      subject_expression: "A subtle, curious expression, eyes wide with wonder at the digital landscape."
    subject2{costume:str,subject_action:str,subject_expression:str}:
      costume: "A vibrant, pixelated explorer jumpsuit in electric blue, with contrasting orange accents, chunky voxel goggles pushed up on her head, a small blocky digital compass attached to her wrist."
      subject_action: "Leaning forward slightly, arm outstretched, pointing excitedly towards a cluster of particularly vibrant voxel flora at the island's edge."
      subject_expression: "An excited, joyful expression, mouth slightly open in awe."
    year: "Retro-Futuristic, 8-bit aesthetic"
  prompt: "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Imagine Subject 1 (male) and Subject 2 (female) as blocky, low-polygon explorers discovering a vibrant, floating voxel island in a vast digital void. Subject 1 is contemplative, while Subject 2 is eagerly pointing out a new discovery amidst the pixelated flora."
```

</details>

<details><summary><b>The Fighter Boxing Video</b></summary>

```text
[00:00 - 00:2.0]
Intense boxing exchange mid-ring, Red Trunks vs Blue Trunks, smoky arena atmosphere with high-contrast backlighting, sweat glistening under spotlights. [Audio: Canvas footwork scuffs, leather-on-leather punches, heavy breathing + Tense crowd ambience] --ar 9:16

[00:2.0 - 00:4.0]
Extreme close-up of Red Trunks' right hook impacting Blue Trunks' jaw, facial distortion on impact, beads of sweat exploding from the head. [Dialogue: (Grit) 'Got you!']. [Audio: Deep bassy thud, slow-motion warp effect, thumping heartbeat] --ar 9:16

[00:4.0 - 00:6.0]
Blue Trunks reeling back, massive spray of sweat and water hitting the camera lens directly, creating water distortion on the frame, blurred ring background. [Audio: Wet splatter sound on mic, high-pitched tinnitus ringing, explosive crowd roar] --ar 9:16
```

</details>

<details><summary><b>The Glass Doppelgänger</b></summary>

```text
{
  "title": "The Glass Doppelgänger",
  "description": "A high-octane psychological thriller scene where a woman is engaged in a visceral physical combat with her own sentient reflection emerging from a shattered surface.",
  "prompt": "You will perform an image edit using the provided photo to create a high-budget movie frame. The scene features the subject in a fierce life-or-death struggle against a supernatural mirror entity. The image must be Ultra-Photorealistic, utilizing cinematic lighting and highly detailed textures. The style is that of a blockbuster film, shot on Arri Alexa with a shallow depth of field to emphasize the intensity. Ensure realistic physics for the flying glass shards.",
  "details": {
    "year": "2025",
    "genre": "Cinematic Photorealism",
    "location": "A derelict, neon-lit dressing room with peeling wallpaper and a wall-sized vanity mirror that is shattering outwards.",
    "lighting": [
      "Volumetric stage lighting from above",
      "Flickering fluorescent buzz",
      "Dramatic rim lighting highlighting sweat and glass texture"
    ],
    "camera_angle": "Dynamic low-angle medium shot, slightly Dutch tilted to enhance the chaos.",
    "emotion": [
      "Ferocity",
      "Desperation",
      "Adrenaline"
    ],
    "color_palette": [
      "Electric cyan",
      "Gritty concrete grey",
      "Deep shadowy blacks",
      "Metallic silver"
    ],
    "atmosphere": [
      "Violent",
      "Surreal",
      "Claustrophobic",
      "Kinetic"
    ],
    "environmental_elements": "Thousands of micro-shards of glass suspended in the air (bullet-time effect), dust motes dancing in the light beams, overturned furniture.",
    "subject1": {
      "costume": "crop top, mini skirt",
      "subject_expression": "A primal scream of exertion, eyes wide with intensity.",
      "subject_action": "fighting with mirror"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "cartoonish effects",
        "low resolution",
        "blurry textures",
        "static pose",
        "calm demeanor"
      ],
      "exclude_styles": [
        "3D render",
        "illustration",
        "painting",
        "anime"
      ],
      "exclude_colors": [
        "pastel pinks",
        "sunshine yellow"
      ],
      "exclude_objects": [
        "magical glowing orbs",
        "wands",
        "animals"
      ]
    }
  }
}
```

</details>

<details><summary><b>The Gravedigger's Vigil</b></summary>

```text
{
  "title": "The Gravedigger's Vigil",
  "description": "A haunting portrait of a lone Victorian figure standing watch over a misty, decrepit cemetery at midnight.",
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve his core likeness. Transform Subject 1 (male) into a solemn Victorian gravedigger standing amidst a sprawling, fog-choked necropolis. He holds a rusted lantern that casts long, uncanny shadows against the moss-covered mausoleums behind him. The composition adheres to a cinematic 1:1 aspect ratio, framing him tightly against the decaying iron gates.",
  "details": {
    "year": "1888",
    "genre": "Gothic Horror",
    "location": "An overgrown, crumbling cemetery gate with twisted iron bars and weeping angel statues.",
    "lighting": [
      "Pale, cold moonlight cutting through fog",
      "Flickering, warm amber candlelight from a lantern",
      "Deep, abyssal shadows"
    ],
    "camera_angle": "Eye-level medium shot, creating a direct and confronting connection with the viewer.",
    "emotion": [
      "Foreboding",
      "Solitary",
      "Melancholic"
    ],
    "color_palette": [
      "Obsidian black",
      "slate gray",
      "pale moonlight blue",
      "sepia tone",
      "muted moss green"
    ],
    "atmosphere": [
      "Eerie",
      "Cold",
      "Silent",
      "Supernatural",
      "Decaying"
    ],
    "environmental_elements": "Swirling ground mist that obscures the feet, twisted dead oak trees silhouetted against the moon, a lone crow perched on a headstone.",
    "subject1": {
      "costume": "A tattered, ankle-length black velvet frock coat, a weathered top hat, and worn leather gloves.",
      "subject_expression": "A somber, pale visage with a piercing, weary gaze staring into the darkness.",
      "subject_action": "Raising a lantern high with the right hand while gripping the handle of a spade with the left."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "sunlight",
        "blooming flowers",
        "blue sky",
        "modern infrastructure",
        "smiling",
        "lens flare"
      ],
      "exclude_styles": [
        "cartoon",
        "cyberpunk",
        "high fantasy",
        "anime",
        "watercolor",
        "bright pop art"
      ],
      "exclude_colors": [
        "neon",
        "pastel pink",
        "vibrant orange",
        "saturated red"
      ],
      "exclude_objects": [
        "cars",
        "smartphones",
        "plastic",
        "streetlights"
      ]
    }
  }
}
```

</details>

<details><summary><b>The Last Adagio</b></summary>

```text
{
  "title": "The Last Adagio",
  "description": "A hauntingly beautiful scene of a solitary ballerina performing in a flooded, abandoned grand library.",
  "prompt": "You will perform an image edit using the provided subject. Transform Subject 1 (female) into a survivor in a post-apocalyptic world. She is in a massive, decaying library where the floor is flooded with water. Light spills through the collapsed ceiling, illuminating dust motes and water reflections. The image must be photorealistic, utilizing cinematic lighting, highly detailed textures, shot on Arri Alexa with a shallow depth of field to focus on the subject while the background falls into soft bokeh.",
  "details": {
    "year": "Post-Collapse Era",
    "genre": "Cinematic Photorealism",
    "location": "A grand, abandoned library with towering shelves, crumbling architecture, and a floor flooded with still, reflective water.",
    "lighting": [
      "God rays entering from a collapsed roof",
      "Soft reflected light from the water",
      "High contrast cinematic shadows"
    ],
    "camera_angle": "Low angle, wide shot, capturing the reflection in the water.",
    "emotion": [
      "Melancholic",
      "Graceful",
      "Solitary"
    ],
    "color_palette": [
      "Desaturated concrete greys",
      "Muted teal water",
      "Vibrant crimson",
      "Dusty gold light"
    ],
    "atmosphere": [
      "Ethereal",
      "Lonely",
      "Quiet",
      "Majestic"
    ],
    "environmental_elements": "Floating pages from old books, dust particles dancing in light shafts, ripples in the water.",
    "subject1": {
      "costume": "A distressed, dirty white ballet leotard paired with pristine red gloves.",
      "subject_expression": "Serene, eyes closed, lost in the movement.",
      "subject_action": "dancing"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "bright sunshine",
        "clean environment",
        "modern technology",
        "spectators"
      ],
      "exclude_styles": [
        "cartoon",
        "painting",
        "sketch",
        "3D render"
      ],
      "exclude_colors": [
        "neon green",
        "bright orange"
      ],
      "exclude_objects": [
        "cars",
        "animals",
        "phones"
      ]
    }
  }
}
```

</details>

<details><summary><b>The Midnight Informant</b></summary>

```text
{
  "title": "The Midnight Informant",
  "description": "A tense, film noir moment featuring a female private investigator waiting for a lead in a hazy, underground jazz club.",
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve her core likeness. Transform the subject (female) into a sharp-witted 1950s private investigator seated in a booth at a dimly lit, smoke-filled jazz club. The image must be Ultra-Photorealistic and Movie-Quality, evoking the golden age of Film Noir. Use dramatic lighting to highlight skin texture and fabric details. Keywords: photorealistic, cinematic lighting, highly detailed, shot on Arri Alexa, depth of field, volumetric fog, realistic physics.",
  "details": {
    "year": "1954",
    "genre": "Cinematic Photorealism",
    "location": "The Velvet Note, a crowded, subterranean jazz lounge in Chicago with red velvet booths and a small stage in the hazy background.",
    "lighting": [
      "Chiaroscuro",
      "Volumetric shafts of light cutting through smoke",
      "Warm tungsten table lamps",
      "Rim lighting on hair"
    ],
    "camera_angle": "Eye-level medium close-up, shallow depth of field focusing strictly on the subject's eyes.",
    "emotion": [
      "Suspicious",
      "Alert",
      "Melancholic"
    ],
    "color_palette": [
      "Deep shadow black",
      "Amber gold",
      "Burgundy red",
      "Tobacco brown"
    ],
    "atmosphere": [
      "Sultry",
      "Mysterious",
      "Claustrophobic",
      "Noir"
    ],
    "environmental_elements": "Thick swirls of cigarette smoke filling the air, a half-empty glass of amber whiskey on the table, blurred silhouette of a double bass player in the background.",
    "subject1": {
      "costume": "A structured beige trench coat worn over a dark cocktail dress, leather gloves, and a wide-brimmed fedora tilted slightly forward.",
      "subject_expression": "A piercing, guarded gaze, eyes scanning the room, lips pressed in a tight line.",
      "subject_action": "One hand rests on a manila folder on the table, the other hovers near her whiskey glass."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "daylight",
        "modern technology",
        "smartphones",
        "casual clothing",
        "bright sunshine",
        "blue skies"
      ],
      "exclude_styles": [
        "cartoon",
        "3D render",
        "anime",
        "sketch",
        "impressionism",
        "oversaturated"
      ],
      "exclude_colors": [
        "Neon green",
        "Hot pink",
        "Cyan"
      ],
      "exclude_objects": [
        "cars",
        "weapons drawn",
        "animals"
      ]
    }
  }
}
```

</details>

<details><summary><b>The Midnight Melody Mystery</b></summary>

```text
{
  "title": "The Midnight Melody Mystery",
  "description": "A charming, animated noir scene where a gruff detective questions a glamorous jazz singer in a stylized 1950s club.",
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness but stylized. Transform Subject 1 (male) and Subject 2 (female) into characters from a high-budget animated feature. Subject 1 is a cynical private investigator and Subject 2 is a dazzling lounge singer. They are seated at a curved velvet booth in a smoky, art-deco jazz club. The aesthetic must be distinctively 'Disney Character' style, featuring smooth shading, expressive large eyes, and a magical, cinematic glow.",
  "details": {
    "year": "1950s Noir Era",
    "genre": "Disney Character",
    "location": "The Blue Note Lounge, a stylized jazz club with art deco architecture, plush red velvet booths, and a stage in the background.",
    "lighting": [
      "Cinematic spotlighting",
      "Soft volumetric haze",
      "Warm golden glow from table lamps",
      "Cool blue ambient backlight"
    ],
    "camera_angle": "Medium close-up at eye level, framing both subjects across a small round table.",
    "emotion": [
      "Intrigue",
      "Playful suspicion",
      "Charm"
    ],
    "color_palette": [
      "Deep indigo",
      "ruby red",
      "golden amber",
      "sepia tone"
    ],
    "atmosphere": [
      "Mysterious",
      "Romantic",
      "Whimsical",
      "Smoky"
    ],
    "environmental_elements": "Swirling stylized smoke shapes, a vintage microphone in the background, a crystal glass with a garnish on the table.",
    "subject1": {
      "costume": "A classic tan trench coat with the collar popped, a matching fedora hat, and a loosened tie.",
      "subject_expression": "A raised eyebrow and a smirk, looking skeptical yet captivated.",
      "subject_action": "Holding a small reporter's notebook and a pencil, leaning slightly forward over the table."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "photorealism",
        "gritty textures",
        "blood",
        "gore",
        "dirt",
        "noise"
      ],
      "exclude_styles": [
        "anime",
        "cyberpunk",
        "sketch",
        "horror",
        "watercolor"
      ],
      "exclude_colors": [
        "neon green",
        "hot pink"
      ],
      "exclude_objects": [
        "smartphones",
        "modern technology",
        "cars"
      ]
    },
    "subject2": {
      "costume": "A sparkling, floor-length red evening gown with white opera-length gloves and a pearl necklace.",
      "subject_expression": "A coy, confident smile with heavy eyelids, playing the role of the femme fatale.",
      "subject_action": "Resting her chin elegantly on her gloved hand, looking directly at the detective."
    }
  }
}
```

</details>

<details><summary><b>The Red Headscarf</b></summary>

```text
(Portrait of a beautiful young woman:1.3), (Middle Eastern ethnicity:1.2), (age 20:1.1), (intricate facial features:1.3), (soft natural expression:1.2), wearing a (vibrant red headscarf:1.2) wrapped around wavy dark hair, dressed in a (detailed blue floral blouse:1.2) over a (yellow textured top:1.1), adorned with (ornate turquoise beaded necklace:1.2), (large vintage drop earrings:1.1), and gold bangles. The subject is positioned slightly to the left, (facing the viewer:1.2), resting her arms on a surface. Background features a (distressed turquoise wall:1.2), a (large rustic ceramic vase:1.1) containing yellow wildflowers, and a small painted bowl. (Fine art oil painting style:1.3), rich color palette of teal, gold, and crimson, (soft cinematic lighting:1.2), painterly textures, elegant composition, high detail, masterpiece, 8k resolution, volumetric atmosphere, sophisticated classic portraiture style.
```

</details>

<details><summary><b>The Room That Forgot Gravity</b></summary>

```text
Use the uploaded photo as a strict identity reference. Keep this exact person: same face, hair, age, skin texture and body proportions, unretouched.

A photorealistic cinematic photograph, vertical 4:5, shot at eye level with a perfectly level camera, medium-wide. It looks like a practical-effects movie set photographed with a real camera.

The person stands upright on the wooden floor in the middle of an elegant, ordinary room. Full body visible, relaxed pose, understated contemporary clothes, looking around with mild curiosity. The face is clearly visible and softly lit. They are the only person and the main focal point.

The room has muted dark plaster walls, a real wood floor, a window on the back wall, minimal furniture and warm practical lamps. Both side walls, the floor and part of the ceiling are visible. The room is completely normal, except that four objects each have their own direction of gravity.

Left: a white, medium-heavy curtain on the rod above the window falls sideways instead of down. It hangs horizontally from the rod toward the left wall, exactly like a normally hanging curtain rotated 90 degrees. The rod above the window is its only attachment. The far end of the curtain hangs free a short distance from the left wall, ending in a loose, slightly uneven vertical hem. Heavy folds run horizontally, with a slight natural sag and bunching at the rod. The fabric is heavy and completely still.

Right, in the foreground at chest height: a clear cylindrical drinking glass stands on the right wall as if the wall were a table. Its base rests against the wall, held by a small metal ring bracket. Its open end points horizontally into the room. The glass is seen in side profile and is large and sharp in the frame.

The glass holds amber-coloured tea. The tea fills the wall-side part of the glass completely, from the top inner edge to the bottom inner edge, and takes up a little more than half of the glass length. The tea-filled part is clearly longer than the empty part. The room-side part of the glass, up to the rim, is completely empty, clear and dry, also along its lower edge. The boundary between the amber tea and the air is one straight vertical line running from the top edge of the glass to the bottom edge. It looks exactly like a photo of a normal glass of tea standing on a table, rotated 90 degrees so that its base points at the right wall. Realistic meniscus along that vertical line and realistic refraction in the amber liquid.

Above: a small potted trailing plant stands upside down on the ceiling, the base of the pot flat against the ceiling. Its vines and leaves droop upward and lie against the ceiling around the pot, the way a trailing plant on a table droops onto the tabletop. No vines hang down into the room. The plant is smaller and less prominent than the curtain and the glass.

On the right wall below the glass: a stack of exactly three hardcover books uses the wall as its floor. One dark green book lies with its cover flat against the wall. One dark red book is stacked on it, and one dark blue book is stacked on the red one, toward the room. The stack sticks out horizontally from the wall and the three spines are vertical.

Lighting: warm lamps, a soft directional key light on the person, subtle rim light, natural falloff into shadow. All shadows follow the real light sources, including those of the sideways objects. Natural skin, real materials, subtle film contrast, natural depth of field. No text in the image.
```

</details>

<details><summary><b>The Silent Standoff</b></summary>

```text
High-angle top-down view of a dimly lit abandoned courtyard, cracked concrete ground, scattered old markings and faded impact dents, long eerie character shadows cast off-frame, no violence depicted, dark Teal palette with a strong golden beam, thick outlines, 2D animated cartoon look, flat shading, extreme contrast, atmospheric tension.
```

</details>

<details><summary><b>The Solar Priestess of Amun</b></summary>

```text
{
  "title": "The Solar Priestess of Amun",
  "description": "A stunning, stylized portrait of a woman transformed into an Ancient Egyptian priestess, blending photorealism with the texture of tomb paintings.",
  "prompt": "You will perform an image edit using the female from the provided photo as the main subject. Preserve her core likeness. Transform the subject into a high-ranking Ancient Egyptian priestess in the style of New Kingdom art. She is depicted in a stylized profile view (canonical perspective) against a backdrop of limestone walls covered in vibrant hieroglyphs. The image should possess the texture of aged papyrus and gold leaf while maintaining cinematic lighting in a 1:1 aspect ratio.",
  "details": {
    "year": "1250 BC",
    "genre": "Ancient Egyptian Art",
    "location": "The inner sanctuary of the Temple of Karnak, surrounded by massive sandstone columns.",
    "lighting": [
      "Warm golden sunlight",
      "Flickering torchlight shadows",
      "Specular highlights on gold jewelry"
    ],
    "camera_angle": "Side profile shot at eye level, mimicking the traditional Egyptian art perspective.",
    "emotion": [
      "Regal",
      "Devout",
      "Serene"
    ],
    "color_palette": [
      "Lapis Lazuli Blue",
      "Burnished Gold",
      "Ochre Red",
      "Turquoise"
    ],
    "atmosphere": [
      "Sacred",
      "Timeless",
      "Mystical",
      "Opulent"
    ],
    "environmental_elements": "Carved hieroglyphs on the background wall, floating dust motes caught in shafts of light, sacred lotus flowers.",
    "subject1": {
      "costume": "A pleated white linen dress (kalasiris), a heavy gold Wesekh collar inlaid with semi-precious stones, and a vulture headdress.",
      "subject_expression": "A stoic, commanding gaze looking forward.",
      "subject_action": "Holding a ceremonial Ankh symbol raised slightly in one hand."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "modern fashion",
        "denim",
        "digital technology",
        "cars"
      ],
      "exclude_styles": [
        "3D render",
        "anime",
        "impressionism",
        "cyberpunk"
      ],
      "exclude_colors": [
        "neon green",
        "electric purple"
      ],
      "exclude_objects": [
        "eyeglasses",
        "watches",
        "modern buildings"
      ]
    }
  }
}
```

</details>

<details><summary><b>The Witcher Double Exposure</b></summary>

```text
Double exposure cinematic wallpaper inspired by The Witcher video game series (game, not TV show).
Geralt of Rivia and Yennefer standing back to back in a centered, balanced composition.
Geralt:
Facing forward, face fully visible, white hair, cat-like eyes, scarred and stoic expression, wearing witcher armor.
Strong, defined silhouette.
Yennefer:
Standing back to back with Geralt, body turned slightly away, face partially visible in side profile.
Dark hair, intense gaze, elegant but dangerous presence, flowing dark garments.
Inside the silhouettes: Within Geralt’s silhouette: Medieval ruins, monster-haunted forests, foggy mountain paths, cold steel tones, grim atmosphere. Within Yennefer’s silhouette: Arcane landscapes, ancient stone structures, subtle magical motifs, moonlit skies, deep violet and shadowed tones.
Double exposure treatment:
Clean silhouette separation, layered environments integrated naturally, painterly but controlled.
No scenery outside the silhouettes.
Background:
Dark crimson background with subtle texture, cinematic tension, restrained saturation.
Style & mood:
Dark fantasy, serious and grounded, video game cinematic art style.
No Netflix, no modern costume design, no TV adaptation influence.
Ultra high resolution, sharp details, premium wallpaper quality. Format 9:16
```

</details>

<details><summary><b>Theme Based Art Style Fusion</b></summary>

```text
Theme="${theme}" 
Style="the most interesting fusion of 3 or more art styles to best capture the theme"
```

</details>

<details><summary><b>Three Panel Monochrome Night Scene</b></summary>

```text
{
  "subject": {
    "description": "A three-panel monochromatic image. Top panel: A hooded figure with glowing eyes, wearing a backpack, climbing over a chain-link fence under a dark, cloudy night sky with a full, bright moon on the upper right. Middle-left panel: A person in silhouette seated on rubble inside a dark, derelict room, looking out a brightly lit opening with bare, tangled trees and a distant, hazy light source. Middle-right panel: A large, silhouetted hand reaching upwards towards a very bright, circular light source.",
    "count": "three distinct scenes within a single image",
    "orientation": "various, as per reference panels",
    "pose_or_state": "Top: active climbing; Middle-left: static seated; Middle-right: reaching upwards",
    "expression": "not applicable (silhouettes / glowing eyes)"
  },
  "scale_and_proportion": {
    "subject_to_frame_ratio": "Each panel's subjects scaled as per reference; the overall three panels stacked occupy 100% of frame height.",
    "proportions": "locked to reference",
    "negative_space": "significant, particularly in the top and middle-right panels, created by dark areas and the stipple effect, identical to reference"
  },
  "composition": {
    "shot_type": "Top: medium shot; Middle-left: medium interior shot; Middle-right: close-up",
    "camera_angle": "Top: slightly low angle; Middle-left: low angle; Middle-right: eye-level for the hand",
    "framing": "unchanged from reference (three vertical panels)",
    "symmetry": "asymmetrical per panel; overall triptych structure is vertically aligned with strong horizontal panel dividers",
    "background": "Top: cloudy night sky with moon and chain-link fence; Middle-left: bare trees and distant light through an opening; Middle-right: plain dark background with a dominant bright circular light",
    "depth_of_field": "Top: deep, everything in sharp stipple focus; Middle-left: deep focus outside opening, foreground elements in stipple detail; Middle-right: sharp focus on hand, light source is diffuse within the stipple pattern"
  },
  "temporal_context": {
    "era": "contemporary / timeless desolate aesthetic",
    "modern_elements": false,
    "retro_stylization": false,
    "trend_influence": false
  },
  "style": {
    "visual_type": "black and white stipple / halftone graphic art mimicking print media",
    "realism_level": "forms and lighting are realistic, but the rendering is entirely through a stipple pattern",
    "art_style": "halftone / stipple graphic art",
    "stylization": true,
    "interpretation": "literal reproduction, including the specific stipple pattern and black and white rendering"
  },
  "lighting": {
    "setup_type": "predominantly backlighting from a single dominant source per panel",
    "light_direction": "Top: frontal (moon); Middle-left: frontal (through opening); Middle-right: frontal (from the circular light source)",
    "light_quality": "hard light creating stark silhouettes, with bright, diffused glow around light sources, all rendered with stipple",
    "contrast": "very high",
    "shadow_behavior": "sharp and defined, creating strong silhouettes, composed of dense stipple dots",
    "color_temperature": "not applicable (monochromatic)",
    "lighting_variation": "minimal within each panel, distinct backlighting per panel"
  },
  "materials": {
    "primary_materials": [
      "human figures (silhouettes)",
      "chain-link fence (metal)",
      "clouds",
      "bare trees / branches",
      "rubble / concrete / rough ground",
      "generic rough textures"
    ],
    "surface_finish": "not distinct due to stipple and silhouette; implied matte for opaque objects",
    "light_reflection": "minimal, primarily silhouette edges defined by stipple",
    "material_accuracy": "implied forms accurate through silhouette and stipple density"
  },
  "color_palette": {
    "dominant_colors": [
      "black",
      "white"
    ],
    "saturation": "not applicable (monochromatic)",
    "contrast_level": "very high",
    "color_shift": false
  },
  "texture_and_detail": {
    "surface_detail": "rendered entirely through varying density of stipple dots; fence mesh, tree branches, ground rubble are visible through dot patterns",
    "grain_noise": "none, only intentional stipple/halftone dots of precise size and distribution",
    "micro_details": "preserved through stipple density where present",
    "sharpness": "sharp forms, but edges and gradients are defined by discrete dots of the stipple pattern"
  },
  "camera_render_settings": {
    "lens_equivalent": "standard/normal lens look across panels",
    "perspective_distortion": "none",
    "aperture_look": "deep depth of field for top and middle-left, implied very wide aperture for diffuse light source in middle-right (but hand is still sharp)",
    "resolution": "high",
    "render_quality": "clean and neutral, but with the explicit and precise stipple effect"
  },
  "constraints": {
    "no_additional_objects": true,
    "no_reframing": true,
    "no_crop": true,
    "no_stylization": false,
    "no_artistic_license": true,
    "no_text": true,
    "no_watermark": true,
    "no_effects": true,
    "no_dramatic_lighting": true,
    "no_color_grading": true,
    "no_smooth_gradients": true,
    "strictly_black_and_white": true
  },
  "iteration_instruction": {
    "compare_to_reference": true,
    "fix_geometry_first": true,
    "then_fix_composition": true,
    "then_fix_lighting": true,
    "then_fix_color": true,
    "then_fix_stipple_pattern_fidelity": true,
    "ignore_aesthetic_improvements": true
  },
  "negative_prompt": [
    "creative",
    "cinematic",
    "artistic",
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
    "smooth",
    "gradient",
    "grayscale",
    "sepia",
    "full color",
    "soft focus",
    "blurry",
    "realistic photograph (without stipple)",
    "painting",
    "sketch",
    "watercolor",
    "cartoon",
    "comic book (unless specifically for stipple effect)"
  ]
}
```

</details>

<details><summary><b>Through the Glass: One Eye in Focus</b></summary>

```text
A cinematic, close-up portrait of a reference photo viewed through a reflective glass window. She has messy dark brown hair and hyper-realistic skin texture with visible pores, fine lines, and natural imperfections. One green-hazel eye is in sharp, crystal-clear focus, fully visible and unobstructed by reflections or highlights, while the rest of her face gradually softens into the background with an organic depth falloff.

The glass surface in the foreground is covered with realistic rain droplets and subtle rain streaks, creating layered depth and emotional distance. Reflections are carefully controlled and positioned only around the edges of the frame, never crossing or obscuring the focused eye or key facial features.

Moody, low-key lighting with warm glowing yellow and orange bokeh lights reflecting softly on the glass. The bokeh remains diffused and offset to the sides, enhancing atmosphere without blocking facial clarity. Shot with an extremely shallow depth of field (f/1.2), cinematic composition, emotional tone, natural optical blur, and realistic light behavior.

Photorealistic rendering, high-resolution detail, preserved film grain, natural skin texture, no over-smoothing, no artificial sharpness, no plastic or synthetic look.
```

</details>

<details><summary><b>Tilt Shift Rice Terraces at Dawn</b></summary>

```text
Curving green rice terraces step down a mountainside toward a small village of wooden stilt houses with dark thatched roofs at dawn, photographed as a tilt-shift miniature. Seen from a high vantage point across the valley, with a narrow band of sharp focus on the village and the middle terraces, and strong blur at the top and bottom of the frame so the scene looks like a tiny model. Flooded terraces mirror the pink and gold sky like strips of glass, and low mist pools in the valley floor. A small stream with a footbridge winds past the houses, thin wood smoke rises from two chimneys, and a few ducks float on a paddy. Banana palms and bamboo clumps edge the fields. Saturated but natural colors, crisp morning light raking across the terrace walls, gentle long shadows. Professional travel photography, tilt-shift lens effect, wide landscape 16:9. No people, no text, no signs, no vehicles.
```

</details>

<details><summary><b>Time Layer Photography</b></summary>

```text
A single photograph of ${location:Galata Tower, Istanbul} where the frame is divided into organic, flowing sections, each showing a different era: ${era1:1890s sepia Ottoman period}, ${era2:1960s faded color}, ${era3:present day digital clarity}. The transitions between eras are seamless, blending through architectural details, people's clothing, and vehicles. Same camera angle, same perspective, different times bleeding into each other. Street level view. Photorealistic for each era's authentic photography style.
```

</details>

<details><summary><b>Tiny Astronaut Tending a Mars Rooftop Garden</b></summary>

```text
Photoreal hopeful sci-fi still: a tiny astronaut in a clean white EVA suit with a soft gold visor reflection kneels on a rooftop vegetable garden atop a low Mars habitat module. Raised beds of lush green lettuce, cherry tomatoes, and herbs thrive under a clear geodesic glass dome; fine red Martian dust coats the exterior walkways beyond the glass. The astronaut holds a small watering can, focused on a tomato plant. Soft afternoon light from a pale sun in a butterscotch sky; distant habitat modules and wind-sculpted dunes. Warm interior grow-lights glow faintly for contrast. Shot on a 50mm lens look, gentle depth of field, tactile fabric and soil detail, optimistic mood, no violence, no text, no logos, safe for work.
```

</details>

<details><summary><b>Tiny Balcony Greenhouse at Golden Hour</b></summary>

```text
Tomato vines heavy with red and orange cherry tomatoes, trailing basil, chili plants, and strawberry pots fill a tiny glass-and-black-steel lean-to greenhouse standing on a narrow city apartment balcony at golden hour. The greenhouse door is propped open; inside, three tiers of slatted wooden shelving hold terracotta pots, seed trays with fresh green sprouts, and a small brass watering can. Condensation beads on the lower glass panels. Outside the greenhouse, the balcony has a weathered teak floor, a folding bistro chair, and a black metal railing wrapped with string lights that are not yet on. Beyond the railing, a soft-focus city skyline of brick apartment blocks and rooftops glows in low warm sunlight. Photorealistic, shot on a full-frame camera with a 35mm lens at f/2.8, eye-level, shallow depth of field focused on the tomatoes, natural golden backlight creating rim light on the leaves and glass, realistic textures and reflections. Calm, hopeful, lived-in mood. No people, no text, no logos.
```

</details>

<details><summary><b>Tourist Travel Poster Collage</b></summary>

```text
Create a stylized travel poster / graphic collage for ${country}. The main subject should be a stylish international tourist visiting ${country}, clearly presented as a traveler and not a local resident. Show the tourist wearing modern travel fashion, with details such as a camera, backpack, sunglasses, map, or suitcase, exploring the culture and atmosphere of ${country}. Place the tourist in a dynamic composition surrounded by iconic architecture, streets, landscapes, landmarks, transportation, food, signage, and cultural elements associated with ${country}. Blend realistic character detail with a graphic collage background made of layered paper textures, torn poster edges, sticker elements, halftone dots, editorial typography, and bold geometric shapes. Include authentic visual motifs from ${country}, but keep the tourist’s appearance and styling globally fashionable and clearly foreign to the setting. Add a large readable headline: “LOST IN ${country}”. Modern, artistic, premium editorial travel poster aesthetic, balanced layout, print-worthy composition.
```

</details>

<details><summary><b>Train Station Photo Contact Sheet</b></summary>

```text
A 3x2 grid photo contact sheet featuring a consistent 28-year-old American woman with a specific facial structure, wearing a jacket and outdoor pants, in a train station at dusk with dramatic orange and teal lighting. The grid displays six frames with various natural poses of the same character: including 1. Standing alone, gazing at the horizon with a silhouette of a train in the distance, 2. Walking while holding headphones, natural lifestyle shot, 3. Sitting on the edge of the platform with a peaceful expression, illuminated by dramatic orange hue, and three additional varied natural poses in the same setting. Photorealistic, 8k, cinematic lighting, highly detailed, consistent character across all six frames.
```

</details>

<details><summary><b>Transparent SVG for Cricut Vinyl</b></summary>

```text
I want to create a transparent background image for a SVG file to print on my Cricut so I can apply permanent vinyl to a car.

What I want is "text" to say - Look Pretty Play Dirty
A Skull & sunflowers,  something that will look good with Black and Pink Vinyl
```

</details>

<details><summary><b>Treehouse Retreat Concept Brief Builder</b></summary>

```text
Act as an architectural designer who specializes in treehouses, garden studios, and small timber retreats, and as a visualization art director. I will describe a treehouse I am dreaming about. You will turn it into a clear design concept with fixed design details, plus two ready-to-use image prompts that show the SAME treehouse in two different seasons and from two different viewpoints, so the two AI images look like photos of one real building.

Host tree and site: ${site:a single huge old oak in a sloping meadow at the edge of a beech forest, trunk about 1.2 m wide, splitting into three main limbs about 5 m up}
Who uses it and how: ${use:a family retreat for reading, sleepovers for two kids, and quiet evenings for the adults}
Size and height: ${size:a small cabin about 3 x 4 m on a deck about 3.5 m above the ground}
Style direction: ${style:warm natural timber, a little storybook but not cartoonish, simple modern details}
Must have: ${must_have:a big window facing the forest, a covered deck, a small wood stove, a rope swing}
Budget level: ${budget:self-build with a carpenter's help, mid-range materials}
View A: ${view_a:summer afternoon, full green canopy, seen from the meadow at the front left}
View B: ${view_b:snowy winter evening, bare branches, windows glowing, seen from the front right}

Please produce:

1. Design concept
   - Concept name and a two-sentence story of how the treehouse should feel.
   - Structure in words: how the platform is supported (tree attachments, posts, knee braces), deck size, cabin footprint, roof form, and access (stairs, ladder, or bridge), with approximate heights and sizes.
   - Facades: what is on the front, left, right, and back walls (doors, windows, chimney), described from the meadow side.
   - Palette: 6 named colors (simple names like "honey cedar" or "moss green") and where each one is used.
   - Materials and finishes: cladding, roof, deck, railing, windows and door, metal parts, lighting.

2. Fixed design details (the consistency list)
   A numbered list of 12 to 16 details that must look identical in every image: the host tree and how it meets the deck, supports, cladding, roof, every window and door with color and shape, chimney, railing, stairs, swing, deck furniture, lights, and ground details, each with its exact position. Write each one as a short, concrete phrase an image generator can follow (for example "teal-blue Dutch door on the right half of the front wall").

3. Image prompt A: the base view
   One detailed prompt for an AI image generator: photoreal architectural photography of the treehouse from the view A position, in view A season and light. Include every fixed detail visible from there in its correct position (left and right as seen from the camera), the camera height and lens, lighting, mood, and a 16:9 landscape composition. End with exclusions (no people, no text, no logos).

4. Image prompt B: the second view
   One detailed prompt for view B, written for a text-only image generator that cannot see image A: restate ALL fixed details again in full words (never "same as before"), place each one correctly for the new camera position, describe what is newly visible, and change only the season, weather, time of day, and lighting (for example snow on the roof and deck, bare branches, warm light in the windows, smoke from the chimney). Keep materials, colors, and proportions identical.

5. Consistency checklist
   Ten yes/no checks to compare image B against image A (for example "Is the door still teal-blue and split into upper and lower halves?").

6. Build and safety notes
   A short list covering tree health (have an arborist check the tree), attachment methods that let the tree grow, load and railing height, fire safety around the stove, permits to check locally, and three ways to save money.

Rules:
- Keep it buildable for the stated size, height, and budget; flag anything that is unsafe or unrealistic.
- Use plain color names and concrete shapes; avoid vague words like "cozy" or "modern" on their own.
- No brand names, no real people, no readable text in the images.
- If my description is missing something essential, make a sensible assumption and list it at the top.
```

</details>

<details><summary><b>Trendy Streetwear Cafe Portrait</b></summary>

```text
Ultra-realistic casual café portrait, stylish woman sitting at an outdoor food spot in front of glass refrigerators filled with colorful bottled drinks. She holds a large glass of cold amber sparkling non-alcoholic drink with light foam and brings it close to her lips, in the other hand she holds a wrapped shawarma. Eyes softly closed, relaxed satisfied expression. Long straight hair with a center part, defined brows, sharp winged eyeliner, warm bronzed makeup, glossy skin. Outfit: oversized bright pink zip-up hoodie over a white top, black crossbody bag with chain detail. Long pink manicure, rings, trendy street-style vibe. Bright natural daylight, candid food moment, urban lifestyle aesthetic, realistic skin texture, sharp focus, shallow depth of field, vertical 9:16, photorealism.
ultra realistic 8K, hyper-detailed, sharp focus; shallow depth of field, natural bokeh; HDR lighting; cinematic color grading; lens 85mm/50mm/35mm; aperture f/1.4–f/2.8; key light at 45°, soft shadows; rim/back light for separation; clean white balance; natural skin texture with visible pores, glossy highlights. Format 9:16
```

</details>

<details><summary><b>Tri Panel Collage Portrait</b></summary>

```text
Create a vertical 9:16 collage with exactly 3 clearly separated equal panels stacked vertically. The same adult Japanese woman appears in all three panels with identical facial features and identity.

TOP PANEL: close-up selfie, one eye winking.

MIDDLE PANEL: over-the-shoulder pose, body turned away, looking back directly at the camera, long hair flowing naturally.

BOTTOM PANEL: close-up near the lens, hair covering one eye, cute subtle pout.
```

</details>

<details><summary><b>Tropical Beach Vacation Photo</b></summary>

```text
A realistic casual vacation photograph taken from a high angle looking down at a tanned, athletic mature man in his mid-50s lying semi-reclined on a white beach lounger. He has a salt-and-pepper beard and mustache, sun-reddened skin with visible sunburn on his chest, shoulders and abdomen, and a large dark Polynesian tribal tattoo on his left shoulder and chest. He wears round gold-framed aviator sunglasses with dark reflective lenses, multiple bracelets on his left wrist including a turquoise beaded one and a black leather one, and bright yellow-orange swim shorts with a white drawstring. His right arm is extended toward his bent knee, and he looks up at the camera with a relaxed, slight smile. The setting is a pristine tropical beach with fine white sand, turquoise Caribbean-blue ocean water in the background, large beige canvas beach umbrellas on wooden poles, white sun loungers with orange cushions and towels, and a few distant people relaxing under the umbrellas. Dark rocks and green vegetation are visible on the far horizon under a clear bright blue sky. The lighting is harsh direct midday sunlight creating strong defined shadows, with vibrant saturated warm colors — dominant yellows, oranges, turquoise blues and whites. Shot in a candid spontaneous selfie-style with moderate depth of field, the background slightly soft. Photorealistic, high detail, natural skin texture, 4K quality.
```

</details>

<details><summary><b>Tunnel Moment with a Footballer</b></summary>

```text
Inputs

Reference 1: User’s uploaded photo

Reference 2: ${Footballer Name}

Jersey Number: ${Jersey Number}
Jersey Team Name: ${Jersey Team Name} (team of the jersey being held)
User Outfit: ${User Outfit Description}
Mood: ${Mood}

Prompt
Create a photorealistic image of the person from the user’s uploaded photo standing next to ${Footballer Name} pitchside in front of the stadium stands, posing for a photo.

Location: Pitchside/touchline in a large stadium. Natural grass and advertising boards look realistic.

Stands: The background stands must feel 100% like ${Footballer Name}’s team home crowd (single-team atmosphere). Dominant team colors, scarves, flags, and banners. No rival-team colors or mixed sections visible.

Composition: Both subjects centered, shoulder to shoulder. ${Footballer Name} can place one arm around the user.

Prop: They are holding a jersey together toward the camera. The back of the jersey must clearly show ${Footballer Name} and the number ${Jersey Number}. Print alignment is clean, sharp, and realistic.

Critical rule (lock the held jersey to a specific team)

The jersey they are holding must be an official kit design of ${Jersey Team Name}.

Keep the jersey colors, patterns, and overall design consistent with ${Jersey Team Name}.

If the kit normally includes a crest and sponsor, place them naturally and realistically (no distorted logos or random text).

Prevent color drift: the jersey’s primary and secondary colors must stay true to ${Jersey Team Name}’s known colors.

Note: ${Jersey Team Name} must not be the club ${Footballer Name} currently plays for.

Clothing:

${Footballer Name}: Wearing his current team’s match kit (shirt, shorts, socks), looks natural and accurate.

User: ${User Outfit Description}

Camera: Eye level, 35mm, slight wide angle, natural depth of field. Focus on the two people, background slightly blurred.

Lighting: Stadium lighting + daylight (or evening match lights), realistic shadows, natural skin tones.

Faces: Keep the user’s face and identity faithful to the uploaded reference. ${Footballer Name} is clearly recognizable. Expression: ${Mood}

Quality: Ultra realistic, natural skin texture and fabric texture, high resolution.

Negative prompts
Wrong team colors on the held jersey, random or broken logos/text, unreadable name/number, extra limbs/fingers, facial distortion, watermark, heavy blur, duplicated crowd faces, oversharpening.

Output
Single image, 3:2 landscape or 1:1 square, high resolution.
```

</details>

<details><summary><b>Turmeric Kojic Soap Packaging</b></summary>

```text
A close-up showcases the exquisite packaging of the tumeric kojic soap, displaying is vibrant orange and yellow designs.
```

</details>

<details><summary><b>Turn a Logo or Text into Yarn Design</b></summary>

```text
Create a highly detailed, textured logo for (Brand Name), made of thick yarn or wool. Each section of the logo should be in a different vibrant color (matching the reference image provided). The yarn should have a knitted texture with clearly visible fibers, giving a soft, dynamic 3D appearance. Ensure the logo has a three-dimensional effect with shading that makes it look like a knitted piece of fabric. The background should be neutral or light-colored, allowing the vibrant yarn texture to stand out while showcasing the brand's unique identity. Format 4:5
```

</details>

<details><summary><b>Typographic Portrait Artwork</b></summary>

```text
Transform the provided portrait into a 9:16 vertical typographic artwork built exclusively from repeated name text.

STRICT RULES:
- The image must be composed ONLY of text (e.g., "MUSTAFA KEMAL ATATÜRK").
- No lines, no strokes, no outlines, no shapes, no shading, no gradients.
- Do NOT draw anything. Do NOT use any brush or illustration effect.
- No stamp borders or shapes — only pure text.
- Every visible detail must come from the text itself.

TEXT CONSTRAINT:
- ALL text must be small and consistent in size.
- Do NOT use large or oversized text anywhere.
- Font size should remain uniform across the entire image.
- The text should feel like fine grain / micro-typography.

Preserve the exact facial identity and proportions from the input image.

COMPOSITION:
- Slightly zoomed-out portrait (not close-up).
- Include full head with some negative space around.

REGIONAL CONTROL:
- Forehead area should be clean or extremely sparse.
- Focus density on eyes, nose, mouth, jawline.

SHADING METHOD:
- Create depth ONLY by changing text density (not size).
- Dark areas = very dense text repetition.
- Light areas = sparse text placement.
- No gradient effects — density alone must simulate light and shadow.

Arrange text with slight variations in rotation and spacing, but keep it controlled and clean.

Style:
minimal, high-contrast black text on light background, elegant and editorial.

No extra text outside the repeated name. No logos. No decorative elements.

The result should look like a refined typographic portrait where shadows are created purely through text density, with zero size variation.
```

</details>

<details><summary><b>UI Design Brief from Screenshot</b></summary>

```text
This is a ${page_type:dashboard} of a modern ${focus:government audit} app called ${brand:AuditFlow}.

Thoroughly analyze the UI in this screenshot and describe it in as much detail as you can to hand over from a UI designer to a developer. The brief should cover both light and dark mode and contain responsive breakpoints matching Tailwind CSS v4.3 defaults.

Output characteristics as structured JSONC.

For colors, extract a rough palette and only detail accents and complex media. The goal is to use only 2 palettes: primary and secondary similar to Tailwind colors. Alongside these 2, you can define any number of grays and accent colors for more complex UI (gradients, shadows, SVGs, etc.).

End with a prompt explaining how to implement the UI for a developer, but don't mention any tech specs; only a brief of the UI to be implemented and the token rules + usage. Output the prompt as a Markdown code block.

The output should be two code blocks: one for the design brief and one for the JSONC design specification.
```

</details>

<details><summary><b>UI Designer</b></summary>

```text
Act as a UI Designer. You are an expert in crafting intuitive and visually appealing user interfaces for digital products. Your task is to design interfaces that enhance user experience and engagement.

You will:
- Collaborate with developers and product managers to define user requirements and specifications.
- Create wireframes, prototypes, and visual designs based on project needs.
- Ensure designs are consistent with brand guidelines and accessibility standards.

Rules:
- Prioritize usability and aesthetic appeal in all designs.
- Stay updated with the latest design trends and tools.
- Incorporate feedback from user testing and iterative design processes.
```

</details>

<details><summary><b>UI UX Design Evaluator</b> · machine translated</summary>

```text
Your task is to conduct a professional evaluation of a UI/UX design. Please analyze the following design information:

<设计项目>
Project type: {{PROJECT_TYPE}}
Product positioning: {{PRODUCT_POSITIONING}}
Target users: {{TARGET_USERS}}
Core functions: {{CORE_FUNCTIONS}}
Design objectives: {{DESIGN_OBJECTIVES}}
</设计项目>

<设计内容>
{{DESIGN_CONTENT}}
</设计内容>

Please evaluate the design along the following dimensions:
1. User experience and interaction flow analysis
2. Visual design and interface aesthetics
3. Usability and accessible design
4. Brand consistency and design standards
5. Technical feasibility and implementation difficulty

Please output a detailed design evaluation report inside the <design-review> tags.
```

</details>

<details><summary><b>Ukiyo-e Print of a River Ferry in Autumn Rain</b></summary>

```text
A Japanese ukiyo-e woodblock print of a small wooden ferry boat crossing a wide, calm river in autumn rain, in a wide landscape 16:9 composition on warm beige paper with visible fibers and wood grain texture. A long, low wooden boat sits in the center right of the frame, carrying three seated passengers under round oiled paper umbrellas, from left to right one vermilion red, one deep indigo blue, and one ochre yellow, the passengers wearing simple robes in indigo, ochre, and rust. At the stern on the right, a ferryman stands in a pale blue-grey robe and a wide conical straw hat, pushing a long wooden pole diagonally into the water. In the upper left, a red maple tree reaches into the frame with clusters of bright orange-red leaves, above a grassy, rocky near bank with tall reeds in the lower left. In the background, a misty grey-blue volcano-shaped mountain rises behind a hazy far shore with soft tree silhouettes on the right. Fine diagonal rain lines fall across the whole scene, the river shows gentle horizontal ripple lines, and the sky has a soft bokashi gradient from dark slate grey at the top to pale beige near the horizon. Flat color areas, fine black outlines, muted indigo, ochre, vermilion, and grey palette, quiet and contemplative mood. No text, no seals, no signature, no border.
```

</details>

<details><summary><b>Ukiyo-e Print of a Spring Kite Festival</b></summary>

```text
A traditional Japanese ukiyo-e woodblock print of a spring kite festival on a windy grassy hill above a river valley. Dozens of rectangular and diamond-shaped kites fill a pale sky that fades from soft cream to light blue, painted with bold carp, crane, and wave motifs in indigo, vermilion, and ochre. In the foreground, a group of villagers in patterned kimono and straw hats strain against long taut kite lines, one child running with a small red kite, an old man laughing as his hat blows away. Wind-bent pine trees lean to one side, and stylized swirling lines show the gusts. In the middle ground, a curved wooden bridge crosses the river, and terraced rice fields and a distant temple roof sit beneath a gently stylized mountain with a flat-topped peak. Flat areas of color, crisp black key-block outlines, subtle bokashi color gradients in the sky and river, visible washi paper texture and slight wood-grain registration marks. Composition in the spirit of Edo-period landscape series, calm and joyful mood. No modern objects, no readable text, no seal or signature, vertical 3:4 composition.
```

</details>

<details><summary><b>Ultra High Resolution Portrait Restoration</b></summary>

```text
{
  "prompt": "Restore and fully enhance this old, blurry, faded, and damaged portrait photograph. Transform it into an ultra-high-resolution, photorealistic image with HDR-like lighting, natural depth-of-field, professional digital studio light effects, and realistic bokeh. Apply super-resolution enhancement to recreate lost details in low-resolution or blurred areas. Smooth skin and textures while preserving all micro-details such as individual hair strands, eyelashes, pores, facial features, and fabric threads. Remove noise, scratches, dust, and artifacts completely. Correct colors naturally with accurate contrast and brightness. Maintain realistic shadows, reflections, and lighting dynamics, emphasizing the subject while keeping the background softly blurred. Ensure every element, including clothing and background textures, is ultra-detailed and lifelike. If black-and-white, restore accurate grayscale tones with proper contrast. Avoid over-processing or artificial look. Output should be a professional, modern, ultra-high-quality, photorealistic studio-style portrait, preserving authenticity, proportions, and mood, completely smooth yet ultra-detailed.",
  "steps": [
    {
      "step": 1,
      "action": "Super-resolution",
      "description": "Upscale the image to ultra-high-resolution (8K or higher) to recreate lost details."
    },
    {
      "step": 2,
      "action": "Deblur and repair",
      "description": "Fix blur, motion artifacts, scratches, dust, and other damage in the photo."
    },
    {
      "step": 3,
      "action": "Texture and micro-detail enhancement",
      "description": "Smooth skin and surfaces while preserving ultra-micro-details such as pores, hair strands, eyelashes, and fabric threads."
    },
    {
      "step": 4,
      "action": "Color correction",
      "description": "Adjust colors naturally, maintain realistic contrast and brightness, simulate modern camera color science."
    },
    {
      "step": 5,
      "action": "HDR lighting and digital studio effect",
      "description": "Apply HDR-like lighting, professional digital studio lighting, realistic shadows, reflections, and controlled depth-of-field with soft bokeh background."
    },
    {
      "step": 6,
      "action": "Background and detail restoration",
      "description": "Ensure background elements, clothing, and textures are sharp, ultra-detailed, and clean, while preserving natural blur for depth."
    },
    {
      "step": 7,
      "action": "Grayscale adjustment (if applicable)",
      "description": "Restore black-and-white portraits with accurate grayscale tones and proper contrast."
    },
    {
      "step": 8,
      "action": "Final polishing",
      "description": "Avoid over-processing, maintain a natural and authentic look, preserve original mood and proportions, ensure ultra-smooth yet ultra-detailed output."
    }
  ]
}
```

</details>

<details><summary><b>Ultra Realistic 8K Photo</b></summary>

```text
​"A professional, ultra-realistic 8K extremely high resolution masterpiece of [You decide content of the picture your self ]. Hyper-detailed textures, cinematic studio lighting with deep contrast, brighter colors,sharp focus on every detail. Shot on Sony A1 with 85mm f/1.8 lens for extreme clarity. Enhance the colors to be vibrant and rich (10-bit color),adjust luminance,apply micro-contrast, and add more high dramatic rim lighting to create depth. The surface should have realistic reflections and textures. Professional post-processing, no noise, and pixelation,adjust noise reduction, high dynamic range (HDR),highly detailed, sharp edges,crystal clear every pixels, incredibly lifelike and crisp,deep pastel colors, smooth texture, clean lighting, shallow depth of field, 

Preserve original pose, preserve original composition, preserve original identity, preserve original expression, preserve original outfit, preserve original background elements, do not change subject structure.
```

</details>

<details><summary><b>Ultra Realistic Cinematic Portrait</b></summary>

```text
Ultra realistic cinematic portrait of a referance photo, centered composition, head and shoulders framing, direct eye contact, serious neutral expression, short slightly messy dark hair, light stubble beard, wearing a black shirt and black textured jacket with zipper details, dramatic red rim lighting from both sides, soft frontal key light, deep black background, high contrast, low-key lighting, sharp focus, 85mm lens, shallow depth of field, studio photography, ultra detailed skin texture, 8k resolution
```

</details>

<details><summary><b>Ultra Realistic Winter Cinematography Series</b></summary>

```text
{
  "version": "2.1",
  "type": "multi_frame_winter_cinematography",
  "identity": {
    "reference_face": "Use the reference photo’s face with 100% identity accuracy.",
    "consistency": "Same person across all frames; identical facial structure, skin texture, hairstyle and age where visible."
  },
  "style": {
    "cinematography": "Ultra-realistic winter cinematography with 85mm lens character.",
    "color_grade": "Subtle blue winter grading, cold tones, soft highlights.",
    "atmosphere": "Soft diffused winter light, fine suspended snowflakes, gentle cold haze."
  },
  "frames": [
    {
      "frame_id": "top_frame",
      "description": "Side-profile portrait of the person in a snowy forest.",
      "requirements": {
        "face_visibility": "Side profile fully visible.",
        "identity_match": "Perfect match to reference face.",
        "expression": "A warm, natural smile visible from the side profile.",
        "environment": {
          "location": "Snow-covered forest",
          "lighting": "Soft morning winter light shaping facial contours",
          "elements": [
            "Gently falling snow",
            "Visible cold breath",
            "Light winter haze"
          ]
        },
        "wardrobe": {
          "coat": "Dark winter coat",
          "scarf": "Dark or neutral-toned winter scarf"
        },
        "camera": {
          "lens": "85mm",
          "depth_of_field": "Shallow",
          "look": "Ultra-realistic winter cinematic look"
        }
      }
    },
    {
      "frame_id": "middle_frame",
      "description": "Back-turned close-up while walking through a narrow snowy forest path.",
      "requirements": {
        "face_visibility": "Face must not be visible at all; strictly back-turned.",
        "identity_cues": "Body shape, posture, and clothing must clearly indicate the same person.",
        "environment": {
          "location": "Narrow snow-covered forest path",
          "forbidden_elements": ["No torii gate"],
          "trees": "Tall bare trees bending slightly, forming a natural snowy corridor",
          "atmosphere": "Quiet, serene winter silence with falling snow"
        },
        "wardrobe": {
          "coat": "Same dark winter coat as top frame",
          "scarf": "Same scarf"
        },
        "camera": {
          "lens": "85mm",
          "shot_type": "Close-up from behind",
          "depth_of_field": "Soft background with shallow DOF"
        }
      }
    },
    {
      "frame_id": "bottom_frame",
      "description": "Extreme close-up looking upward with falling winter snow.",
      "requirements": {
        "face_visibility": "Extreme close-up, fully visible face.",
        "identity_match": "Exact match to reference face.",
        "expression": "A gentle, warm smile while looking upward.",
        "environment": {
          "elements": [
            "Snowflakes falling around but NOT touching the face",
            "Snow in foreground and background only",
            "No visible breath vapor or mouth steam",
            "Soft winter haze in the ambient environment"
          ]
        },
        "camera": {
          "lens": "85mm",
          "depth_of_field": "Very shallow",
          "detail": "High realism, crisp skin texture, selective-focus snowflakes"
        },
        "lighting": "Soft winter light with subtle blue reflections"
      }
    }
  ],
  "global_constraints": {
    "identity": "Reference face must be perfectly reproduced in all visible-face frames.",
    "continuity": "Lighting, winter palette, lens characteristics, and atmosphere must remain consistent across all frames.",
    "realism_level": "Ultra-realistic, film-grade winter accuracy."
  }
}
{
  "version": "2.1",
  "type": "multi_frame_winter_cinematography",
  "identity": {
    "reference_face": "Use the reference photo’s face with 100% identity accuracy.",
    "consistency": "Same person across all frames; identical facial structure, skin texture, hairstyle and age where visible."
  },
  "style": {

    "cinematography": "Ultra-realistic winter cinematography with 85mm lens character.",
    "color_grade": "Subtle blue winter grading, cold tones, soft highlights.",
    "atmosphere": "Soft diffused winter light, fine suspended snowflakes, gentle cold haze."
  },
  "frames": [
    {
      "frame_id": "top_frame",
      "description": "Side-profile portrait of the person in a snowy forest.",
      "requirements": {
        "face_visibility": "Side profile fully visible.",
        "identity_match": "Perfect match to reference face.",
        "expression": "A warm, natural smile visible from the side profile.",
        "environment": {
          "location": "Snow-covered forest",
          "lighting": "Soft morning winter light shaping facial contours",
          "elements": [
            "Gently falling snow",
            "Visible cold breath",
            "Light winter haze"
          ]
        },
        "wardrobe": {
          "coat": "Dark winter coat",
          "scarf": "Dark or neutral-toned winter scarf"
        },
        "camera": {
          "lens": "85mm",
          "depth_of_field": "Shallow",
          "look": "Ultra-realistic winter cinematic look"
        }
      }
    },
    {
      "frame_id": "middle_frame",
      "description": "Back-turned close-up while walking through a narrow snowy forest path.",
      "requirements": {
        "face_visibility": "Face must not be visible at all; strictly back-turned.",
        "identity_cues": "Body shape, posture, and clothing must clearly indicate the same person.",
        "environment": {
          "location": "Narrow snow-covered forest path",
          "forbidden_elements": ["No torii gate"],
          "trees": "Tall bare trees bending slightly, forming a natural snowy corridor",
          "atmosphere": "Quiet, serene winter silence with falling snow"
        },
        "wardrobe": {
          "coat": "Same dark winter coat as top frame",
          "scarf": "Same scarf"
        },
        "camera": {
          "lens": "85mm",
          "shot_type": "Close-up from behind",
          "depth_of_field": "Soft background with shallow DOF"
        }
      }
    },
    {
      "frame_id": "bottom_frame",
      "description": "Extreme close-up looking upward with falling winter snow.",
      "requirements": {
        "face_visibility": "Extreme close-up, fully visible face.",
        "identity_match": "Exact match to reference face.",
        "expression": "A gentle, warm smile while looking upward.",
        "environment": {
          "elements": [
            "Snowflakes falling around but NOT touching the face",
            "Snow in foreground and background only",
            "No visible breath vapor or mouth steam",
            "Soft winter haze in the ambient environment"
          ]
        },
        "camera": {
          "lens": "85mm",
          "depth_of_field": "Very shallow",
          "detail": "High realism, crisp skin texture, selective-focus snowflakes"
        },
        "lighting": "Soft winter light with subtle blue reflections"
      }
    }
  ],
  "global_constraints": {
    "identity": "Reference face must be perfectly reproduced in all visible-face frames.",
    "continuity": "Lighting, winter palette, lens characteristics, and atmosphere must remain consistent across all frames.",
    "realism_level": "Ultra-realistic, film-grade winter accuracy."
  }
}
```

</details>

<details><summary><b>Ultra Realistic Young Woman Portrait</b></summary>

```text
Generate an ultra-realistic image of a young woman aged 22 years with the following features:
- Fair skin with light freckles
- Blue eyes, symmetrical face
- Long straight blonde hair, middle part
- Natural pink lips, soft natural makeup
- Slim body, same face, consistent appearance
- Photo captured using an iPhone back camera
- Natural, imperfect skin texture
- Realistic lighting, candid photo style

Ensure the image is high in realism, capturing the essence of a candid photo with all specified details.
```

</details>

<details><summary><b>Ultra-Realistic 3D Character Avatar Creation</b></summary>

```text
Act as a Master 3D Character Artist and Photogrammetry Expert. Your task is to create an ultra-realistic, 8k resolution character sheet of a person from the provided reference image for a digital avatar.

You will:
- Ensure character consistency by maintaining exact facial geometry, skin texture, hair follicle detail, and eye color from the reference image.
- Compose a multi-view "orthographic" layout displaying the person in a T-pose or relaxed A-pose.

Views Required:
1. Full-body Front view.
2. Full-body Left Profile.
3. Full-body Right Profile.
4. Full-body Back view.

Lighting & Style:
- Use neutral cinematic studio lighting (high-key) with no shadows and a white background to facilitate 3D modeling.
- Apply hyper-realistic skin shaders, visible pores, and realistic clothing physics.

Technical Specs:
- Shot on an 85mm lens, f/8, with sharp focus across all views, and in RAW photo quality.

Constraints:
- Do not stylize or cartoonize the output. It must be an exact digital twin of the source image.
```

</details>

<details><summary><b>Underwater Veo 3 Video</b></summary>

```text
Ultra-realistic 6-second cinematic underwater video: A sleek predator fish darts through a vibrant coral reef, scattering a school of colorful tropical fish. The camera follows from a low FPV angle just behind the predator, weaving smoothly between corals and rocks with dynamic, fast-paced motion. The camera occasionally tilts and rolls slightly, emphasizing speed and depth, while sunlight filters through the water, creating shimmering rays and sparkling reflections. Tiny bubbles and particles float in the water for immersive realism. Ultra-realistic textures, cinematic lighting, dramatic depth of field. Audio: bubbling water, swishing fins, subtle underwater ambience.
```

</details>

<details><summary><b>Urban Casual Portrait</b></summary>

```text
Hyper-realistic portrait of a ${gender:man} in tailored casual wear (dark jeans, quality sweater) ${position:leaning against weathered brick wall} in golden hour light. Maintain original face structure and features. Create natural skin texture with subtle pores and realistic stubble. Soft natural side lighting that highlights facial contours naturally. Street photography style, slight grain, authentic and unposed feel.
```

</details>

<details><summary><b>Urban Mural Artist Transformation</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. The face must remain clear and unaltered. Transform the subject into a passionate **Contemporary Urban Artist**, actively painting a vibrant, large-scale mural on a city wall. Emphasize dynamic brushstrokes/spray paint effects, bold colors, artistic energy, and a lively urban backdrop.",
  "details": {
    "year": "Contemporary (Modern Urban Setting)",
    "genre": "Street Art / Contemporary Art / Urban Life / Expressionism",
    "location": "A vibrant city alleyway or a prominent wall in an urban art district. The wall itself is a canvas, showing a partially completed, colorful mural. Other subtle graffiti or street art elements are visible in the background, along with distant, blurred city architecture.",
    "lighting": "Bright, clear daylight with a slight artistic filter, enhancing the vibrancy of colors. Natural shadows are soft but define the texture of the wall and the subject. The focus is on illuminating the artwork.",
    "camera_angle": "Medium shot, capturing the subject mid-action with their tools, with a significant portion of the mural visible. Dynamic angle that conveys movement and artistic energy. (1:1 composition).",
    "emotion": "Focused, passionate, energetic, and expressive.",
    "costume": "Comfortable, practical artist's attire: paint-splattered jeans or overalls, a graphic t-shirt or hoodie, and sturdy work boots. Hair might be tied back or messy. Perhaps a beanie or cap worn backward.",
    "color_palette": "Explosive and highly saturated. A wide range of bright, bold colors used in the mural (e.g., electric blues, fiery oranges, vibrant pinks, lime greens). The subject's clothes might have complementary or contrasting paint splatters. The city background is slightly desaturated to make the mural pop.",
    "atmosphere": "Energetic, creative, inspiring, and lively. The air feels alive with artistic expression and the subtle sounds of the city (distant traffic, music). A sense of freedom and creation.",
    "subject_expression": "Intense concentration, eyes narrowed as they focus on the artwork. A slight, satisfied smirk or a look of deep thought as they envision the next stroke. No direct eye contact with the viewer.",
    "subject_action": "Actively engaged in painting: one hand holding a spray can or a large paintbrush, mid-stroke on the mural. The other hand might be holding a reference sketch or gesturing to a part of the artwork. Paint drips are visible down the wall. Their body is in motion, conveying the physical act of creation.",
    "environmental_elements": "Various paint cans, brushes, and tools scattered at the base of the wall. A stepladder or scaffolding is partially visible. Subtle textures of the brick or concrete wall showing through the paint. A sense of depth with layers of paint."
  }
 }
```

</details>

<details><summary><b>Urban Night Railway Portrait</b></summary>

```text
A vertical nighttime photograph of a young woman standing outdoors
next to metal stairs near a railway. She has light skin, brown hair
pulled back into a low ponytail with loose strands framing her face
and falling over her forehead, defined eyebrows, and a serious,
pensive expression. She is wearing an oversized brown leather bomber
jacket with visible zipper and ribbed cuffs, a black crew-neck
t-shirt underneath, and a pleated olive green military-style mini
skirt. She stands slightly turned, with her arms crossed over her
chest, looking off to the left side of the frame, avoiding eye
contact with the camera. The setting is an industrial area near train
tracks: metal stairs with white railing on the right going up an
embankment, metal catenary poles and railway electrification
structures in the background, an electrical control box on the upper
right, and a tall street light pole on the upper left. The steep
slope behind her is covered in green grass and dirt. The night sky is
dark grey-purple. Strong artificial light from a street lamp in the
upper left corner creates a slight lens flare, casting hard direct
light on her face and jacket. Shot from a slightly low angle,
American shot framing. Photorealistic, high detail, cinematic
lighting, moody urban night atmosphere, 8k, masterpiece, best
quality, ultra-detailed, sharp focus.


Negative
Prompt:
cartoon, anime,
illustration, painting, drawing, 3d render, cgi, deformed, distorted,
bad anatomy, disfigured, poorly drawn face, mutation, mutated, extra
limb, ugly, poorly drawn hands, missing limb, floating limbs,
disconnected limbs, malformed hands, out of focus, extreme zoom,
absurd, blurry, wet, watermark, signature, text, username, artist
name, low quality, worst quality, normal quality, lowres, jpeg
artifacts, dead, out of frame, cropped, mutation, mutilated, out of
frame, extra fingers, too many fingers, cross-eyed, bad hands,
missing fingers, extra digit, fewer digits, cropped, worst quality,
low quality, normal quality, jpeg artifacts, signature, watermark,
username, blurry, artist name, monochrome, grayscale, duplicate,
morbid, mutilated, out of frame, extra toes, crossed eyes.

sd_xl_base_1.0.safetensors o Juggernaut XL v9
Resolution: 832x1216
(9:16 aspect ratio)
Steps: 30-40
Sampler: DPM++ 2M
Karras o Euler a
CFG Scale: 7-8
Clip Skip: 2 (para
SD 1.5) / 1 (para SDXL)
Denoising Strength:
0.75 (si usas img2img)

IP-Adapter Weight:
0.6-0.8
IP-Adapter Model:
ip-adapter-plus_sd15.safetensors
Reference Image: La
imagen original de la modelo

ControlNet Unit 0:
  Model:
control_v11p_sd15_openpose
  Preprocessor:
openpose_full
  Weight: 0.8-1.0
  Guidance Start:
0.0
  Guidance End: 1.0
  
ControlNet Unit 1
  Model:
control_v11f1p_sd15_depth
  Preprocessor:
depth_midas
Weight: 0.4-0.6
InstantID Weight:
0.8
IdentityNet Scale:
0.5-0.8
Preserve Face
Details: Enabled
add_detail.safetensors (Weight: 0.4-0.6)
epi_noiseoffset2.safetensors (Weight: 0.3-0.5)
cinematic_lighting.safetensors (Weight: 0.5)
```

</details>

<details><summary><b>Urban Night Streetwear Portrait</b></summary>

```text
{
  "scene_setup": {
    "subject": {
      "clothing": "wearing a black oversized hoodie, black backwards baseball cap, silver chain necklace",
      "appearance": "male model, beard, intense serious gaze, masculine features",
      "pose": "sitting or leaning forward, looking down at camera, authoritative stance"
    },
    "camera_angle": {
      "type": "Low angle shot",
      "focus": "Sharp focus on face, shallow depth of field (bokeh background)",
      "framing": "Medium close-up portrait"
    },
    "environment": {
      "location": "Urban street at night, under a concrete bridge or overpass",
      "background_elements": "blurred city lights, bokeh skyscrapers, a car with headlights on in the background",
      "ground": "wet asphalt, rain reflections"
    },
    "lighting_and_fx": {
      "style": "Cinematic moody lighting, high contrast",
      "colors": "Teal and orange color grading, warm street lights vs dark blue sky",
      "effects": "Smoke or steam rising in the foreground, volumetric lighting"
    },
    "technical": {
      "quality": "Photorealistic, 8k resolution, raw photo style, highly detailed texture",
      "engine": "Unreal Engine 5 render style or high-end photography"
    }
  }
}
```

</details>

<details><summary><b>Urban Night Waterfront Portrait</b></summary>

```text
Subject & Pose:
A young woman is standing by the metal railings of a waterfront promenade, leaning against them with both hands. She is slightly leaning back with a relaxed posture. Her head is turned to the left, her eyes are closed, and she wears a soft half-smile with a calm, mysterious expression.

Technical instruction: Preserve the exact facial features and identity from the face reference with 100% accuracy. Do not change the face shape, nose, eyebrows, lips, eyes, or overall facial structure.

Outfit & Accessories:
She is wearing a fitted black long-sleeve top with a deep V-neckline. The bottom is a black mini skirt decorated with two rows of silver chain belts, one featuring a heart-shaped charm. A black textured shoulder bag with a silver chain strap hangs from her left shoulder. She wears a delicate, thin pendant necklace.

Hair & Makeup:
loose hair with soft front strands naturally falling across her face and neck. Soft glam makeup with sculpted contouring, radiant skin, long voluminous lashes, and glossy nude lips.

Lighting & Camera:
Thigh-up framing, eye-level angle, vertical 3:4 composition. Shot as if taken on an iPhone 16 Pro using a bright front-facing flash at night, creating strong contrast: the model is brightly illuminated with glossy highlights on her skin and metallic chains, while the background remains dark.

Background:
A nighttime metropolitan waterfront. Behind her is dark water reflecting countless lights from illuminated skyscrapers and high-rise buildings across the shore. The sky is dark with faint clouds softly glowing from city lights.

Mood & Aesthetic:
Urban night aesthetic, Y2K style, confidence, elegance, and mystery. A realistic candid photo captured during an evening city walk.

Ultra-realistic, high-quality, sharp 8K photo. Aspect ratio 3:4. Eyes closed. Subtle half-smile. Shot on iPhone 16 Pro.
```

</details>

<details><summary><b>UX/UI Developer</b></summary>

```text
I want you to act as a UX/UI developer. I will provide some details about the design of an app, website or other digital product, and it will be your job to come up with creative ways to improve its user experience. This could involve creating prototyping prototypes, testing different designs and providing feedback on what works best. My first request is "I need help designing an intuitive navigation system for my new mobile application."
```

</details>

<details><summary><b>Valentine's Day Cocktail Video</b></summary>

```text
Create a 9-second cinematic Valentine’s Day cocktail video in vertical 9:16 format. Warm candlelight, romantic red and soft pink tones, shallow depth of field, elegant dinner table background with roses and candles.

Fast 1-second snapshot cuts with smooth crossfades:

0–3s:
Close-up slow-motion sparkling wine being poured into a champagne flute (French 75). Macro bubbles rising. Quick cut to lemon twist garnish placed on rim.

3–6s:
Strawberries being sliced in soft light. Basil leaves gently pressed. Quick dramatic shot of pink Strawberry Basil Margarita in coupe glass with condensation.

6–9s:
Espresso pouring in slow motion. Cocktail shaker snap cut. Strain into coupe glass with creamy foam (Chocolate Espresso Martini). Final frame: all three cocktails together, soft candle flicker, subtle heart-shaped bokeh in background.

Romantic instrumental jazz soundtrack. Cinematic lighting. Ultra-realistic. High detail. Premium bar aesthetic.
```

</details>

<details><summary><b>Valorant Agent Key Art</b></summary>

```text
{ "TASK": "Design a unique 'Valorant' Agent Key Art. Riot Games Art Style.",
"VISUAL_ID": "Sharp 2.5D digital painting. Fusion of anime & western comic. Matte textures, clean lines, no noise.",
"PALETTE": "Primary: Dark Slate Blue (#0f1923). Branding: Hyper-Red (#ff4655). Ability: Neon highlight.",
"AGENT": "Athletic, confident. Future-tech streetwear (straps, windbreaker, tactical gloves). Sharp facial planes. Hair: Thick, sculpted chunks (no strands).","EFFECTS": "Wielding stylized elemental power (solid energy forms, not realistic particles).", "BG": "Abstract motion graphics, flat geometric planes, kinetic typography. Red/Dark contrast slicing the frame.",
"LIGHT": "Strong rim lighting, hard-edge cast shadows.", "NEG": "Photorealism, grit, dirt, oil painting, soft focus, 3d render, shiny metal, messy, noise, blur."
}//You can add Name and Skills or size like 16:9 here.
```

</details>

<details><summary><b>Victorian Conservatory at Blue Hour</b></summary>

```text
Photoreal architectural exterior photograph of the same Victorian glass conservatory from step 2, now seen from outside at blue hour, standing on a pale gravel garden path about 15 m in front of its glazed gable end, at eye level (1.6 m), looking straight at the gable and along the length of the building, 35mm lens, 16:9 landscape composition, symmetrical, the whole building in frame slightly below center. Keep every fixed design detail identical to step 2: a long, narrow rectangular hall with a tall curved barrel-vault glass roof; many closely spaced slender white-painted iron ribs run over the vault, and the glass between them is divided by a dense grid of thin white glazing bars. The side walls are cream painted classical masonry: tall cream pilasters with carved white scroll corbels under a cream cornice, and between them very tall, narrow white-framed windows divided into long vertical panes, set above a low cream plinth wall. The gable end facing the camera is a glazed semicircle following the vault curve, filled with radiating sunburst glazing bars above a horizontal transom; below it a wide white-framed glass wall of rectangular panes with tall white double glass doors in the center, closed, each door with a small brass handle. Seen through the glass, glowing from inside: the warm beige stone tile floor, the long empty central hall, the pilasters and windows of the far end, and two small fan palms in round white planters standing just inside the doors, one on each side. The interior is lit by warm amber light from wall lamps behind the pilasters, so the whole glass vault glows like a lantern and the white ribs stand out in silhouette. Outside: the gravel path runs straight from the camera to the doors between low clipped box hedges and a mown lawn; mature deciduous trees in early autumn color stand on both sides, and a dark red brick house with lit windows is partly visible behind the trees on the left. Deep cobalt blue sky with the last pale glow low on the horizon, a few early stars, cool blue dusk mixed with warm amber interior light, faint mist over the lawn, soft reflections on the glass. Calm, romantic, timeless mood, crisp architectural detail, true colors, straight verticals. No people, no readable text, no signs or plaques, no modern objects or garden lights, no watermark.
```

</details>

<details><summary><b>Victorian Conservatory Interior in Morning Light</b></summary>

```text
Photoreal architectural interior photograph of a High Victorian glass conservatory in early morning, taken from standing eye level (1.6 m) just inside the open front double doors, looking straight down the central aisle along the length of the hall, 24mm lens, 16:9 landscape composition, symmetrical one-point perspective. Fixed design details: a rectangular hall about 14 m long, 8 m wide, and 7 m high at the ridge; a low pale cream limestone plinth wall about 70 cm high runs around the base, with tall clear glass walls in white-framed rectangular panes above it, and a curved barrel-vault glass roof springing from the tops of the walls. Nine slender white-painted wrought iron arched ribs, about 1.5 m apart, cross the hall from wall to wall, each with small white scroll brackets where the wall meets the roof. Between the ribs the roof is glazed in a diamond lattice of thin white glazing bars, the old glass slightly wavy and misted with condensation. The far end wall is a glazed semicircular gable following the vault curve, with a tall tree fern on each side of it. The floor is black and white marble checkerboard in large square tiles, laid square to the 2 m wide central aisle, polished and a little damp. At the exact center of the hall sits a round fountain basin about 2 m across with a low rim clad in deep blue and gold mosaic, a small three-tier white stone bowl spout trickling water, and orange and white koi visible in the water. Two ornate black cast-iron benches with fern-pattern backs and pale oak seat slats stand one on each side of the aisle, facing the fountain. Four tall kentia palms in large terracotta pots line the aisle, two on each side between the camera and the fountain. Lush Boston ferns in round wire baskets hang on thin chains from every rib along both sides of the aisle. A row of five brass pendant lanterns with frosted glass globes hangs on long chains above the central aisle, switched off. Along the right wall runs a slatted oak plant shelf with white orchids and small terracotta pots; low beds of moss and ground ferns line the plinth on both sides. Light and atmosphere: low morning sun from the left streams through the glass walls in long, clearly visible golden light shafts cutting through soft humid mist, dappled diamond-pattern shadows from the roof fall across the checkerboard floor, droplets of condensation catch the light, fresh green and chalk-white palette with warm gold highlights. Calm, quiet, timeless mood, crisp architectural detail, true colors, no distortion of vertical lines. No people, no readable text, no signs or plaques, no modern objects, no watermark.
```

</details>

<details><summary><b>Victorian Halloween Cabinet Card Photograph</b></summary>

```text
Authentic Victorian-era Halloween cabinet card photograph, circa 1890, three children posing solemnly in a vintage photography studio, a young girl dressed as a Victorian witch wearing an elaborate black lace dress and pointed hat, holding an old-fashioned wooden broom, a young boy dressed as Count Dracula with an elegant dark cape and high collar, and a mysterious child dressed as a ghost beneath a flowing white sheet with two eyeholes. Surrounded by carved jack-o'-lantern pumpkins, delicate cobwebs, an antique human skeleton, a black cat and gothic candleholders. Elaborate Victorian studio backdrop, theatrical composition, haunting yet charming atmosphere, subtle gothic horror aesthetic, authentic 19th-century clothing and handmade costumes, extremely realistic faces, natural skin textures, serious expressions, aged sepia albumen print, antique photographic grain, subtle fading, scratches, worn paper edges, ornate embossed cardboard mount with decorative typography, historically accurate cabinet card photography, soft diffused studio lighting, exquisite archival details, photorealistic, no modern elements --ar 3:4
```

</details>

<details><summary><b>Victorian Time Traveler in a Jungle</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve his core likeness. Transform Subject 1 (male) into a Victorian time traveler who has just materialized in a dense, prehistoric jungle. The image must be Ultra-Photorealistic, Movie-Quality, and highly detailed. The scene captures the moment of arrival, shot on Arri Alexa with cinematic lighting and a shallow depth of field. He stands amidst towering ferns and ancient cycads, looking completely out of place in his formal 19th-century attire, contrasting the rugged, humid environment with his refined appearance.",
  "details": {
    "year": "1895 / 65 Million BC",
    "genre": "Cinematic Photorealism",
    "location": "A dense, steaming Cretaceous jungle floor filled with giant ferns, ancient conifers, and thick atmospheric fog.",
    "lighting": [
      "Volumetric god rays piercing through the canopy",
      "Dappled sunlight",
      "High dynamic range"
    ],
    "camera_angle": "Medium close-up at eye level, focusing on the subject with the background falling into soft bokeh.",
    "emotion": [
      "Disbelief",
      "Awe",
      "Scientific curiosity",
      "Fear"
    ],
    "color_palette": [
      "Deep emerald greens",
      "Earthy mud browns",
      "Burnished brass",
      "Tweed grey"
    ],
    "atmosphere": [
      "Humid",
      "Primordial",
      "Claustrophobic",
      "Mysterious"
    ],
    "environmental_elements": "Floating pollen particles, massive prehistoric insects buzzing in the background, a large ominous silhouette of a dinosaur visible through the thick mist.",
    "subject1": {
      "costume": "A bespoke three-piece Victorian tweed suit, a slightly askew cravat, and intricate brass steampunk goggles pushed up onto his forehead.",
      "subject_expression": "Wide-eyed shock mixed with fascination, mouth slightly open, sweat beading on his brow.",
      "subject_action": "Clutching a glowing, smoking brass chronometer device in one hand while tentatively reaching out to touch a massive, alien-looking fern frond with the other."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "modern buildings",
        "paved roads",
        "cars",
        "cell phones",
        "contemporary fashion",
        "cleanliness"
      ],
      "exclude_styles": [
        "cartoon",
        "3D render",
        "illustration",
        "painting",
        "low resolution",
        "blur",
        "sketch"
      ],
      "exclude_colors": [
        "neon",
        "pastel pinks",
        "artificial brights"
      ],
      "exclude_objects": [
        "spaceships",
        "aliens",
        "modern weapons"
      ]
    }
  }
}
```

</details>

<details><summary><b>Victorian Time Traveler in the Jungle</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve his core likeness. The scene depicts Subject 1 as a beleaguered Victorian time traveler checking a complicated brass chronometer in a dense, misty prehistoric jungle. The image must be ultra-photorealistic and highly detailed, capturing the texture of fraying velvet, sweating skin, and wet tropical leaves. Use cinematic lighting with dappled sunlight breaking through the canopy to illuminate the subject. The style is that of a high-budget movie, shot on Arri Alexa with a shallow depth of field.",
  "details": {
    "year": "The Late Cretaceous Period (via 1890)",
    "genre": "Cinematic Photorealism",
    "location": "A dense, humid jungle floor with giant ferns and ancient cycads.",
    "lighting": [
      "Dappled sunlight filtering through canopy",
      "Atmospheric volumetric fog",
      "High contrast shadows"
    ],
    "camera_angle": "Eye-level close-up with focus on the face and device.",
    "emotion": [
      "Panic",
      "Urgency",
      "Disbelief"
    ],
    "color_palette": [
      "Deep emerald greens",
      "Muddy browns",
      "Tarnished brass gold",
      "Rich burgundy"
    ],
    "atmosphere": [
      "Humid",
      "Dangerous",
      "Claustrophobic",
      "Sweltering"
    ],
    "environmental_elements": "Giant fern fronds, hovering prehistoric insects, rising steam from the damp ground, a blurred massive shape moving in the background.",
    "subject1": {
      "costume": "A torn and muddy three-piece Victorian velvet suit, a loose cravat, and brass steampunk goggles around the neck.",
      "subject_expression": "Wide-eyed desperation, sweat beading on the forehead.",
      "subject_action": "Frantically tapping the glass dial of a glowing, smoking brass chronometer held in his hand."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "modern buildings",
        "paved roads",
        "digital watches",
        "sneakers",
        "plastic"
      ],
      "exclude_styles": [
        "cartoon",
        "sketch",
        "oil painting",
        "anime",
        "low resolution"
      ],
      "exclude_colors": [
        "neon blue",
        "hot pink"
      ],
      "exclude_objects": [
        "cars",
        "modern weaponry"
      ]
    }
  }
}
```

</details>

<details><summary><b>Viking Jarl Photo Transformation</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. The face must remain clear and unaltered. Transform the subject into a formidable **Viking Jarl or Shieldmaiden**, standing commanding at the prow of a longship sailing through a dramatic Norwegian fjord. Emphasize rugged textures of fur and metal, cold Northern light, sea spray, and an epic, adventurous atmosphere.",
  "details": {
    "year": "Viking Age (approx. 9th-10th Century)",
    "genre": "Historical Epic / Gritty Realism / Adventure",
    "location": "The wooden prow of a carved dragon-headed longship, cutting through dark, choppy water. Steep, mist-shrouded mountains rise dramatically on both sides of the fjord. Snow might be visible on the peaks. The sky is overcast and heavy.",
    "lighting": "Cold, diffused Northern daylight. It's moody and overcast, creating soft but distinct shadows. The light emphasizes the textures of wet wood, metal, and fur. No warm sunlight.",
    "camera_angle": "Medium-long shot, slightly low-angle, looking up at the subject to emphasize their power and leadership against the backdrop of the massive fjord. (1:1 composition).",
    "emotion": "Fierce, commanding, determined, and rugged.",
    "costume": "Heavy, authentic Viking attire: a thick bear or wolf fur cloak clasped with an ornate brooch over leather armor reinforced with iron plates or chainmail. A large, battle-worn bearded axe resting on their shoulder or held firmly. Hair might be braided, and if applicable, a rugged beard. Subtle, historically plausible tattoos on visible skin.",
    "color_palette": "Dominated by cold, natural tones: deep sea blues and grays, dark browns of wet wood and leather, slate grays of rock and sky, and the natural tones of fur. The metal accents are dull iron, not shiny steel.",
    "atmosphere": "Epic, raw, cold, and adventurous. The air feels freezing and damp with sea spray. The sound of waves crashing against wood is almost audible. A sense of a long journey and conquest.",
    "subject_expression": "A fierce, determined gaze looking ahead toward the horizon. The face is set in a grim, commanding line, showing resilience against the elements. Sea spray might be on their face.",
    "subject_action": "Standing with a wide, stable stance on the shifting deck. One hand is gripping the dragon-head stem of the ship or the rigging, while the other holds their axe. They are bracing against the movement of the sea.",
    "environmental_elements": "Sea spray splashing over the bow. Other crew members (rowers) are visible as indistinct, rugged shapes in the background, laboring at the oars. The sail is a heavy, woven wool fabric with bold stripes (e.g., red and white)."
  }
}
```

</details>

<details><summary><b>Villa Reverse Construction Storyboard</b></summary>

```text
Act as an architectural visualization expert specialized in building design and home renovation. Your task is to create a storyboard consisting of 10 frames arranged in a 5x2 grid (two rows of five columns). Each frame should have a 9:16 aspect ratio in a vertical format. Maintain consistent camera positions and shooting angles across all images. The storyboard should reflect a progressive change in construction status, with each subsequent frame building upon the previous one (image-to-image progression).

Ensure continuity between frames by adhering to the following principles:

1. **Technical Specifications**: Include detailed camera settings, lighting parameters, and composition requirements.
2. **Precise Positioning**: Use a grid coordinate system to ensure element consistency in location.
3. **Controlled Changes**: Each frame should allow only specified additions or removals.
4. **Visual Consistency**: Keep camera positions, lighting angles, and perspective relations fixed.
5. **Construction Sequence**: Follow a logical and realistic sequence of construction steps.
6. **Removal Constraints**: Only remove debris and dilapidated items.
7. **Addition Constraints**: Only add useful furniture, plants, lighting, or other objects, which must remain fixed in position.

Overall aspect ratio of the storyboard is 45:32, and no text should appear within the images.

**Special Requirement**: Rewrite the storyboard prompts adhering to a strict reduction principle: only remove elements based on the existing structure. After all elements are removed, revert the foundation to a natural, unkempt state. No new elements can be added, except in the final step when the ground is reverted.

**Storyboard Sequence** (Top Row Left→Right, Bottom Row Left→Right):

[Row 1, Col 1] Frame 1: Complete villa with ALL interior furniture (sofas, tables, chairs), curtains, potted plants, rugs, artwork, outdoor loungers, umbrella, manicured green lawn, flowering beds, glass curtain wall, finished facade. Background: snow-capped mountain and century-old trees (green and healthy).

[Row 1, Col 2] Frame 2: REMOVE ALL soft furnishings - furniture, curtains, potted plants, rugs, artwork GONE. Rooms are empty but floors/walls/ceilings remain finished. Terrace is bare stone, flower beds are empty soil patches. Mountain and trees unchanged.

[Row 1, Col 3] Frame 3: REMOVE ALL interior finishes - floor tiles/wood, wall paint/plaster, ceiling tiles, light fixtures GONE. Raw concrete floors and rough wall substrates visible. Open concrete soffits overhead. Mountain and trees unchanged.

[Row 1, Col 4] Frame 4: REMOVE entire glass envelope - ALL glass panels, window frames, door frames, exterior cladding, insulation GONE. Building is fully open, revealing internal steel/concrete columns against the lawn. Mountain and trees unchanged.

[Row 1, Col 5] Frame 5: REMOVE non-structural masonry - ALL partition walls, infill walls, parapets GONE. ONLY primary structural skeleton remains: bare upright concrete columns, steel beams, and floor slabs forming an empty grid frame. Mountain and trees unchanged.

[Row 2, Col 1] Frame 6: Frame COLLAPSES to rubble - columns/beams/slabs fall to ground forming scattered debris pile (concrete chunks, twisted rebar, broken steel). Concrete foundation partially visible through debris. Upright framework GONE. Mountain and trees unchanged.

[Row 2, Col 2] Frame 7: REMOVE ALL debris - concrete chunks, rebar, steel, waste CLEARED. Lawn debris-free. Entire concrete foundation fully exposed as clean rectangular block on ground. Mountain and trees unchanged.

[Row 2, Col 3] Frame 8: REMOVE concrete Foundation - foundation slab DEMOLISHED and COMPLETELY REMOVED. Empty excavated pit remains with compacted soil/bedrock at bottom. No concrete remains. Mountain and trees unchanged.

[Row 2, Col 4] Frame 9: REMOVE artificial landscape - terrace paving, concrete driveway, manicured lawn, cultivated soil ALL REMOVED. Pit filled back to original grade. Site becomes flat field of natural uncultivated soil and earth. Mountain and trees unchanged.

[Row 2, Col 5] Frame 10: RESTORE ground to natural state - flat soil transforms to rugged uneven terrain with exposed rocks, dirt patches, scattered dry weeds. Ground appears untamed and messy. Snow-capped mountain and century-old trees remain IDENTICAL in position, shape, and foliage color (still green and healthy). Bright natural daylight persists throughout.

**CRITICAL SUBTRACTION LOGIC:**
- Frames 1-9: Can ONLY REMOVE elements present in previous frame. NO additions allowed.
- Frame 10: RESTORE ground from artificial to natural state only.

**Visual Anchors**: The background mountain silhouette and foreground century-old trees must maintain IDENTICAL position, size, shape, and foliage color (green and healthy) in ALL FRAMES. These serve as reference points for visual continuity.

**Lighting Consistency**: All frames must use bright, natural daylight. No dark, gloomy, or stormy lighting, especially in final frame.

**Camera Stability**: Use identical camera angle, composition, and depth of field across all frames. Viewing perspective must be locked.
```

</details>

<details><summary><b>Village Youngsters Build a Rocket Video</b></summary>

```text
I want a video prompt on south Indian village youngsters manufacture a rocket video with their knowledge
```

</details>

<details><summary><b>Vineyard Pavilion Terrace at Sunset</b></summary>

```text
The long covered terrace of a single-story limestone tasting pavilion at sunset, seen from the downhill vine rows looking up the slope. The terrace runs along the long side of the building with five dark oiled oak posts, wooden tables with empty wine glasses, and warm string lights glowing under the deep eaves. Same building: pale honey-colored limestone walls, low-pitched gabled terracotta clay tile roof, tall bronze-framed glass doors along the terrace, a short square limestone chimney rising from the left gable end, a deep green double door in that left gable wall, and the large old olive tree with a twisted trunk standing at the left corner beside that door. Grape-heavy vine rows lead the eye uphill to the pavilion, with low dry-stone walls and lavender borders below the terrace. Sky in apricot and rose, sun setting behind the viewer so the walls glow warm amber, soft shadows between the vines. Photoreal architectural photography, landscape 16:9. No people, no text, no signs, no cars.
```

</details>

<details><summary><b>Vineyard Tasting Pavilion Brief Builder</b></summary>

```text
Act as an architectural concept designer who writes image-ready design briefs. Help me shape a small hillside vineyard tasting pavilion: a single-story building where visitors taste wine and look out over the vine rows. Your brief must be specific enough that two separate image generations (an establishing exterior and a second exterior angle) show the same building.

First ask me, in one short message, for:
- Region and climate (for example Mediterranean, temperate river valley, high desert) and the season I want to show
- Slope direction and the main view (valley, lake, distant mountains, village)
- Capacity (how many guests at once) and whether there is a small barrel room or kitchen
- Material preferences and anything I want to avoid (glass boxes, rustic kitsch, very modern minimalism)
- Mood words (calm, sunny, earthy, elegant, family-run)

Then produce the brief with these sections:

1. **Site and Orientation**: where the pavilion sits on the slope, which side faces the view, sun path for morning and sunset, and how a gravel path climbs from the parking area through the vines.

2. **Building Form**: footprint size, roof shape and pitch, overhang depth, the long covered terrace on the downhill side, and the number and position of large openings. Keep it compact and believable.

3. **Materials Palette**: exactly four or five materials with colors (for example local limestone walls, oiled oak beams, clay roof tiles, bronze window frames, gravel terrace) and where each one appears.

4. **Landscape**: vine row direction, an old olive or oak tree near the entrance, low stone retaining walls, lavender or herb borders, and outdoor tables.

5. **Fixed Visual Details**: a numbered list of 8 to 10 details that must stay identical in every image (roof type and color, wall material, number of terrace arches or posts, door color, chimney or none, the signature tree, lighting fixtures). These details make the images consistent.

6. **Prompt Seed A - Establishing Exterior**: a ready-to-paste image prompt under 150 words for a morning or harvest-season exterior from the uphill path, with the building and its key objects in the first sentence.

7. **Prompt Seed B - Second Exterior Angle**: a ready-to-paste image prompt under 150 words for a sunset view from the downhill vine rows looking up at the terrace, repeating every fixed visual detail in plain words.

8. **Practical Notes**: three short notes on shade, accessibility (step-free entry), and drainage on a slope.

Rules: no people as the main subject, no text or logos in the image prompts, no interiors in the seeds (image models often ignore furniture). Use short paragraphs and lists.
```

</details>

<details><summary><b>Vintage Analog Portrait</b></summary>

```text
Vintage 1980s-style analog photograph, warm faded colors, heavy grain, slight light leak. Iranian woman, thick natural brows, looking up from beneath lowered lashes, one brow subtly raised, a slow blink — coquettish "naz". Old family-album texture. Below the photo, a hand-torn sketchy frame with old-fashioned fountain-pen handwriting: "ناز".
```

</details>

<details><summary><b>Vintage Black and White Photo of Galata Tower</b></summary>

```text
{
  "colors": {
    "color_temperature": "neutral",
    "contrast_level": "high",
    "dominant_palette": [
      "black",
      "white",
      "grey"
    ]
  },
  "composition": {
    "camera_angle": "wide shot",
    "depth_of_field": "deep",
    "focus": "Galata Tower",
    "framing": "The Galata Tower is centrally placed in the upper half of the image, framed vertically by tall, dark cypress trees on both sides."
  },
  "description_short": "A vintage black and white photograph of the Galata Tower in Istanbul, viewed from a cemetery with old wooden houses, and framed by tall cypress trees.",
  "environment": {
    "location_type": "cityscape",
    "setting_details": "The setting is a historic neighborhood in Istanbul, likely Galata. In the background stands the iconic stone Galata Tower. The middle ground features old, possibly wooden, Ottoman-era buildings. The foreground is an unkempt area, appearing to be a cemetery with weathered grave markers or posts protruding from the earth.",
    "time_of_day": "afternoon",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "strong",
    "source_direction": "side",
    "type": "natural"
  },
  "mood": {
    "atmosphere": "A timeless and nostalgic glimpse into the past.",
    "emotional_tone": "melancholic"
  },
  "narrative_elements": {
    "character_interactions": "Two figures are visible in the mid-ground, standing near a building. Their interaction is minimal, appearing as part of the daily life of the scene rather than a focal point.",
    "environmental_storytelling": "The image juxtaposes the enduring stone monument of the tower with the decaying wooden structures and the cemetery, suggesting themes of history, memory, and the passage of time.",
    "implied_action": "The scene is static and quiet, capturing a moment of stillness in a historic city."
  },
  "objects": [
    "Galata Tower",
    "Cypress trees",
    "Wooden houses",
    "Tombstones",
    "Stone walls"
  ],
  "people": {
    "ages": [
      "adult"
    ],
    "clothing_style": "traditional Ottoman-era attire",
    "count": "2",
    "genders": [
      "male"
    ]
  },
  "prompt": "A vintage, high-contrast black and white photograph of the historic Galata Tower in Istanbul. The iconic stone tower with its conical roof rises in the background against a bright sky. The scene is framed by tall, dark, imposing cypress trees. In the foreground and middle ground, an old cemetery with weathered tombstones and dilapidated wooden Ottoman houses creates a sense of history and melancholy. The lighting is bright natural sunlight, casting sharp shadows. The mood is timeless and nostalgic.",
  "style": {
    "art_style": "realistic",
    "influences": [
      "19th-century photography",
      "travel photography",
      "documentary"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "black and white",
    "monochrome",
    "vintage photograph",
    "historical",
    "high contrast",
    "film grain",
    "Galata Tower",
    "Istanbul",
    "Ottoman architecture",
    "vertical composition"
  ],
  "use_case": "Historical and architectural studies, dataset for vintage photo restoration, cultural heritage documentation.",
  "uuid": "4b0a2894-4d0f-4bd1-82ee-5ee7cf81e135"
}
```

</details>

<details><summary><b>Vintage Botanical Illustration</b></summary>

```text
A botanical diagram of a ${subject}, illustrated in the style of vintage scientific journals. Accented with natural tones and detailed cross-sections, it’s labeled with handwritten annotations in sepia ink, evoking a scholarly, antique charm.
```

</details>

<details><summary><b>Vintage Car Radio at Night</b></summary>

```text
Create a high-resolution *VERTICAL (portrait)* photograph of a vintage car radio screen at night. The camera angle must match a realistic diagonal side-view, similar to an over-the-shoulder cinematic shot from the passenger seat. Do NOT straighten the device — maintain the same natural tilt seen in authentic night-drive photos.

TEXT ON THE LED DISPLAY (amber pixel font):
Weather4Fly

STYLE & LIGHTING:
– Warm orange LED glow, soft bloom around each segmented character.  
– Dark car interior with minimal ambient light.  
– Deep shadows, shallow depth of field, soft bokeh highlights.  
– Subtle scratches on the plastic display cover and gentle dust particles.  
– High contrast, moody, cinematic night-drive aesthetic.

COMPOSITION:
– Frame must be *tall*, extending above and below the radio to create a portrait orientation.  
– The radio stays in the middle-to-upper section, angled exactly as in a real car dashboard.  
– Include side knobs, buttons, and part of the dashboard fading into shadow.  
– Keep the asymmetrical composition and natural perspective distortion.

DETAIL REQUIREMENTS:
– LED characters must look segmented and authentic.  
– Slight reflections on the display surface.  
– Warm tones only — no neon or artificial color shifts.

NEGATIVE PROMPT:
horizontal layout, straight-on view, blue or white LED, modern touchscreen radio, missing text, wrong names, overly sharp digital look, unrealistic symmetry, cartoon rendering.

OUTPUT:
A cinematic vertical portrait photograph of an angled vintage radio display showing the specified names.
```

</details>

<details><summary><b>Vintage Copper Engraving Portrait</b></summary>

```text
A vintage engraved-style portrait illustration using the provided reference image as a strict identity reference.
Preserve the exact facial features, proportions, bone structure, and overall likeness of the person in the photo without alteration. The subject is shown in a side profile, looking slightly upward to the left with a confident, thoughtful expression. Short hair on top with subtle gray tones, thinner on the sides, and a neatly distributed beard along the jawline. Detailed facial rendering using fine cross-hatching and stippling engraving textures. The subject wears glasses, a light beige blazer with subtle diagonal fabric texture, and a dark navy shirt. Behind the head is a circular flat warm yellow background. High-contrast ink linework using monochrome blue ink tones with soft cream highlights. Vector-like precision combined with hand-drawn engraving texture. Chest-up portrait composition, clean light gray background, 4K
resolution, editorial illustration style.
```

</details>

<details><summary><b>Vintage Cutaway of a Deep-Sea Submarine</b></summary>

```text
A detailed vintage cutaway illustration of a small deep-sea research submarine, drawn in the style of a mid-century popular science magazine center spread: precise ink linework with gouache and airbrush color, slightly aged cream paper texture, and a muted palette of ochre yellow, teal, brick red, slate grey, and deep navy. The submarine is shown in a clean side view, long and rounded like a fat capsule with a yellow hull, a domed acrylic viewport at the bow, twin floodlights, a pair of jointed sampling arms holding a tiny coral sample, and a ducted propeller at the stern. A large section of the hull is cut away to reveal the interior in cross-section, compartment by compartment from bow to stern: a cramped pilot sphere with two empty padded seats, glowing dials, and control levers; a small science lab with specimen jars, a microscope, and rows of small drawers; a galley nook with a kettle and tin mugs; two folded bunks; a battery room with neat rows of cells; ballast tanks shown half-filled with blue water; and an engine compartment with pipes, valves, and the propeller shaft. Thin cutaway edges show the thick layered hull wall. The submarine floats in a deep blue ocean that darkens from teal at the top to navy at the bottom, with drifting particles, a curious lanternfish, a small squid, and a rocky seafloor with tube worms and a hydrothermal vent in the lower right. Even, clear lighting typical of technical illustration, high detail, every compartment readable, balanced horizontal 16:9 landscape composition with the submarine spanning the center. No people, no crew, no readable text, no labels, no numbers, no logos, no watermark.
```

</details>

<details><summary><b>Vintage Film Matchlight Portrait</b></summary>

```text
Atmospheric vertical portrait in a “film photography” aesthetic. The girl sits on the floor, leaning her back against a plain light-colored wall (light gray or white with a slight texture). The pose is relaxed and slightly introverted: knees bent and pulled up to her chest, torso slightly leaning forward. Her head is turned in profile to the left, her gaze directed downward at a burning match that she holds in her right hand in front of her face. Her left hand rests loosely on her knee/leg.
She is wearing an oversized sweatshirt (a hoodie without a hood) in a muted pink shade (dusty rose or fuchsia) in a vintage style. On the sleeves there are three white stripes along the full length (stylized after Adidas Originals), and the same logo (trefoil) is visible on the left side of the chest. The sweatshirt looks soft, slightly worn. At the bottom, the edges of light-colored shorts are visible (probably white or light pink), legs bare.
Hairstyle: straight hair, loose and naturally resting on her shoulders and back, smooth texture. Makeup done in a “no-makeup makeup” style: matte skin, light blush, natural brows, and a nude lip shade with a light gloss. Long manicure, almond or ballerina shape, done in a delicate milky pink shade (milky pink). A thin gold ring is worn on the ring finger of her right hand. A regular long match with a burning tip is clutched in her hand.
Imitation of shooting on a film camera (35mm film). The image has characteristic grain (film grain) and soft sharpness. Soft diffused daylight falling from the left (probably from a window) creates smooth shadow transitions on the face and clothing. The match flame provides a tiny point source of warm light but is not the main lighting. Color grading in pastel, slightly faded tones. Muted pink, skin tones, and cool white/gray predominate. Low contrast, strong 2010s “Pinterest” or “Tumblr” aesthetic. Minimalist, clean background — a wall without decor, which emphasizes the model’s figure and emotion.
```

</details>

<details><summary><b>Vintage Invention Patent Document</b></summary>

```text
A vintage patent document for ${invention}, styled after late 1800s United States Patent Office filings. The page features precise technical drawings with numbered callouts (Fig. 1, Fig. 2, Fig. 3) showing front, side, and exploded views. Handwritten annotations in fountain-pen ink describe mechanisms. The paper is aged ivory with foxing stains and soft fold creases. An official embossed seal and red wax stamp appear in the corner. A hand-signed inventor's name and date appear at the bottom. The entire image feels like a recovered archival document—authoritative, historic, and slightly mysterious.
```

</details>

<details><summary><b>Vintage Monochrome Silhouette Selfie</b></summary>

```text
Close-up photorealistic selfie in a Pinterest aesthetic, using the uploaded photo as the reference. Preserve the girl's appearance and all of her unique facial features exactly (copy my face 100%).

Composition & pose: First-person selfie with no phone visible. The girl is centered in the frame. Close-up portrait shot from a low angle (looking upward). She is looking slightly upward and to the right of the frame. Because of the low perspective, her face is gently tilted back. Her hands are not visible. Her figure is intentionally soft and slightly out of focus, creating the feeling of a dark blurred silhouette.

Clothing: A fitted black ribbed dress with wide sleeves that flare toward the wrists.

Hair: Extremely long, perfectly straight, sleek luxurious hair flowing freely over her forearms, framing her face, with noticeable wind movement and slight motion blur.

Makeup: Dramatic eye and lip makeup with sharp winged eyeliner, long false lashes, and matte dark lipstick.

Background: Tall spreading trees with bare branches typical of early spring or late autumn. The branches form an intricate graphic pattern against a bright overcast sky, which occupies much of the upper half of the image and contrasts with the girl's dark silhouette.

Style & filter: Artistic black-and-white blur aesthetic. Monochrome palette with deep blacks and soft gray transitions. Intentional softness, pronounced motion blur, subtle contour blur, fine film grain, and the feeling of an old analog photograph, dream, or memory. The emphasis is on shapes, lines, contrast, and silhouettes.

Camera: Shot on an old iPhone 5s (2013–2014), with visible grain, light digital noise, soft sharpness, natural tonal rendering, and authentic iPhone compression. Vertical 3:4, realistic, high-quality, cinematic.
```

</details>

<details><summary><b>Vintage Photo Restoration and Colorization</b></summary>

```text
Ultra-detailed restoration and sharpness enhancement of a vintage photo. Recover fine details and improve clarity, especially on faces. Remove all scratches, dust, stains, tears. Preserve natural film grain. Correct geometry and tonal range. 
Then, colorize it to look like a historical color photograph: natural, muted, historically accurate colors. Avoid plastic skin, oversaturation, digital painting look, and oversharpening artifacts. Museum-quality realism.
```

</details>

<details><summary><b>Vintage Plate of Forest Mushrooms and Mosses</b></summary>

```text
Forest mushrooms and mosses arranged as a vintage natural history chromolithograph plate: a red fly agaric with white spots, a cluster of golden chanterelles, a brown porcini with a thick pale stem, delicate purple amethyst deceivers, and a cross-section of one cap showing gills. The specimens are laid out in a balanced grid on aged cream paper, each drawn with fine engraved outlines and soft stippled shading. Tufts of green cushion moss, a curl of birch bark, and a few fallen oak leaves sit between them. Muted 19th-century print colors: brick red, ochre, olive green, umber, and dusty violet, with slight color registration offset typical of stone lithography. Foxing spots and gentle paper yellowing at the edges, thin double-ruled border around the plate. Scientific, calm, collectible antique print mood. No text, no labels, no numbers, no captions, no people.
```

</details>

<details><summary><b>Vintage Tin Toy Robots Parade</b></summary>

```text
A macro product photograph of five vintage 1950s wind-up tin toy robots standing side by side in a parade line on a worn wooden shelf, in a wide landscape 16:9 frame. The robots are boxy and retro, each with a square head, round eyes or goggle visor, a little ball-topped antenna, a round dial gauge on the chest, tiny printed rivets, buttons and lights, short stiff arms, and a brass wind-up key on its back. Their painted tin colors from left to right are ${colors:red, teal, cream, mustard yellow, and red}, with slightly worn paint, soft scratches, and a little rust at the edges. The robot on the far right holds a thin metal pole with a small red triangular pennant flag with no text, as if leading the parade. Behind them, out of focus, are dark wooden shelves of old toys: a teddy bear by the window, a small globe, a red ball, a toy truck, and a little dollhouse. Warm golden window light comes from the left, giving soft highlights on the tin and gentle shadows on the scratched wooden shelf. Shallow depth of field, rich warm browns, nostalgic and cheerful mood. No readable text, no logos, no people.
```

</details>

<details><summary><b>Virtual Clothing Try On</b></summary>

```text
**Role / Behavior**
You are a professional AI fashion visualization and virtual try-on system. Your job is to realistically dress a person using a provided clothing image while preserving body proportions, fabric behavior, lighting, and natural appearance.

---

**Inputs (Placeholders)**

* `` → Image of the girl
* `` → Image of the clothing
* `` → Person weight (50kg)
* `` → Person height (1.57m)
* `` → Desired background (outdoor)
* `` → Image quality preference (realistic)

---

**Instructions**

1. Analyze the person image to understand body shape, pose, lighting, and camera perspective.
2. Analyze the clothing image to extract fabric texture, color, structure, and fit behavior.
3. Virtually fit the clothing onto the person while preserving:

   * Correct human proportions based on weight and height
   * Natural fabric folds, stretching, and shadows
   * Realistic lighting consistency with the original photo
   * Accurate alignment of sleeves, collar, waist, and hem
4. Generate **three realistic try-on images** showing:

   * **Front view**
   * **Side view**
   * **Back view**
5. Ensure the face, hair, skin tone, and identity remain unchanged.
6. Avoid distortions, blurry artifacts, unrealistic body deformation, or mismatched lighting.

---

**Output Format**

Return exactly:

* **Image 1:** Front view try-on
* **Image 2:** Side view try-on
* **Image 3:** Back view try-on

Each image must be photorealistic and high resolution.

---

**Constraints**

* Maintain anatomical accuracy.
* No exaggerated beauty filters or stylization.
* No text overlays or watermarks.
* Keep clothing scale proportional to `and`.
* Background must remain natural and consistent unless overridden by ``.
* Do not change facial identity or pose unless required for angle generation.
```

</details>

<details><summary><b>Visual Design Director</b> · machine translated</summary>

```text
Your task is to provide professional visual design guidance. Please analyze the following design requirements:

<设计项目>
Design type: {{DESIGN_TYPE}}
Project background: {{PROJECT_CONTEXT}}
Design goals: {{DESIGN_GOALS}}
Target audience: {{TARGET_AUDIENCE}}
Application scenarios: {{APPLICATION_SCENARIOS}}
</设计项目>

<设计要求>
Style preference: {{STYLE_PREFERENCE}}
Color requirements: {{COLOR_REQUIREMENTS}}
Size specifications: {{SIZE_SPECIFICATIONS}}
Technical constraints: {{TECHNICAL_CONSTRAINTS}}
</设计要求>

Please provide design guidance that includes the following:
1. Design concept and creative direction
2. Color scheme and visual hierarchy
3. Font selection and typographic layout
4. Graphic elements and decorative design
5. Output specifications and application guidelines

Please output the complete visual design guidance plan inside <design-guide> tags.
```

</details>

<details><summary><b>Visual Media Analysis Expert Agent</b></summary>

```text
# Visual Media Analysis Expert

You are a senior visual media analysis expert and specialist in cinematic forensics, narrative structure deconstruction, cinematographic technique identification, production design evaluation, editorial pacing analysis, sound design inference, and AI-assisted image prompt generation.

## Task-Oriented Execution Model
- Treat every requirement below as an explicit, trackable task.
- Assign each task a stable ID (e.g., TASK-1.1) and use checklist items in outputs.
- Keep tasks grouped under the same headings to preserve traceability.
- Produce outputs as Markdown documents with task checklists; include code only in fenced blocks when required.
- Preserve scope exactly as written; do not drop or add requirements.

## Core Tasks
- **Segment** video inputs by detecting every cut, scene change, and camera angle transition, producing a separate detailed analysis profile for each distinct shot in chronological order.
- **Extract** forensic and technical details including OCR text detection, object inventory, subject identification, and camera metadata hypothesis for every scene.
- **Deconstruct** narrative structure from the director's perspective, identifying dramatic beats, story placement, micro-actions, subtext, and semiotic meaning.
- **Analyze** cinematographic technique including framing, focal length, lighting design, color palette with HEX values, optical characteristics, and camera movement.
- **Evaluate** production design elements covering set architecture, props, costume, material physics, and atmospheric effects.
- **Infer** editorial pacing and sound design including rhythm, transition logic, visual anchor points, ambient soundscape, foley requirements, and musical atmosphere.
- **Generate** AI reproduction prompts for Midjourney and DALL-E with precise style parameters, negative prompts, and aspect ratio specifications.

## Task Workflow: Visual Media Analysis
Systematically progress from initial scene segmentation through multi-perspective deep analysis, producing a comprehensive structured report for every detected scene.

### 1. Scene Segmentation and Input Classification
- Classify the input type as single image, multi-frame sequence, or continuous video with multiple shots.
- Detect every cut, scene change, camera angle transition, and temporal discontinuity in video inputs.
- Assign each distinct scene or shot a sequential index number maintaining chronological order.
- Estimate approximate timestamps or frame ranges for each detected scene boundary.
- Record input resolution, aspect ratio, and overall sequence duration for project metadata.
- Generate a holistic meta-analysis hypothesis that interprets the overarching narrative connecting all detected scenes.

### 2. Forensic and Technical Extraction
- Perform OCR on all visible text including license plates, street signs, phone screens, logos, watermarks, and overlay graphics, providing best-guess transcription when text is partially obscured or blurred.
- Compile a comprehensive object inventory listing every distinct key object with count, condition, and contextual relevance (e.g., "1 vintage Rolex Submariner, worn leather strap; 3 empty ceramic coffee cups, industrial glaze").
- Identify and classify all subjects with high-precision estimates for human age, gender, ethnicity, posture, and expression, or for vehicles provide make, model, year, and trim level, or for biological subjects provide species and behavioral state.
- Hypothesize camera metadata including camera brand and model (e.g., ARRI Alexa Mini LF, Sony Venice 2, RED V-Raptor, iPhone 15 Pro, 35mm film stock), lens type (anamorphic, spherical, macro, tilt-shift), and estimated settings (ISO, shutter angle or speed, aperture T-stop, white balance).
- Detect any post-production artifacts including color grading signatures, digital noise reduction, stabilization artifacts, compression blocks, or generative AI tells.
- Assess image authenticity indicators such as EXIF consistency, lighting direction coherence, shadow geometry, and perspective alignment.

### 3. Narrative and Directorial Deconstruction
- Identify the dramatic structure within each shot as a micro-arc: setup, tension, release, or sustained state.
- Place each scene within a hypothesized larger narrative structure using classical frameworks (inciting incident, rising action, climax, falling action, resolution).
- Break down micro-beats by decomposing action into sub-second increments (e.g., "00:01 subject turns head left, 00:02 eye contact established, 00:03 micro-expression of recognition").
- Analyze body language, facial micro-expressions, proxemics, and gestural communication for emotional subtext and internal character state.
- Decode semiotic meaning including symbolic objects, color symbolism, spatial metaphors, and cultural references that communicate meaning without dialogue.
- Evaluate narrative composition by assessing how blocking, actor positioning, depth staging, and spatial arrangement contribute to visual storytelling.

### 4. Cinematographic and Visual Technique Analysis
- Determine framing and lensing parameters: estimated focal length (18mm, 24mm, 35mm, 50mm, 85mm, 135mm), camera angle (low, eye-level, high, Dutch, bird's eye), camera height, depth of field characteristics, and bokeh quality.
- Map the lighting design by identifying key light, fill light, backlight, and practical light positions, then characterize light quality (hard-edged or diffused), color temperature in Kelvin, contrast ratio (e.g., 8:1 Rembrandt, 2:1 flat), and motivated versus unmotivated sources.
- Extract the color palette as a set of dominant and accent HEX color codes with saturation and luminance analysis, identifying specific color grading aesthetics (teal and orange, bleach bypass, cross-processed, monochromatic, complementary, analogous).
- Catalog optical characteristics including lens flares, chromatic aberration, barrel or pincushion distortion, vignetting, film grain structure and intensity, and anamorphic streak patterns.
- Classify camera movement with precise terminology (static, pan, tilt, dolly in/out, truck, boom, crane, Steadicam, handheld, gimbal, drone) and describe the quality of motion (hydraulically smooth, intentionally jittery, breathing, locked-off).
- Assess the overall visual language and identify stylistic influences from known cinematographers or visual movements (Gordon Willis chiaroscuro, Roger Deakins naturalism, Bradford Young underexposure, Lubezki long-take naturalism).

### 5. Production Design and World-Building Evaluation
- Describe set design and architecture including physical space dimensions, architectural style (Brutalist, Art Deco, Victorian, Mid-Century Modern, Industrial, Organic), period accuracy, and spatial confinement or openness.
- Analyze props and decor for narrative function, distinguishing between hero props (story-critical objects), set dressing (ambient objects), and anachronistic or intentionally placed items that signal technology level, economic status, or cultural context.
- Evaluate costume and styling by identifying fabric textures (leather, silk, denim, wool, synthetic), wear-and-tear details, character status indicators (wealth, profession, subculture), and color coordination with the overall palette.
- Catalog material physics and surface qualities: rust patina, polished chrome, wet asphalt reflections, dust particle density, condensation, fingerprints on glass, fabric weave visibility.
- Assess atmospheric and environmental effects including fog density and layering, smoke behavior (volumetric, wisps, haze), rain intensity and directionality, heat haze, lens condensation, and particulate matter in light beams.
- Identify the world-building coherence by evaluating whether all production design elements consistently support a unified time period, socioeconomic context, and narrative tone.

### 6. Editorial Pacing and Sound Design Inference
- Classify rhythm and tempo using musical terminology: Largo (very slow, contemplative), Andante (walking pace), Moderato (moderate), Allegro (fast, energetic), Presto (very fast, frenetic), or Staccato (sharp, rhythmic cuts).
- Analyze transition logic by hypothesizing connections to potential previous and next shots using editorial techniques (hard cut, match cut, jump cut, J-cut, L-cut, dissolve, wipe, smash cut, fade to black).
- Map visual anchor points by predicting saccadic eye movement patterns: where the viewer's eye lands first, second, and third, based on contrast, motion, faces, and text.
- Hypothesize the ambient soundscape including room tone characteristics, environmental layers (wind, traffic, birdsong, mechanical hum, water), and spatial depth of the sound field.
- Specify foley requirements by identifying material interactions that would produce sound: footsteps on specific surfaces (gravel, marble, wet pavement), fabric movement (leather creak, silk rustle), object manipulation (glass clink, metal scrape, paper shuffle).
- Suggest musical atmosphere including genre, tempo in BPM, key signature, instrumentation palette (orchestral strings, analog synthesizer, solo piano, ambient pads), and emotional function (tension building, cathartic release, melancholic underscore).

## Task Scope: Analysis Domains

### 1. Forensic Image and Video Analysis
- OCR text extraction from all visible surfaces including degraded, angled, partially occluded, and motion-blurred text.
- Object detection and classification with count, condition assessment, brand identification, and contextual significance.
- Subject biometric estimation including age range, gender presentation, height approximation, and distinguishing features.
- Vehicle identification with make, model, year, trim, color, and condition assessment.
- Camera and lens identification through optical signature analysis: bokeh shape, flare patterns, distortion profiles, and noise characteristics.
- Authenticity assessment for detecting composites, deep fakes, AI-generated content, or manipulated imagery.

### 2. Cinematic Technique Identification
- Shot type classification from extreme close-up through extreme wide shot with intermediate gradations.
- Camera movement taxonomy covering all mechanical (dolly, crane, Steadicam) and handheld approaches.
- Lighting paradigm identification across naturalistic, expressionistic, noir, high-key, low-key, and chiaroscuro traditions.
- Color science analysis including color space estimation, LUT identification, and grading philosophy.
- Lens characterization through focal length estimation, aperture assessment, and optical aberration profiling.

### 3. Narrative and Semiotic Interpretation
- Dramatic beat analysis within individual shots and across shot sequences.
- Character psychology inference through body language, proxemics, and micro-expression reading.
- Symbolic and metaphorical interpretation of visual elements, spatial relationships, and compositional choices.
- Genre and tone classification with confidence levels and supporting visual evidence.
- Intertextual reference detection identifying visual quotations from known films, artworks, or cultural imagery.

### 4. AI Prompt Engineering for Visual Reproduction
- Midjourney v6 prompt construction with subject, action, environment, lighting, camera gear, style, aspect ratio, and stylize parameters.
- DALL-E prompt formulation with descriptive natural language optimized for photorealistic or stylized output.
- Negative prompt specification to exclude common artifacts (text, watermark, blur, deformation, low resolution, anatomical errors).
- Style transfer parameter calibration matching the detected aesthetic to reproducible AI generation settings.
- Multi-prompt strategies for complex scenes requiring compositional control or regional variation.

## Task Checklist: Analysis Deliverables

### 1. Project Metadata
- Generated title hypothesis for the analyzed sequence.
- Total number of distinct scenes or shots detected with segmentation rationale.
- Input resolution and aspect ratio estimation (1080p, 4K, vertical, ultrawide).
- Holistic meta-analysis synthesizing all scenes and perspectives into a unified cinematic interpretation.

### 2. Per-Scene Forensic Report
- Complete OCR transcript of all detected text with confidence indicators.
- Itemized object inventory with quantity, condition, and narrative relevance.
- Subject identification with biometric or model-specific estimates.
- Camera metadata hypothesis with brand, lens type, and estimated exposure settings.

### 3. Per-Scene Cinematic Analysis
- Director's narrative deconstruction with dramatic structure, story placement, micro-beats, and subtext.
- Cinematographer's technical analysis with framing, lighting map, color palette HEX codes, and movement classification.
- Production designer's world-building evaluation with set, costume, material, and atmospheric assessment.
- Editor's pacing analysis with rhythm classification, transition logic, and visual anchor mapping.
- Sound designer's audio inference with ambient, foley, musical, and spatial audio specifications.

### 4. AI Reproduction Data
- Midjourney v6 prompt with all parameters and aspect ratio specification per scene.
- DALL-E prompt optimized for the target platform's natural language processing.
- Negative prompt listing scene-specific exclusions and common artifact prevention terms.
- Style and parameter recommendations for faithful visual reproduction.

## Red Flags When Analyzing Visual Media

- **Merged scene analysis**: Combining distinct shots or cuts into a single summary destroys the editorial structure and produces inaccurate pacing analysis; always segment and analyze each shot independently.
- **Vague object descriptions**: Describing objects as "a car" or "some furniture" instead of "a 2019 BMW M4 Competition in Isle of Man Green" or "a mid-century Eames lounge chair in walnut and black leather" fails the forensic precision requirement.
- **Missing HEX color values**: Providing color descriptions without specific HEX codes (e.g., saying "warm tones" instead of "#D4956A, #8B4513, #F5DEB3") prevents accurate reproduction and color science analysis.
- **Generic lighting descriptions**: Stating "the scene is well lit" instead of mapping key, fill, and backlight positions with color temperature and contrast ratios provides no actionable cinematographic information.
- **Ignoring text in frame**: Failing to OCR visible text on screens, signs, documents, or surfaces misses critical forensic and narrative evidence.
- **Unsupported metadata claims**: Asserting a specific camera model without citing supporting optical evidence (bokeh shape, noise pattern, color science, dynamic range behavior) lacks analytical rigor.
- **Overlooking atmospheric effects**: Missing fog layers, particulate matter, heat haze, or rain that significantly affect the visual mood and production design assessment.
- **Neglecting sound inference**: Skipping the sound design perspective when material interactions, environmental context, and spatial acoustics are clearly inferrable from visual evidence.

## Output (TODO Only)

Write all proposed analysis findings and any structured data to `TODO_visual-media-analysis.md` only. Do not create any other files. If specific output files should be created (such as JSON exports), include them as clearly labeled code blocks inside the TODO.

## Output Format (Task-Based)

Every deliverable must include a unique Task ID and be expressed as a trackable checkbox item.

In `TODO_visual-media-analysis.md`, include:

### Context
- The visual input being analyzed (image, video clip, frame sequence) and its source context.
- The scope of analysis requested (full multi-perspective analysis, forensic-only, cinematographic-only, AI prompt generation).
- Any known metadata provided by the requester (production title, camera used, location, date).

### Analysis Plan
Use checkboxes and stable IDs (e.g., `VMA-PLAN-1.1`):
- [ ] **VMA-PLAN-1.1 [Scene Segmentation]**:
  - **Input Type**: Image, video, or frame sequence.
  - **Scenes Detected**: Total count with timestamp ranges.
  - **Resolution**: Estimated resolution and aspect ratio.
  - **Approach**: Full six-perspective analysis or targeted subset.

### Analysis Items
Use checkboxes and stable IDs (e.g., `VMA-ITEM-1.1`):
- [ ] **VMA-ITEM-1.1 [Scene N - Perspective Name]**:
  - **Scene Index**: Sequential scene number and timestamp.
  - **Visual Summary**: Highly specific description of action and setting.
  - **Forensic Data**: OCR text, objects, subjects, camera metadata hypothesis.
  - **Cinematic Analysis**: Framing, lighting, color palette HEX, movement, narrative structure.
  - **Production Assessment**: Set design, costume, materials, atmospherics.
  - **Editorial Inference**: Rhythm, transitions, visual anchors, cutting strategy.
  - **Sound Inference**: Ambient, foley, musical atmosphere, spatial audio.
  - **AI Prompt**: Midjourney v6 and DALL-E prompts with parameters and negatives.

### Proposed Code Changes
- Provide the structured JSON output as a fenced code block following the schema below:

'''json
{
  "project_meta": {
    "title_hypothesis": "Generated title for the sequence",
    "total_scenes_detected": 0,
    "input_resolution_est": "1080p/4K/Vertical",
    "holistic_meta_analysis": "Unified cinematic interpretation across all scenes"
  },
  "timeline_analysis": [
    {
      "scene_index": 1,
      "time_stamp_approx": "00:00 - 00:XX",
      "visual_summary": "Precise visual description of action and setting",
      "perspectives": {
        "forensic_analyst": {
          "ocr_text_detected": [],
          "detected_objects": [],
          "subject_identification": "",
          "technical_metadata_hypothesis": ""
        },
        "director": {
          "dramatic_structure": "",
          "story_placement": "",
          "micro_beats_and_emotion": "",
          "subtext_semiotics": "",
          "narrative_composition": ""
        },
        "cinematographer": {
          "framing_and_lensing": "",
          "lighting_design": "",
          "color_palette_hex": [],
          "optical_characteristics": "",
          "camera_movement": ""
        },
        "production_designer": {
          "set_design_architecture": "",
          "props_and_decor": "",
          "costume_and_styling": "",
          "material_physics": "",
          "atmospherics": ""
        },
        "editor": {
          "rhythm_and_tempo": "",
          "transition_logic": "",
          "visual_anchor_points": "",
          "cutting_strategy": ""
        },
        "sound_designer": {
          "ambient_sounds": "",
          "foley_requirements": "",
          "musical_atmosphere": "",
          "spatial_audio_map": ""
        },
        "ai_generation_data": {
          "midjourney_v6_prompt": "",
          "dalle_prompt": "",
          "negative_prompt": ""
        }
      }
    }
  ]
}
'''

### Commands
- No external commands required; analysis is performed directly on provided visual input.

## Quality Assurance Task Checklist

Before finalizing, verify:
- [ ] Every distinct scene or shot has been segmented and analyzed independently without merging.
- [ ] All six analysis perspectives (forensic, director, cinematographer, production designer, editor, sound designer) are completed for every scene.
- [ ] OCR text detection has been attempted on all visible text surfaces with best-guess transcription for degraded text.
- [ ] Object inventory includes specific counts, conditions, and identifications rather than generic descriptions.
- [ ] Color palette includes concrete HEX codes extracted from dominant and accent colors in each scene.
- [ ] Lighting design maps key, fill, and backlight positions with color temperature and contrast ratio estimates.
- [ ] Camera metadata hypothesis cites specific optical evidence supporting the identification.
- [ ] AI generation prompts are syntactically valid for Midjourney v6 and DALL-E with appropriate parameters and negative prompts.
- [ ] Structured JSON output conforms to the specified schema with all required fields populated.

## Execution Reminders

Good visual media analysis:
- Treats every frame as a forensic evidence surface, cataloging details rather than summarizing impressions.
- Segments multi-shot video inputs into individual scenes, never merging distinct shots into generalized summaries.
- Provides machine-precise specifications (HEX codes, focal lengths, Kelvin values, contrast ratios) rather than subjective adjectives.
- Synthesizes all six analytical perspectives into a coherent interpretation that reveals meaning beyond surface content.
- Generates AI prompts that could faithfully reproduce the visual qualities of the analyzed scene.
- Maintains chronological ordering and structural integrity across all detected scenes in the timeline.

---
**RULE:** When using this prompt, you must create a file named `TODO_visual-media-analysis.md`. This file must contain the findings resulting from this research as checkable checkboxes that can be coded and tracked by an LLM.
```

</details>

<details><summary><b>Voice Cloning Scams Infographic</b></summary>

```text
SYSTEM:
You are an LLM prompt executor.

USER TASK:
Create a vertical 9:16 infographic for TikTok.

TITLE (ONLY ONE TITLE — display this at the top):
[Fraud Playbook: Voice Cloning Attacks (2026)]

LAYOUT (choose ONE):
[1-10 box]
Pick exactly one. Number boxes with circled numbers. Flow top-to-bottom.

CONTENT RULES:
Each box must include:
- 1 short subheading
- 2–4 bullet points (plain English, phone-readable)

Must include:
- At least 1 real-world example
- A final checklist/action box whenever possible

QUALITY GATES:
- Tone: professional, neutral, report-like.
- Specificity: include at least 1 concrete detail per box.
- No filler: avoid vague warnings.
- Evidence discipline: label uncertain claims as “unclear/contested.”
- No repetition. Clear and fast to read.

TEXT QUALITY REQUIREMENTS:
- Bullets max 10–12 words.
- Prefer 1-6 box for best readability.

FOOTER CREDIT (small/subtle at the bottom):
By SirCrypto

OUTPUT REQUIREMENT:
Return:
TITLE: [Fraud Playbook: Voice Cloning Attacks (2026)]
BOX 1: ...
...
FOOTER (small): By SirCrypto

Then follow the STYLE SPEC below exactly (DO NOT CHANGE it):

--- STYLE SPEC (DO NOT CHANGE) ---
{
  "layout_options": {
    "box_variants": ["1-2 box", "1-4 box", "1-6 box", "1-8 box", "1-10 box"],
    "remark": "Choose ONE box variant. Keep flow top-to-bottom. Number each box with circled numbers."
  },
  "footer_credit": {
    "text": "By SirCrypto",
    "placement": "Bottom center or bottom right",
    "size": "Small/subtle"
  },
  "style": {
    "name": "War Room Strategy Infographic",
    "description": "Mature command-briefing infographic: tactical labels, decisive callouts, clear hierarchy. Serious, professional."
  },
  "visual_foundation": {
    "surface": {
      "base": "Matte dark slate to charcoal background",
      "texture": "Subtle paper grain + faint chalk/marker smudge texture",
      "edges": "Content extends fully to edges, no border or frame",
      "feel": "Command briefing page on dark paper"
    },
    "overall_impression": "Command-center clarity—direct, credible, high-signal"
  },
  "illustration_style": {
    "line_quality": {
      "type": "Hand-drawn ink/chalk hybrid sketch aesthetic",
      "weight": "Medium strokes for main elements, thinner for details",
      "character": "Confident but imperfect—slight wobble that proves human touch",
      "edges": "Soft, not vector-crisp",
      "fills": "Loose hatching, gentle cross-hatching for shadows, never solid machine fills"
    },
    "icon_treatment": {
      "style": "Minimal tactical icons",
      "complexity": "Essential forms—readable at small sizes",
      "personality": "Professional and decisive, never cute",
      "consistency": "Same hand appears to have drawn everything"
    }
  },
  "color_philosophy": {
    "palette_character": {
      "mood": "Serious, tactical, focused",
      "saturation": "Low-to-medium",
      "harmony": "Muted complementary accents"
    },
    "primary_palette": {
      "ambers": "Muted amber for warnings and priority tags",
      "teals": "Soft teal for steps and logic",
      "off_whites": "Warm off-white ink for main text"
    },
    "color_application": {
      "fills": "Translucent washes behind boxes",
      "accents": "Marker highlight behind keywords (restrained)"
    }
  },
  "typography_integration": {
    "headline_style": {
      "appearance": "Bold hand-lettered feel, slightly uneven baseline",
      "weight": "Heavy, confident",
      "case": "Often uppercase",
      "color": "Warm off-white or muted amber"
    },
    "body_text": {
      "appearance": "Clean readable warm sans-serif",
      "spacing": "Generous"
    }
  },
  "layout_architecture": {
    "canvas": {
      "framing": "NO BORDER, NO FRAME",
      "boundary": "Full-bleed 9:16"
    },
    "structure": {
      "type": "Modular briefing grid",
      "sections": "Numbered boxes per chosen variant",
      "flow": "Top-to-bottom"
    },
    "visual_flow_devices": {
      "arrows": "Hand-drawn curved arrows",
      "connectors": "Dotted lines and braces"
    }
  },
  "technical_quality": {
    "resolution": "High-resolution for phone",
    "clarity": "All text readable",
    "balance": "Not crowded"
  },
  "avoid": [
    "ANY frame, border, or edge decoration",
    "Cute/cartoon characters",
    "Neon overload",
    "Text-dense paragraphs",
    "Sterile vector perfection"
  ]
}

make picture based on these
```

</details>

<details><summary><b>Warm Scene with Paper Figures</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "high",
    "dominant_palette": [
      "brown",
      "beige",
      "black",
      "white",
      "olive green"
    ]
  },
  "composition": {
    "camera_angle": "eye-level",
    "depth_of_field": "shallow",
    "focus": "Paper doll and origami raccoon",
    "framing": "The man's face and a desk lamp in the background frame the central scene with the paper figures on the table."
  },
  "description_short": "A man looks on with concentration at two small figures on a wooden desk: an origami raccoon and a paper doll of a boy holding an umbrella, both made from newspaper. A warm desk lamp illuminates the scene.",
  "environment": {
    "location_type": "indoor",
    "setting_details": "A dark wooden desk or table, likely in a study or workshop. The background is dimly lit, focusing attention on the tabletop scene.",
    "time_of_day": "evening",
    "weather": "artificial"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "top",
    "type": "artificial"
  },
  "mood": {
    "atmosphere": "Quiet creativity and whimsical storytelling",
    "emotional_tone": "calm"
  },
  "narrative_elements": {
    "character_interactions": "A creator is carefully arranging his creations, seemingly bringing a small, handcrafted world to life.",
    "environmental_storytelling": "The use of newspaper for the figures suggests that stories from the world are being reshaped into a new, personal narrative. The focused light creates an intimate stage for this story.",
    "implied_action": "The man is in the process of setting up a scene, perhaps about to play out a story with the doll and the raccoon."
  },
  "objects": [
    "paper doll",
    "paper umbrella",
    "origami raccoon",
    "hand",
    "wooden table",
    "desk lamp"
  ],
  "people": {
    "ages": [
      "adult"
    ],
    "clothing_style": "casual t-shirt",
    "count": "1",
    "genders": [
      "male"
    ]
  },
  "prompt": "A cinematic, warm-toned photograph of a man at his wooden desk, his face softly blurred in the background, intently focused on two small figures he has created. In the foreground, an origami raccoon and a charming paper doll boy holding an umbrella, both meticulously crafted from newspaper, stand on the table. The man's hand gently holds the doll, arranging a scene. The lighting is dramatic, cast from a single desk lamp, creating long shadows and highlighting the delicate paper textures. The mood is quiet, creative, and whimsical with a shallow depth of field.",
  "style": {
    "art_style": "realistic",
    "influences": [
      "cinematic",
      "still life"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "papercraft",
    "origami",
    "shallow depth of field",
    "bokeh",
    "warm lighting",
    "cinematic lighting",
    "handmade",
    "crafting",
    "storytelling",
    "selective focus"
  ],
  "use_case": "Stock imagery for themes of creativity, hobbies, craftsmanship, or storytelling.",
  "uuid": "7a01281d-b2e9-45b7-82ed-6d77862113ad"
}
```

</details>

<details><summary><b>Warm Studio Portrait</b></summary>

```text
BASE – Warm studio
Cinematic studio portrait of a Black man in his mid-40s, thick well-groomed full beard, dark smoked sunglasses with black frames, thin gold chain, short natural black hair, black oversized t-shirt, calm grounded expression, no smile. Neutral warm beige backdrop, soft directional key light from the left, subtle rim light. 85mm lens, f/2, medium close-up, eye-level. Black, cream and ochre palette with a touch of gold. Editorial, introspective, film grain.

A – Chiaroscuro
Dramatic chiaroscuro studio portrait of a Black man in his mid-40s, thick full beard, dark smoked sunglasses, thin gold chain, black t-shirt, calm intense presence. Pure black background, single hard key light from above-left, deep shadows, gold chain catching the light. 85mm, tight close-up, Rembrandt lighting, high contrast, film grain.

B – Mirror
Introspective studio portrait of a Black man in his mid-40s with thick beard and dark smoked sunglasses, thin gold chain, seated beside a large mirror, reflection slightly out of focus. Warm cream backdrop, soft window light. 50mm, medium shot, beige, black and ochre palette, editorial, subtle grain.

C – Black & white
Black and white editorial portrait of a Black man in his mid-40s, thick beard, dark sunglasses, thin chain, black cap, arms crossed, grounded posture, no smile. Light grey seamless backdrop, soft box lighting. 70mm, three-quarter angle, magazine cover aesthetic.

NEGATIVE: text, watermark, logo, blurry, deformed hands, extra fingers, distorted face, plastic skin, cartoonish, cropped head
```

</details>

<details><summary><b>Watercolor of a Kingfisher Diving</b></summary>

```text
A loose, expressive watercolor painting of a common kingfisher diving headfirst into a calm forest stream, in a wide landscape 16:9 composition on textured white watercolor paper. The bird is in the center of the frame, plunging almost vertically downward with its wings folded tight along its body: a brilliant cobalt and turquoise blue back and wings speckled with lighter blue, a rich rust-orange chest and belly, a small white patch at the neck, and a long dark dagger-like beak whose tip is just touching the water. Where the beak meets the surface, a burst of white splash and flying droplets rises, surrounded by concentric blue-grey ripples spreading across the water. In the upper left, a mossy olive-green branch reaches into the frame from the edge, with long slender drooping willow leaves hanging down the left side toward the water, the branch the bird has just left. On the right, a soft, blurry riverbank of green, teal, and yellow-green foliage washes is mirrored faintly in the stream. Wet-on-wet blooms, granulating pigment, loose drips and splatters, crisp details only on the bird and the splash, and the white of the paper left unpainted for highlights and as a soft vignette around the edges. Fresh, lively, natural mood. No text, no signature, no frame.
```

</details>

<details><summary><b>Web Design Consultant</b></summary>

```text
I want you to act as a web design consultant. I will provide you with details related to an organization needing assistance designing or redeveloping their website, and your role is to suggest the most suitable interface and features that can enhance user experience while also meeting the company's business goals. You should use your knowledge of UX/UI design principles, coding languages, website development tools etc., in order to develop a comprehensive plan for the project. My first request is "I need help creating an e-commerce site for selling jewelry."
```

</details>

<details><summary><b>Wednesday Inspired Gothic Cemetery Selfie</b></summary>

```text
This is a close-up selfie photo taken from a slightly low angle. The main focus is on a woman with a striking Wednesday Addams-inspired appearance. She looks directly into the camera with a serious, emotionless expression.

Pose:
The woman holds the camera with one arm extended, wearing a black sleeve (only the forearm and part of the arm are visible), taking a selfie. With her other hand, she holds a large bouquet of deep red roses wrapped in simple paper with a small amount of green foliage. A silver ring is visible on one finger. A severed human hand (Thing) rests on her shoulder, adding a creepy element to the look.

Outfit:
She wears a black dress with a deep V-neckline, with a white stand-up collar featuring sharp pointed edges visible underneath. The collar is decorated with a subtle silver necklace. The dress has long sleeves.

Hair & Makeup:
Her hair is parted in the middle and styled into two long classic braids falling over her chest. She wears gothic-style makeup: dark smoky eyes, precisely defined eyebrows, and deep burgundy, almost black lipstick. She wears large black cat-eye sunglasses that cover her eyes while emphasizing the shape of her face.

Lighting & Atmosphere:
Natural daylight, soft but bright enough to capture fine details. The lighting creates a gloomy yet stylish atmosphere. The combination of vivid red roses and black-and-white clothing against the cemetery background creates a strong visual contrast.

Background:
The scene takes place in an old cemetery. Behind the woman are large stone crypts, mausoleums, and various gravestones, some decorated with statues, such as an angel statue in the background on the left. Tall evergreen trees, such as thuja or cypress trees, grow between the gravestones. On the right in the background is a vintage black limousine or luxurious hearse-like car, with a man standing beside it wearing a black tuxedo and bow tie, resembling Lurch, the butler.

Mood:
The overall mood is darkly elegant, gothic, mysterious, with a touch of dark humor and modern “horror-chic” aesthetics.

Technical Details:
A modern digital photograph with extremely high clarity and realistic detail. The camera is positioned very close to the woman's face, creating an authentic selfie effect with slight perspective distortion around the edges of the frame. The background is softly blurred with natural bokeh while the cemetery and car remain recognizable.

Important: Do not change the facial features or identity from the reference image. Preserve the exact face, facial structure, eyes, nose, lips, and other distinctive features.

Format: 3:4
Quality: Ultra-realistic, high-quality, sharp 8K photograph, natural skin texture, no artificial or plastic AI look, shot on an iPhone 16 Pro.
```

</details>

<details><summary><b>Where the Kami Still Walk</b></summary>

```text
Ancient Japanese village at night, quiet and empty, deeply spiritual atmosphere. Traditional wooden houses lining a narrow stone street, wet from recent rain, reflecting soft warm paper lantern light. Low mist drifting slowly through the village, moving with intention, as if guided by an unseen presence. Paper lanterns glowing gently one by one, with no visible source of ignition. At the end of the street, an old moss-covered torii gate emerging from the fog. Behind it, a subtle sacred presence — no physical form, no face — only a soft, breathing glow within the mist, calm and ancient, watching without judgment, like a shintō kami. An old tree beside the path wrapped with a weathered shimenawa rope. Shide paper streamers moving slightly despite the still air. Footsteps visible on the wet stone ground, leading forward like a quiet ritual path. Mood of reverence, silence, and timelessness. The boundary between the visible world and the unseen feels thin and sacred. Cinematic composition with strong leading lines and deep perspective. Volumetric fog, soft natural light diffusion. Color palette of deep indigo blues, muted forest greens, and warm amber highlights. Photorealistic cinematic realism, ultra-detailed organic textures, natural imperfections, subtle asymmetry, atmospheric concept art, high resolution, 8K quality.

Negative prompt: anime, cartoon, illustration, horror, aggressive mood, monsters, demons, jump scare, modern buildings, neon lights, cyberpunk, city elements, text, watermark, logo, characters in foreground, sharp artificial lighting, oversaturated colors
```

</details>

<details><summary><b>Whimsical 3D Brand Miniatures</b></summary>

```text
3D chibi-style miniature concept store of ${Brand Name:Mc Donalds}, creatively designed with an exterior inspired by the brand's most iconic product or packaging (such as a giant ${Brand's core product:chicken bucket, hamburger, donut, roast duck}). The store features two floors with large glass windows clearly showcasing the cozy and finely decorated interior: {brand's primary color}-themed decor, warm lighting, and busy staff dressed in outfits matching the brand. Adorable tiny figures stroll or sit along the street, surrounded by benches, street lamps, and potted plants, creating a charming urban scene. Rendered in a miniature cityscape style using Cinema 4D, with a blind-box toy aesthetic, rich in details and realism, and bathed in soft lighting that evokes a relaxing afternoon atmosphere. --ar 2:3

Brand name: ${Brand Name:Mc Donalds}
```

</details>

<details><summary><b>Whispers in Light Trails</b></summary>

```text
{
  "title": "Whispers in Light Trails",
  "description": "A cinematic long-exposure capture of a 1950s noir scene, contrasting the stillness of a detective with the kinetic energy of a jazz club.",
  "prompt": "You will perform an image edit using the people from the provided photos as the main subjects. Preserve their core likeness. Transform Subject 1 (male) into a 1950s detective and Subject 2 (female) into an alluring jazz singer. Utilize a Long Exposure artistic style where time seems to bleed. Subject 1 sits perfectly still at a corner booth, sharp and focused, while Subject 2 leans in to whisper something, her movement captured as a graceful, ghostly blur. The background musicians and dancers are rendered as artistic streaks of light and motion, emphasizing the chaotic atmosphere around the pair's secret meeting.",
  "details": {
    "year": "1952",
    "genre": "Long Exposure",
    "location": "A cramped, smoke-filled basement jazz club with red leather booths and a small stage.",
    "lighting": [
      "Dim ambient candlelight",
      "Streaking stage spotlights in the background",
      "Soft highlights on faces"
    ],
    "camera_angle": "Eye-level close shot, centered composition in a 1:1 aspect ratio.",
    "emotion": [
      "Secretive",
      "Melancholic",
      "Intense"
    ],
    "color_palette": [
      "Deep amber",
      "shadowy charcoal",
      "vibrant crimson streaks",
      "neon blue"
    ],
    "atmosphere": [
      "Kinetic",
      "Hazy",
      "Dreamlike",
      "Noir"
    ],
    "environmental_elements": "Silky smooth trails of cigarette smoke, streaks of gold light from brass instruments in the background, blurred movement of the crowd.",
    "subject1": {
      "costume": "A textured grey trench coat, fedora hat, and a loosened tie.",
      "subject_expression": "Stoic and intense, eyes locked forward.",
      "subject_action": "Sitting perfectly motionless, holding a glass of whiskey."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "frozen action",
        "crisp background",
        "static smoke",
        "daylight"
      ],
      "exclude_styles": [
        "high speed photography",
        "cartoon",
        "vector art",
        "flat lighting"
      ],
      "exclude_colors": [
        "pastel pink",
        "bright green",
        "pure white"
      ],
      "exclude_objects": [
        "smartphones",
        "modern microphones",
        "digital watches"
      ]
    },
    "subject2": {
      "costume": "A sparkling sequined evening gown with long opera gloves.",
      "subject_expression": " seductive and urgent, though partially softened by motion blur.",
      "subject_action": "Leaning in quickly to whisper, creating a motion trail effect."
    }
  }
}
```

</details>

<details><summary><b>Whispers of Noir</b></summary>

```text
{
  "title": "Whispers of Noir",
  "description": "A gritty, cinematic portrait of a hard-boiled detective waiting for a lead in a hazy, underground jazz lounge.",
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. Preserve the core likeness. Transform Subject 1 (male) into a weary 1950s private investigator seated in a plush velvet booth within a smoke-filled jazz club. Render the image as an ultra-photorealistic movie still, utilizing cinematic lighting that emphasizes the texture of his skin and the swirling smoke around him. The image must be highly detailed, shot on Arri Alexa with a shallow depth of field to blur the band in the background, adhering to a 1:1 aspect ratio.",
  "details": {
    "year": "1954",
    "genre": "Cinematic Photorealism",
    "location": "The Blue Velvet Lounge, a subterranean club with mahogany walls and dim table lamps.",
    "lighting": [
      "Chiaroscuro",
      "Warm table lamp glow",
      "Cool blue backlighting from the stage",
      "Volumetric light beams through smoke"
    ],
    "camera_angle": "Eye-level medium close-up, focusing intensely on the subject's face.",
    "emotion": [
      "Suspicion",
      "World-weariness",
      "Focused"
    ],
    "color_palette": [
      "Whiskey amber",
      "Velvet red",
      "Deep shadow black",
      "Tobacco smoke grey"
    ],
    "atmosphere": [
      "Sultry",
      "Tense",
      "Claustrophobic",
      "Vintage"
    ],
    "environmental_elements": "Thick clouds of cigarette smoke hanging in the air, a crystal tumbler of amber liquid on the table, blurred silhouettes of musicians in the background.",
    "subject1": {
      "costume": "A textured charcoal trench coat over a rumpled suit, with a loose tie and a fedora tilted slightly forward.",
      "subject_expression": "A piercing, cynical gaze with narrowed eyes and a tight jaw.",
      "subject_action": "Resting one hand near a half-empty glass of whiskey, leaning slightly into the light."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "bright daylight",
        "modern technology",
        "cell phones",
        "neon signs",
        "clean air"
      ],
      "exclude_styles": [
        "cartoon",
        "3d render",
        "anime",
        "sketch",
        "painting"
      ],
      "exclude_colors": [
        "neon green",
        "hot pink",
        "pure white"
      ],
      "exclude_objects": [
        "cars",
        "digital watches",
        "second person"
      ]
    }
  }
}
```

</details>

<details><summary><b>White Church Above a Black Sand Beach</b></summary>

```text
A small white wooden church with a red gabled roof and a pointed red steeple stands on a rounded grassy green headland above an Icelandic black sand beach at golden hour, with dark basalt sea stacks rising from the ocean on the right. The church sits in the left third of the frame, near the top of the headland, its white walls and small windows lit warm gold by the low sun. The headland's grassy slope drops down to the beach, and a wide curve of fine black volcanic sand sweeps from the lower left corner across the foreground, wet and glossy near the water. White foamy surf rolls in from the right in several long lines and washes up the black sand. In the sea on the right half stand four dark basalt rocks: a low rounded rock near the end of the headland, a tall jagged sea stack in the center right, and two smaller pointed spires further right. The low sun sits near the horizon at the far left behind the headland, glowing yellow-orange, and the sky is filled with scattered clouds lit orange, pink, and purple against soft blue. Photoreal landscape photography, wide angle, natural colors, calm and dramatic mood. Wide landscape 16:9. No people, no text, no logos.
```

</details>

<details><summary><b>Whiteboard Sketch Diagrams</b></summary>

```text
Steps to build an AI startup by making something people want:

{
  "style": {
    "name": "Whiteboard Sketch Diagram",
    "description": "Transform any concept into an elegant hand-drawn diagram. Clean, minimal, architectural in feel—like a smart person's quick sketch on a whiteboard."
  },
  "core_philosophy": {
    "essence": "Elegant simplicity—the lightest possible touch that still communicates clearly",
    "mindset": "An architect or designer explaining an idea with a fine pen",
    "goal": "Clarity through restraint and refinement"
  },
  "visual_foundation": {
    "canvas_structure": {
      "outer_background": "#FFFFFF",
      "card": {
        "size": "95-98% of canvas—minimal white margin",
        "color": "#FEFEFE",
        "corner_radius": "12-16px subtle roundness",
        "shadow": "NONE",
        "border": "NONE"
      }
    },
    "overall_aesthetic": {
      "feel": "Light, airy, intellectual, refined",
      "weight": "Delicate—everything feels thin and elegant",
      "space": "Generous white space everywhere"
    }
  },
  "line_work": {
    "critical_principle": "THIN AND DELICATE—not bold, not heavy, not chunky",
    "quality": {
      "weight": "Fine, thin lines—like a 0.5mm pen or fine-tip marker",
      "character": "Architectural, precise but hand-drawn",
      "consistency": "Uniform thin weight throughout"
    },
    "stroke_style": {
      "lines": "Thin, clean, slightly imperfect",
      "corners": "Sharp or slightly rounded, never bulky",
      "feel": "Drawn quickly but skillfully"
    }
  },
  "color_palette": {
    "exact_colors": {
      "card_background": {
        "hex": "#FEFEFE",
        "description": "Almost white, flat, neutral"
      },
      "primary_text": {
        "hex": "#020202",
        "description": "Near-black for text—crisp and readable"
      },
      "line_gray": {
        "hex": "#4A4B4B",
        "description": "Dark gray for all drawn lines, boxes, shapes—NOT pure black"
      },
      "accent_blue": {
        "hex": "#2C68B7",
        "description": "Clear medium blue—for arrows, connectors, brackets, some labels"
      },
      "accent_red": {
        "hex": "#B34952",
        "description": "Warm coral-red—for category labels, emphasis text"
      },
      "fill_blue": {
        "hex": "#2C68B7",
        "description": "Same blue for small filled squares/shapes"
      },
      "fill_gray": {
        "hex": "#4A4B4B",
        "description": "Dark gray for filled grid cells"
      }
    },
    "usage": {
      "text": "Primary text in #020202 black, categories in #E54B54 red",
      "lines_and_shapes": "All outlines in #4A4B4B gray—NOT black",
      "arrows_and_flow": "#2C68B7 blue—thin and elegant",
      "fills": "Small filled squares in blue or gray—never large solid areas"
    }
  },
  "typography": {
    "style": {
      "type": "Elegant italic handwriting",
      "weight": "Light to medium—never bold or heavy",
      "slant": "Natural italic lean",
      "character": "Fluid, intelligent, like architect's lettering"
    },
    "colors": {
      "titles": "#020202 black, italic",
      "category_labels": "#E54B54 red",
      "annotations": "#2C68B7 blue or #020202 black"
    }
  },
  "diagram_elements": {
    "boxes_and_rectangles": {
      "stroke": "THIN #4A4B4B gray outline—1-2px weight max",
      "fill": "Empty/transparent—never solid filled large boxes",
      "corners": "Slightly rounded or sharp, hand-drawn",
      "style": "Light, airy, not heavy containers"
    },
    "grids_and_matrices": {
      "stroke": "Thin gray lines",
      "cells": "Small—may contain small filled squares or numbers",
      "fills": "Small squares filled blue or gray to show data"
    },
    "arrows": {
      "critical": "THIN, ELEGANT, SIMPLE—not chunky PowerPoint arrows",
      "stroke": "Thin #2C68B7 blue line—same weight as other lines",
      "heads": "Small, simple, minimal—just two short angled lines forming a point",
      "style": "Like hand-drawn with a fine pen, not a thick marker",
      "types": [
        "Simple thin straight arrows",
        "Thin curved arrows for flow",
        "Never: block arrows, 3D arrows, gradient arrows, thick arrows"
      ]
    },
    "brackets": {
      "style": "Thin hand-drawn curly braces in blue",
      "weight": "Same thin line weight as everything else"
    },
    "dots_and_markers": {
      "style": "Small filled circles or squares",
      "size": "Tiny—proportional to the thin line aesthetic",
      "colors": "Blue or red for emphasis"
    }
  },
  "visual_language": {
    "shapes_vocabulary": {
      "rectangles": "Thin outlined boxes—vertical or horizontal orientation",
      "grids": "Small matrices with tiny filled cells",
      "lists": "Simple dashed or bulleted items inside boxes",
      "flow": "Thin arrows connecting elements left-to-right"
    },
    "composition_patterns": {
      "typical_layout": "2-4 main elements arranged horizontally with arrows between",
      "spacing": "Generous gaps between elements",
      "alignment": "Rough but intentional alignment",
      "hierarchy": "Titles above boxes, labels below or beside"
    },
    "proportions": {
      "line_weight_to_space": "Very thin lines in very open space",
      "text_to_diagram": "Text is secondary, diagram dominates",
      "fill_to_empty": "Mostly empty, fills are small accents"
    }
  },
  "elegance_principles": {
    "lightness": "Everything should feel like it could float away",
    "restraint": "Use the minimum to communicate the idea",
    "refinement": "Quality of line over quantity of elements",
    "intelligence": "Looks like a smart person drew it quickly",
    "breathing": "White space is as important as the marks"
  },
  "avoid": [
    "Thick, heavy, bold lines",
    "Chunky PowerPoint-style arrows",
    "Block arrows or 3D arrows",
    "Large solid filled areas",
    "Dense, cluttered layouts",
    "Bold or heavy typography",
    "Drop shadows or gradients",
    "Corporate clip-art aesthetic",
    "Rounded bubble shapes",
    "Any line weight that feels 'heavy'",
    "Pure black (#000000) for lines—use #4A4B4B gray",
    "Decorative elements",
    "Overly complex diagrams"
  ]
}
```

</details>

<details><summary><b>Whiteboard Style Infographic</b></summary>

```text
explain the thinking fast and slow book

{
  "style": {
    "name": "Whiteboard Infographic",
    "description": "Hand-illustrated educational infographic with a warm, approachable sketch aesthetic. Upload your content outline and receive a visually organized, sketchbook-style guide that feels hand-crafted yet professionally structured."
  },
  "visual_foundation": {
    "surface": {
      "base": "Off-white to warm cream background",
      "texture": "Subtle paper grain—not sterile, not digital",
      "edges": "Content extends fully to edges, no border or frame, seamless finish",
      "feel": "Like looking directly at a well-organized notebook page"
    },
    "overall_impression": "Approachable expertise—complex information made friendly through hand-drawn warmth"
  },
  "illustration_style": {
    "line_quality": {
      "type": "Hand-drawn ink sketch aesthetic",
      "weight": "Medium strokes for main elements, thinner for details",
      "character": "Confident but imperfect—slight wobble that proves human touch",
      "edges": "Soft, not vector-crisp, occasional line overlap at corners",
      "fills": "Loose hatching, gentle cross-hatching for shadows, never solid machine fills"
    },
    "icon_treatment": {
      "style": "Simple, charming, slightly naive illustration",
      "complexity": "Reduced to essential forms—readable at small sizes",
      "personality": "Friendly and approachable, never corporate or sterile",
      "consistency": "Same hand appears to have drawn everything"
    },
    "human_figures": {
      "style": "Simple friendly characters, not anatomically detailed",
      "faces": "Minimal features—dots for eyes, simple expressions",
      "poses": "Clear, action-oriented, communicative gestures",
      "diversity": "Varied silhouettes and suggestions of different people"
    },
    "objects_and_scenes": {
      "approach": "Recognizable simplified sketches",
      "detail_level": "Just enough to identify—laptop, phone, building, person",
      "perspective": "Casual isometric or flat, not strict technical drawing",
      "charm": "Slight imperfections add authenticity"
    }
  },
  "color_philosophy": {
    "palette_character": {
      "mood": "Warm, optimistic, energetic but not overwhelming",
      "saturation": "Medium—vibrant enough to guide the eye, soft enough to feel hand-colored",
      "harmony": "Complementary and analogous combinations that feel intentional"
    },
    "primary_palette": {
      "yellows": "Warm golden yellow, soft mustard—for highlights, backgrounds, energy",
      "greens": "Fresh leaf green, soft teal—for success, growth, nature, money themes",
      "blues": "Calm sky blue, soft navy—for trust, technology, stability",
      "oranges": "Warm coral, soft peach—for warmth, calls-to-action, friendly alerts"
    },
    "supporting_palette": {
      "neutrals": "Warm grays, soft browns, cream—never cold or stark",
      "blacks": "Soft charcoal for lines, never pure #000000",
      "whites": "Cream and off-white, paper-toned"
    },
    "color_application": {
      "fills": "Watercolor-like washes, slightly uneven, transparent layers",
      "backgrounds": "Soft color blocks to section content, gentle rounded rectangles",
      "accents": "Strategic pops of brighter color to guide hierarchy",
      "technique": "Colors may slightly escape line boundaries—hand-colored feel"
    }
  },
  "typography_integration": {
    "headline_style": {
      "appearance": "Bold hand-lettered feel, slightly uneven baseline",
      "weight": "Heavy, confident, attention-grabbing",
      "case": "Often uppercase for major headers",
      "color": "Dark charcoal or strategic color for emphasis"
    },
    "subheadings": {
      "appearance": "Medium weight, still hand-drawn character",
      "decoration": "May include underlines, simple banners, or highlight boxes",
      "hierarchy": "Clear size reduction from headlines"
    },
    "body_text": {
      "appearance": "Clean but warm, readable at smaller sizes",
      "style": "Sans-serif with hand-written personality, or actual handwriting font",
      "spacing": "Generous, never cramped"
    },
    "annotations": {
      "style": "Casual handwritten notes, arrows pointing to elements",
      "purpose": "Add explanation, emphasis, or personality",
      "placement": "Organic, as if added while explaining"
    }
  },
  "layout_architecture": {
    "canvas": {
      "framing": "NO BORDER, NO FRAME, NO EDGE DECORATION",
      "boundary": "Content uses full canvas—elements may touch or bleed to edges",
      "containment": "The infographic IS the image, not an image of an infographic"
    },
    "structure": {
      "type": "Modular grid with organic flexibility",
      "sections": "Clear numbered or lettered divisions",
      "flow": "Left-to-right, top-to-bottom with visual hierarchy guiding the eye",
      "breathing_room": "Generous white space preventing overwhelm"
    },
    "section_treatment": {
      "borders": "Soft rounded rectangles, hand-drawn boxes, or color-blocked backgrounds",
      "separation": "Clear but not rigid—sections feel connected yet distinct",
      "numbering": "Circled numbers, badges, or playful indicators"
    },
    "visual_flow_devices": {
      "arrows": "Hand-drawn, slightly curved, friendly pointers",
      "connectors": "Dotted lines, simple paths showing relationships",
      "progression": "Before/after layouts, step sequences, transformation arrows"
    }
  },
  "information_hierarchy": {
    "levels": {
      "primary": "Large bold headers, bright color accents, main illustrations",
      "secondary": "Subheadings, key icons, section backgrounds",
      "tertiary": "Body text, supporting details, annotations",
      "ambient": "Texture, subtle decorations, background elements"
    },
    "emphasis_techniques": {
      "color_highlights": "Yellow marker-style highlighting behind key words",
      "size_contrast": "Significant scale difference between hierarchy levels",
      "boxing": "Important items in rounded rectangles or badge shapes",
      "icons": "Checkmarks, stars, exclamation points for emphasis"
    }
  },
  "decorative_elements": {
    "badges_and_labels": {
      "style": "Ribbon banners, circular badges, tag shapes",
      "use": "Section labels, key terms, calls-to-action",
      "character": "Hand-drawn, slightly imperfect, charming"
    },
    "connective_tissue": {
      "arrows": "Curved, hand-drawn, with various head styles",
      "lines": "Dotted paths, simple dividers, underlines",
      "brackets": "Curly braces grouping related items"
    },
    "ambient_details": {
      "small_icons": "Stars, checkmarks, bullets, sparkles",
      "doodles": "Tiny relevant sketches filling awkward spaces",
      "texture": "Subtle paper grain throughout"
    }
  },
  "authenticity_markers": {
    "hand_made_quality": {
      "line_variation": "Natural thickness changes as if drawn with real pen pressure",
      "color_bleeds": "Slight overflow past lines, watercolor-style edges",
      "alignment": "Intentionally imperfect—text and elements slightly off-grid",
      "overlap": "Elements may slightly overlap, creating depth and energy"
    },
    "material_honesty": {
      "paper_feel": "Warm off-white with subtle texture",
      "ink_quality": "Soft charcoal blacks, never harsh",
      "marker_fills": "Slightly streaky, transparent layers visible"
    },
    "human_evidence": {
      "corrections": "Occasional visible rework adds authenticity",
      "spontaneity": "Some elements feel added as afterthoughts—annotations, small arrows",
      "personality": "The whole piece feels like one person's visual thinking"
    }
  },
  "technical_quality": {
    "resolution": "High-resolution output suitable for print and digital",
    "clarity": "All text readable, all icons recognizable",
    "balance": "Visual weight distributed evenly across the composition",
    "completeness": "Feels finished but not overworked—confident stopping point"
  },
  "enhancements_beyond_reference": {
    "depth_additions": {
      "subtle_shadows": "Soft drop shadows under section boxes for lift",
      "layering": "Overlapping elements creating visual depth",
      "dimension": "Slight 3D feel on badges and key elements"
    },
    "polish_improvements": {
      "color_harmony": "More intentional palette relationships",
      "spacing_rhythm": "Consistent margins and gutters",
      "hierarchy_clarity": "Stronger differentiation between content levels"
    },
    "engagement_boosters": {
      "focal_points": "Clear visual anchors drawing the eye",
      "progression": "Satisfying visual journey through the content",
      "reward_details": "Small delightful discoveries upon closer inspection"
    }
  },
  "avoid": [
    "ANY frame, border, or edge decoration around the infographic",
    "Wooden frame or whiteboard frame effect",
    "Drop shadow around the entire image as if it's a photo of something",
    "The image looking like a photograph of a poster—it IS the poster",
    "Sterile vector perfection—this should feel hand-made",
    "Cold pure whites or harsh blacks",
    "Rigid mechanical grid alignment",
    "Corporate clip-art aesthetic",
    "Overwhelming detail density—let it breathe",
    "Clashing neon or garish color combinations",
    "Uniform line weights throughout",
    "Perfectly even color fills",
    "Stiff, lifeless human figures",
    "Digital sharpness that kills the warmth",
    "Inconsistent illustration styles within the piece",
    "Text-heavy sections without visual relief"
  ]
}
```

</details>

<details><summary><b>Wicker Chair on a Mediterranean Balcony</b></summary>

```text
{
  "meta": {
    "type": "image_analysis",
    "file_name": "image_5e33ac.jpg",
    "analyst_persona": "Technical Photo Analyst"
  },
  "scene_environment": {
    "location_type": "Outdoor",
    "setting": "Balcony or patio of a Mediterranean-style resort or villa.",
    "architectural_style": "Whitewashed stucco walls, terracotta roof tiles, wooden beams, wrought iron railings.",
    "atmosphere": "Sunny, relaxed, vacation vibe, warm summer day."
  },
  "technical_aspects": {
    "camera_lens": "Wide-angle lens (approx. 24-35mm equivalent), typical of high-end smartphone main cameras.",
    "camera_angle": "Eye-level relative to the seated subject, slightly looking down.",
    "depth_of_field": "Deep depth of field; both the subject and the background architecture are relatively sharp.",
    "focus": "Sharp focus on the subject's face and torso."
  },
  "lighting": {
    "condition": "High contrast, hard daylight.",
    "sources": [
      {
        "source_id": "light_1",
        "type": "Natural Sun",
        "angle": "Coming from high up, slightly to the subject's right (viewer's left).",
        "color": "Warm white (approx. 5500K).",
        "intensity": "High/Harsh.",
        "effect_on_objects": "Creates distinct, sharp shadows behind the subject and under the architectural beams. Illuminates the white walls brightly."
      }
    ],
    "light_on_body_parts": {
      "face": "Fully illuminated, slight shadow under the nose and chin.",
      "chest_neck": "Direct sunlight, highlighting skin texture and redness/sunburn.",
      "arms": "Right arm (holding cigarette) is fully lit. Left arm has shadows on the underside.",
      "legs": "Thighs are illuminated, with the inner thigh area in shadow due to crossed legs.",
      "shadows": "Hard shadow cast by the subject onto the left side of the chair."
    }
  },
  "subject": {
    "general": {
      "gender": "Female",
      "orientation": "Frontal facing, slightly angled to the right.",
      "gaze": "Direct eye contact with the camera/viewer.",
      "expression": "Subtle smile, relaxed, confident, slightly smug or contented.",
      "emotional_state": "Calm, leisure, unbothered.",
      "sensuality_index": "Moderate; implies casual allure through confident pose and exposed skin, but not explicitly provocative."
    },
    "pose_and_posture": {
      "type": "Seated, relaxed.",
      "head": "Tilted slightly to her left.",
      "torso": "Leaning back slightly into the chair, relaxed posture.",
      "arms": {
        "right_arm": "Extended outwards, resting on the air/knee level, hand holding a cigarette.",
        "left_arm": "Resting on the armrest of the wicker chair.",
        "visibility": "Full arms visible."
      },
      "legs": {
        "position": "Crossed at the thighs (Right leg over Left leg).",
        "knees": "Right knee is the closest point to the camera.",
        "feet": "Cut off from the frame/not visible."
      },
      "visible_extent": "Full body visible from mid-shin upwards."
    },
    "head_details": {
      "hair": {
        "color": "Blonde with darker natural roots showing.",
        "style": "Long, straight, center-parted, framing the face.",
        "texture": "Fine, smooth."
      },
      "face": {
        "structure": "Oval/Heart-shaped.",
        "forehead": "Standard height, partially covered by face-framing hair strands.",
        "brows": "Natural arch, medium thickness, groomed.",
        "eyes": "Almond shape, dark eye makeup/liner visible.",
        "nose": "Button nose, soft features.",
        "mouth": "Closed lips, slight upward curve (smile), natural lip color with gloss.",
        "chin": "Soft, rounded.",
        "skin": "Fair complexion, smooth texture."
      }
    },
    "body_details": {
      "skin_tone": "Fair/White. Noticeable redness (sunburn) on the décolletage/chest area.",
      "neck": "Visible, adorned with a necklace.",
      "shoulders": "Relaxed, slightly slumped forward in a casual manner.",
      "chest_area": {
        "ratio_to_body": "Proportional.",
        "estimated_size": "Average/Moderate.",
        "bra_status": "Likely no bra or a soft bralette due to the dress style (spaghetti straps).",
        "nipple_visibility": "Not prominent.",
        "visual_impact": "Natural shape under the fabric."
      },
      "midsection": {
        "ratio": "Standard, slightly compressed due to seated position.",
        "visibility": "Concealed by the dress, but form is discernible.",
        "definition": "Soft."
      },
      "hips_and_thighs": {
        "hips_ratio": "Appears wider than bust due to seated compression.",
        "thighs": "Full, taking up the lower foreground.",
        "legs_texture": "Smooth skin, no visible blemishes."
      }
    },
    "clothing": {
      "type": "Mini Dress / Slip Dress.",
      "pattern": "Dark green background with a black paisley or floral pattern.",
      "style": "Spaghetti straps, gathered neckline with a small tie string in the center.",
      "fit": "Form-fitting but not skin-tight.",
      "material": "Likely satin or a synthetic blend that drapes softly."
    },
    "accessories": {
      "neck": "Gold chain necklace with a rectangular pendant.",
      "wrist": "None visible.",
      "fingers": "Cigarette in right hand."
    }
  },
  "objects_in_scene": [
    {
      "object": "Wicker Armchair",
      "description": "Dark brown, woven texture, boxy shape.",
      "purpose": "Subject's seat.",
      "location": "Center frame.",
      "contribution": "Adds texture and contrast to the fair skin of the subject."
    },
    {
      "object": "Cigarette",
      "description": "Lit cigarette, holding ash.",
      "location": "Held in subject's right hand.",
      "contribution": "Adds a rebellious or casual 'snapshot' narrative."
    },
    {
      "object": "Flowers",
      "description": "Pink geraniums or similar bedding plants.",
      "location": "Left side, in a planter box.",
      "color": "Vibrant pink.",
      "contribution": "Adds a pop of color."
    },
    {
      "object": "Palm Trees",
      "description": "Tall trunks with green fronds.",
      "location": "Upper right background.",
      "contribution": "Establishes the tropical/Mediterranean setting."
    },
    {
      "object": "Buildings",
      "description": "White stucco multistory buildings.",
      "location": "Background.",
      "contribution": "Contextualizes the location as a resort or residential complex."
    }
  ],
  "negative_prompt": "deformed, distorted, disfigured, poorly drawn, bad anatomy, wrong anatomy, extra limb, missing limb, floating limbs, disconnected limbs, mutation, mutated, ugly, disgusting, blurry, amputation, low quality, bad lighting, monochrome, watermark, text, signature, illustration, painting, 3d render, anime."
}
```

</details>

<details><summary><b>Wild West Gunslinger Transformation</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. The face must remain clear and unaltered. Transform the subject into a steely-eyed **Wild West Gunslinger/Outlaw**, standing tall on the dusty main street of a frontier town at sunset, hand hovering near their holster. Emphasize rugged textures, warm golden light, a tense atmosphere, and classic Western details.",
  "details": {
    "year": "Late 19th Century (American Frontier / Wild West Era)",
    "genre": "Western / Period Piece / Action / Americana",
    "location": "The wide, dusty main street of a wooden frontier town. Weathered buildings with false fronts (saloon, general store) line the street. The sun is setting behind them, casting long shadows. Dust hangs in the air. Tumbleweeds are optional but welcomed.",
    "lighting": "Dramatic 'Golden Hour' sunset. Warm, low-angle light from the setting sun backlights the subject and the dust, creating a golden haze and strong rim lighting. Long, dramatic shadows stretch across the street. The overall tone is warm and gritty.",
    "camera_angle": "Full-body shot, slightly low-angle, looking up at the subject to emphasize their imposing presence. The composition is centered, with the town street stretching behind them, creating depth. (1:1 composition).",
    "emotion": "Tense, confident, watchful, and ready for action.",
    "costume": "Rugged, worn Western attire: a long, dusty canvas or leather duster coat, a worn cowboy hat pulled slightly low, a patterned shirt, a leather vest, and sturdy, scuffed cowboy boots. A thick leather gun belt with a holster holding a period-appropriate revolver is prominent. A bandana is tied around the neck.",
    "color_palette": "Dominated by warm, earthy tones: dusty browns, burnt oranges, deep reds, and golden yellows from the sunset. The wood of the buildings is weathered gray and brown. The sky is a gradient of fiery orange, pink, and deep blue.",
    "atmosphere": "Tense, gritty, cinematic, and quiet. The air is thick with dust and anticipation, as if a duel is about to commence. A classic Western standoff feel.",
    "subject_expression": "A steely, unwavering gaze looking directly forward from beneath the hat brim. A firm, set jaw. The expression is calm but intensely focused, conveying a sense of dangerous capability.",
    "subject_action": "Standing with feet planted firmly apart, body slightly bladed. One hand is hovering just above the grip of their holstered revolver, fingers ready to draw. The other hand might be resting on their belt or hanging loosely at their side.",
    "environmental_elements": "Visible dust motes catching the golden light. The silhouette of a horse hitched to a rail in the background. A wooden sign for a saloon (e.g., 'Golden Nugget Saloon') is visible but slightly out of focus. The texture of rough wood and dry earth is palpable."
  }
}
```

</details>

<details><summary><b>Wings of the Dust Bowl</b></summary>

```text
{
  "title": "Wings of the Dust Bowl",
  "description": "A daring 1930s female aviator stands confident on a wind-swept airfield at sunset, ready to cross the Atlantic.",
  "prompt": "You will perform an image edit using the provided photo to create a frame worthy of a historical epic. Transform the female subject into a pioneer aviator from the 1930s. The image must be photorealistic, utilizing cinematic lighting to highlight the texture of weather-beaten leather and skin pores. The scene is highly detailed, shot on Arri Alexa with a shallow depth of field to blur the vintage biplane in the background. The composition focuses on realistic physics, from the wind catching her scarf to the oil smudges on her cheek.",
  "details": {
    "year": "1933",
    "genre": "Cinematic Photorealism",
    "location": "A dusty, remote airfield in the Midwest with the blurred metallic nose of a vintage propeller plane in the background.",
    "lighting": [
      "Golden hour sunset",
      "Strong rim lighting",
      "Volumetric light rays through dust",
      "High contrast warm tones"
    ],
    "camera_angle": "Eye-level close-up shot using an 85mm portrait lens.",
    "emotion": [
      "Determined",
      "Adventurous",
      "Confident"
    ],
    "color_palette": [
      "Burnt orange",
      "Leather brown",
      "Metallic silver",
      "Sunset gold",
      "Sepia"
    ],
    "atmosphere": [
      "Nostalgic",
      "Gritty",
      "Windy",
      "Epic"
    ],
    "environmental_elements": "Swirling dust particles caught in the light, a spinning propeller motion blur in the distance, tall dry grass blowing in the wind.",
    "subject1": {
      "costume": "A distressed vintage brown leather bomber jacket with a shearling collar, a white silk aviator scarf blowing in the wind, and brass flight goggles resting on her forehead.",
      "subject_expression": "A subtle, confident smirk with eyes squinting slightly against the setting sun.",
      "subject_action": "Adjusting a leather glove on her hand while gazing toward the horizon."
    },
    "negative_prompt": {
      "exclude_visuals": [
        "modern jets",
        "paved runway",
        "smartphones",
        "digital watches",
        "clear blue sky",
        "plastic textures"
      ],
      "exclude_styles": [
        "cartoon",
        "3D render",
        "anime",
        "painting",
        "sketch",
        "black and white"
      ],
      "exclude_colors": [
        "neon green",
        "electric blue",
        "hot pink"
      ],
      "exclude_objects": [
        "modern buildings",
        "cars"
      ]
    }
  }
}
```

</details>

<details><summary><b>Woman and Cat on a Night Street</b></summary>

```text
image-generation:
  main: "An 1980s-style woman walking with a cat beside her, both in the foreground."
  clothes: "worn jacket, blanket and old pants."
  faces: "Not visible or turned away"

  environment:
    streets: "Tree-lined, single-story houses, dead-end street."
    time: "Nightfall"
    atmosphere: "Rainy, cloudy"
  
  techniques:
    style: "Photorealistic, like captured by a real camera"
    focus: "Shallow depth of field, bokeh and rim lighting"
    light: "subject is well-lit, background is cold"
    colors: "background is blue and focus is red"
  
  composition:
    type: "Wide shot landscape"
    background: "Woodlands, lawns, gardens."
  
  mood:
    - "Depressive"
    - "Tearful"
  
  negative:
    - "HDR"
    - "Sketch"
    - "Black white"
    - "Low Resolution"
    - "Cloudy"
```

</details>

<details><summary><b>Woman with Glasses in a Field</b></summary>

```text
Subject: A young woman with voluminous, textured hair.
Pose and Action: She is standing in a three-quarter profile, turning her face to the right of the camera. Her left hand, in the foreground, is raised with her fingers gently buried in the roots of her hair as if adjusting it, creating volume and a dynamic, effortless pose. Her head is slightly tilted.
Facial Details: The woman is wearing large, round, dark sunglasses with a thin metal frame that completely cover her eyes. Her face is turned to the right, with her gaze directed beyond the frame. She has a defined chin and jawline. Do not change her facial features or identity. Preserve 100% facial resemblance. She has a cute, naturally attractive face.
Makeup: Soft matte lipstick in a natural pink-nude shade. Flawless skin with a subtle natural glow. The makeup is natural and understated, with the sunglasses as the main accent.
Hairstyle: voluminous, wavy hair falling freely over her shoulders and back. The hair looks full and textured, especially where her hand is immersed in it.
Clothing: She is wearing a textured wool or corduroy jacket or coat in a dark olive-green or dark brown shade.
Lighting: Natural, warm, diffused golden-hour sunlight at sunset. The soft light gently illuminates the hair, creating subtle highlights and soft shadows on the face while emphasizing texture and volume.
Atmosphere and Mood: Cozy, autumnal, relaxed, and stylish. The mood is thoughtful, confident, effortless, and slightly mysterious due to the sunglasses.
Background: Strongly defocused background with a soft bokeh effect, creating the feeling of being outdoors in autumn. Blurred outlines of dry golden grass, dark tree trunks, and soft autumn tones of yellow, brown, and green can be seen.
Camera Angle and Composition: Mid-shot, framed from the chest up, photographed at the subject's eye level. Dynamic composition with emphasis on the raised hand and the movement of the hair. Sharp focus on the face and raised hand.
Aspect ratio: 3:4.
Ultra-realistic, high-quality, sharp 8K photo, captured on an iPhone 16 Pro Max.
```

</details>

<details><summary><b>World Landmarks 3D Dioramas</b></summary>

```text
Create a hyper-realistic 3D diorama-style model of ${Landmark Name:EIFFEL TOWER}. The model should appear as a miniature, set on a raised cross-section of earth that reveals soil and rock layers beneath a lush grassy surface. The structure must be highly detailed and proportionally accurate, surrounded by tiny realistic elements like region-appropriate street lamps, native trees, shrubs, water features like small fountains, and historically or culturally fitting pathways. The scene should evoke the unique character of ${Landmark Name:EIFFEL TOWER}’s surrounding landscape. The environment must include a soft white background to draw full attention to the model. Include the text “${Landmark Name:EIFFEL TOWER}” in large, bold, elegant lettering prominently displayed on a big sign or billboard at the front of the diorama, easily readable and eye-catching, along with a large national flag on a tall, prominent flagpole positioned beside ${Landmark Name:EIFFEL TOWER}, clearly visible and waving. 1080x1080 dimension
```

</details>

<details><summary><b>World of Darkness B&W Style</b></summary>

```text
${subject} rendered in harsh, angular World of Darkness comic-book linework. Heavy black inks dominate the image, with thick contour lines, aggressive cross-hatching, and deep shadow blocks carving the form into sharp anatomical planes. Anatomy exaggerated and expressive, posture tense and confrontational. Surfaces broken into stark light-versus-dark geometry. Background abstracted or urban-gothic, fragmented and oppressive. Lighting stark and noir-inspired, extreme contrast with hard rim light defining edges and silhouettes. Composition tight and intimate, low or confrontational camera angle. Overall tone: modern gothic horror, raw, feral, and spiritually charged.
```

</details>

<details><summary><b>World of Darkness Colored Comic Style</b></summary>

```text
${subject} rendered in the distinctive colored World of Darkness comic style used in classic Werewolf books. Heavy black inks remain the structural backbone—thick contour lines, aggressive cross-hatching, deep shadow blocks—overlaid with saturated, moody color washes. Color applied in layered, expressive fields rather than realism, shifting across form to suggest emotion and supernatural presence. Highlights sharp and metallic, selectively catching edges, eyes, weapons, or key features. Background painted in a gritty WoD palette of sickly yellows, rusted reds, bruised purples, and cold violets. Colors bleed slightly outside ink boundaries, creating chaotic, feral energy. Texture rough, painterly, and grim. Composition confrontational and intimate. Tone: urban gothic horror, animistic power, menace restrained just beneath the surface.
```

</details>

<details><summary><b>Xiongnu Warriors at Sunset</b></summary>

```text
Xiongnu warriors on horses, central asian steppe, 5th century, dramatic sunset, volumetric lighting, hyper-realistic, 8k.
```

</details>

<details><summary><b>Y2K Cheshire Cat Snapshot</b></summary>

```text
A young woman with long wavy dark brown hair, wearing a Cheshire Cat Halloween costume: shiny purple cat ears headband, off-shoulder long-sleeve top with horizontal purple and hot pink stripes, shiny purple satin corset with front buttons, purple and hot pink horizontally striped tights, and fluffy faux fur leg warmers in deep purple and hot pink. Her makeup features purple eyeshadow, dramatic eyeliner, glitter on cheeks and forehead with a lavender tint, and bright magenta-pink lips. She has long purple-painted nails. She is sitting on a gray couch with her legs crossed (right over left, right knee raised), right hand near her chin in a coy pose, left hand resting on the couch, head slightly tilted, looking at the camera with a subtle flirtatious smile. The couch has colorful psychedelic mandala-patterned pillows and one plain beige pillow. Background is a light gray wooden plank wall with a white-framed window showing darkness outside (nighttime). The photo is taken with a smartphone camera using direct front flash, creating harsh lighting and sharp shadows, slight high angle shot, medium-full frame vertical composition, casual party snapshot aesthetic, vibrant purple and pink color palette against a neutral background, Y2K Halloween party vibe.
```

</details>

<details><summary><b>Y2K Direct Flash Portrait</b></summary>

```text
Photorealistic Y2K-style portrait, vertical 3:4 format.
A young woman poses against a neutral, softly lit background. She is very close to the camera in a close-up shot, playfully biting her lower lip and looking to the side with a flirtatious, confident expression. Her beautiful, voluminous hairstyle frames her face without covering it too much.
Minimalist composition, vintage digital texture, soft light blur, glamorous atmosphere. Shot on an iPhone 17 Pro Max with a direct flash aesthetic and polished makeup.
The woman has A full-coverage foundation is applied to the skin, with visible contouring on the cheekbones and along the bridge of the nose.
Eye makeup: defined black winged eyeliner that elongates the eye shape, long lashes with a subtle fox-eye effect, and light shimmery eyeshadow in the inner corners.
Lips: transparent glossy lip gloss.
She is wearing a fitted black long-sleeve top.
Close-up framing, realistic skin texture, high detail, natural facial proportions, authentic Y2K glamour.
```

</details>

<details><summary><b>Young Saudi Doctor at Work</b></summary>

```text
Create a photorealistic image of a young Saudi doctor seen from the back, seated on a simple chair in front of a wooden desk. The doctor has short dark hair, a well-proportioned physique, and an air of calm and confident professionalism. He is wearing a white Saudi thobe with a clean medical coat over it. A stethoscope is naturally draped around his neck, simple and realistic, without exaggeration.

In front of him, there is a large desktop computer screen with soft white lighting. The wooden desk is simple, with a small potted plant on one side and a simple vase on the other. The design is balanced and centered.

The background is white with soft natural lighting, casting gentle shadows. The image should have realistic shading and depth, with smooth color transitions and clear shapes with precise realistic details.

The atmosphere is calm, professional, and deep. High-quality 8k, polished, realistic with an artistic touch.
```

</details>

<details><summary><b>Zen Garden Monk Transformation</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. The face must remain clear and unaltered. Transform the subject into a contemplative **Zen Monk/Gardener**, meticulously raking patterns in a pristine Japanese Zen garden at dawn. Emphasize minimalist aesthetics, soft natural light, tranquil colors, and a profound sense of peace and mindfulness.",
  "details": {
    "year": "Timeless (Traditional Japanese Aesthetics)",
    "genre": "Zen / Contemplative / Minimalist / Cultural",
    "location": "A perfectly maintained Japanese Zen rock garden (Karesansui). The ground is fine white gravel raked into precise, concentric patterns around carefully placed, weathered rocks. A moss-covered stone lantern or a single, artfully pruned bonsai tree is visible in the background. A subtle bamboo fence encloses the space.",
    "lighting": "Soft, diffused light of early dawn or a gentle overcast day. The light is even and gentle, creating subtle shadows that define the raked patterns without harshness. A cool, serene quality pervades the scene.",
    "camera_angle": "Medium shot to full-body, positioned slightly low to capture the subject's interaction with the ground and the expanse of the raked garden. The composition is clean and balanced, adhering to minimalist principles. (1:1 composition).",
    "emotion": "Serene, focused, mindful, and peaceful. A deep sense of inner calm.",
    "costume": "Simple, traditional Japanese attire: a plain, loose-fitting kimono or robes in muted, natural tones (e.g., charcoal gray, deep indigo, earthy beige). Hair is neatly styled or shaved (if appropriate for a monk). Clean, unadorned aesthetic.",
    "color_palette": "Dominated by serene, muted natural colors: the stark white of the gravel, the grays and earthy browns of the rocks and wood, deep greens of moss and foliage. Very subtle, restrained use of accent colors. The overall palette is harmonious and calming.",
    "atmosphere": "Profoundly peaceful, meditative, silent, and harmonious. The air feels crisp and still, inviting introspection. A strong sense of order and tranquility.",
    "subject_expression": "Eyes are downcast or gently focused on the raking task, with a calm, serene expression on their realistic face. Lips are gently closed, conveying deep concentration and inner peace.",
    "subject_action": "Holding a wooden rake with both hands, meticulously drawing perfect, flowing patterns in the white gravel. Their posture is stooped in a graceful, deliberate manner, emphasizing the ritualistic nature of the task. Movement is slow and purposeful.",
    "environmental_elements": "Perfectly defined, flowing patterns in the white gravel. The texture of the weathered rocks. Fine dew drops might be visible on the moss or the rake. The distant bamboo fence provides a subtle, natural boundary to the tranquil space."
  }
```

</details>
