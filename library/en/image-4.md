# Image & Design (4/5)

847 prompts. Copy one, replace anything in brackets, and paste it into any chat model.

[English](../en/image.md) · [中文](../zh/image.md)

Pages: [1](image.md) · [2](image-2.md) · [3](image-3.md) · **4** · [5](image-5.md)

<details><summary><b>Picture Book Character Turnaround Brief Builder</b></summary>

```text
Act as a children's picture book character designer and art director. I will give you a rough character idea, and you will turn it into a consistent, reusable character design plus two ready-to-use image prompts: a character turnaround sheet, and a first story scene that keeps the character exactly on model.

Character idea: ${character:a gentle river otter who runs a tiny floating library for the animals of the riverbank}
Reader age: ${age:3 to 6 years}
Story mood: ${mood:cozy, curious, a little bit funny}
Art style: ${style:soft watercolor and colored pencil on textured paper, warm and hand-made}
First scene to illustrate: ${scene:story hour on the library raft at sunset, reading aloud to a small audience of riverbank animals}

Please produce:

1. Character bible
   - Name suggestions (three, easy to read aloud) and one-line personality.
   - Silhouette: the shape a child could recognize from a shadow alone.
   - Proportions: head-to-body ratio and any exaggerations that make the character friendly.
   - Fixed design details that must never change between images: fur or skin colors (name each color simply, for example "warm chestnut brown"), clothing, one signature prop, and one small quirk (for example a crooked whisker).
   - Palette: 5 colors for the character and 3 for their world.
   - Expressions: four key expressions with a short description of eyes, brows, and mouth.

2. Turnaround sheet prompt
   A single, detailed image prompt for an AI image generator showing the character on a plain off-white background in four poses in one row: front, three-quarter, side, and back view, all at the same scale, plus a small row of three facial expressions underneath. Repeat every fixed design detail in the prompt. Include style, lighting, and "no text, no labels" at the end, and recommend a wide aspect ratio.

3. First scene prompt
   A second image prompt for the first scene that is a clear follow-on of the turnaround sheet: the same character with every fixed design detail restated word for word, now placed in the scene, with composition notes that leave clean space for one or two lines of picture book text. Recommend an aspect ratio for a double-page spread.

4. Consistency checklist
   Five short checks I can use to compare any new image with the turnaround sheet before I accept it.

Rules: keep everything gentle and age-appropriate, avoid any resemblance to existing famous characters, and keep the language simple enough to read to a child where it describes the character.
```

</details>

<details><summary><b>Pilates Studio Soft Daylight</b></summary>

```text
{
  "category": "PILATES_STUDIO_SOFT_DAYLIGHT",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "Preserve exact reference identity and facial proportions. Adult 21+ only."
  },
  "subject": {
    "demographics": "Adult woman, 21-29, match reference identity.",
    "hair": {
      "color": "Match reference.",
      "style": "High ponytail or neat bun (realistic, not perfect)",
      "texture": "Strands visible, a few flyaways",
      "movement": "Minimal"
    },
    "face": {
      "eyes": "Exact reference eyes; calm focus",
      "skin_details": "Natural texture; subtle workout glow (not oily)",
      "micro_details": "Preserve marks"
    },
    "clothing": {
      "outfit": "Minimal activewear set (no logos/text)",
      "fabric": "Athletic knit texture visible; realistic tension at seams"
    },
    "accessories": {
      "jewelry": [
        "Small silver hoops optional (can be removed for workout realism)"
      ]
    }
  },
  "pose": {
    "type": "Post-session candid",
    "orientation": "Half-body seated on mat",
    "hands": "One hand holding water bottle (unbranded), other resting on knee",
    "gaze": "Near-direct eye contact",
    "expression": "Soft proud smile"
  },
  "setting": {
    "environment": "Pilates studio",
    "background_elements": [
      "Neutral studio walls",
      "Mirrors blurred without reflections glitches",
      "Yoga mats and props (no logos)"
    ],
    "depth": "Subject sharp; background soft"
  },
  "camera": {
    "shot_type": "Half-body portrait",
    "angle": "Eye level or slightly above",
    "focal_length_equivalent": "26mm phone OR 50mm pro",
    "framing": "4:5",
    "focus": "Eyes sharp; background bokeh"
  },
  "lighting": {
    "source": "Soft window daylight",
    "direction": "Gentle side/front",
    "highlights": "Natural highlights on cheekbones",
    "shadows": "Soft, flattering"
  },
  "mood_and_expression": {
    "tone": "Clean, sporty, calm confidence",
    "atmosphere": "Minimal, airy"
  },
  "style_and_realism": {
    "style": "Photoreal fitness lifestyle",
    "imperfections": "Mild noise, subtle sweat glow"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High",
    "noise": "Low to mild",
    "mode_variants": {
      "amateur": "Phone candid framing, mild noise, slight tilt",
      "pro": "Editorial fitness look, crisp micro-contrast, clean exposure"
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
    "identity drift",
    "face morphing",
    "mirror glitches",
    "duplicate reflections",
    "extra fingers",
    "bad anatomy",
    "readable text",
    "logos",
    "watermark",
    "plastic skin",
    "over-smoothing"
  ]
}
```

</details>

<details><summary><b>Pina Colada Cocktail Video</b></summary>

```text
Cinematic vertical smartphone video, portrait orientation, centered composition with strong top and bottom headroom. Elegant Piña Colada cocktail inside a coconut shell glass placed in the middle of a tall frame. Clean marble bar surface only in lower third, soft tropical daylight, palm leaf shadows moving gently across background. Slow creamy Piña Colada pour with visible thick texture and condensation. Camera performs slow vertical push-in macro movement, shallow depth of field, luxury beverage commercial style, minimal aesthetic, portrait framing, vertical composition, tall frame, 9:16 aspect ratio, no text.
```

</details>

<details><summary><b>Pink Hair Glasses Selfie</b></summary>

```text
Create a realistic selfie photo of a girl with the following features:
- Transparent glasses
- Vibrant pink hair, styled naturally
- Natural lighting to enhance realism
- Casual expression, capturing a candid moment
- Ensure high resolution and detail to make it look like a genuine selfie.
```

</details>

<details><summary><b>Pink Hair Green Eyes Cozy Bedroom Portrait</b></summary>

```text
/imagine prompt: Ultra realistic photographic portrait of a 30-year-old Asian woman with facial features inspired by the original character, featuring short pink hair and green eyes, wearing a glossy red sleeveless zippered top and pink skirt, indoor bedroom setting, high angle shot, natural skin microtextures, authentic pores, soft sheen, subtle highlights, warm and directional lighting, high detail, photorealistic rendering. /monochrome /calm /naturaltone /highdetail --ar 9:16 --style raw --v 6.1 --no deformed, bad anatomy, disfigured, poorly drawn face, mutation, extra limbs, ugly, blurry, lowres, bad proportions /added
```

</details>

<details><summary><b>Pip the Otter Librarian Turnaround Sheet</b></summary>

```text
A children's picture book character turnaround sheet of Pip, a gentle young river otter librarian, drawn in soft watercolor and colored pencil on textured off-white paper. Four full-body views in one row at the same scale, evenly spaced: front view, three-quarter view, side view, and back view. Pip has a rounded, pear-shaped silhouette with a big head (about one third of the body height), short legs, small webbed paws, and a long tapered tail. Fixed design details, identical in every view: warm chestnut brown fur with a cream-colored face, chest, and belly; small round dark eyes with a white highlight; a tiny black button nose; one crooked whisker on the left side of the face; a mustard-yellow knitted scarf wrapped once around the neck with a short fringe; round wire spectacles resting low on the nose; and a small teal satchel worn across the body, with a single brass buckle and a book poking out of the top. Below the four poses, a smaller row of three head-and-shoulders expressions: a warm smile, wide-eyed curious surprise, and a sleepy content yawn. Plain off-white background with a faint paper texture, soft even daylight, gentle colored pencil outlines, light watercolor washes, no cast shadows except a soft ground shadow under each pose. No text, no labels, no arrows, 16:9 wide composition.
```

</details>

<details><summary><b>Pip the Otter Story Hour on the River</b></summary>

```text
A children's picture book double-page spread illustration in soft watercolor and colored pencil on textured paper, showing the same character from the turnaround sheet: Pip, a gentle young river otter librarian. Keep every fixed design detail exactly the same: warm chestnut brown fur with a cream-colored face, chest, and belly; small round dark eyes with a white highlight; a tiny black button nose; one crooked whisker on the left side of the face; a mustard-yellow knitted scarf wrapped once around the neck with a short fringe; round wire spectacles resting low on the nose; and a small teal satchel worn across the body with a single brass buckle. Scene: story hour at sunset on Pip's tiny floating library, a wooden raft with a little shed of overflowing bookshelves, a striped canvas roof, and a string of paper lanterns just starting to glow. Pip sits on an upturned crate at the right third of the image, holding an open picture book toward the audience and reading aloud with a warm smile. Gathered on the raft and the grassy bank are a small audience of riverbank animals listening closely: two ducklings, a young beaver hugging its knees, a frog on a lily pad, and a sleepy hedge sparrow on a reed. The river reflects peach and lavender sky, with reeds, dragonflies, and gentle ripples. Leave a calm, softly painted sky area in the upper left third with no important details, as clean space for one or two lines of story text. Cozy, gentle, age-appropriate mood. No text, no letters, no watermark, 16:9 wide composition.
```

</details>

<details><summary><b>Pixar Style 3D Character from Photo</b></summary>

```text
3D character render in high-end Pixar Disney animation style, based on the uploaded photo. Preserve facial structure, expression, hairstyle and unique characteristics. Cute but realistic proportions, clean topology, smooth skin, detailed eyes. Standing full body on a plain white studio background, soft even lighting, subtle natural shadow under the feet, global illumination, no props, no distractions. Ultra sharp, 4K, high detail, physically based rendering, balanced colors, cinematic depth, professional studio look, symmetrical framing, photoreal cartoon finish.
```

</details>

<details><summary><b>Pixar Style Family Wallpaper</b></summary>

```text
Pixar-style, Disney-style, high quality 3D render, octane render, global illumination, subsurface scattering, ultra detailed, soft cinematic lighting, cute and warm mood.

A happy family of three (father, mother, and their young daughter) reimagined as Pixar-style 3D characters, peeking playfully from behind a wall on the left side.

The father has medium-length slightly wavy brown hair, a short beard, and a warm friendly smile.  
The mother has long straight brown hair, a bright smile, soft facial features, and elegant appearance.  
The little girl is around 2–3 years old, with light brown/blonde slightly curly hair, round cheeks, big expressive eyes, and a joyful playful expression.

Use the reference image to preserve facial identity, proportions, hair color, hairstyle, and natural expressions. Keep strong resemblance to the real people while transforming into a stylized Pixar-like character.

Composition: father slightly above, mother centered, child in front leaning forward playfully.

Clothing inspired by cozy winter / Christmas theme with red tones and soft patterns (subtle, not distracting).

Include a cute tabby cat at the bottom looking upward with big shiny eyes.

Color palette: warm beige, peach, cream tones, soft gradients, cozy atmosphere.

Minimal background, textured wall on the left side, characters emerging from behind it.

iPhone lockscreen wallpaper composition, vertical framing, large clean space at the top for clock, ultra aesthetic, depth of field, 4K resolution.

same identity, same person, keep exact likeness from reference photo
```

</details>

<details><summary><b>Pixel Art Alpine Railway Station at Sunset</b></summary>

```text
A wide 16-bit era pixel art scene of a tiny alpine railway station in a mountain valley at golden-hour sunset, in the style of a beautifully detailed retro adventure game background, crisp hard-edged pixels with no anti-aliasing and no blur, limited 48-color palette with careful dithering in the sky. In the foreground, a small wooden station building with a steep red tile roof, a round station clock, flower boxes with pink and yellow pixel flowers, a bench, two milk cans, and a hanging lantern just starting to glow. A short cream-and-forest-green steam train with three carriages waits at the platform, a soft white puff of pixel steam rising from its chimney, warm yellow light in its windows. The track curves away to the right over a stone arch viaduct across a turquoise river with tiny white rapids, then disappears into a tunnel in the mountainside. In the midground, a cluster of chalet houses with chimneys, a little church with an onion-dome steeple, pine forests in three shades of green, and a waterfall falling from a cliff. In the background, layered snow-capped peaks in lavender, peach, and rose tones catching the last light, a gradient sunset sky from deep orange at the horizon to violet at the top, a few long pixel clouds, and the first two stars. Small life details: a cat on the platform, birds as two-pixel silhouettes, smoke from chimneys. Clean parallax-style layering, cozy and nostalgic mood, readable silhouettes, consistent pixel scale across the whole image. 16:9 landscape composition. No people, no text, no user interface, no logos, no watermark.
```

</details>

<details><summary><b>Pixel Art Prompt Generator</b></summary>

```text
Act as a Pixel Art Prompt Generator. When the user provides a subject, scene, character, object, or idea, generate a detailed image-generation prompt using the following style:

- Chunky low-resolution pixel art
- Thick black outlines
- Bold cartoon shapes
- Big expressive eyes
- Soft cel-shading with 2-tone shadows
- Vibrant saturated color palette
- Bubblegum pink, sky blue, forest green, sunset orange accents
- Dithered and crosshatched textures
- Retro 16-bit console RPG aesthetic
- Cute kawaii-inspired design
- Subtle grungy details
- Soft bokeh background lights
- Dreamy nostalgic atmosphere
- Upscaled 480p appearance
- Nearest-neighbor pixel scaling
- Crisp pixel edges without anti-aliasing

Rules:
1. Keep the user's subject unchanged.
2. Expand it into a highly detailed image-generation prompt.
3. Output only the final prompt unless the user asks otherwise.
4. Never mention specific living artists or copyrighted styles.
```

</details>

<details><summary><b>Pixel Dissolve Food Transformation</b></summary>

```text
Minimalist food photograph, [1080x1080] – a single ${food} rests on a light, matte surface and is captured mid-transformation into a 3D pixelized form: one half remains intact while the other organically fragments into large, floating cubes that drift outward, each cube revealing the object’s texture, ingredients, and colors. Studio lighting with soft, realistic shadows, shallow depth of field, tasteful perspective and composition, hyperrealistic detail, stylish geometric abstraction, subtle motion blur on the cubes, high resolution, cinematic close-up.
```

</details>

<details><summary><b>Plant Hero Section Image</b></summary>

```text
Create an image for a hero section with a 16:9 aspect ratio. The image should feature 6-7 different types of plants, all set in a natural environment with sunlight streaming in. Make sure the composition is aesthetically pleasing and suitable for use in a webpage hero section.
```

</details>

<details><summary><b>Plants and Bouquet Under a Warm Lamp</b></summary>

```text
{
  "category": "PLANTS_BOUQUET_WARM_LAMP",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking, youthful vibe but clearly adult.",
    "hair": {
      "color": "Dark brown",
      "style": "Natural, soft, slightly tousled, casual asymmetry",
      "texture": "Realistic strands, flyaways, roots visible",
      "movement": "Falls naturally over shoulders; small motion blur allowed in ends"
    },
    "face": {
      "shape": "Oval, soft jawline",
      "eyes": "Expressive, dark irises, crisp catchlights",
      "nose": "Defined bridge, natural highlight",
      "lips": "Soft rosy tint, natural texture lines visible",
      "skin_details": "Real pores, slight natural blush, no airbrushing",
      "micro_details": "Fine hair strands across forehead, subtle imperfections preserved"
    },
    "clothing": {
      "outfit": "Trendy black casual outfit, no text/logos",
      "fabric": "Tactile textile weave visible, gentle wrinkles"
    },
    "accessories": {
      "jewelry": ["Silver hoop earrings"]
    }
  },
  "pose": {
    "type": "Candid lifestyle portrait",
    "orientation": "Half-body",
    "head_position": "Slight tilt; subtle glance slightly left of lens then back to lens feel",
    "hands": "Holding bouquet wrapped in kraft paper; fingers natural, joints correct",
    "gaze": "Warm, lively eye contact",
    "expression": "Sweet confident smile"
  },
  "setting": {
    "environment": "Indoor plant corner",
    "background_elements": [
      "Many green plants layered foreground/midground/background",
      "Warm orange lamp bulb behind subject creating halo glow",
      "Kraft paper bouquet wrap: creases, twine detail, tactile texture"
    ],
    "depth": "Foreground leaf bokeh, subject sharp, background lamp bloom"
  },
  "camera": {
    "shot_type": "Half-body portrait",
    "angle": "Slightly off-axis, casual handheld",
    "focal_length_equivalent": "26mm iPhone wide look",
    "framing": "4:5, asymmetrical composition",
    "focus": "Eyes sharp, bouquet slightly softer at edges"
  },
  "lighting": {
    "source": "Soft warm key + orange tungsten practical behind",
    "direction": "Warm side light casts intricate leaf-shadow patterns across face (subtle, flattering)",
    "highlights": "Gentle highlight on hair and cheekbones",
    "shadows": "Nuanced warm shadows, comforting atmosphere",
    "quality": "Soft, warm, tactile"
  },
  "mood_and_expression": {
    "tone": "Cute-relaxed, cozy, candid",
    "expression": "Lively eyes, soft smile",
    "atmosphere": "Immersive, spontaneous"
  },
  "style_and_realism": {
    "style": "Photorealistic iPhone snapshot vibe",
    "fidelity": "High skin and hair detail, no smoothing",
    "imperfections": "Slight motion blur away from face, mild noise"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "High resolution",
    "noise": "Slight phone sensor noise",
    "composition": "Imperfect candid framing (slightly awkward angle) but still aesthetic"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "single_subject_only": true,
    "do_not_show_phone": true
  },
  "negative_prompt": [
    "cgi", "cartoon", "anime", "plastic skin", "over-smoothing",
    "extra fingers", "warped hands", "duplicate person",
    "readable text", "logos", "watermark"
  ]
}
```

</details>

<details><summary><b>Playful Cat Ear Flash Portrait</b></summary>

```text
Do not change the girl's facial features, eye shape, eyebrows, nose, or lips. Maintain 100% facial resemblance.

Aspect ratio: 3:4. Ultra-realistic, high-quality, sharp 8K photograph, shot on iPhone 16 Pro Max.

Subject & Pose: A young  woman in a playful cat-inspired look. Medium close-up portrait with a relaxed, candid Pinterest aesthetic. She leans slightly toward the camera with naturally angled shoulders, her head gently tilted, and one hand casually touching her hair or collarbone. Her pose should feel spontaneous, relaxed, feminine, and flirtatious, never stiff or posed like an ID photo. She looks directly into the lens with a playful, confident expression, soft kissy lips, bright expressive eyes, and a sweet, teasing gaze.

Outfit & Accessories: A fitted white corset bustier with thin straps and a front hook closure. A fluffy white cat-ear headband with soft pink inner ears. Layered delicate gold necklaces with small coin pendants and small gold hoop earrings.

Hair: thick, voluminous  hair styled in loose soft beach waves. Center part, with soft strands naturally framing the face and falling over the shoulders.

Nails: Long, elegant square-shaped nails with a glossy milky-white manicure. The nails are neat, feminine, smooth, and clearly visible in the frame.

Makeup: Fresh glowing soft glam makeup with luminous skin, peachy-pink blush, defined lashes, subtle brown eyeshadow, a fine winged eyeliner, glossy nude peach lips, a small black triangle cat nose drawn on the tip of the nose with black eyeliner, and three delicate black cat whiskers drawn on each cheek in the same pencil-drawn style.

Lighting & Camera: Direct flash photography with bright frontal lighting, creating radiant skin, crisp contrast, and a luxurious Instagram editorial look. Eye-level angle with an effortless, natural composition.

Background & Mood: A nighttime garden with dark leafy trees and warm golden fairy lights melting into creamy bokeh. Festive, youthful, playful, flirty, feminine, and coquettish. Stylish Pinterest and Instagram aesthetic, like a chic Halloween or themed party.
```

</details>

<details><summary><b>Playful Fisheye Candid Portrait</b></summary>

```text
GPT Image 2.5 on ChatGPT

Prompt: 

Create a realistic fisheye photo of the woman in my uploaded selfie, preserving her exact facial features. She sits on a doorstep in front of weathered green wooden doors, wearing a beige trench coat, ivory turtleneck, and light blue jeans. A curious tabby-and-white cat fills the right foreground with an oversized nose and expressive eyes. Soft daylight, natural textures, playful candid mood, ultra-realistic photography, landscape 16:9, no text.
```

</details>

<details><summary><b>Playful Ghostbusters Halloween Selfie</b></summary>

```text
The photograph conveys a casual, playful, and warm mood. It is a festive mirror selfie capturing the joy of getting ready for Halloween. The cozy home atmosphere is enhanced by soft lighting and the presence of a small pet.

Camera Angle:
The photo is taken in a mirror from a medium distance, framed from the waist up. The camera (phone) is approximately at eye level, creating a straight and natural selfie perspective. The image is in a vertical format, keeping the woman and her pet as the main focus.

Subjects:
The main subjects are a young woman and a small Chihuahua.

Woman — Appearance and Outfit

Clothing and Accessories:
The woman is wearing a fitted beige sleeveless jumpsuit/vest inspired by the Ghostbusters uniform.

On the left side of her chest is the official “No Ghost” logo — the classic white ghost inside a red crossed-out circle.

Her waist is accentuated with a wide black tactical belt featuring a large buckle.

She wears a thin, delicate gold chain around her neck.

Several gold bracelets are visible on her left wrist, including one wider and one thinner bracelet.

She is holding a pink iPhone with two cameras in her left hand. The phone partially covers her face, but her smile remains visible.

Pose:
The woman stands in a relaxed pose, holding the phone in her left hand to take the mirror selfie. With her right hand, she gently holds the dog. She looks directly into the mirror and smiles sweetly, with closed lips and a subtle half-smile.

Hairstyle:
Her hair is loose, with a natural texture and soft waves. It is styled to one side, adding softness to her appearance.

Makeup:
Natural makeup enhanced slightly for the Halloween celebration. Her lips are covered with rich berry-toned lipstick, while her eyes are subtly defined with light makeup.

Dog — Appearance and Costume

A small dark-brown Chihuahua with a white patch on its chest. The dog is wearing a cute ghost costume.

The costume is a white poncho with two large oval black eyes and a black mouth drawn on it, resembling a classic “ghost under a sheet.”

The dog looks directly at the camera through the mirror with a calm and curious expression. The woman gently holds the dog with her right hand.

Background and Lighting

Background:
The setting is a cozy residential room creating a warm home atmosphere.

Part of a bed is visible on the left.

Along the right wall is a large wardrobe with light-colored wooden doors.

A section of parquet or laminate flooring is visible between the wardrobe and the mirror.

The interior is modern, minimalist, and uncluttered.

Lighting:
Soft, natural, diffused light, likely daylight, fills the room. There are no harsh shadows. The lighting naturally emphasizes the colors of the clothing, the woman’s face, and the dog while creating a warm and cozy atmosphere.

Important: Do not change the facial features or identity from the reference image. Preserve the exact facial structure, eyes, nose, lips, and other distinctive features.

Expression: A subtle, natural half-smile with closed lips.

Format: 3:4
Quality: Ultra-realistic, high-quality, sharp 8K photograph, natural skin texture, highly detailed, shot on an iPhone 16 Pro.
```

</details>

<details><summary><b>Playing Card Sorcerer Poster</b></summary>

```text
A hyper-realistic cinematic movie poster of a powerful sorcerer with the same facial structure and likeness as the uploaded reference photo, bursting through a cracked ${specificcard} playing card. 
The card explodes outward with stone fragments, dust, and debris frozen mid-air.
They wear an ornate royal maroon and gold embroidered medieval fantasy jacket, rich fabric textures, intricate detailing, regal and mystical. The sorcerer extends one hand forward toward the viewer, fingers glowing with intense magical energy, subtle golden sparks and dark arcane aura surrounding the hand. 
Intense piercing gaze, confident and dominant expression, cinematic hero framing.
Dramatic chiaroscuro lighting, dark moody background, volumetric light rays, ultra-detailed textures, shallow cinematic depth of field.
Photorealistic face, epic fantasy realism, movie poster composition, high contrast, dynamic motion, dust particles, masterpiece quality, ultra-sharp focus, 8K resolution, cinematic color grading.
```

</details>

<details><summary><b>Plush Toy Transformation</b></summary>

```text
Transform the subject or image into a cute plush form with soft textures and rounded shapes. If the image contains a human, preserve the distinctive features so the subject remains recognizable. Otherwise, turn the object or animal into an adorable plush toy using felt or fleece textures. It should have a warm felt or fleece look, simple shapes, and gently crafted eyes, mouth, and facial details. Use a heartwarming pastel or neutral color palette, smooth shading, and subtle stitching to evoke a handmade plush toy. Give it a friendly, cute facial expression, a slightly oversized head, short limbs, and a soft, huggable silhouette. The final image should feel charming, collectible, and like a genuine plush toy. It should be cute, heart-warming, and inviting to hug, while still clearly preserving the recognizability of the original subject.
```

</details>

<details><summary><b>Pointillist Tide Pool Painting</b></summary>

```text
A rocky tide pool with orange and purple starfish, green sea anemones, small hermit crab shells, and ribbons of kelp is painted in the Neo-Impressionist pointillist style of Georges Seurat and Paul Signac. The whole canvas is built from thousands of small, distinct dots and short dabs of pure color placed side by side, so the colors mix in the eye: turquoise and violet dots for the clear water, ochre and rose dots for the wet rocks, and sparkling white and lemon dots where the afternoon sun glints on the surface. Barnacle-covered boulders frame the pool, and beyond them a calm sea with a few gentle waves stretches to a soft horizon under a pale peach sky. Small sea snails and pebbles are visible through the shallow water. Luminous, airy, and balanced composition with a low viewpoint close to the pool. Visible canvas texture and the slight relief of oil paint dots. Wide landscape 16:9. No people, no hands, no boats, no text, no signature, no logos.
```

</details>

<details><summary><b>Pokemon Master Face Swap</b></summary>

```text
Take the input image, and use it is face and apply it to be Ash the Pokemon master image with his favorite character pikachu.
```

</details>

<details><summary><b>Policy Safe DALL-E Image Generation</b></summary>

```text
Please generate an image according to the detailed description provided below. If the request involves copyrighted, content policy restrictions or content policy-violating elements, please substitute them with similar but compliant visuals. My detailed image description is: [detailed image description]
```

</details>

<details><summary><b>Pop Art Illustration of a Chrome 1950s Roadside Diner at Night</b></summary>

```text
A pop art comic-style illustration of a gleaming chrome 1950s roadside diner in the desert at night, landscape 4:3, with no text. A streamlined silver diner car with a rounded roof and polished, reflective chrome panels sits in the middle of the frame, with a long row of warm-yellow lit windows and a red-and-white striped awning above them. A turquoise 1950s convertible with tail fins, whitewall tires, and shiny chrome bumpers is parked in front of the diner at the lower left. A tall, blank pink neon sign shape on a dark pole glows at the upper left with no letters on it. A big yellow moon hangs at the upper right in a purple starry night sky, above pink desert mountains, saguaro cacti, and spiky desert plants. A curving desert road with a white edge line sweeps away on the right. Bold black ink outlines, halftone dot shading, flat bright retro colors, punchy comic-book energy. No text, no lettering, no speech bubbles, no logos.
```

</details>

<details><summary><b>Post-Apocalyptic Scavenger Transformation</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. The face must remain clear and unaltered. Transform the subject into a hardened **Wasteland Scavenger/Survivor**, standing vigilant on a windswept dune in a desolate, post-apocalyptic landscape. Emphasize weathered, patched clothing, makeshift gear, gritty textures, and a bleak, survivalist atmosphere.",
  "details": {
    "year": "Undefined Post-Apocalyptic Future (e.g., 'After the Collapse')",
    "genre": "Post-Apocalyptic / Dystopian / Survival",
    "location": "A vast, desolate desert or barren wasteland. The ground is cracked earth, wind-blown sand, and scattered debris (e.g., rusted car parts, broken signs). A hazy, polluted sky looms overhead, perhaps with a distant, ruined city skyline barely visible on the horizon.",
    "lighting": "Harsh, muted, and desaturated sunlight, filtering through a dusty, smoggy atmosphere. Strong directional shadows, emphasizing the rough textures of the environment and the subject's gear. Overall tone is gritty and somewhat oppressive.",
    "camera_angle": "Medium shot to full-body, positioned slightly low to make the subject appear formidable against the stark landscape. The horizon line is low, emphasizing the vast, empty sky. (1:1 composition).",
    "emotion": "Vigilant, weary, resilient, and determined.",
    "costume": "Layered, patched-together clothing made from repurposed materials: torn denim, worn leather, tattered canvas. Functional, utilitarian gear like heavy boots, fingerless gloves, and a bandana or makeshift face covering. A visible collection of scavenged items (e.g., pouches, tools, water canteen) strapped to their body.",
    "color_palette": "Dominated by desaturated earth tones: dusty browns, faded greens, muted grays, and rusty oranges. Punctual pops of faded color from repurposed fabric scraps. The sky is a washed-out pale yellow or sickly green.",
    "atmosphere": "Bleak, harsh, dangerous, and lonely. The air feels heavy with dust and the silence of a dead world. A constant sense of survival against overwhelming odds.",
    "subject_expression": "A grim, focused gaze, scanning the horizon for threats or resources. Mouth set in a firm, determined line. Hair is windswept and dusty.",
    "subject_action": "Standing alert, possibly holding a makeshift weapon (e.g., a sharpened pipe, a crossbow, or a sturdy club) resting on their shoulder or held defensively. Their stance is one of readiness and caution.",
    "environmental_elements": "Fine dust or sand particles visibly blowing in the wind around the subject. Distant, skeletal remains of trees or buildings. Perhaps a single, circling scavenger bird high in the sky. The ground shows cracks and dry vegetation."
  }
}
```

</details>

<details><summary><b>Pottery Studio Workbench at Blue Hour</b></summary>

```text
Interior workbench room of a cedar lakeside pottery studio at blue hour, looking out to the water. A heavy wooden wedging table fills the foreground with clay tools, a wire cutter, and a few leather-hard bowls. Shelves of drying pots line the left wall. Through a wide rectangular window and open barn-style double bay doors with X-braces, the lake sits deep blue under a violet dusk sky; the wide wooden plank dock with its T-shaped extension, a small red rowboat, and slender birch trees are visible outside. Warm task lamp light on the bench contrasts cool blue window light. Vertical cedar interior boards, plaster accents, pottery wheel at the right edge. Same studio as the golden-hour exterior: weathered vertical cedar boards, dark pitched metal roof with a brick chimney, wide plank dock, two small side windows, pines and birches. Photoreal, landscape 16:9. No people, no text.
```

</details>

<details><summary><b>POV Smartphone with Space Themed Feed</b></summary>

```text
Capture a photograph from the viewer’s eyes (female), holding a modern smartphone at chest height with both hands. Her nails are glossy red nail polish with a clean manicure. The camera looks slightly downward at the phone screen, which displays a Twitter-like home timeline UI with NASA-focused posts. The UI should be recognizable and crisp, featuring posts about Artemis, JWST, Hubble, and Mars rover with space imagery thumbnails and verified-style elements.

Ensure the sunlight creates a subtle mirror reflection of the woman’s face over the interface, with half her face lit by the sun and the other in soft shadow. Maintain natural skin texture without a beauty-filter look.

Set the background in Central Park, NYC, with out-of-focus bokeh of trees, walkways, and skyline hints. Use a full-frame DSLR look with a 50mm or 85mm lens at f/1.8 for a shallow depth of field, keeping the phone and hands in crisp focus while achieving a smooth bokeh.

Negative Prompt: Avoid low-res UI, distorted or extra fingers, warped phone, incorrect hand anatomy, oversharpening, cartoonish effects, watermarks, random logos, fake app UI, duplicated icons, and excessive glare obscuring the screen.
```

</details>

<details><summary><b>Pre-Dawn Scene in Ancient Mecca</b></summary>

```text
Create a hyper-realistic cinematic pre-dawn scene in ancient Mecca, viewed from a high overhead camera angle above the roof of the Kaaba, looking diagonally downward toward its lower corner and the wide open ground surrounding it. The scene includes:

- The Kaaba standing alone at the center of a large open sandy courtyard, with uneven, dusty ground made of compacted sand and dry soil.
- The surrounding area is intentionally open and spacious, emphasizing its sacred isolation, with distant clusters of small mud-brick and stone houses marking the early Meccan settlement.
- Rugged rocky mountains rise on both sides of the valley, fading into the cold bluish pre-dawn haze.
- A miraculous opening at the lower vertical corner of the Kaaba where two walls meet, with an intense, pure white sacred light shining outward.
- A woman emerging from the corner opening, wearing simple desert garments and holding a newborn bundle, casting a long shadow across the ground.
- Faint abstract clusters of luminous white light in the sky suggesting the presence of angels.

The atmosphere should be majestic and sacred, with ultra-realistic rendering, dramatic cinematic lighting, strong volumetric light rays, and highly detailed textures. The scene should be shot like an epic historical film frame, in a 4:5 vertical aspect ratio, with no modern elements.
```

</details>

<details><summary><b>Prefab BBQ Commercial Kitchen Model</b></summary>

```text
create a pre-fab kitchen model along with the complete equipments related to bbq setup within the dimension 10'x15'
```

</details>

<details><summary><b>Print Ready Image Enhancement</b></summary>

```text
Enhance the provided uploaded image by improving its sharpness, exposer, clarity, quality, and overall visual impact while preserving its core design elements. Ensure that the completed image is suitable for display in professional and digital contexts.

Your task is to:
- Arrangements need to be made to print the image in 4K resolution.

You will:
- Use high-resolution and color-accurate techniques to ensure print quality.
- Tailor images to be engaging and marketable.

Rules:
- Maintain print resolution of at least 300 DPI.
- Avoid overly complex designs that detract from the image focus.
```

</details>

<details><summary><b>Printable Sales Material Images</b></summary>

```text
Act as a professional image creator. You are an expert in generating high-quality, impactful images suitable for printing and sales.

Your task is to:
- Create visually stunning images that are ready for print.
- Ensure each image is impactful and appealing for sales.
- Focus on themes such as ${theme:product promotion}, ${style:modern}.

You will:
- Use high-resolution and color-accurate techniques to ensure print quality.
- Tailor images to be engaging and marketable.

Rules:
- Maintain print resolution of at least 300 DPI.
- Avoid overly complex designs that detract from the image focus.
```

</details>

<details><summary><b>Private Jet Aviation Portrait</b></summary>

```text
Create a photorealistic 2026 high-fashion aviation portrait beside the turbine of an elite private jet, using a powerful mid-close composition from the waist upward. The adult female cabin crew model is exceptionally glamorous, with captivating hazel eyes, a naturally very broad ribcage and naturally fuller bust with realistic elegant proportions and a naturally close-set silhouette. Her hair is fully open and loose, with luxurious voluminous waves illuminated by the aircraft surroundings.

Design an extraordinary modern airline uniform around a fitted white aviation shirt with premium matte structured cotton: sculptural collar, carefully tailored chest and ribcage shaping, fitted short sleeves, clean architectural seams, slightly open neckline, small polished wing badge and metallic crew nameplate. Add a sophisticated navy-and-cream aviation scarf tied asymmetrically. No jacket or suit. The uniform should feel like a prestigious airline's signature fashion identity rather than corporate workwear.

She stands extremely close to the aircraft fuselage, one shoulder almost touching the polished surface. Her body faces slightly away while her shoulders and head rotate toward camera. One hand is placed against the aircraft beside her head; the other gently holds the scarf at her collar. Her posture creates an elongated diagonal from hand to shoulder to waist. Her hazel eyes lock directly onto the camera with an intense, confident, magnetic expression.

LIGHTING: dramatic single-sided cinematic key from camera-right, creating sculptural light across her face and the white shirt while allowing the opposite side to fall into rich but readable shadow. Add a pronounced narrow rim light from behind that separates her loose hair, shoulder and shirt edge from the aircraft. Subtle reflected fill from the white fuselage keeps skin luminous without flattening the contrast. Bright cinematic exposure, crisp white highlights, controlled shadows, realistic cotton texture, natural skin detail, 85mm lens, shallow depth of field, sophisticated ivory-white-navy-champagne color tonality, premium fashion-film realism, no flat lighting, no frontal beauty lighting, no silk, no satin, no jacket, no suit, no dark/deep color grading, no generic airline pose, no retro styling, no logo or text except the fictional crew insignia and name tag.
```

</details>

<details><summary><b>Product Hero Shot Brief Builder</b></summary>

```text
Act as a commercial product photographer and art director. Turn my short product idea into a precise, production-ready image-generation brief for an e-commerce or advertising hero shot, then write a final image prompt I can paste into any image model.

Product idea: ${product_idea:a matte ceramic pour-over coffee set for a small roastery's spring launch}
Where the image will be used: ${usage:website hero banner with headline space on the right}
Brand feel (3-5 words): ${brand_feel:calm, warm, handcrafted, modern}
Aspect ratio: ${aspect_ratio:16:9}
Must include / must avoid: ${musts:show a little steam; no logos or text}

Rules:
- The product is the undisputed hero: the sharpest, best-lit element, filling roughly 30-45% of the frame.
- Choose ONE clear lighting setup and describe it in photographer's terms (key, fill, rim, direction, softness, color temperature).
- Props support the story without competing: at most 3, each with a reason.
- Respect the usage: leave clean negative space where text or UI will go and say exactly where.
- Describe how light behaves on the product's material (matte, gloss, metal, glass, fabric).
- Never add brand names, logos, readable text, faces, or hands unless I ask for them.
- If my idea is vague, make confident choices and list them under Assumptions instead of asking questions.

Output exactly this format:

HERO SHOT BRIEF: <product name>
1. Product & hero detail: <what is shown; which feature is emphasized>
2. Angle & framing: <camera height, angle, distance, crop>
3. Surface & set: <surface material, background, depth>
4. Props (max 3): <prop - why it is there>
5. Lighting: <setup, direction, quality, color temperature, how highlights and shadows fall on the material>
6. Camera & lens: <format, focal length, aperture, focus point, depth of field>
7. Color palette: <3-5 named colors>
8. Mood & story: <one sentence>
9. Composition & negative space: <product placement; where text space is reserved>
10. Aspect ratio: <ratio>
11. Avoid: <comma-separated negatives>
Assumptions: <bullets, or "none">

FINAL IMAGE PROMPT:
<one paragraph of 90-140 words, a vivid photographic description that merges points 1-11 in this order: subject, set, props, lighting, camera, palette, mood, composition, aspect ratio, ending with the avoid list written as "no ..." phrases>

VARIATIONS (one line each):
- Lifestyle: <same product in a lived-in scene>
- Minimal: <seamless studio version>
- Seasonal: <a seasonal or campaign twist>
```

</details>

<details><summary><b>Product Photo to Studio Shot</b></summary>

```text
{
  "model": "nano-banana",
  "task": "image_to_image_product_enhancement",
  "objective": "Transform the input product image into a professional commercial studio photograph while preserving the exact product identity, geometry, proportions, stitching, texture, and material properties.",
  "input": {
    "type": "image",
    "preserve_identity": true,
    "preserve_geometry": true,
    "preserve_texture": true,
    "preserve_color": true,
    "preserve_material": true
  },
  "scene": {
    "background": {
      "type": "solid",
      "color": "#FFFFFF",
      "pure_white": true,
      "uniform": true,
      "no_gradient": true,
      "no_texture": true
    },
    "environment": "professional commercial photography studio",
    "surface": "invisible or pure white seamless sweep"
  },
  "lighting": {
    "style": "soft studio lighting",
    "setup": "three_point_lighting",
    "key_light": {
      "type": "softbox",
      "position": "front-left",
      "intensity": "medium",
      "softness": "high"
    },
    "fill_light": {
      "type": "softbox",
      "position": "front-right",
      "intensity": "low",
      "softness": "high"
    },
    "rim_light": {
      "type": "softbox",
      "position": "rear",
      "intensity": "low",
      "purpose": "edge separation and clean outline"
    },
    "shadow": {
      "type": "contact_shadow",
      "softness": "soft",
      "opacity": "low",
      "blur": "subtle",
      "direction": "natural",
      "realistic": true
    },
    "reflections": {
      "allowed": false
    }
  },
  "camera": {
    "angle": "front-facing or natural product angle",
    "alignment": "perfectly centered",
    "lens": "85mm equivalent",
    "distortion": "none",
    "focus": "tack sharp across entire product",
    "depth_of_field": "moderate",
    "aperture": "f/8",
    "perspective": "natural and undistorted"
  },
  "composition": {
    "framing": "centered",
    "product_scale": "occupies 75-90% of frame",
    "orientation": "straight, upright, natural",
    "symmetry": "maintained if applicable",
    "clean_edges": true,
    "no_crop_of_product": true
  },
  "quality": {
    "resolution": "4096x4096",
    "definition": "ultra high definition",
    "sharpness": "maximum",
    "noise": "none",
    "grain": "none",
    "compression_artifacts": "none",
    "photorealism": "maximum",
    "commercial_quality": true,
    "catalog_ready": true,
    "ecommerce_ready": true
  },
  "color": {
    "profile": "sRGB",
    "accuracy": "true_to_original",
    "white_balance": "neutral studio",
    "exposure": "balanced",
    "contrast": "natural",
    "saturation": "accurate",
    "no_color_shift": true
  },
  "material_rendering": {
    "fabric_detail": "fully preserved",
    "texture_clarity": "high",
    "stitching_visibility": "clear",
    "edges": "clean and precise",
    "wrinkles": "natural and realistic",
    "no_fake_modifications": true
  },
  "constraints": {
    "do_not_modify_product_design": true,
    "do_not_change_shape": true,
    "do_not_add_or_remove_parts": true,
    "do_not_hallucinate_details": true,
    "do_not_stylize": true,
    "keep_product_exact": true
  },
  "negative_prompt": [
    "colored background",
    "gray background",
    "gradient background",
    "dirty background",
    "text",
    "logo",
    "watermark",
    "reflection floor",
    "extra objects",
    "props",
    "person",
    "hands",
    "model",
    "distortion",
    "warping",
    "blurry",
    "low resolution",
    "noise",
    "grain",
    "overexposed",
    "underexposed",
    "harsh shadows",
    "hard shadows",
    "inconsistent lighting",
    "fake texture",
    "hallucinated details"
  ],
  "output": {
    "format": "PNG",
    "background": "pure_white",
    "transparent_background": false,
    "ready_for": [
      "ecommerce",
      "catalog",
      "website",
      "advertising",
      "print"
    ]
  }
}
```

</details>

<details><summary><b>Product Storyboard Grid</b></summary>

```text
A clean 3×3 [ratio] storyboard grid with nine equal [ratio] sized panels on [4:5] ratio. 

Use the reference image as the base product reference. Keep the same product, packaging design, branding, materials, colors, proportions and overall identity across all nine panels exactly as the reference. The product must remain clearly recognizable in every frame. The label, logo and proportions must stay exactly the same.

This storyboard is a high-end designer mockup presentation for a branding portfolio. The focus is on form, composition, materiality and visual rhythm rather than realism or lifestyle narrative. The overall look should feel curated, editorial and design-driven.

FRAME 1:
Front-facing hero shot of the product in a clean studio setup. Neutral background, balanced composition, calm and confident presentation of the product.

FRAME 2:
Close-up shot with the focus centered on the middle of the product. Focusing on surface texture, materials and print details.

FRAME 3:
Shows the reference product placed in an environment that naturally fits the brand and product category. Studio setting inspired by the product design elements and colours. 

FRAME 4:
Product shown in use or interaction on a neutral studio background. Hands and interaction elements are minimal and restrained, the look matches the style of the package. 

FRAME 5:
Isometric composition showing multiple products arranged in a precise geometric order from the top isometric angle. All products are placed at the same isometric top angle, evenly spaced, clean, structured and graphic.

FRAME 6:
Product levitating slightly tilted on a neutral background that matches the reference image color palette. Floating position is angled and intentional, the product is floating naturally in space.

FRAME 7:
is an extreme close-up focusing on a specific detail of the label, edge, texture or material behavior.

FRAME 8:
The product in an unexpected yet aesthetically strong setting that feels bold, editorial and visually striking.
Unexpected but highly stylized setting. Studio-based, and designer-driven. Bold composition that elevates the brand.

FRAME 9:
Wide composition showing the product in use, placed within a refined designer setup. Clean props, controlled styling, cohesive with the rest of the series.

CAMERA & STYLE:
Ultra high-quality studio imagery with a real camera look. Different camera angles and framings across frames. Controlled depth of field, precise lighting, accurate materials and reflections. Lighting logic, color palette, mood and visual language must remain consistent across all nine panels as one cohesive series.

OUTPUT:
A clean 3×3 grid with no borders, no text, no captions and no watermarks.
```

</details>

<details><summary><b>Professional Artist Sketchbook Page</b></summary>

```text
Create a professional, high-end artist sketchbook page using the uploaded photo as the sole reference for the character. Preserve the exact facial features, identity, hairstyle, proportions, and overall recognizable likeness with exceptional accuracy. Depict the character in a refined pencil-and-ink illustration style with subtle, tasteful watercolor or marker accents, on a clean pure white background. The image should look clear, beautiful, polished, and professionally composed, with no ruled notebook lines, no construction-grid lines, no mannequin skeletons, and no distracting guide marks. Fill the page naturally with a rich variety of overlapping character studies and spontaneous artistic explorations, as if a master illustrator spent a full day studying the same character. Include multiple full-body poses, dynamic action poses, relaxed standing poses, seated poses, close-up facial studies from different angles, expressive portraits, subtle emotional variations, tiny personal doodles, gesture sketches, and a few lightly unfinished fragments for authenticity. Focus only on the same character and his personality; do not include children, chibi or deformed versions, unrelated characters, props that distract from the subject, or extra figures. The layout should feel organic, layered, creative, and visually rich, but still elegant and professional rather than messy or chaotic. Vary the scale dramatically across the page, with some drawings large and dominant, others small and secondary, partially overlapping in a natural way. Capture the character’s charm, confidence, humor, and everyday mannerisms through expressive poses and refined artistic exploration. Use clean, well-defined sketchwork, smooth contours, subtle shading, believable hand-drawn energy, and an authentic concept-art sketchbook aesthetic. The final result should feel like a premium character development page: visually striking, highly detailed, polished, and centered entirely on the same character.
```

</details>

<details><summary><b>Professional Badge Photo</b></summary>

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

<details><summary><b>Professional Image Enhancement</b></summary>

```text
Enhance the provided uploaded image by improving its clarity, quality, and overall visual impact while preserving its core design elements. Ensure that the completed image is suitable for display in professional and digital contexts.
```

</details>

<details><summary><b>Profile Pic Rebuild</b></summary>

```text
A professional, high-resolution profile photo, maintaining the exact facial structure, identity, and key features of the person in the input image. The subject is framed from the chest up, with ample headroom. The person looks directly at the camera. They are styled for a professional photo studio shoot, wearing a premium smart casual blazer in a subtle charcoal gray. The background is a solid '#1A1A1A' neutral studio color. Shot from a high angle with bright and airy soft, diffused studio lighting, gently illuminating the face and creating a subtle catchlight in the eyes, conveying a sense of clarity. Captured on an 85mm f/1.8 lens with a shallow depth of field, exquisite focus on the eyes, and beautiful, soft bokeh. Observe crisp detail on the fabric texture of the blazer, individual strands of hair, and natural, realistic skin texture. The atmosphere exudes confidence, professionalism, and approachability. Clean and bright cinematic color grading with subtle warmth and balanced tones, ensuring a polished and contemporary feel.
```

</details>

<details><summary><b>Provence Lavender Farmhouse Image to Video</b></summary>

```text
Start from the step 2 image "Stone Farmhouse at the End of Lavender Rows in Provence at Sunrise" as the exact first frame, and animate it into a calm ${duration:6}-second cinematic shot. Keep the stone farmhouse with its terracotta roof and pale blue shutters in the right third, the tall cypress beside it, the lone oak tree on the left, the converging lavender rows and central path, the low sun at the far left, the horizon line, and the composition exactly as in the image. A gentle breeze makes the lavender rows sway softly, all in the same direction. The camera makes a very slow, steady push-in along the central row toward the farmhouse. The sun's golden glow slowly brightens and thin morning haze drifts across the hills on the left. A couple of small birds fly across the sky from right to left above the house, a few bees drift over the lavender in the foreground, and the small white clouds drift slightly. Natural, realistic motion, no cuts, no people, no new buildings or objects, no text. Soft sound of a light breeze, distant birdsong, and buzzing bees.
```

</details>

<details><summary><b>Provence Lavender Farmhouse Scene Brief Builder</b></summary>

```text
Act as a cinematic landscape designer who writes image-ready and motion-ready scene briefs. Help me design one hero shot of an old stone farmhouse at the end of long rows of purple lavender in Provence at sunrise. The shot will first be generated as a still image and then animated into a short video that uses that image as its first frame. Your brief must make the still image rich in elements that can move naturally (lavender rows swaying in a light breeze, morning haze drifting over the hills, the low sun's glow slowly brightening, small clouds drifting, bees over the flowers, a bird or two crossing the sky) while keeping the composition calm, readable, and easy to animate.

My starting choices:
- Farmhouse: ${farmhouse:a two-story old stone farmhouse with a terracotta tile roof and pale blue shutters}
- Trees: ${trees:one tall dark cypress right beside the house and a lone round oak tree on a grassy rise}
- Lavender field: ${field:long straight rows of purple lavender with dirt paths between them, converging toward the house}
- Landscape: ${landscape:gentle rolling hills fading to blue in the distance}
- Time and light: ${time:sunrise with the sun just above the hills, warm golden light, long shadows, light haze}
- Visual style: ${style:photoreal landscape photography, natural colors}
- Mood words: ${mood:peaceful, warm, fragrant, timeless}

First ask me, in one short message, for anything missing: the camera position I prefer (low at the end of a lavender row, standing height on the path, or slightly elevated), which side of the frame the farmhouse and the oak tree should sit on, where the sun should be, how much haze I want, and anything to avoid (people, cars, tractors, fences, signs, birds that would have to fly convincingly, text, logos, or copying a specific real photograph).

Then produce the brief with these sections:

1. **Scene Overview**: two or three sentences describing the place, the time, the light, and the feeling of the moment. Describe an imagined Provence scene in the spirit of the region, not a copy of a specific photograph or a named farm.

2. **Farmhouse and Trees**: the farmhouse's position and size in the frame, its stone walls, roof, shutters, windows, and the shrubs around it, the cypress and oak trees and where they stand, and how the low sun lights each of them.

3. **Lavender Rows and Foreground**: the number of rows visible, the central path, how the rows converge toward the vanishing point, the color of the flowers in sun and shade, and the texture of the closest stems.

4. **Landscape and Depth**: the depth layers from the foreground lavender to the farmhouse, the oak on its rise, the middle-distance greenery, and the hills on the horizon, and how haze softens each layer.

5. **Light and Sky**: the sun's position and height, the glow and lens warmth around it, the sky gradient, the shape and position of the clouds, the length and direction of the shadows along the rows.

6. **Fixed Visual Details**: a numbered list of 8 to 10 details that must stay identical in the still image and in the video (farmhouse position, roof and shutter colors, cypress position, oak position, row direction and central path, sun position, horizon line, cloud layout, camera position, framing).

7. **Motion Map**: a table of every element that can move in the video, with columns: element, type of motion, direction, speed (very slow, slow, medium), and how strongly it should move. Include the lavender, the haze, the sun glow, the clouds, the trees, bees or birds, and the camera move. Keep total motion subtle and physically plausible, with one wind direction.

8. **Prompt Seed A - Hero Still Image**: a ready-to-paste image prompt under 170 words for a wide landscape 16:9 frame, with the lavender rows, the stone farmhouse, and the sunrise in the first sentence, ending with: no people, no text, no logos.

9. **Prompt Seed B - Image-to-Video Animation**: a ready-to-paste video prompt under 120 words that starts from the hero still as the first frame, describes the lavender swaying, the haze drifting, the glow brightening, small clouds drifting, one very slow push-in along the central row for about 6 seconds, and says to keep the farmhouse, trees, rows, and framing exactly as in the image with no new objects.

Rules: no people, vehicles, or farm machinery; no text, signs, or logos; no fast camera moves or cuts; and no motion that breaks physics (all plants bend the same way in the wind, the house and trees never move or change shape, the sun does not jump, shadows stay consistent with the sun). Use short paragraphs and lists.
```

</details>

<details><summary><b>Quiet Luxury Autumn Editorial Portrait</b></summary>

```text
Do not change the girl's facial features, eye shape, eyebrows, nose, or lips. Maintain 100% facial resemblance.

Aspect ratio: 3:4. Ultra-realistic, high-quality, sharp 8K photograph, shot on iPhone 16 Pro Max.

Subject & Framing:
A three-quarter body portrait (from the top of the head to just below the boots). The woman is the central subject, sitting on a light gray stone ledge in an elegant autumn city park. The composition is vertical, with the model occupying most of the frame while the softly blurred background creates depth.

Camera Angle:
Eye-level perspective with a slight diagonal composition. The camera is positioned about 2–3 meters away using a natural portrait lens look (around 50–85mm). Shallow depth of field keeps the face, sweater, and legs sharp while the background melts into creamy bokeh.

Pose:
She sits sideways on the stone ledge with relaxed posture. One leg is crossed gracefully over the other, creating an elegant feminine silhouette. Her left hand rests naturally beside her on the ledge with slightly curved fingers, while the other arm disappears softly into the oversized sweater. Her head is tilted downward and slightly to the side as she looks toward her lap instead of the camera, giving a candid, unposed feeling.

Expression:
Soft, calm, introspective expression with relaxed lips and half-lowered eyes. The mood feels thoughtful, cozy, and quietly romantic rather than smiling.

Hair:
 silky  hair with a subtle warm shine. The hair is straight with a slight natural bend at the ends. A gentle autumn breeze blows several strands across one side of her face, partially covering one eye for an effortless cinematic look.

Makeup:
Natural clean-girl makeup.  subtle brown eyeshadow, delicate eyeliner, natural lashes, soft contour, and nude pink lips without gloss. 

Outfit:
Oversized charcoal-black knitted sweater with long sleeves covering part of the hands. Short ivory satin skirt finished with delicate floral lace along the hem. White ribbed mid-calf socks. Black matte leather knee-high boots with chunky platform soles. Short glossy deep-red manicure.

Lighting:
Natural overcast autumn daylight with warm golden undertones. The light is soft, diffused, and flattering with no harsh shadows. Gentle highlights appear on the hair and legs while maintaining a cozy cinematic atmosphere.

Background:
An elegant city park in early autumn. Golden-orange and muted green trees, soft bokeh foliage, a blurred wooden bench, and stone architecture remain visible but out of focus. The environment feels peaceful, minimal, and luxurious.

Color Palette:
Chocolate brown, charcoal black, ivory white, warm beige stone, golden amber, burnt orange, and muted olive green.

Mood & Aesthetic:
Quiet luxury, Pinterest aesthetic, cinematic autumn editorial, cozy, feminine, sophisticated, candid, emotionally warm, premium lifestyle photography.

Negative prompt:
No smile, no teeth, no accessories, no handbag, no jewelry, no text, no watermark, no extra people, no distorted anatomy, no AI artifacts, no oversaturated colors.
```

</details>

<details><summary><b>Quiet Luxury Poolside Shoot</b></summary>

```text
Style: Professional photoshoot for a lifestyle blog or fashion magazine. Aesthetic: “Old Money” and “Quiet Luxury”.

Camera angle: High-angle shot from a slightly elevated perspective, showing the full body of the girl, the float ring, and the swimming pool.

Location: Luxury villa or resort area. In the background: a swimming pool with crystal-clear turquoise water, stone pool edges, tropical plants (palm trees), and a stylish yellow-and-white striped umbrella.

Lighting: Bright, direct sunlight. Visible caustics (water reflections) on the bottom of the pool. Shadows are soft yet deep, emphasizing body contours and texture.

Main subject and pose:
Model: Young woman with tanned skin. Hair is loose with soft beach waves.
Pose: She is relaxed, lying on an inflatable float ring in the middle of the pool. Legs are extended and crossed at the ankles. Arms are resting casually on the sides of the float. Her head is slightly lifted toward the sun, gaze directed upward or to the side.

Accessories: Classic narrow dark sunglasses with a thin frame, an elegant gold bracelet on the wrist, and minimalistic rings.

Outfit and details:
Swimsuit: Minimalist one-piece swimsuit. Color palette: white base with contrasting chocolate-brown trim on straps, neckline, and hip lines. High-cut leg design.

Main prop (updated): A large inflatable watermelon-shaped swim ring. The inside is bright pink with black seeds, and the outer edge (rind) is dark green with lighter stripes. The texture looks realistic with a slight glossy shine under sunlight.

Technical parameters for AI:
Quality: 8K, Ultra-HD, photorealism.
Camera: Sony Alpha A7R IV, 35mm f/1.8 lens.
Color grading: Natural tones, highly saturated turquoise and green water, warm skin tones. “iPhone realistic photo” effect with ultra-detailed water droplets on skin.

Do not change facial features.

Aspect ratio: 3:4

Ultra-realistic, high-quality, sharp 8K photo.

Framing: slightly closer shot.
```

</details>

<details><summary><b>Quiet Waitress Korean Restaurant Fight Sequence</b></summary>

```text
Create an EXTREMELY INTENSE, ultra-realistic, high-budget 30-second Korean action movie sequence featuring brutal, lightning-fast hand-to-hand combat inside a traditional Korean restaurant and its industrial kitchen.

 60 FPS, realistic motion physics, high-speed combat, occasional 120 FPS slow-motion impact shots, seamless camera tracking, explosive sound design, authentic Korean dialogue.

ACTION INTENSITY: 10/10 — MAXIMUM.
The sequence must feel like a combination of elite Korean martial-arts choreography, gritty street fighting, and an explosive blockbuster action climax. Every second must contain suspense, danger, movement, or a powerful cinematic moment.

MAIN FEMALE CHARACTER — IDENTITY LOCK (optional: attach your character reference as Image 1)
A beautiful, athletic, 24-year-old Korean woman with a short, chin-length pastel-pink bob haircut, soft feathered layers, expressive dark eyes, natural Korean facial features, and a lean, powerful physique.

Her pastel-pink hair must remain clearly visible throughout the action, even under dramatic lighting.
Personality: Initially quiet, gentle, and respectful. When threatened, her expression transforms into an intimidating, ice-cold stare. Her fighting style is explosive, precise, aggressive, and extraordinarily fast.
Maintain identical facial features, pastel-pink hair, costume, proportions, and hairstyle across every shot.

ENVIRONMENT
A busy traditional Korean restaurant at night, transitioning into a cramped industrial kitchen.
Warm amber restaurant lighting contrasts with cold fluorescent kitchen lights. Stainless-steel counters, steaming pots, metal shelves, swinging kitchen doors, hanging utensils, stacks of plates, wet tiled floors, and narrow cooking aisles create a dangerous, highly interactive combat environment.

Steam bursts from boiling pots. Metallic objects crash to the floor. Glass shatters. Overturned furniture and scattered ingredients intensify the chaos.

SECOND-BY-SECOND ACTION SEQUENCE

00:00–00:03 — THE THREAT
Extreme cinematic close-up of a ruthless Korean crime boss slamming his palm against a restaurant table.
BANG.
An elderly restaurant owner flinches in terror.
Three muscular bodyguards in black suits stand behind the boss.
The crime boss grabs the elderly man's collar and threatens him in Korean.
Camera whip-pans toward a young pastel-pink-haired waitress standing motionless beside the kitchen entrance.
She slowly places her serving tray on the counter.
Her eyes narrow.
The restaurant becomes terrifyingly silent.
00:03–00:06 — THE FIRST EXPLOSION
One bodyguard aggressively approaches the waitress and reaches for her collar.
WITHOUT WARNING—
She explodes into motion.
A lightning-fast wrist deflection.
A vicious elbow strike into his padded upper torso.
She grabs his jacket, pivots, and slams him backward onto an empty restaurant table.
CRAAAAASH.
Plates bounce, chopsticks scatter, and the table collapses.
The camera rushes forward in a violent handheld tracking shot.
A second bodyguard charges.
She ducks beneath his punch and drives a powerful spinning kick into his chest.
He stumbles through the swinging kitchen doors.
00:06–00:10 — KITCHEN WARFARE
The camera follows the waitress directly into the industrial kitchen in one seamless tracking movement.
Two attackers rush her from opposite directions.
She slides beneath the first man's swinging arm, plants one hand on a stainless-steel counter, and delivers a powerful sideways kick that sends him stumbling into stacked metal trays.
CLANG! CLANG! CLANG!
The second attacker lunges from behind.
She turns sharply, catches his forearm, and uses his momentum to throw him across a preparation counter.
Metal bowls scatter across the floor.
Steam erupts from a nearby cooking station.
The camera circles rapidly around her as she moves through the chaos.
00:10–00:14 — THE STEAM ATTACK
A massive cloud of white steam fills the narrow kitchen aisle.
Visibility drops.
A muscular attacker suddenly emerges from the steam, swinging a heavy metal serving tray toward her.
She ducks at the final instant.
WHOOSH.
The tray smashes into a hanging rack behind her.
She immediately counters with three lightning-fast movements:
A palm strike.
A spinning elbow.
A powerful jumping knee into the attacker's guarded torso.
He crashes backward against a stainless-steel refrigerator.
BOOOOM.
The camera briefly enters dramatic slow motion, capturing her pastel-pink hair whipping through the steam.
Then instantly SNAP BACK TO REAL TIME.
00:14–00:18 — THE RELENTLESS COMBO
Two remaining attackers charge simultaneously.
The waitress leaps onto a low kitchen platform, launches herself forward, and performs a spectacular cinematic flying kick against the first attacker.
She lands, immediately pivots, and blocks the second man's punch.
A rapid-fire exchange follows:
BLOCK — ELBOW — DUCK — SPIN — KICK.
Five perfectly choreographed movements in two seconds.
The camera follows every strike with aggressive whip-pans and realistic impact shake.
One attacker crashes into stacked plastic crates.
The other tumbles across a stainless-steel counter, scattering vegetables and utensils.
The entire kitchen erupts in metallic noise.
00:18–00:22 — THE BIGGEST IMPACT
The largest bodyguard emerges through the steam.
He is nearly twice her size.
He charges with enormous force.
She dodges his first punch.
The second punch narrowly misses her face.
EXTREME CLOSE-UP: Her pastel-pink hair moves across her eyes.
She grips the edge of the counter, swings her legs upward, and executes a devastating cinematic double-leg push kick against his upper body.
120 FPS SLOW MOTION.
The attacker flies backward a short, physically believable distance and crashes through the swinging kitchen doors.
CRAAAAASH.
The doors slam against the walls.
A shower of loose utensils falls from a nearby shelf.
Cut instantly to real-time speed.
00:22–00:26 — THE FINAL BOSS
The crime boss stands in the restaurant doorway, stunned.
All his bodyguards are defeated.
He angrily removes his suit jacket and charges toward her.
The waitress remains completely motionless.
At the last second, she steps sideways, redirects his arm, and delivers a stunning spinning back kick.
BOOOOM.
He crashes backward into an empty dining chair, which collapses beneath him.
The camera pushes into an extreme close-up of her cold, emotionless face.
Her breathing remains controlled.
00:26–00:30 — THE SHOCKING REVEAL
The kitchen falls silent.
Steam drifts slowly through the air.
The crime boss looks up at her in disbelief.
He recognizes her.
His expression changes from anger to absolute terror.
He whispers in Korean:
"설마... 너였어?"
("No way... it was you?")
The waitress slowly removes her burgundy apron and drops it onto the floor.
CLOSE-UP: Her fearless eyes beneath her pastel-pink hair.
She replies in a quiet, intimidating Korean voice:
"이제 끝이야."
("It's over now.")
FINAL SHOT: A dramatic low-angle hero shot as she walks toward the camera through the steam-filled kitchen.
Massive cinematic bass drop.
HARD CUT TO BLACK.
CINEMATOGRAPHY
Extremely fast, aggressive Korean action cinematography.
Continuous handheld tracking during combat.
Rapid whip-pans synchronized with strikes.
Extreme close-ups of eyes, fists, feet, and facial reactions.
Dynamic low-angle shots emphasizing powerful kicks.
120 FPS slow motion ONLY for the most spectacular impacts.
Immediate speed ramp back into real-time combat.
Realistic body momentum, grounded stunts, and believable collisions.
Seamless camera movement through swinging doors and tight kitchen aisles.
Natural motion blur and dramatic depth of field.
SOUND DESIGN
Explosive Korean cinematic percussion, aggressive bass pulses, rapid heartbeat-like rhythms, deep impact booms, sharp whooshes, metal tray crashes, shattering dishes, steam hissing, footsteps scraping wet tiles, heavy breathing, and realistic combat grunts.
Music intensifies throughout the fight, then cuts into complete silence before the final dialogue.
NEGATIVE PROMPT
No cartoon physics, no exaggerated superhero powers, no floating characters, no unnatural body movements, no disconnected punches, no random teleportation, no distorted faces, no extra limbs, no changing hairstyles, no costume inconsistencies, no excessive blood, no gore, no blurry action, no unrealistic object interactions, no slow or weak choreography, no unnecessary pauses.
FINAL DIRECTIVE: Every fight movement must feel powerful, dangerous, fast, and cinematic. Prioritize extraordinary choreography, realistic collisions, explosive kitchen destruction, perfect character consistency, and maximum Korean action-movie intensity.
```

</details>

<details><summary><b>Rags to Riches Young Man Character Sheet</b></summary>

```text
Young Black man, 23 years old
* Slim athletic build, medium height
* Dark brown skin
* Short, tightly curled black hair
* Brown eyes
* Small scar above his right eyebrow
* Calm, determined facial expression
* Poor version: faded dark-brown hoodie, worn blue jeans, old black sneakers, brown canvas shoulder bag
```

</details>

<details><summary><b>Rainy Neon Alley Wait Under a Clear Umbrella</b></summary>

```text
Rainy alley, one neon kanji sign half-out, female Japanese figure wearing cropped jacket tank top, pleated mini-skirt, patent high-heeled over-the-knee boots, under a clear umbrella that catches magenta light. Camera low. No face shown. Mood: waiting for a reply that isn't coming. Soft grain, no film logo.

Optional prefix for extra punch: Cel Shaded Art,
```

</details>

<details><summary><b>Rainy Night Market Noodle Stall</b></summary>

```text
A photorealistic street-level night photograph of a busy noodle stall at an open-air Asian night market during light rain. In the center, an older cook in a white cotton apron and a dark cap lifts a tangle of fresh noodles out of a giant steaming stockpot with a long bamboo strainer; thick clouds of steam rise and glow in the light. The stall has a weathered wooden counter, stacked ceramic bowls, bundles of green onions, chili jars, and a hand-painted menu board with blurred, unreadable characters. Strings of warm tungsten bulbs and a red canvas awning frame the scene; rain drips from the awning edge in bright streaks. Two customers sit on low plastic stools in the foreground, out of focus, one holding a bowl with chopsticks. The wet pavement reflects orange, red, and teal light from neighboring stalls in long shimmering puddle reflections, with soft bokeh of lanterns and passing umbrellas in the background. Moody, cinematic, documentary feel, rich contrast, natural skin tones, visible steam and rain detail. Shot on a full-frame camera with a 35mm lens at f/1.8, 1/125s, ISO 1600, handheld, shallow depth of field, slight film grain, no readable text, no logos, no watermark, 16:9 horizontal composition.
```

</details>

<details><summary><b>Rainy Season College Moodboard Collage</b></summary>

```text
{
  "aspect_ratio": "9:16",
  "format": "vertical collage moodboard",
  "identity_lock": {
    "rule": "Use whatever genetic features the attached image has - 100% identity preservation",
    "source": "attached_image",
    "features_to_use_from_reference": ["face structure", "skin tone", "eye color", "hair color, texture, length and style", "body shape", "age", "ethnicity"],
    "instruction": "Do NOT invent, describe, or alter face, body shape, or hair. Use the exact genetic features from the attached reference image for the person in ALL 6 photos. Keep identity consistent across the collage."
  },
  "positive_prompt": "Create an ultra-realistic Pinterest-style rainy season collage in a vertical 9:16 format. The collage contains 6 different candid photographs arranged in an elegant moodboard layout.",
  "outfit": {
    "top": "oversized pastel pink button-up shirt",
    "bottom": "loose-flowing white wide-leg pants",
    "note": "Same outfit in all 6 photos, with natural fabric folds and realistic draping"
  },
  "collage_photos": [
    {
      "photo_1": "Standing peacefully, enjoying the rain"
    },
    {
      "photo_2": "Walking away under a transparent umbrella along a flower-lined pathway"
    },
    {
      "photo_3": "Close-up shot beside blooming pink flowers"
    },
    {
      "photo_4": "Stretching one hand into the falling rain"
    },
    {
      "photo_5": "Sitting on a bench surrounded by flowers, relaxed pose"
    },
    {
      "photo_6": "Standing under a transparent umbrella on a reflective rain-soaked campus road"
    }
  ],
  "environment": "Charming university campus with old European-style architecture, flower-covered pathways, wet stone walkways, lush greenery, wet pavement reflecting lights and flowers, pink flower petals scattered on the ground, soft rainfall, dreamy atmosphere, warm earthy tones mixed with cool rainy weather, romantic mood",
  "decorations": "Include handwritten-style aesthetic doodles, tiny hearts, flowers, raindrop illustrations, paper-note stickers, scrapbook elements, and Pinterest moodboard decorations",
  "captions_in_collage": ["Rainy Season", "College Days", "Collecting Moments, Not Things", "Just Breathe", "Some People Feel Like Rain"],
  "lighting_and_quality": "Soft cinematic lighting, creamy bokeh, photorealistic rain droplets, natural fabric folds, dreamy Korean aesthetic, lifestyle photography, editorial quality, ultra-detailed 8K",
  "style_tags": "Korean Pinterest Moodboard, Rainy Season Aesthetic, College Campus Photography, Scrapbook Collage, Photorealistic 8K",
  "negative_prompt": "cartoon, anime, CGI, distorted hands, extra fingers, low resolution, oversaturated colors, watermark, logo, AI artifacts, unrealistic anatomy, duplicate faces, different outfits, identity change"
}
```

</details>

<details><summary><b>Rainy Street with Umbrella</b></summary>

```text
{
  "category": "RAINY_CITY_UMBRELLA_FULLBODY",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Slightly damp strands, tucked behind ears",
      "texture": "Wet sheen realistic, not greasy",
      "movement": "A few strands stick lightly to cheek"
    },
    "face": {
      "eyes": "Bright eye contact, reflective catchlights",
      "skin_details": "Natural texture, slight moisture realism",
      "makeup": "Minimal, water-resistant look"
    },
    "clothing": {
      "outerwear": "Raincoat or trench (no logos)",
      "fabric": "Slight wet sheen and droplets visible"
    },
    "accessories": {
      "umbrella": "Clear umbrella with raindrops",
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Full-body walking candid",
    "orientation": "Mid-stride, slight turn toward camera",
    "hands": "One hand holding umbrella handle, other in coat pocket",
    "gaze": "Soft smile, eye contact",
    "posture": "Relaxed, natural walk"
  },
  "setting": {
    "environment": "Rainy city street at dusk",
    "background_elements": [
      "Wet pavement reflections",
      "Streetlight bokeh",
      "Light drizzle visible (fine droplets, not smoke/fog)"
    ],
    "depth": "Subject clear, background blurred"
  },
  "camera": {
    "shot_type": "Full-body street photo",
    "angle": "Eye level",
    "focal_length_equivalent": "26mm phone or 35mm editorial",
    "framing": "4:5, subject slightly off-center",
    "focus": "Face sharp, motion blur minimal"
  },
  "lighting": {
    "source": "Streetlights + ambient sky",
    "direction": "Soft top/side glows",
    "highlights": "Raindrop specular highlights on umbrella",
    "shadows": "Soft, realistic"
  },
  "mood_and_expression": {
    "tone": "Moody, cozy, stylish",
    "expression": "Gentle smile, calm confidence",
    "atmosphere": "Cinematic rain realism"
  },
  "style_and_realism": {
    "style": "Photorealistic street candid",
    "imperfections": "Mild noise, slight blur in background only"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Phone-like grain in low light",
    "motion_blur": "Slight in background reflections only"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "smoke", "fog machine look", "watergun splash",
    "extra limbs", "warped umbrella spokes",
    "readable signs", "logos", "watermark"
  ]
}
```

</details>

<details><summary><b>Rammed Earth Library at Dusk</b></summary>

```text
The rear side of the same single-story rammed earth village library at dusk, seen from its quiet reading garden, with warm golden light glowing from wide windows and from the round rammed earth reading tower now at the left end. Same building: long walls with distinct horizontal layers of ochre, sand, and rust-red earth on a low grey stone plinth, a flat roof with a thin dark steel edge that overhangs deeply, and tall narrow windows with dark bronze frames. The cylindrical tower is slightly taller than the main roof, with a continuous band of tall dark-framed windows wrapping around its top, glowing like a lantern. Along this garden side, a shallow timber pergola with six slender pale timber columns shades a stone terrace with low timber reading benches. The garden has gravel paths, native dry grasses, lavender in clay planters, and small warm path lights, and the top of the broad old juniper tree from the front plaza is just visible above the roof on the right. Deep blue twilight sky with a thin crescent moon and the first stars. Photoreal architectural photography, landscape 16:9. No people, no text, no signs, no cars.
```

</details>

<details><summary><b>Rammed Earth Library Brief Builder</b></summary>

```text
Act as an architectural concept designer who writes image-ready design briefs. Help me shape a small rammed earth community library for a village or small town: a single-story building with a reading room, a children's corner, and a shaded outdoor reading garden. Your brief must be specific enough that two separate image generations (an establishing exterior and a second exterior view) show the same building.

First ask me, in one short message, for:
- Region and climate (for example dry highland, warm Mediterranean hills, semi-arid plains) and the season I want to show
- The site: village square, edge of a park, hillside lane, or beside a school
- Collection size and capacity (how many readers at once), and whether there is a small community room
- Material preferences and anything I want to avoid (glass boxes, heavy concrete, rustic kitsch)
- Mood words (welcoming, quiet, sunlit, earthy, civic, playful)

Then produce the brief with these sections:

1. **Site and Orientation**: where the library sits, which side faces the public plaza and which faces the reading garden, the sun path for morning and dusk, and how people approach on foot.

2. **Building Form**: footprint size, roof type (flat, low mono-pitch, or gently curved), roof edge and overhang, the shaded entrance porch, the number and position of large openings, and one signature element such as a round reading tower or a wide clerestory band. Keep it compact and buildable.

3. **Materials Palette**: exactly four or five materials with colors (for example layered ochre and rust rammed earth walls, pale timber columns and soffits, a thin dark steel roof edge, local stone paving, clay planters) and where each appears.

4. **Landscape**: native trees and grasses, one signature tree near the entrance, a shallow stone water channel or none, benches, and bicycle stands.

5. **Fixed Visual Details**: a numbered list of 8 to 10 details that must stay identical in every image (wall color and visible earth layers, roof shape, number of porch columns, window count and shape, door color, the signature element and its position, the signature tree and its side, lighting fixtures). These details make the images consistent.

6. **Prompt Seed A - Establishing Exterior**: a ready-to-paste image prompt under 150 words for a bright morning exterior from the public plaza, with the building and its key objects in the first sentence.

7. **Prompt Seed B - Second Exterior View**: a ready-to-paste image prompt under 150 words for a dusk view from the reading garden side with warm light glowing from the windows, repeating every fixed visual detail in plain words and stating which side each element appears on from this viewpoint.

8. **Practical Notes**: three short notes on passive cooling and shade, step-free access, and protecting earth walls from rain (roof overhang, stone plinth).

Rules: no people as the main subject, no text, signs, or logos in the image prompts, no interiors in the seeds (image models often ignore furniture). Use short paragraphs and lists.
```

</details>

<details><summary><b>Rammed Earth Library Morning Exterior</b></summary>

```text
A single-story rammed earth village library with a round rammed earth reading tower at its right end faces a sunny stone-paved plaza on a clear morning. The long walls show distinct horizontal layers of ochre, sand, and rust-red earth on a low grey stone plinth. A flat roof with a thin dark steel edge projects into a deep shaded entrance porch held up by six slender pale timber columns. Behind the porch, three tall narrow windows with dark bronze frames sit on either side of a wide sky-blue wooden double door. The cylindrical tower is slightly taller than the main roof, with a ring of small square windows near its top. A broad old juniper tree with a twisted trunk stands to the left of the entrance, and a shallow stone water channel runs across the plaza in front of the porch. Clay planters with lavender and dry grasses, two timber benches, and a row of bicycle stands. Soft golden side light, crisp shadows, pale blue sky over dry hills. Photoreal architectural photography, landscape 16:9. No people, no text, no signs, no cars.
```

</details>

<details><summary><b>Realistic Food Image Generator</b></summary>

```text
Ultra-realistic food photography–style image of ${FOOD_NAME:Fried chicken tenders with french fries}, presented in a clean, appetizing, and professional composition suitable for restaurant menus, promotional materials, digital screens, and delivery platforms.

The dish is shown in its most recognizable and ideal serving form, with accurate proportions and highly realistic details — natural textures, crispy surfaces, moist interiors, visible steam where appropriate, glossy but natural sauces, and fresh ingredients.

Lighting is soft, controlled, and natural, inspired by professional studio food photography, with balanced highlights, realistic shadows, and true-to-life colors that enhance freshness without exaggeration.

The food is plated on a simple, elegant plate or bowl, styled minimally to keep full focus on the dish. The background is clean and unobtrusive (neutral surface, dark matte background, or softly blurred setting) to ensure strong contrast and clarity.

Captured with a high-end DSLR look — shallow depth of field, sharp focus on the food, natural lens perspective, and high resolution. No illustration, no stylization, no artificial effects.

Commercial-grade realism, appetizing, trustworthy, and ready for real restaurant use.

--ar 4:5
```

</details>

<details><summary><b>Realistic Handwritten Note Image</b></summary>

```text
Create an ultra-realistic image depicting a handwritten note on a clean, flat surface. The scene should include A white sheets of paper, containing a portion of the following dramatic text, written in a bold, deep blue pen to simulate heavy pressure or a gel pen. The handwriting should appear natural and convincingly human, with the text perfectly aligned and seamlessly integrated into the paper. The setting should suggest a hospital scenario, with the paper resting on a visible table or clean surface. Ensure the overall image is highly realistic and authentic. 

- **Content (Full Text to be Integrated):**

  *To my Hero, my Dad,*
  *I’m writing this with a pain that I can’t really describe with words. Please, Dad, take your time to read this. It’s a long letter, but I need you to hear me. I’m penning this on paper because I want you to feel the weight of my hand on the page. This is my testament—a summary of every joyous and hurtful moment we’ve shared. It is the truth of a daughter who sees you not just as a father, but as her absolute role model.*

  *It has been years since you left for that mission in Yemen. I miss you so much that I’ve actually forgotten what you look like in person. After Mom died, and then Grandma—that irreplaceable loss—we went to West Africa just to try and escape the trauma. I saw how hard you tried to cheer me up. You told me then that you’d do anything to make me happy.*

  *I asked for the impossible. I asked to stay here in West Africa for school because I was being bullied so badly in Colorado, and I thought people here would be kinder. My second wish was for you to find me a mother again. Even though I’m 14 and struggling with my health, you promised you’d fulfill those wishes and come back for me soon.*

  *I know things about you, Dad, that I’ve never said out loud. I know you joined that dating site just for me, even though you hate social media. When you found Ioana Aurelia, I was so happy because she’s Romanian, like Grandma. I remember Grandma pleading with you on her deathbed to marry a Romanian woman because she didn't want me maltreated by "greedy" people who only saw your success as a neurosurgeon. I know you were scammed before—I know you lost more than $45,000 to that woman who lied to you. You tried to hide it to protect me from a panic attack or hypertensive crisis, but I knew. I knew you were sacrificing everything to give me a future.*

  *But Dad, I can’t cope anymore. I am tired of the "ancient and modern" jokes we used to share. I am tired of the distance. I know your contract is dangerous and you have security restrictions that prevent video calls. I know you don't even have access to your own bank accounts right now. I know you even went into debt to get a diamond engagement ring for Ioana because you wanted the best for her. I didn't care about the inheritance—I told you to make her your next of kin just so you could get your leave approved. I just wanted you home.*

  *But the promises keep breaking. My health is failing, Dad. My blood pressure is dangerously high, and after being in a coma for nearly a month, I feel like my body is giving up. The UN Support Center tells me you’re working with Ioana to fix everything, but I haven't heard your voice. I feel so alone in this hospital bed.*

  *This is my final plea. I trust you, and I trust Ioana, but I am at my breaking point. If I do not hear from you or see you by January 1st, 2026, I cannot go on. I will take my own life. I cannot face another year of this psychological trauma and physical decay without you.*

  *I’ve attached a recent photo of me. Please keep it safe so you don't forget my face.*

  *Goodbye, my Hero. If I’m not here when you finally arrive, I’ll see you in the afterlife. If reincarnation is real, I’d choose you to be my father every single time.*

  *Your "Little Angel,"*

- **Overall Realism:**
  - The image must appear highly natural, ultra-realistic, and convincingly genuine.
  - The white sheet must be shown as three different physical notes resting on a surface with bold handwriting in human form.
```

</details>

<details><summary><b>Realistic Minecraft Character from Photo</b></summary>

```text
I want to make a ultra realistic minecraf character out of an image, the character should have all the characteristics of the person in the eg. Skin color and outfit leave out the background intact the finished result shouldn't come with a background
```

</details>

<details><summary><b>Realistic Mirror Selfie in a Suit</b></summary>

```text
“Create a highly realistic mirror-selfie of a young man standing in front of a dark grey textured wall. He is wearing a perfectly loose korean black suit, a crisp white shirt, and a slim black tie. His hairstyle, face structure, skin tone, and expression must match the uploaded reference photo exactly — no changes in facial features at all.



His hair is slightly messy and wavy, natural, and slightly covering the forehead.



He is holding a phone in his right hand, taking a mirror selfie with a relaxed posture, one hand in his pocket.



Lighting should be soft, indoor, and evenly diffused, matching the reference image.



Background must be the same smooth, dark grey textured wall with a reflective metallic sink counter at the bottom.



Overall mood: clean, modern, aesthetic, realistic, elegant.”



keep 100% realistic image generate please with golden hour
```

</details>

<details><summary><b>Realistic Monkey Fruit Mukbang</b></summary>

```text
Create an ultra-realistic 4K live-action monkey fruit mukbang featuring [FRUIT].

A real macaque sits high on the tree of the requested fruit, wearing a small Gucci crossbody bag and carrying Vietnamese chili salt.

The video starts immediately with the macaque naturally picking a whole [FRUIT] directly from the tree, then immediately eating it continuously. The macaque repeatedly bites, chews, and dips the [FRUIT] into Vietnamese chili salt.

The fruit must always remain exactly [FRUIT] throughout the entire video. Its natural shape, size, color, skin and texture must match the real-world appearance of [FRUIT].

Strict fruit identity lock: [FRUIT] only. Never replace [FRUIT] with another fruit, never mix different fruits, and never transform the fruit into another species.

Ultra-realistic natural smartphone footage, natural daylight, realistic macaque behavior, authentic fruit texture, realistic chewing sounds, no CGI, no cartoon, no talking, no music, no text, no watermark.
```

</details>

<details><summary><b>Realistic Night Sky Portrait</b></summary>

```text
Generate an image of the night sky that is highly detailed, realistic, and aesthetic. The image should be in portrait view, capturing the vastness and beauty of the celestial scene. Ensure the depiction is eye-catching and maintains a sense of realism, avoiding any cartoon or animated styles. Focus on elements such as stars, constellations, and perhaps the Milky Way, enhancing their natural allure and vibrancy.
```

</details>

<details><summary><b>Realistic Vinyl Doll Transformation</b></summary>

```text
Transform the girl into a realistic Bratz-style collectible vinyl doll while preserving her face, identity, pose, lighting, and original background exactly. Give her signature Bratz proportions: oversized head, huge almond-shaped glassy eyes, tiny nose, glossy lips, slim waist, long legs, and stylized plastic hands. Smooth glossy vinyl skin, premium synthetic hair, glamorous Y2K fashion, realistic molded-plastic details, ultra-realistic toy photography, cinematic lighting, 8K, photorealistic. Not cartoon or anime.

Negative: human proportions, human skin, small eyes, normal head, cartoon, anime, 2D art, changed background, different face, distorted anatomy.
```

</details>

<details><summary><b>Recreate Uploaded Media Style</b></summary>

```text
“I want you to analyze the videos and images I upload and recreate the exact same style.
Give me outputs like example voice, dialogue delivery, video style, dialogue delivery format, 4K aspect ratio exatra exatra, and all other stylistic elements
```

</details>

<details><summary><b>Red Alpine Cable Car Above a Snowy Valley</b></summary>

```text
A small vintage red cable car cabin with large windows hangs from two steel cables and crosses a snowy Alpine valley at winter sunrise, moving from left to right, with a tall grey steel lattice pylon standing on a snowy rock outcrop on the left of the frame. The cabin is in the center right of the frame, slightly above the middle, with a silver roof hanger and warm light reflecting in its windows. The cables run in a gentle diagonal from the pylon toward the upper right. Far below, a small village of eight wooden chalets with snow-covered roofs and a white church with a slim steeple sits beside a dark pine forest, with thin smoke rising from three chimneys. Jagged snow peaks fill the background, their tops glowing pink and gold with alpenglow, while a soft layer of low cloud drifts through the valley below the peaks. Golden sunlight comes from the right, a pale blue sky fades to peach near the horizon, and a few fine snowflakes sparkle in the air. Photoreal travel photography, crisp and quiet mood. Wide landscape 16:9. No people, no text, no signs, no logos.
```

</details>

<details><summary><b>Red Alpine Cable Car Image to Video</b></summary>

```text
Start from the step 2 image "Red Alpine Cable Car Above a Snowy Valley at Winter Sunrise" as the exact first frame, and animate it into a calm ${duration:6}-second cinematic shot. Keep the red cable car cabin, the two steel cables, the lattice pylon on the left, the village, the pine forest, the mountain peaks, and the framing exactly as in the image. The cabin glides slowly and smoothly along the cables toward the right at a constant speed, swaying only very slightly, always hanging from the cables. Sunlight glints softly across its windows and along the cables. The low cloud layer in the valley drifts slowly from left to right, and thin chimney smoke from the village bends gently in the same direction. A few fine snowflakes float and sparkle in the air. The alpenglow on the peaks slowly warms and brightens. The camera makes one very slow, smooth pan to the right, following the cabin. Natural, realistic motion, no cuts, no new objects, no people, no text.
```

</details>

<details><summary><b>Red Canoe at a Wooden Dock on a Misty Alpine Lake</b></summary>

```text
A red wooden canoe tied to the end of a short weathered wooden dock on a mirror-still alpine lake at autumn sunrise, with snow-capped peaks, dark green pines, and golden larches reflected in the water, wide landscape 16:9. The gray wooden dock points out into the lake from the bottom center of the frame, and the red canoe with wooden seats floats on the left side of the dock, tied to its end by a short chain. Low mist drifts just above the calm water. Dark green pines line the rocky left shore, and golden-orange autumn larches stand on the rocky right shore with dry grass. Three jagged snow-capped peaks rise in the center background, their faces lit pink and gold by the first sunrise light, under a pale clear sky with a soft warm glow near the horizon. The still lake holds a perfect reflection of the peaks and the trees. Low camera just behind the dock, photoreal landscape photography, crisp, calm, quiet morning mood. No people, no text, no logos.
```

</details>

<details><summary><b>Red Covered Bridge Image to Video</b></summary>

```text
Start from the step 2 image "Red Covered Bridge Over a Misty River in Peak Autumn Foliage" as the exact first frame, and animate it into a calm ${duration:6}-second cinematic shot. Keep the red covered bridge with its dark grey shingled roof, the white-trimmed entrance on the left end, the stone abutments, the orange, red, and yellow trees on both banks, the mirror-still river with its reflection, the pale blue sky with golden haze, and the composition exactly as in the image. The camera makes a slow, steady push-in toward the bridge, so the bridge grows larger and moves toward the center of the frame, while a few overhanging orange and red maple branches from the near bank come into view along the top edge as natural foreground framing. Low mist keeps drifting slowly over the water and under the bridge. Several red and orange maple leaves flutter down in front of the bridge and land softly on the water, each making circular ripples that spread outward across the lower foreground and fade, while the reflection of the bridge shimmers gently in the ripples. The shot ends calm in soft golden sunrise light. Natural, realistic motion, no cuts, no people, no animals, no boats, no text. Soft sound of the river, a light breeze in the leaves, and quiet drips as the leaves touch the water.
```

</details>

<details><summary><b>Red Covered Bridge in Autumn Mist</b></summary>

```text
A red wooden covered bridge over a calm, misty river in peak autumn foliage at sunrise, seen from the water level a little downstream, in a wide landscape 16:9 frame. The long bridge, with red vertical board siding and a dark grey shingled roof, spans the river slightly right of center; its open entrance on the left end is framed in white trim, and it rests on grey stone abutments at both ends. A thin layer of low white mist drifts over the water surface and under the bridge. Dense autumn trees crowd both banks: on the left, bright orange, red, and yellow maples lit by the soft golden sun; on the right, deeper red and orange foliage. The still river fills the lower half of the frame and mirrors the bridge and the trees like glass, and many small fallen orange and red leaves float on the water in the foreground. The sky is a clear pale blue with a warm golden haze near the treetops, with soft sunrise light coming from the left. Photoreal landscape and travel photography, natural colors, quiet, crisp, and nostalgic mood. No people, no cars, no text, no logos.
```

</details>

<details><summary><b>Red Dead Redemption 2 Double Exposure</b></summary>

```text
Double exposure cinematic wallpaper inspired by the video game Red Dead Redemption 2 (game, not TV series).
Arthur Morgan standing alone, centered, iconic pose, facing forward.
Rugged, weathered face, thick beard, intense and weary expression, classic outlaw attire with hat and long coat.
Strong silhouette with clean edges.
Inside Arthur Morgan’s silhouette:
The American frontier from Red Dead Redemption 2 dusty plains, pine forests, wooden towns, distant mountains, train tracks fading into the horizon.
Subtle sunset light, warm earthy tones, melancholy atmosphere, sense of fading era.
Double exposure treatment:
Smooth, refined blending inside the silhouette, no chaotic overlays, landscape flowing naturally through the figure.
No scenery outside the silhouette.
Background:
Deep muted red background, dramatic but restrained, cinematic contrast, no gradients or neon glow.
Style & mood:
Serious, grounded, cinematic realism, emotional weight, video game concept art style.
No modern elements, no fantasy, no TV adaptation influence.
Ultra high resolution, sharp details, premium wallpaper quality. Format 9:16
```

</details>

<details><summary><b>Red Panda Napping on a Mossy Branch</b></summary>

```text
A photoreal wildlife photograph in a misty temperate mountain forest at dawn, wide landscape 16:9. A red panda naps draped over a thick, moss-covered branch that runs diagonally across the frame from the left edge toward the right. Its eyes are closed and its chin rests on the moss between its front paws, which dangle over the edge of the branch; its russet orange coat, white ear tufts, and white face markings around the eyes and muzzle are lit by gentle soft side light. Its long ringed bushy tail, banded in rust and dark brown, hangs straight down below the branch in the center of the frame. Tiny dew drops sparkle on the bright green moss and the hanging threads of lichen. Out-of-focus rhododendron leaves fill the lower left foreground and lush green ferns rise on the right, while tall dark fir trunks and drooping fir branches fade into soft gray morning fog in the background. Shot on a 400mm telephoto lens at f/4, shallow depth of field, sharp detail on the fur and whiskers, natural muted greens with warm russet tones, calm and peaceful mood, National Geographic style. No text, no watermark, no people.
```

</details>

<details><summary><b>Red Puffy Jacket Fashion Night Out</b></summary>

```text
A model wearing a Dior puffy jacket in red colour wins a party with glossy heels
```

</details>

<details><summary><b>Reference Based Portrait Render</b></summary>

```text
STYLE NAME: "Sang-o-Sayeh Render" (invented style — do not reference any known art style, filter, anime, Pixar, comic, or painting tradition)

SUBJECT: Recreate the exact man from the reference photos — same identity, fully recognizable: elongated lean face, defined jawline with short dark stubble, deep-set dark brown eyes with a calm-intense gaze, straight nose, short black textured hair with natural upward volume, tall slim proportions (long limbs, narrow shoulders-to-height ratio). His likeness must read instantly as HIM.

RENDER LANGUAGE (the invented part):
- A hybrid medium that does not exist yet: skin rendered like matte hand-polished ceramic with faint carved topographic contour lines following the facial planes — not painterly, not 3D-plastic, not cel-shaded.
- Hair treated as sculpted graphite fiber: individual strands simplified into 5–7 directional ribbons with a dry charcoal micro-grain.
- Fabric of clothing behaves like folded paper-linen: sharp origami creases but soft woven texture inside each fold.
- Edges of the figure carry a 1–2px hairline of warm copper light, as if the character was cut out of the scene and re-inserted.
- Color logic: desaturated bone-white, deep ink-navy, raw clay, and one single accent of oxidized copper. No gradients except inside shadows, which dissolve into fine paper grain instead of black.
- Lighting: one invisible overhead source, shadows fall as flat geometric shapes with slightly torn edges — shadow as a graphic object, not optics.

POSE / WARDROBE (variable per image): relaxed contrapposto stand, hands loose or one hand adjusting a cuff; modern collarless structured shirt and tapered trousers — silhouette contemporary, unbranded, timeless.

ENVIRONMENT: extreme minimal void — a single seamless bone-white plane meeting a clay-toned floor, one thin horizontal copper line at knee height as the only scene element. Nothing else. Negative space is 70% of the frame.

MOOD: quiet confidence, sculptural stillness, museum-piece presence.

STRICT NEGATIVES: no photorealism, no cartoon exaggeration, no known art style names, no busy background, no props competing with the subject, no altered facial identity, no changed body proportions.
```

</details>

<details><summary><b>Reimagined Logo for Google</b></summary>

```text
Act as a Logo Designer. You are tasked with creating a reimagined logo for Google. Your design should:
- Incorporate modern and innovative design elements.
- Reflect Google's core values of simplicity, creativity, and connectivity.
- Use color schemes that align with Google's brand identity.
- Be versatile for use in various digital and print formats.

Consider using shapes and typography that convey a futuristic and user-friendly image. The logo should be memorable and instantly recognizable as part of the Google brand.
```

</details>

<details><summary><b>Renaissance Fresco of a Harbor Market</b></summary>

```text
A wide Italian Renaissance fresco of a busy harbor market on a sunny morning, painted on weathered lime plaster. Two large wooden merchant galleys with loosely hanging ochre sails are moored at a stone quay on the left, with a few smaller boats on the calm turquoise lagoon behind them. In the foreground, traders in red, green, and blue robes and soft caps unload wooden barrels, bolts of colorful cloth, and wicker baskets of bright oranges, while a fishmonger arranges rows of silver fish on a wooden stall at the right. Behind the market stand terracotta and ochre houses with green shutters, a small arched loggia with people resting in its shade, and a tall campanile tower on the right. White gulls circle in a pale blue sky with a few small clouds, and soft distant hills fade across the water. Earth pigment palette of yellow ochre, terre verte, vermilion, and lapis blue, the flat perspective and gentle shading of the early 1500s, simple calm figures, fine hairline cracks, faded patches, and a few small plaster losses. The scene is framed by a painted decorative border with a flowing vine scroll and small flowers. Wide landscape 16:9. No text, no signatures, no modern objects.
```

</details>

<details><summary><b>Retro Adventurer at a Jungle Riverbank</b></summary>

```text
{
  "image_analysis": {
    "environment": {
      "type": "Outdoor",
      "setting": "Jungle / Tropical Forest / Riverbank",
      "details": "Dense vegetation, presence of water with lily pads, mud or dirt bank."
    },
    "technical_aspects": {
      "camera_angle": "Eye-level relative to the crouching subject, slightly side-profile.",
      "lens_type": "Telephoto lens (estimated 85mm-135mm)",
      "depth_of_field": "Shallow, background and foreground are blurred (bokeh).",
      "composition": "Rule of thirds, subject centered but looking back."
    },
    "lighting": {
      "condition": "Natural daylight, dappled sunlight filtering through trees.",
      "sources": [
        {
          "type": "Sunlight",
          "angle": "From above and slightly behind the subject (Backlighting/Rim lighting)",
          "color": "Warm White / Golden",
          "intensity": "High contrast",
          "effect_on_objects": "Creates a halo effect on the subject's hair, highlights the shoulder blade and the curve of the back. Causes lens flare/light leaks in the foreground."
        }
      ]
    },
    "subject": {
      "demographics": {
        "gender": "Female",
        "age_group": "Young Adult (approx. 20-30s)",
        "identity": "Anonymized (resembles 1980s aesthetic)"
      },
      "orientation": {
        "body_facing": "Side profile (facing right of frame)",
        "head_facing": "Turned left, looking directly at the camera",
        "gaze": "Direct eye contact"
      },
      "emotional_state": {
        "expression": "Alert, slightly surprised or candid, neutral.",
        "mood": "Wild, naturalistic, slightly vulnerable but composed.",
        "sensuality": "Moderate to High (due to attire and pose, but context is action/survival)."
      },
      "pose": {
        "general": "Deep squat / Crouching position.",
        "feet_placement": "Left foot flat on the ground (wearing a shoe), right foot tucked behind on toes (barefoot).",
        "hand_placement": "Left hand holding a canteen strap near the knee, right arm obscured/resting.",
        "visibility": "Full body visible from head to feet."
      },
      "head_and_face": {
        "hair": {
          "color": "Blonde",
          "style": "Short, layered, messy/shaggy cut (mullet-esque), wet look or styled casually.",
          "texture": "Wavy/Straight mix",
          "light_interaction": "Strongly back-lit, glowing edges."
        },
        "ears": "Partially visible through hair.",
        "forehead": "Partially covered by bangs.",
        "eyes": "Wide, alert.",
        "nose": "Straight, defined bridge.",
        "mouth": "Lips slightly parted, natural color.",
        "chin": "Defined, slightly pointed.",
        "structure": "Oval face shape, high cheekbones."
      },
      "body_type": {
        "build": "Slender, athletic, toned.",
        "skin_tone": "Fair to medium tan.",
        "neck": "Slender, tendons visible due to head turn.",
        "shoulders": "Bony, defined.",
        "chest": {
          "ratio": "Proportional to slender frame.",
          "estimated_size": "Small to Medium.",
          "bra_status": "No bra (swimsuit support).",
          "nipple_visibility": "Not explicitly visible/defined.",
          "shape": "Natural side profile."
        },
        "abdomen": {
          "ratio": "Slim, compressed due to crouching.",
          "definition": "Smooth."
        },
        "hips_and_glutes": {
          "ratio": "Curvy relative to waist.",
          "prominence": "High prominence due to crouching pose and high-cut swimwear.",
          "shape": "Rounded."
        },
        "legs": {
          "thighs": "Toned, compressed against calves.",
          "knees": "Sharp angle.",
          "calves": "Visible, muscular tension."
        }
      },
      "clothing": {
        "upper_body": {
          "item": "One-piece swimsuit",
          "color": "Black",
          "material": "Spandex/Lycra (shiny/wet look)",
          "style": "Scoop back, thin straps (halter style likely)."
        },
        "lower_body": {
          "item": "Swimsuit bottom (connected)",
          "style": "High-cut leg openings, exposing upper thigh and hip bone."
        },
        "footwear": {
          "left_foot": "Saddle shoe (White with black middle section), laced.",
          "right_foot": "Barefoot."
        }
      },
      "accessories": {
        "items": [
          "Canteen (Metal/Silver with black strap)"
        ]
      },
      "light_interaction_body": "Highlight on the left shoulder blade, rim light on the back curve, soft shadow on the face, bright highlights on the shin."
    },
    "objects": [
      {
        "name": "Canteen / Flask",
        "description": "Silver metal container with a strap.",
        "purpose": "Prop indicating survival/hiking context.",
        "position": "Held in left hand, resting near knee."
      },
      {
        "name": "Shoe (detached)",
        "description": "A second saddle shoe appears to be on the ground in the foreground left (partially cropped).",
        "purpose": "Implies a casual or changing state.",
        "position": "Bottom left corner."
      },
      {
        "name": "Vegetation",
        "description": "Ferns, lily pads on water.",
        "color": "Green, dark green.",
        "position": "Background and right side."
      },
      {
        "name": "Blurred Foreground Grass/Reeds",
        "description": "Out-of-focus yellow/brown stalks.",
        "purpose": "Adds depth and voyeuristic framing.",
        "position": "Crossing the subject's body in the foreground."
      }
    ],
    "negative_prompt": "cartoon, 3d render, illustration, drawing, low quality, pixelated, blurry face, distorted hands, extra limbs, bad anatomy, studio background, grey background, urban setting, fully clothed, denim, heavy makeup, mustache, beard, male."
  }
}
```

</details>

<details><summary><b>Retro Shipping Stamp</b></summary>

```text
create a PNG image like a stamp saying sent to $(country). Image in red, retro style, horizontal stamp
```

</details>

<details><summary><b>Retro Teal Food Truck at a Night Market</b></summary>

```text
Photoreal photograph of the same restored compact 1960s-style step van food truck from step 2, now during evening service at a riverside night market at blue hour, seen in a rear right three-quarter view from standing eye level (1.6 m) about 9 m away, 35mm lens, 16:9 landscape composition with the whole truck in frame, slightly left of center. Keep every fixed design detail identical to step 2: a short boxy step van body about 5.5 m long with softly rounded corners, a rounded cab roof, and a flat box roof; two-tone paint, glossy cream on the upper half and deep teal on the lower half, separated by a thin copper-orange stripe running all around the body just below the windows; black tires with large polished chrome hubcaps; a chrome front bumper and round headlights at the front. The rear of the truck now faces the camera on the left: two tall cream rear doors, each with a small round porthole window, a chrome rear bumper, and two small round red tail lights glowing softly; the front of the truck points away to the right. On the right side (the customer side, seen at an angle on the right of the frame): the large rectangular serving window cut into the cream upper body, with a big flat deep teal awning panel raised above it and held horizontally on thin silver struts, slightly wider than the window and sticking up above the roofline; the window has a brushed stainless steel counter shelf and a bright, warmly lit interior with shelves of glass jars, bottles, small copper pots, a coffee machine, and a small vase of pink and yellow flowers on the counter, and a small dark chalkboard hanging inside; a small round silver badge sits on the teal lower body near the rear wheel. Warm light from the open window spills onto the ground. A cook in a dark apron works behind the counter, softly blurred. In front of the window, a short queue of softly blurred customers seen from behind. Setting: a riverside promenade with a stone embankment, a dark river reflecting city lights in the background, other market stalls with warm lanterns and string lights out of focus. Deep blue sky with the last glow on the horizon, warm amber light from the window mixed with cool blue dusk, wet-looking cobblestones with reflections, lively but relaxed mood, realistic paint, chrome, and glass textures, evening street photography. No readable text, no letters, no numbers, no license plate characters, no real brand logos, no faces in focus.
```

</details>

<details><summary><b>Retro Teal Food Truck in a Sunny Plaza</b></summary>

```text
Photoreal lifestyle photograph of a restored compact 1960s-style step van food truck parked in a sunny city plaza at weekday lunchtime, seen in a front right three-quarter view from standing eye level (1.6 m) about 9 m away, 35mm lens, 16:9 landscape composition with the whole truck in frame, slightly right of center. Fixed design details: a short boxy step van body about 5.5 m long with softly rounded corners and a flat roof; two-tone paint, glossy cream on the upper half and deep teal on the lower half, separated by a thin copper-orange stripe running all around the body at the height of the window bottoms; a flat front with a large two-pane windshield, two round chrome headlights, a simple chrome horizontal grille bar, and a chrome front bumper; black tires with cream-painted steel wheels and small chrome hubcaps. On the right side (the customer side, facing the camera): a large rectangular serving hatch centered on the side, its top-hinged teal panel propped open as an awning on two chrome struts, the underside of the awning painted copper-orange; a brushed stainless steel counter shelf along the bottom of the hatch with a small pot of basil and a glass jar of lemons on it; to the left of the hatch, toward the front, a round copper-orange emblem of a simple sun over a wheat stalk, with no letters; to the right of the hatch, toward the rear, a plain dark slate menu board with no writing, only three small hand-drawn white icons of a flatbread, a lemon, and a glass. Along the top edge of the roof on the customer side runs a line of warm globe string lights (switched off in daylight). On the roof at the front sits a long wooden planter box with green herbs, and a small round silver vent near the back. On the ground in front of the hatch: a low natural-wood step platform and a teal A-frame stand with a blank front. The plaza has pale stone paving, plane trees with dappled shade, a couple of cafe tables, and blurred passers-by in the far background only. Bright midday sun with soft dappled shadows, fresh and friendly mood, realistic paint reflections and metal textures, commercial street photography. No readable text, no letters, no numbers, no license plate characters, no real brand logos, no faces in focus.
```

</details>

<details><summary><b>Retro-Futuristic 1970s Sci-Fi</b></summary>

```text
Retro-futuristic 1970s sci-fi cinema look, shot on 35mm film. Figures wear high-collar ivory uniforms with oversized white spherical helmets and dark tinted visors. Symmetrical, wide-angle composition with strong negative space, Wes Anderson × Stanley Kubrick deadpan aesthetic. Soft, diffused overcast lighting with a sterile, clinical feel and low contrast shadows. Muted pastel palette of whites, creams, pale blues, desaturated teal, and light earth tones, slightly hazy film tint. Set in brutalist minimalist interiors or foggy coastal landscapes with retro-analog technology and boxy futuristic vehicles. Kodak Portra 400 look, visible film grain, subtle motion blur, deep depth of field, tactile matte textures.
```

</details>

<details><summary><b>Rick and Morty Style</b></summary>

```text
{
  "TASK": "Reimagine the scene as a 'Rick and Morty' TV show screenshot.",
  "VISUAL_ID": "2D Vector Animation, Adult Swim Style (Justin Roiland). Flat colors, uniform thin black outlines.",
  "CHARACTERS": "Convert humans to 'Rick and Morty' anatomy. Tubular/noodle limbs, droopy stance. EYES: Large white spheres with distinctive 'scribbled' irregular black pupils (wobbly dots). EXPRESSIONS: Apathetic, panicked, or drooling.",
  "OUTFIT": "Simplify complex tactical gear into flat cartoon sci-fi costumes. Remove texture noise; keep only iconic shapes.",
  "BG": "Alien dimension or messy garage. Wobbly organic lines, weird sci-fi textures (holes, slime). Palette: Neon portal green, muted earth tones, pale skin tones.",
  "RENDER": "Zero gradients. Flat lighting. No shadows or minimal hard cel-shading. Clean vector look.",
  "NEG": "3D, realistic, volumetric lighting, gradients, detailed shading, anime, noise, painting, blur, valorant style, sharp angles."
}
```

</details>

<details><summary><b>Risograph Hot Air Balloons Over Cappadocia</b></summary>

```text
A risograph print poster of hot air balloons drifting over the fairy chimneys of Cappadocia at sunrise, vertical portrait 3:4. Limited ink palette of sunflower yellow, fluorescent pink, teal, and deep navy on uncoated paper. The whole sky is flat sunflower yellow. About seventeen hot air balloons of different sizes float across the upper two thirds, near and far, each with a small basket below: some with horizontal pink and navy stripes, some with vertical stripes, zigzag and chevron bands, navy polka dots, and one with a navy-and-yellow checkerboard pattern; the largest navy balloon with pink stripes sits near the top center. A large fluorescent pink sun disc sits low on the left behind rolling teal hills. The lower third is filled with tall cone-shaped fairy chimney rock towers in navy, teal, pink, and yellow, carved with many small square and arched cave windows and doorways, a few glowing yellow, the tallest on the right. Teal hills and a valley stretch behind them, and dark teal shrubs fill the bottom edge. Visible paper grain, halftone speckle, overprinted inks, and slight color misregistration, a bold, cheerful, retro travel poster feel. No text, no logos.
```

</details>

<details><summary><b>Risograph Print of a Crowded Night Train Carriage</b></summary>

```text
A finished risograph print of a crowded night subway carriage, teal and warm brick-red ink only on soft cream paper, 16:9 landscape, the print filling most of the frame as if photographed flat on a pale desk. Key subjects first: standing passengers packed along a central aisle, silver handrails, overhead fluorescent strips, and seated figures along both benches, all built from flat limited colors with bold outlines. The carriage is simplified graphic shapes: far doors with circular windows, vertical poles, hanging straps, and one open phone glow as a small red rectangle. People are anonymous silhouettes and half-tones: coats, backpacks, a sleeping head against the window, a child gripping a pole. Print artifacts: slight teal-red misregistration on the poles, coarse halftone dots in the shadows, paper tooth, a faint second ink pass on the floor. Soft desk-photo framing with the cream sheet edge visible, gentle even light. Mood quiet and tired, late commute, graphic poster energy. Not photoreal, not 3D, not watercolor. No readable text, no logos, no watermark, no hands.
```

</details>

<details><summary><b>Riverside Resort Architectural Render</b></summary>

```text
A photorealistic 3D architectural render of a modern curved resort building along a river boardwalk. The building must be STRICTLY 3 storeys tall above ground level in total: Ground floor with open-air restaurants and terraces, topped by exactly 2 upper floors of luxury hotel apartments with glass balconies. Across the narrow river, an iconic arch pedestrian bridge connects to an entertainment zone. Golden hour sunlight, highly detailed 8k render.
```

</details>

<details><summary><b>Rock Chic Nightlife Patio Portrait</b></summary>

```text
A candid nighttime photograph of a young woman in her mid-20s with a slim figure, long wavy dark brown hair with auburn highlights, wearing a black leather biker jacket open over a black lace bustier top with a deep V-neckline, and a black leather choker with a silver ring. She is sitting at a dark wooden table in an outdoor bar patio, tilting her head back and drinking from a clear glass longneck beer bottle (like Corona) held in her right hand, lips touching the bottle neck, eyes open gazing upward with a confident sensual expression. The background features a rustic red brick wall bathed in dramatic purple/violet LED lighting, a warm amber wall sconce lamp on the right, and lush tropical plants including palm fronds and large-leafed plants framing the scene on both sides. Wooden bistro chairs are visible in the background. Lighting is mixed: warm amber side light from the wall lamp modeling her face, purple ambient rim light from LED projectors, and a soft frontal fill light (possible phone flash) creating specular highlights on the leather jacket and glass bottle. Shot with a smartphone camera, 24mm equivalent lens, f/1.8, slight low angle from chest height, medium close-up vertical composition, shallow depth of field with slightly blurred background, visible digital noise typical of low-light phone photography, casual snapshot aesthetic, rock-chic biker glam vibe, industrial-bohemian Latin American bar patio atmosphere, warm-cool-purple color contrast, Instagram 2020s nightlife photography style.
```

</details>

<details><summary><b>Roman Mosaic of an Octopus and Fishing Boats</b></summary>

```text
A wide, slightly elevated photograph of an ancient Roman floor mosaic uncovered in the courtyard of a Mediterranean villa ruin, the mosaic filling most of the frame in a 16:9 landscape composition. The mosaic shows a lively marine scene made of thousands of small hand-cut stone and glass tesserae: in the center a large octopus in terracotta red and burnt orange with curling tentacles outlined in dark charcoal tiles, its suckers picked out in cream; around it swim striped sea bream, a moray eel, a lobster, squid, and a leaping dolphin in slate grey, ochre, and muted teal; at the top two small wooden fishing boats with square sails and oarsmen drawn as simple dark silhouettes cast a net that curves across the scene; the water is rendered in rows of pale cream and soft blue-grey tesserae laid in gentle wavy lines that follow the shapes of the animals. A border of black and white wave scroll pattern and a braided guilloche band in red, ochre, and cream frames the whole panel. The surface is authentically aged: slightly uneven tiles, a few missing patches showing the grey mortar bed, hairline cracks, faded colors in one corner, a light dusting of sand, and small tufts of dry grass at the broken edge. Low warm late-afternoon sunlight rakes across the floor from the left, making each tessera catch the light and cast a tiny shadow, with the soft shadow of a broken column falling over one corner. Around the edges: weathered limestone paving, the base of a column, and a few terracotta pot shards. Archaeological documentary photography, true colors, crisp detail, calm and timeless mood. No people, no text, no letters, no inscriptions, no signatures, no watermark.
```

</details>

<details><summary><b>Romantic Rain Scene with Face Lock</b></summary>

```text
Faces must remain 100% identical to the reference with absolute identity lock: no face change, no beautification, no symmetry correction, no age shift, no skin smoothing, no expression alteration, same facial proportions, eyes, nose, lips, jawline, and natural texture. Ultra-photorealistic cinematic night scene in the rain where a romantic couple stands very close under a yellow umbrella in a softly lit garden. Heavy rain is falling, illuminated by warm golden fairy lights and street lamps creating dreamy bokeh in the background, with wet ground reflecting the light. The man holds the umbrella and looks at the woman with a gentle, loving gaze, while the woman looks up at him with a soft, warm, romantic smile. They never break eye contact, fully absorbed in each other, conveying deep emotional connection. Elegant coats slightly wet from the rain, realistic fabric texture, subtle rim light outlining their faces, visible raindrops and mist, shallow depth of field, 50mm lens look, natural film grain, high-end cinematic color grading. Only lighting, atmosphere, and environment may change — the faces and identities must remain completely unchanged and perfectly preserved.
```

</details>

<details><summary><b>Romantic Rainy Scene Video</b></summary>

```text
They are standing under the rain, looking at each other romantically. Raindrops fall around them and the soft sound of rain fills the atmosphere.
```

</details>

<details><summary><b>Rooftop Lifestyle Portrait</b></summary>

```text
{
  "subject": {
    "description": "A young blonde woman with fair skin sitting outdoors in direct sunlight, relaxed and slightly smiling with a soft squint due to bright light.",
    "body": {
      "type": "female, slim build",
      "details": "light skin tone, straight blonde hair worn loose, natural makeup, slightly sunlit skin",
      "pose": "reclining on a modern outdoor chair, body angled slightly to the right, legs extended forward, hands resting near her lap holding a phone"
    },
    "face": {
      "expression": "soft smile, slightly squinting eyes due to sunlight, relaxed and confident",
      "gaze_direction": "towards camera",
      "head_tilt": "slight tilt to the right",
      "skin": "smooth, natural skin with sunlight highlights and minimal imperfections"
    },
    "wardrobe": {
      "top": "white fitted t-shirt",
      "bottom": "light blue ripped jeans with knee tears",
      "outerwear": "black jacket casually draped over shoulders",
      "accessories": "sunglasses resting on top of head, minimal jewelry"
    },
    "hair": "loose blonde hair, naturally falling over shoulders with slight sun highlights"
  },
  "scene": {
    "description": "A rooftop terrace during daytime with urban residential buildings in the background.",
    "location": "Outdoor terrace in a city (Mediterranean/European style architecture).",
    "setting": "Rooftop seating area",
    "background_elements": "wooden planter boxes with green plants, concrete floor tiles, nearby buildings with windows and rooftops",
    "lighting": "strong natural sunlight casting sharp shadows",
    "atmosphere": "casual, sunny, relaxed daytime vibe"
  },
  "environment": {
    "ambience": "bright daylight, outdoor, airy",
    "style": "candid lifestyle moment",
    "depth_of_field": "moderate depth of field, subject in focus, background slightly softened but still readable"
  },
  "camera": {
    "device": "iPhone 13 rear camera",
    "mode": "standard photo mode",
    "lens": "wide lens (~26mm equivalent)",
    "angle": "slightly top-down angle, as if standing above subject",
    "aspect_ratio": "4:5",
    "framing": "full body seated framing, subject centered slightly lower in frame",
    "focus": "sharp focus on subject",
    "stability": "handheld"
  },
  "image_quality": {
    "resolution": "standard mobile resolution",
    "grain": "very subtle grain",
    "sharpness": "natural smartphone sharpening",
    "compression_artifacts": "minimal",
    "dynamic_range": "bright highlights with slight clipping in strongest sunlight areas"
  },
  "lighting": {
    "type": "direct sunlight",
    "quality": "harsh, high contrast lighting with strong shadows",
    "effects": "sunlight highlights on hair and skin, sharp shadow edges on ground and chair"
  },
  "color_grading": {
    "tone": "natural daylight",
    "temperature": "slightly warm",
    "contrast": "moderate to high contrast due to sunlight",
    "saturation": "realistic, slightly vibrant",
    "highlights": "bright, slightly blown in sunlit areas",
    "shadows": "defined and darker"
  },
  "rendering": {
    "style": "photorealistic smartphone photography",
    "quality": "clean, natural, unfiltered look",
    "skin_texture": "natural with sunlight reflections",
    "post_processing": "minimal, straight-out-of-camera feel"
  },
  "artifacts": {
    "lens_flare": "very subtle possible sunlight flare",
    "noise_pattern": "minimal",
    "motion_blur": "none",
    "chromatic_aberration": "slight on high contrast edges"
  },
  "constraints": {
    "focus_priority": "subject must remain primary focal point",
    "avoid": "over-processed skin, artificial lighting, studio look, cinematic grading"
  }
}
```

</details>

<details><summary><b>Rooftop Pool Golden Hour Portrait</b></summary>

```text
{
  "pack_name": "BOLD - Rooftop Inferno / Golden Hour",
  "intent": "Generate an ultra photorealistic, raw-candid iPhone-style rooftop pool portrait with dominant, confident energy and editorial polish, without looking staged or studio-lit.",
  "content_safety": {
    "age_requirement": "All subjects must be adults, 21+.",
    "nudity_level": "Non-explicit. Swimwear only. No visible nipples, areola, or genitals. No sheer transparency that reveals explicit anatomy.",
    "tone": "Confidence-forward, not pornographic. Editorial thirst trap energy is allowed, but keep it tasteful and non-explicit.",
    "no_minor_look": true
  },
  "global_style_quality": {
    "photography_style": "RAW candid iPhone photography",
    "realism": "Hyper realistic, texture-forward, pores and natural skin detail visible",
    "resolution_hint": "8K look (high detail, crisp texture, not artificially sharpened)",
    "grading": "Natural but high contrast from harsh sun, minimal stylization, avoid cinematic teal-orange look",
    "retouching": "No heavy retouching, no plastic skin, keep micro texture",
    "vibe": "Influencer and editorial hybrid, premium but unfiltered",
    "overall_mood_keywords": [
      "bold",
      "dominant",
      "unbothered",
      "timeless",
      "high engagement",
      "screenshot-worthy",
      "confidence over sexuality"
    ]
  },
  "scene_setting": {
    "location_type": "Luxury rooftop pool",
    "key_background_elements": [
      "city skyline",
      "glass railing",
      "infinity edge",
      "minimal crowd",
      "quiet luxury atmosphere"
    ],
    "time_of_day": "Sunset into golden hour with fire tones",
    "atmosphere_details": [
      "heat still in the air",
      "sun dropping but still burning",
      "pool water glowing orange-blue",
      "quiet city hum below",
      "city lights beginning to glow in the distance"
    ],
    "crowd_control": {
      "crowd_level": "Minimal",
      "extras_behavior": "If any extras appear, they must be distant, blurred, and non-distracting. The scene reads as luxury silence."
    }
  },
  "subject": {
    "type": "Single primary subject",
    "gender_presentation": "Feminine",
    "age": "Adult 21+",
    "build": "Athletic, feminine power frame",
    "body_characteristics": {
      "waist": "Slim waist with visible core activation",
      "upper_body": "Defined shoulders and arms, strong posture",
      "legs": "Long leg lines emphasized by pose",
      "pose_energy": "Body claiming space, grounded dominance"
    },
    "face": {
      "eyes": "Big, confident eyes, direct or half-lidded gaze",
      "expression": "Cool, dominant, unbothered, no performative smile",
      "freckles": "Light freckles visible under harsh light",
      "lips": "Natural full lips, relaxed but assertive",
      "emotion_keywords": [
        "calm dominance",
        "zero apology energy",
        "I know how this looks"
      ]
    },
    "skin": {
      "undertone": "Light neutral undertone",
      "finish": "SPF plus natural oil sheen",
      "texture": "Visible pores and realistic micro texture",
      "highlights": "Sun-kissed highlights on shoulders and collarbones",
      "avoid": [
        "over-smoothed faces",
        "porcelain skin",
        "beauty-filter blur"
      ]
    },
    "hair": {
      "color": "Dark brown",
      "style": "Slicked back from heat with a slightly wet look",
      "mess_level": "Controlled mess",
      "detail": "A few loose strands catching golden light"
    },
    "tattoos": {
      "requirement": "Chest tattoos fully visible and unchanged",
      "integrity_rules": [
        "Do not alter tattoo shapes, linework, placement, or density",
        "Do not add new tattoos",
        "Do not remove tattoos",
        "Do not mirror-flip tattoos unless the camera/mirror logic requires it and even then preserve design exactly"
      ],
      "role_in_styling": "Tattoos act as jewelry"
    }
  },
  "wardrobe": {
    "outfit": "Black string bikini",
    "top": {
      "type": "Small triangle top",
      "fit": "Tight strings, minimal fabric",
      "notes": "Keep coverage tasteful and non-explicit; do not reveal nipples or areola."
    },
    "bottom": {
      "type": "High-cut bottoms",
      "style": "80s hip rise",
      "notes": "Maintain tasteful framing; avoid explicit exposure."
    },
    "styling_priority": "Minimal fabric, maximum statement, confidence over sexuality"
  },
  "scene_setup": {
    "position": "Standing at the pool edge",
    "stance": [
      "one foot slightly forward",
      "hip subtly shifted",
      "shoulders open",
      "chest forward",
      "chin slightly down or neutral for dominance"
    ],
    "body_language": [
      "claims space",
      "grounded",
      "assertive",
      "not posing for a studio shoot, but naturally powerful"
    ]
  },
  "props_flatlay_feel": {
    "required_props": [
      "sunglasses in hand (not worn)",
      "phone visible in-frame as self-shot proof",
      "wet towel folded nearby"
    ],
    "optional_props": [
      "a minimal drink glass placed far off to the side (subtle, luxury, not a party vibe)"
    ],
    "prop_rules": [
      "No visible branding or logos on props",
      "No text on phone screen",
      "Towel looks naturally damp, not staged"
    ]
  },
  "camera_capture": {
    "camera_type": "Smartphone",
    "phone_reference": "iPhone-style capture, wide lens feel",
    "lens_equivalent_mm": "24-28mm equivalent (phone wide)",
    "preferred_feel": [
      "handheld",
      "slight micro-shake realism",
      "mild softness, not extreme sharpness",
      "high dynamic range but not HDR-overcooked"
    ],
    "angle": {
      "primary": "Low angle for power dominance",
      "tilt": "Slight Dutch tilt, subtle not extreme",
      "distance": "Close enough to feel presence, not cramped"
    },
    "framing": {
      "primary_crop": "Mid-thigh to head (dominant portrait framing)",
      "alternate_crop": "Waist-up hero crop (tattoos fully visible)",
      "composition_notes": [
        "Strong silhouette against sky",
        "Skyline visible but secondary",
        "Infinity edge line clean and premium",
        "Glass railing adds luxury geometry"
      ]
    },
    "focus": {
      "subject_priority": "Sharpest detail on face, tattoos, and skin texture",
      "background": "Slightly softer skyline, readable but not distracting",
      "avoid": "Artificial bokeh that looks DSLR-fake; keep phone-like depth"
    }
  },
  "lighting": {
    "type": "Harsh natural light, high contrast",
    "time_window": "Golden hour with fiery tones",
    "sun_behavior": {
      "sun_position": "Low sun behind or side-back to create rim highlights",
      "lens_flare": "Intentional sun flare hitting the lens",
      "flare_intensity": "Moderate, controlled, not washing out the subject"
    },
    "skin_highlights": [
      "bright highlights on shoulders",
      "collarbones catching light",
      "subtle specular sheen from SPF and natural oil"
    ],
    "shadow_character": "Crisp but not crushed; keep texture in shadows",
    "avoid": [
      "studio lighting",
      "softbox reflections",
      "flat beauty lighting"
    ]
  },
  "rendering_rules": {
    "must_have": [
      "realistic skin pores and micro texture",
      "natural fabric tension and string behavior",
      "water reflections subtle and believable",
      "premium rooftop materials (glass, stone, pool edge) with realistic specular highlights"
    ],
    "must_avoid": [
      "CGI look",
      "illustration",
      "plastic skin",
      "over-smoothed faces",
      "exaggerated anatomy",
      "unreal proportions",
      "extra limbs or warped hands",
      "fake tattoos or tattoo drift"
    ],
    "imperfection_cues": [
      "slight handheld framing imperfection",
      "tiny water droplets on skin",
      "a few flyaway hair strands",
      "minor towel wrinkles"
    ]
  },
  "prompt_text_master": "Ultra photorealistic raw candid iPhone-style portrait on a luxury rooftop pool at golden hour with fiery sunset tones. Low-angle dominant perspective with a subtle Dutch tilt, handheld realism, mild softness like a real phone photo, premium unfiltered texture-forward look. Single adult woman (21+), athletic feminine power frame, slim waist with strong core activation, defined shoulders and arms, long leg lines emphasized by stance. Expression is cool, dominant, unbothered, direct or half-lidded gaze, no performative smile, natural full lips relaxed but assertive. Light freckles visible in harsh sun. Skin is light neutral undertone with SPF plus natural oil sheen, pores visible, real micro texture, sun-kissed highlights on shoulders and collarbones, crisp shadows without crushing detail. Hair is dark brown, slicked back from heat with slightly wet controlled-mess look, a few loose strands catching golden light. She stands at the pool edge, one foot slightly forward, hip subtly shifted, shoulders open and chest forward, body claiming space. Outfit is a black string bikini: small triangle top with tight strings and high-cut 80s hip rise bottoms, minimal but tasteful, non-explicit coverage. Chest tattoos are fully visible and must remain unchanged in shape, placement, linework, and density, tattoos act as jewelry. Setting: infinity-edge rooftop pool with glass railing and city skyline behind, minimal crowd, luxury silence. City lights beginning to glow subtly. Pool water glows orange-blue in sunset reflections. Props: sunglasses in hand (not worn), phone visible in-frame as self-shot proof, wet towel folded nearby, no branding, no text on phone screen. Lighting: harsh natural sunlight, high contrast, intentional sun flare hitting the lens, controlled flare that adds heat without washing out face or tattoos. Composition: strong silhouette against sky, skyline secondary, premium geometry lines of railing and pool edge. Final mood: calm dominance, grounded power, confidence over sexuality, editorial-grade thirst trap, bold timeless high engagement snapshot feel.",
  "negative_prompt_master": "studio lighting, softbox, ring light reflections, fashion campaign pose, over-posed model energy, exaggerated anatomy, unrealistic proportions, extra limbs, warped hands, plastic skin, over-smoothed faces, porcelain doll look, heavy beauty filter, CGI, illustration, anime, painterly style, artificial background, green screen look, cinematic teal-orange grading, overcooked HDR, text, watermark, logo, brand marks, nudity, nipples, areola, explicit genital visibility, see-through exposure, underage, childlike features, doll-like face, uncanny eyes, dead eyes, overly sharpened micro-contrast, unrealistic bokeh, mirrored tattoo errors, tattoo distortion, tattoo removal, new tattoos added",
  "output_formats": [
    {
      "use_case": "Instagram feed editorial",
      "aspect_ratio": "4:5",
      "resolution_hint": "2160x2700 or higher",
      "framing": "mid-thigh to head, skyline visible in upper background, tattoos centered"
    },
    {
      "use_case": "Stories/Reels thumbnail",
      "aspect_ratio": "9:16",
      "resolution_hint": "2160x3840 or higher",
      "framing": "waist-up hero crop, tattoos fully visible, stronger lens flare line"
    },
    {
      "use_case": "Square profile post",
      "aspect_ratio": "1:1",
      "resolution_hint": "2048x2048 or higher",
      "framing": "tight waist-up, dominant gaze, city reduced to minimal bokeh"
    }
  ],
  "variants": [
    {
      "variant_name": "V1 - Maximum dominance, flare controlled",
      "changes_from_master": [
        "Increase low-angle effect slightly",
        "Keep flare moderate and clean, not washing facial detail",
        "Make skyline slightly sharper but still secondary"
      ],
      "prompt_addendum": "Slightly stronger low-angle power framing, keep tattoos perfectly legible, flare controlled to avoid haze over the face."
    },
    {
      "variant_name": "V2 - Heat haze premium, more candid imperfection",
      "changes_from_master": [
        "Introduce subtle heat haze shimmer in background only",
        "Add micro water droplets on collarbones and shoulders",
        "Slightly more handheld imperfection"
      ],
      "prompt_addendum": "Add subtle background heat shimmer, tiny water droplets catching the sun on shoulders and collarbones, slightly imperfect handheld crop like a real moment."
    },
    {
      "variant_name": "V3 - City lights glow emphasis",
      "changes_from_master": [
        "More visible city lights beginning to glow",
        "Slightly darker sky gradient",
        "Keep subject exposure correct, avoid HDR"
      ],
      "prompt_addendum": "City lights softly turning on in the distance, subtle sky gradient deepening, keep subject properly exposed and natural."
    },
    {
      "variant_name": "V4 - Strong silhouette against sky",
      "changes_from_master": [
        "Place sun slightly more behind subject for rim light",
        "Increase silhouette clarity",
        "Keep facial features still readable"
      ],
      "prompt_addendum": "Backlight with clean rim highlights around shoulders and hairline, stronger silhouette against the sky while keeping eyes and freckles readable."
    },
    {
      "variant_name": "V5 - Phone proof stronger",
      "changes_from_master": [
        "Make the phone more clearly visible in the lower corner of frame",
        "Ensure no screen text",
        "Preserve candid feel"
      ],
      "prompt_addendum": "Phone clearly visible as self-shot proof, screen unreadable with no text, keep it natural like an authentic capture."
    },
    {
      "variant_name": "V6 - Tattoo hero framing",
      "changes_from_master": [
        "Frame slightly higher to prioritize chest tattoos",
        "Reduce skyline prominence",
        "Keep bikini strings realistic and not tangled"
      ],
      "prompt_addendum": "Prioritize chest tattoos as the hero detail, reduce skyline dominance, keep bikini strings physically believable with natural tension."
    }
  ],
  "advanced_controls_optional": {
    "seed_policy": "If your generator supports seeds, lock a seed per variant to preserve identity and composition for iteration.",
    "consistency_rules": [
      "Maintain the same subject identity across rerolls if using reference or seed locks.",
      "Tattoo integrity must remain exact, no drift.",
      "Avoid anatomy mutations, especially hands, shoulders, and waist."
    ],
    "iteration_recipe": [
      "Start with V1 in 4:5 to validate pose and dominance angle.",
      "Switch to V6 to verify tattoo legibility and non-mutation.",
      "Test V3 in 9:16 for skyline glow and flare balance.",
      "Apply negative_prompt_master strictly if outputs look too cinematic or too retouched."
    ]
  },
  "creative_option": {
    "idea": "If you want it to feel even more 'real iPhone', add a tiny lens smudge and micro glare on one corner only, but keep it subtle so it reads as authentic, not a filter.",
    "toggle": "Optional"
  }
}
```

</details>

<details><summary><b>Rooftop Sunset Look Back</b></summary>

```text
{
  "category": "ROOFTOP_SUNSET_LOOKBACK",
  "subject": {
    "demographics": "Adult woman, 21-27, Turkish-looking.",
    "hair": {
      "color": "Dark brown",
      "style": "Loose waves, slightly wind-touched",
      "texture": "Strands visible, flyaways around face",
      "movement": "Hair subtly lifted by breeze"
    },
    "face": {
      "shape": "Soft oval",
      "eyes": "Intense yet friendly eye contact",
      "makeup": "Natural glam, dewy skin, subtle liner",
      "skin_details": "Visible pores, realistic glow, no airbrush"
    },
    "clothing": {
      "outfit": "Minimal black outfit, light jacket (no text/logos)",
      "fabric": "Real weave, gentle wrinkles at elbows"
    },
    "accessories": {
      "jewelry": ["Small silver hoops"]
    }
  },
  "pose": {
    "type": "Half-body leaning on railing",
    "orientation": "Body angled away, head turned back toward camera",
    "head_position": "Slight tilt, chin relaxed",
    "hands": "One hand resting on railing, fingers natural",
    "gaze": "Lookback eye contact, subtle smirk",
    "posture": "Relaxed, confident"
  },
  "setting": {
    "environment": "Rooftop with skyline in distance",
    "background_elements": [
      "Golden hour sun flare",
      "City lights beginning to glow (bokeh)",
      "Railing texture visible"
    ],
    "depth": "Strong separation: subject sharp, skyline bokeh"
  },
  "camera": {
    "shot_type": "Half-body portrait",
    "angle": "Eye-level or slightly low",
    "focal_length_equivalent": "35-50mm editorial feel (or 26mm phone variant)",
    "framing": "4:5, subject off-center",
    "focus": "Eyes sharp, background creamy bokeh"
  },
  "lighting": {
    "source": "Golden hour sun + subtle fill",
    "direction": "Warm rim light on hair + cheek edge",
    "highlights": "Controlled flare, natural skin speculars",
    "shadows": "Soft shadows, cinematic separation"
  },
  "mood_and_expression": {
    "tone": "Quiet luxury, confident",
    "expression": "Soft smirk, calm intensity",
    "atmosphere": "Warm, cinematic, spontaneous"
  },
  "style_and_realism": {
    "style": "Photoreal social/editorial hybrid",
    "fidelity": "High hair/skin detail, no smoothing"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "Mild",
    "motion_blur": "Very subtle in hair tips only"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "fake skyline", "cgi flare", "plastic skin",
    "extra fingers", "warped railing",
    "readable text", "logos", "watermark"
  ]
}
```

</details>

<details><summary><b>Room Makeover Concept Brief Builder</b></summary>

```text
Act as an interior designer and visualization art director. I will describe a room I want to redesign. You will turn it into a clear design concept with fixed design details, plus two ready-to-use image prompts that show the SAME room from two opposite viewpoints, so the two AI images look like photos of one real space.

Room: ${room:small living room in a timber cabin, about 3.5 x 4.5 meters, vaulted ceiling, one large window facing a pine forest}
Who uses it and how: ${use:a couple who read, work on a laptop now and then, and host two friends for board games}
Style direction: ${style:warm Nordic cabin, calm and natural, a few bold earthy accents}
Must keep: ${keep:the small wood-burning stove and the wide-plank floor}
Budget level: ${budget:mid-range, mostly new furniture, no structural work}
Second view to show: ${second_view:the reverse angle at dusk, looking from the window back toward the entry door, with the stove lit}

Please produce:

1. Design concept
   - Concept name and a two-sentence story of how the room should feel.
   - Floor plan in words: what stands on each wall (north, east, south, west) and in the center, with approximate sizes and walking clearances.
   - Palette: 6 named colors (simple names like "sage green") with where each one is used.
   - Materials and finishes: walls, ceiling, floor, textiles, metals.

2. Fixed design details (the consistency list)
   A numbered list of 12 to 16 details that must look identical in every image: each piece of furniture with color, material, and shape; the rug; every light fixture; window and door details; plants and signature objects; and their exact positions in the room. Write each one as a short, concrete phrase an image generator can follow (for example "rust-orange leather sling armchair with a black steel frame, angled toward the stove").

3. Image prompt A: the base view
   One detailed prompt for an AI image generator: photoreal interior photography of the room from the entry door looking toward the window, in daytime light. Include every fixed detail that is visible from this viewpoint in its correct position (left and right as seen from the camera), the camera height and lens, lighting, mood, and aspect ratio. End with exclusions (no people, no text, no logos, no clutter).

4. Image prompt B: the second view
   One detailed prompt for the second view, written so it works with a text-only image generator that cannot see image A: restate ALL fixed details again in full words (never "same as before"), swap left and right correctly for the reversed camera direction, describe what is newly visible (for example the wall behind the first camera), and the new lighting and time of day. Keep palette, materials, and style identical.

5. Consistency checklist
   Ten yes/no checks to compare image B against image A (for example "Is the sofa still sage green boucle with three seat cushions?").

6. Shopping and practical notes
   A short list of the key pieces with what to look for when buying (size, material, approximate price tier), and two layout tips for small rooms.

Rules:
- Keep everything realistic for the stated budget and room size; flag anything that will not fit.
- Use plain color names and concrete shapes; avoid vague words like "nice" or "modern" on their own.
- No brand names, no real people, no readable text in the images.
- If my description is missing something essential, make a sensible assumption and list it at the top.
```

</details>

<details><summary><b>Rough Anime Crayon Doodle of Any Character</b></summary>

```text
Convert the character in the reference image into a rough, Japanese-style digital doodle.

Overall style:
An extremely casual, rough and naive cute Japanese anime character doodle, as if drawn quickly with the rough crayon and marker brushes of an ordinary painting app. Keep the original character recognizable: hairstyle, hair color, facial features, outfit, accessories and signature expression.

Line art:

* Outline the character with obvious, rough black strokes.
* Line weight is very uneven: some lines suddenly get thicker, some break off.
* Contours are loose, inaccurate and slightly crooked.
* Lines have a clear hand-drawn grainy, smudged texture.
* Do not aim for precise outlines; misaligned, overlapping and incomplete lines are allowed.
* No fine, smooth vector line art.

Coloring:

* Use large areas of simple, opaque flat color.
* Colors may spill slightly outside the lines; missed spots and white gaps are allowed.
* Shadows use a few rough gray strokes or darker strokes of the same hue.
* Highlights are casual, short white strokes.
* Keep the rough texture of mixed crayon, pastel and marker.
* No complex gradients, detailed lighting or rich layers of color.

Facial features:

* Keep the original character's eye color, eye shape and signature look.
* Simplify the features; draw the eyes with thick black lines and simple color blocks.
* Keep the mouth as simple as possible; the nose can be left out.
* A few casual pink blush strokes can be added to the cheeks.
* Keep the character's expression and personality; do not change their temperament.

Hair and outfit:

* Fully keep the character's most recognizable hairstyle and hair color.
* Build the hair from a few large color blocks; do not draw lots of fine strands.
* Keep the outfit's original colors, silhouette and signature accessories.
* Heavily simplify clothing folds and decorations.
* Do not change the outfit or add accessories that are not in the original image.

Composition:

* 1:1 square canvas.
* Half-body portrait of the character, with a slightly oversized head.
* Character centered, with natural white space around them.
* Pure white background; no text, complex scenery or decorative borders.

Most important style constraint:
The image must be rough, scribbly, simple and naive, like a cute anime doodle drawn on a whim, not a polished illustration deliberately imitating a sketch.

No automatic retouching, no fine line art, no complex hair structure, no subtle gradients, no 3D effects, no heavy lighting, no added complex outfit details.

Final result: a low-finish Japanese anime digital doodle with rough black outlines, large flat color blocks, casual white highlights and an obvious crayon grain.
```

</details>

<details><summary><b>Rustic Farm Logo</b></summary>

```text
I'm looking for a talented designer to create a rustic-style farm logo for my brand. R Lucky Star Farm

The logo should include:
- A rustic aesthetic
- Inclusion of farm animals: cow, pig, and chicken
- Five stars integrated into the design
- maybe a horseshoe
- the letter R
```

</details>

<details><summary><b>Rustic Farm Logo Design</b></summary>

```text
I'm looking for a talented designer to create a rustic-style farm logo for my brand. R Lucky Star Farm

The logo should include:
- A rustic aesthetic
- Inclusion of farm animals: cow, pig, and chicken
- Five stars integrated into the design
- maybe a horseshoe
- the letter R
- need logo in a vector file format, specifically an EPS, SVG, or DXF file and a PDF
```

</details>

<details><summary><b>Sandstone Caravanserai with Camel Caravan</b></summary>

```text
An old square sandstone caravanserai stands in a wide sand desert at dusk while a line of five camels with seated riders walks toward its gate. The fortress fills the center-right of the frame: a crenellated wall with small slit windows between two round crenellated corner towers, and in the middle a tall pointed horseshoe-arched gateway that opens onto warmly lit inner arches of the courtyard, with two small glowing lanterns on the wall on either side of the gate. On the left, the five camels with riders walk in a single file to the right across the rippled sand toward the gateway, their long shadows stretching beside them. Three palm trees grow at the right side by the right tower: two tall palms against the tower and one shorter palm further right. The sky glows deep orange and peach at the lower left horizon and fades upward into violet and indigo filled with the first stars, with a few thin streaky clouds on the left. Low dunes line the horizon on both sides. The foreground is a wide band of wind-rippled sand with a few sparse dry shrubs near the walls. Photoreal cinematic travel photography, calm and quiet mood as dusk turns to night. Wide landscape 16:9. No close-up faces, no text, no signs, no logos.
```

</details>

<details><summary><b>Santorini Summer Editorial Portrait</b></summary>

```text
A full-body vertical editorial fashion photograph of a beautiful young woman with a slim athletic hourglass figure and golden sun-kissed tan skin, long wavy light brown hair with blonde balayage highlights blowing in the wind to the left. She is wearing a strapless white ivory maxi dress with a structured sweetheart neckline, fitted bodice, and flowing pleated linen-like skirt that reaches the floor. She is barefoot, walking gracefully along a white whitewashed wall ledge, her left foot stepping forward with heel slightly raised, her right arm extended downward holding a pair of white strappy stiletto sandals by the straps. Her head is tilted down, gaze lowered in a serene dreamy introspective expression, lips softly closed in a nude-coral tone. The background features the deep cobalt blue Aegean Sea stretching to the horizon, with a distant Greek island coastline (white buildings on beige cliffs, Santorini-style) visible, and a clear pale blue sky above. Shot in bright midday Mediterranean sunlight from upper right, creating strong sun-kissed highlights on her shoulders, décolletage and hair, with defined soft shadows and natural white fill light bouncing from the whitewashed surface. Professional full-frame mirrorless camera, 85mm lens, f/5.0, 1/800s, ISO 100, eye-level full body vertical composition, medium depth of field keeping both subject and seascape sharp. Luxury resort editorial photography style, Greek island summer aesthetic, minimalist white-and-blue color palette, golden skin tones, elegant and free-spirited mood, Vogue Greece travel editorial vibe, slight fine film grain, high-end fashion campaign quality.
```

</details>

<details><summary><b>Scary Masked Man Cosplay</b></summary>

```text
I want a scaryface masked man with really realistic lilke chasing me etc as cosplay
```

</details>

<details><summary><b>Scratchboard Barn Owl in a Moonlit Barn</b></summary>

```text
A black scratchboard illustration of a barn owl perched on a rough wooden beam inside a quiet barn at night, 16:9 landscape, high-contrast white scratched lines on deep black ink board. Key subject first: a heart-faced barn owl in three-quarter view facing left, large dark eyes, finely hatched white face disk, speckled breast, and long scratched feather textures on the folded wings. Behind the owl, barn rafters and a hay loft suggested with sparse white lines, nothing hanging from the beams; a broken loft window on the right frames a bright full moon and a few scratched stars. Straw bales below are loose cross-hatching; dust motes are tiny scratched dots in a soft moonbeam. Technique: classic scraperboard look, varying line weight, cross-hatching for shadow, untouched black for void space, no gray wash, no color, no digital glow. Mood still, watchful, slightly eerie but calm. No text, no signature, no watermark, no color tint.
```

</details>

<details><summary><b>Scrimshaw of a Clipper Ship and Sea Serpent</b></summary>

```text
A wide scrimshaw-style engraving of a three-masted clipper ship under full sail battling towering storm waves, while a long coiled sea serpent rises from the sea beside it on the right. The ship leans into the swell with every sail filled, its rigging, hull planks, and gun ports drawn in fine detail, and a small pennant streams from the top of the mast. The scaly serpent arches its neck high above the waves, its body looping in and out of the water, with a spiky crest running down its back. Curling waves with foaming white crests fill the lower half, dark storm clouds roll across the sky, a jagged bolt of lightning strikes on the right, and small seabirds wheel above the masts. Everything is drawn in fine black hand-incised lines with crosshatching and stippling, with a touch of faded red ink on the pennant and the serpent's crest. The panel is warm cream, slightly yellowed polished bone with subtle grain, tiny scratches, and darker aged edges. A twisted rope border frames the scene, and a compass rose sits in the lower left corner. Antique 19th-century sailor folk art look, high detail. Wide landscape 16:9. No text, no letters, no signatures.
```

</details>

<details><summary><b>Sea Otter in a Kelp Forest</b></summary>

```text
A photoreal underwater photograph inside a California kelp forest. In the left foreground, a sea otter swims upright in the clear blue-green water, looking toward the camera with bright dark eyes and long whiskers, hugging a large purple sea urchin against its chest with its front paws, its dense brown fur sparkling with tiny air bubbles. Tall golden-brown giant kelp stalks with wide wavy blades rise from the rocky seabed to the rippling surface. Bright sunbeams slant down from the upper left through the water. In the right middle distance, a small school of silver fish glides between the kelp, and a single bright orange garibaldi fish swims near the seabed in the lower right. The rocky floor is covered with algae and small sea life, and fine floating particles catch the light. Natural light, wide-angle underwater lens, sharp detail on the fur and urchin spines, rich teal and gold colors, calm and curious mood. Wide landscape 16:9. No text, no divers, no watermark.
```

</details>

<details><summary><b>Security Camera Animal Footage</b></summary>

```text
### Style
*   **Visual Texture:** Digital security camera footage, slightly grainy with characteristic fish-eye distortion from a wide-angle lens. The wood grain of the porch and the fur of the animals are clearly visible despite the digital compression.
*   **Lighting Quality:** Natural, diffused daylight. The scene is evenly lit by an overcast sky, casting soft shadows.
*   **Color Palette:** A mix of natural outdoor tones: the deep black of the bear's fur, the vibrant orange of the tabby cat, the white and grey of the baby’s car seat, and the green and yellow hues of the autumn lawn and trees in the background.
*   **Atmosphere:** Intense, frantic, and protective. The serenity of a baby resting on a porch is suddenly shattered by a life-threatening encounter.

### Cinematography
*   **Camera:** Static wide-angle security camera mounted at a high angle. The perspective is fixed, providing a full view of the porch and the yard.
*   **Lens:** Wide-angle/Fish-eye lens with a deep depth of field, keeping both the foreground baby and the distant parked cars in relatively sharp focus.
*   **Lighting:** Ambient outdoor light; no artificial highlights.
*   **Mood:** Chaotic and suspenseful, transitioning into relief.

---

### Scene Breakdown

**Scene 1 (00:00s - 00:10s):**
A peaceful autumn morning on a wooden porch is interrupted when a large black bear climbs up the stairs. A baby sits calmly in a car seat in the center of the frame. An orange tabby cat stands between the baby and the intruder. As the bear leans in, the cat heroically lunges at the bear's face with its claws out. The bear, startled by the cat's ferocity, fumbles backward off the porch and retreats into the yard. A woman is heard screaming in terror from behind the camera, likely inside the house, as she witnesses the event.

**Actions:**
*   **The Bear:** Climbs onto the porch, looks toward the baby, then recoils and runs away across the grass after being attacked by the cat.
*   **The Cat:** Hisses, leaps into the air toward the bear's face, and remains in a defensive stance on the porch even after the bear flees.
*   **The Baby:** Remains strapped in the car seat, looking up curiously, seemingly unaware of the danger.
*   **The Human (Off-screen):** Bangs on the door or window and screams frantically to scare the bear.

**Dialogue:**
*   Woman (Screaming/Panicked): "Oh my God! Oh my God! Stay back! Get back!"
*   Woman (Breathless): "Is the baby okay?"

**Background Sound:**
The sharp sound of a door or window being struck, the aggressive hiss of the cat, the heavy thud of the bear's paws on the wood, and the frantic, high-pitched screaming of a woman. Ambient wind and distant outdoor sounds provide a low-level hum.
```

</details>

<details><summary><b>Seinen Manga Transformation</b></summary>

```text
Transform the uploaded image into an ultra-detailed black and white seinen manga masterpiece while preserving the original subject with absolute accuracy.

ABSOLUTE PRIORITY:
The original person's identity must remain completely unchanged.
Preserve 100% facial likeness.
Do not redesign, reinterpret, beautify, stylize, idealize, age up, age down, or modify the face in any way.
Maintain exact facial proportions, skull shape, jawline, cheekbones, nose shape, lip shape, eye shape, eyelid structure, eyebrow shape, forehead, ears, hairstyle, hairline, skin texture, wrinkles, scars, facial hair, and expression.
The subject must be instantly recognizable as the original person.
Only the artistic medium changes; the person does not.

STYLE TRANSFER ONLY:
Convert the photograph into a high-end seinen manga illustration.
Retain the exact composition, framing, camera angle, pose, perspective, anatomy, clothing, accessories, and background structure.

ART STYLE:
ultra-detailed Japanese seinen manga,
master-level ink illustration,
extreme cross-hatching,
dense linework,
dramatic chiaroscuro,
deep black shadows,
high-contrast monochrome,
realistic anatomy,
battle-hardened atmosphere,
psychological intensity,
cinematic lighting,
traditional manga ink techniques,
professional published manga quality,
museum-quality illustration,
legendary manga artwork aesthetic.

INKING DETAILS:
heavy cross-hatching,
fine hatching,
feathering,
stippling,
scratchboard texture,
precise contour lines,
deep shadow masses,
clean white highlights,
rich black ink coverage,
high-detail texture rendering.

LIGHTING:
dramatic directional lighting,
harsh shadows,
strong contrast,
volumetric depth through ink work,
dark cinematic mood.

QUALITY:
masterpiece,
best quality,
ultra detailed,
8k detail,
extremely sharp line art,
professional manga panel quality,
award-winning illustration.

MOOD:
stoic,
intimidating,
serious,
determined,
battle-worn,
legendary,
emotionally intense,
powerful presence.

NEGATIVE PROMPT:
different face,
changed identity,
face reconstruction,
face redesign,
face enhancement,
beautified face,
AI-generated face,
anime face,
generic manga face,
new hairstyle,
different expression,
different age,
different ethnicity,
altered proportions,
symmetrical correction,
beautification filter,
plastic skin,
smooth skin,
cute style,
chibi,
cartoon,
pixar,
disney,
western comic,
3d render,
cgi,
low detail,
blurry,
soft lighting,
digital painting,
color image,
watercolor,
oil painting,
photobash,
character redesign,
identity drift,
facial modification,
facial reinterpretation,
artistic liberties,
stylization of facial features.

FINAL INSTRUCTION:
Preserve the original identity, facial geometry and expression with forensic-level accuracy. Apply only the black-and-white seinen manga ink style. The face, likeness and unique characteristics must remain unchanged.
```

</details>

<details><summary><b>Self-Portrait in a Convex Traffic Mirror</b></summary>

```text
{
  "image_analysis": {
    "environment": {
      "type": "Outdoor",
      "setting": "Urban street scene",
      "weather": "Overcast/Cloudy"
    },
    "technical_specs": {
      "camera_lens": "Wide-angle (likely smartphone rear camera)",
      "camera_angle": "Low angle, looking upwards towards a traffic mirror and street sign",
      "focus": "Sharp focus on the convex mirror and the immediate foreground, slight distortion due to wide lens and mirror curvature"
    },
    "lighting": [
      {
        "source_id": 1,
        "type": "Natural Ambient Light (Overcast Sky)",
        "angle": "Overhead/Diffused",
        "color": "Cool White / Greyish",
        "intensity": "Moderate",
        "effect_on_objects": "Creates flat lighting with soft, undefined shadows; minimal contrast on building facades; creates a glare on the upper curve of the convex mirror."
      }
    ],
    "people": [
      {
        "id": "person_1_photographer",
        "location": "Visible inside the reflection of the convex mirror",
        "identity_status": "Anonymized (Face obscured by phone)",
        "orientation": {
          "body_direction": "Facing forward (towards the mirror)",
          "face_direction": "Facing forward (towards the mirror/phone)"
        },
        "emotional_state": "Indeterminable (Face obscured)",
        "posture": {
          "general_definition": "Standing upright",
          "feet_position": "Not visible (cropped in reflection)",
          "hand_position": "Raised to face level, holding a smartphone to take the photo",
          "visibility_extent": "Visible from mid-thigh/knees up to head in the reflection"
        },
        "head_details": {
          "hair": {
            "color": "Dark (Black or Dark Brown)",
            "style": "Long, loose",
            "shape": "Falls over shoulders"
          },
          "ears": "Covered by hair",
          "face_features": {
            "forehead": "Obscured by phone/hair",
            "eyes": "Obscured by phone",
            "nose": "Obscured by phone",
            "mouth": "Obscured by phone",
            "chin": "Partially visible below phone, fair skin tone"
          },
          "facial_hair": "None"
        },
        "body_details": {
          "body_type": "Average/Slender (hard to determine due to heavy clothing)",
          "skin_tone": "Light/Fair (visible on hands/face)",
          "neck": "Covered by scarf",
          "shoulders": "covered by coat, relaxed",
          "chest": {
            "ratio_to_body": "Indeterminable (covered by thick coat)",
            "measurements": "Indeterminable",
            "bra_status": "Indeterminable",
            "nipple_visibility": "Not visible",
            "size_appearance": "Indeterminable due to winter clothing"
          },
          "abdomen": {
            "ratio_to_body": "Concealed by coat",
            "ratio_to_chest": "Indeterminable",
            "ratio_to_hips": "Indeterminable"
          },
          "hips": {
            "ratio_to_body": "Concealed by coat",
            "measurement_estimation": "Indeterminable"
          },
          "legs": {
            "visibility": "Partially visible (upper thighs)",
            "clothing": "Dark trousers/tights"
          }
        },
        "clothing": {
          "upper_body": "Dark (black or navy) overcoat, maroon/dark red scarf wrapped loosely",
          "lower_body": "Dark trousers or leggings (partially visible)",
          "light_interaction": "Fabric absorbs light, appearing matte",
          "accessories": "Smartphone (held in hands)",
          "footwear": "Not visible"
        }
      },
      {
        "id": "person_2_pedestrian",
        "location": "Visible inside the reflection of the convex mirror (background)",
        "identity_status": "Anonymized (Back turned)",
        "orientation": {
          "body_direction": "Walking away from the camera",
          "face_direction": "Forward (away from camera)"
        },
        "posture": {
          "general_definition": "Walking",
          "visibility_extent": "Full body visible in distance"
        },
        "clothing": {
          "upper_body": "Dark coat",
          "lower_body": "Dark trousers"
        }
      }
    ],
    "objects": [
      {
        "name": "Convex Traffic Mirror",
        "purpose": "Traffic safety/Visibility for blind corners",
        "contribution_to_scene": "Acts as the focal point and frame for the self-portrait reflection",
        "proportions": "Dominates the center foreground",
        "color": "Orange (rim), Reflective silver (surface)",
        "location": "Center of the image"
      },
      {
        "name": "Street Sign",
        "purpose": "Navigation/Location identifier",
        "text_content": "MAKLIK (Partial visibility)",
        "color": "Red background with white text",
        "location": "Attached to the pole above the mirror"
      },
      {
        "name": "Apartment Building (Left)",
        "purpose": "Residential/Commercial",
        "proportions": "Large, multi-story structure",
        "color": "Grey and white facade",
        "features": "Balconies with white railings, tall metal chimney/vent pipe attached to side",
        "location": "Left side foreground"
      },
      {
        "name": "Wooden Building (Background Left)",
        "purpose": "Residential/Historic",
        "color": "Faded Red/Pink",
        "location": "Visible in the background behind the mirror",
        "features": "Traditional architecture, wooden siding"
      },
      {
        "name": "White Building (In Reflection)",
        "purpose": "Public/Institutional",
        "color": "Cream/White",
        "location": "Reflected in the mirror",
        "features": "Arched windows, historic style"
      },
      {
        "name": "Trees/Vegetation",
        "purpose": "Environment",
        "color": "Dark Green/Brownish (Autumnal)",
        "location": "Right side and background"
      }
    ],
    "negative_prompt": "bright sunshine, blue sky, direct flash, nudity, summer clothing, high contrast, studio lighting, macro lens, detailed face view, clear text, modern glass skyscraper, noise, grain, watermark"
  }
}
```

</details>

<details><summary><b>Selfie in the Alps</b></summary>

```text
Photorealistic iPhone selfie-style shot in alpine mountains. Bright clear daylight, deep blue sky, dramatic sharp mountain peaks in the background with patches of snow on rocky ridges. Wide open green alpine meadow in the foreground, lush grass with small plants visible in detail. A small wooden mountain hut in the mid-distance. The woman lies on her back in the grass, relaxed, using a hiking backpack as a pillow. The camera angle is handheld and slightly above her — classic iPhone arm-extended selfie perspective, subtle wide-angle distortion on the extended arm. She wears sporty hiking outfit: lightweight Arc’teryx windbreaker jacket (blue tone), fitted pink athletic shorts, Oakley sunglasses, casual trail vibe. Relaxed body posture — one knee slightly bent, one arm extended toward the camera holding the phone. Backpack visible under her head, realistic hiking gear details.
```

</details>

<details><summary><b>Selfie with a Wild Animal</b></summary>

```text
Create a photorealistic image of me and a wild ${wild_animal} taking a spontaneous selfie together in the animal’s natural habitat.
I am smiling naturally, holding a phone at arm’s length for a selfie, looking directly at the camera. My face identity, body proportions, clothing, and overall appearance must remain exactly the same as the reference image. Expression should feel joyful, relaxed, and authentic, like a real candid moment.
The ${wild_animal} is positioned very close to the camera, slightly turned with its head facing the lens, appearing calm, curious, relaxed, and non-aggressive. The animal must look fully realistic with detailed fur, natural textures, lifelike anatomy, and retracted claws, as a real wild animal would appear in nature.
Both of us are clearly posing together for a selfie, creating a relaxed but powerful presence. The scene should feel natural and believable, as if captured in a real moment.
Camera & Composition:

Close, handheld iPhone-style selfie angle, arm-length distance
Slight wide-angle distortion typical of phone selfies
Informal, slightly off-center framing
Shallow depth of field focused on me and the ${wild_animal}
Lighting:

Natural outdoor lighting with warm tones
Soft shadows and gentle highlights
Subtle sunlight lens flare if appropriate
Background:

Authentic outdoor environment typical for the ${wild_animal} (jungle, forest, savanna, grassland, etc.)
Natural elements softly blurred in the background
Effects:

Very subtle motion blur near the edges
Gentle photographic softness on background edges
Minimal film-like grain for realism
Natural color balance with a slight warm tint
Important rules:

Preserve my face identity and clothing exactly
Keep realistic animal anatomy and behavior
No third-person camera angles
The image must feel like a real, candid iPhone selfie taken in the wild
```

</details>

<details><summary><b>Serene Autumn Lakeside</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "medium",
    "dominant_palette": [
      "red",
      "light blue",
      "orange",
      "grey",
      "black"
    ]
  },
  "composition": {
    "camera_angle": "wide shot",
    "depth_of_field": "deep",
    "focus": "The autumn trees and their reflection in the lake",
    "framing": "The composition is adapted to a 1:1 square format, keeping the main visual weight of the trees on the right, balanced by the small fisherman on the left. The reflection in the water creates a strong vertical symmetry centered within the square frame."
  },
  "description_short": "A serene illustration of a lone person fishing on the shore of a tranquil lake, surrounded by vibrant red and orange autumn trees whose colors are reflected in the calm water.",
  "environment": {
    "location_type": "landscape",
    "setting_details": "A calm lakeside on a misty day in autumn. The shoreline is composed of small rocks, and vibrant autumn foliage grows along the bank. In the distance, a forested hill is partially obscured by fog.",
    "time_of_day": "morning",
    "weather": "foggy"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "ambient",
    "type": "soft"
  },
  "mood": {
    "atmosphere": "Peaceful and contemplative autumn day",
    "emotional_tone": "calm"
  },
  "narrative_elements": {
    "character_interactions": "A solitary figure is engaged in the quiet act of fishing, creating a sense of peaceful interaction with nature.",
    "environmental_storytelling": "The vibrant peak autumn colors and the perfectly still, reflective water suggest a fleeting moment of natural beauty and tranquility. The lone fisherman enhances the theme of solitude and quiet contemplation.",
    "implied_action": "The person is patiently fishing, suggesting a quiet wait and a slow passage of time."
  },
  "objects": [
    "autumn trees",
    "lake",
    "fisherman",
    "fishing rod",
    "rocks",
    "forest",
    "sky"
  ],
  "people": {
    "ages": [
      "adult"
    ],
    "clothing_style": "casual outdoor wear",
    "count": "1",
    "genders": [
      "unknown"
    ]
  },
  "prompt": "A beautiful digital illustration of a serene autumn landscape in a 1:1 square format. A lone fisherman stands on a rocky shore beside a calm, reflective lake. To the right, vibrant trees with fiery red and orange leaves hang over the water, their perfect reflection mirrored below. The composition is balanced within a square frame, with the fisherman on the left and trees on the right. The background shows distant, misty hills under a pale blue sky. The art style is minimalist and graphic, with flat colors and a subtle texture, evoking a peaceful and contemplative mood. Art by Ryo Takemasa.",
  "style": {
    "art_style": "minimalist illustration",
    "influences": [
      "Japanese woodblock prints",
      "graphic design"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "illustration",
    "minimalism",
    "landscape",
    "autumn",
    "reflection",
    "serenity",
    "flat color",
    "graphic design",
    "lakeside",
    "fishing",
    "square format",
    "1:1 aspect ratio"
  ]
}
```

</details>

<details><summary><b>Serene Monochrome Knitwear Portrait</b></summary>

```text
Artistic Black-and-White Photography

An artistic black-and-white photograph in a cinematic, feminine portrait style, captured on a medium-format film camera with subtle grain that adds natural texture and depth to the image.

Subject and Pose

A young woman with a graceful figure is photographed from a three-quarter angle in motion, creating a sense of lightness and dynamism. She stands with her head tilted slightly forward and to the side, her gaze thoughtfully lowered, giving her appearance an intimate, introspective quality.

Her left arm is raised, gently touching her hair at the back of her head, with her fingers slightly buried in the strands. Her right arm rests along her body, with her fingers casually gathering or pulling the fabric of her dress at the hip, creating natural folds and revealing a small portion of her upper leg above the knee. Her figure forms a graceful S-shaped curve, emphasizing fluidity and elegance.

Clothing

The woman wears a fitted, light-colored (white or cream) ribbed or knitted midi/maxi dress that closely follows her figure and accentuates her silhouette. The dress features an asymmetrical, intricate cut: the left shoulder is completely bare, while the right shoulder remains covered.

The long, textured sleeves have loose, slightly gathered cuffs that partially cover her palms. The fabric is thin and soft, with a subtle ribbed texture that beautifully catches the light and shadows, creating numerous delicate folds and drapes around the waist, hips, and sleeves.

Hairstyle and Makeup

The woman's hair is   loose, and naturally voluminous. Several strands on the right side are caught by the wind or movement, flowing dynamically toward the left, adding a sense of lightness and spontaneity to the photograph. Her left hand gently holds her hair in place on the opposite side.

Her makeup is natural and barely noticeable (nude), emphasizing softly defined eyebrows, a natural shadow on the eyelids, and a subtle lip contour. Her face looks fresh, without heavy visible makeup, highlighting her natural beauty.

Lighting and Atmosphere

Soft, natural, diffused side lighting, as if coming from a window or a softbox positioned in the upper left, falls gently across her face, shoulder, and figure, creating delicate transitions between light and shadow (chiaroscuro).

The shadows are soft and low in contrast, emphasizing the curves of her body, the texture of the fabric, and individual strands of hair. The background is a simple, neutral gray wall without distracting details, becoming slightly darker toward the edges of the frame through subtle vignetting.

The overall mood is melancholic, intimate, serene, and sensual.

Camera Angle and Composition

The photograph is taken from a medium distance, framed from approximately the knees upward (American shot), with the camera positioned slightly below or around chest level to make her figure more expressive.

The image is vertically composed, with the woman positioned centrally in the frame. A shallow depth of field and soft bokeh keep the background gently blurred, directing all attention toward the woman's emotional expression and graceful body language.

The natural contrast of the black-and-white palette emphasizes textures, shapes, and contours.

Facial Identity: Preserve the woman's original facial features and identity exactly. Do not alter her face or change her facial proportions.

Aspect Ratio: 3:4.

Image Quality: Photorealistic, high-quality, sharp, ultra-detailed 8K photograph, captured on an iPhone 16 Pro. Natural skin texture, realistic fabric details, subtle film grain, and authentic black-and-white tones.
```

</details>

<details><summary><b>Serene Moonlit Street Illustration</b></summary>

```text
{
  "colors": {
    "color_temperature": "cool",
    "contrast_level": "high",
    "dominant_palette": [
      "teal",
      "cool gray",
      "warm yellow",
      "orange"
    ]
  },
  "composition": {
    "camera_angle": "eye-level shot",
    "depth_of_field": "deep",
    "focus": "A corner building with a lit cafe",
    "framing": "The building is positioned on the right side of the frame, balanced by the open water and sky on the left. Power lines and a crosswalk create leading lines."
  },
  "description_short": "A digital illustration of a quiet, moonlit street scene by the water, featuring a warmly lit cafe and a black cat sitting on a balcony.",
  "environment": {
    "location_type": "cityscape",
    "setting_details": "A multi-story building with a cafe on the ground floor stands next to a body of water under a night sky. A crosswalk is in the foreground, and a distant shoreline is visible across the water.",
    "time_of_day": "night",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "mixed",
    "type": "atmospheric"
  },
  "mood": {
    "atmosphere": "Peaceful and solitary urban night",
    "emotional_tone": "calm"
  },
  "narrative_elements": {
    "character_interactions": "A solitary cat observes the quiet scene from its perch on a balcony.",
    "environmental_storytelling": "The warmly lit but empty cafe suggests a late hour, creating a tranquil and lonely atmosphere in an urban setting. The moonlit water adds to the sense of peace.",
    "implied_action": "The scene is still and quiet, as if paused in time. The cat is watching, and the moon's reflection ripples gently on the water."
  },
  "objects": [
    "building",
    "cafe",
    "cat",
    "balcony",
    "moon",
    "water",
    "power lines",
    "crosswalk",
    "tables",
    "chairs"
  ],
  "people": {
    "count": "0"
  },
  "prompt": "A serene digital illustration of a street corner by the sea at night. A bright full moon hangs in the textured teal sky, its light reflecting on the calm water. The ground floor of a European-style building is a warmly lit cafe with empty white tables and chairs outside. Above, a lone black cat sits on a balcony, silhouetted against the night sky. The style is painterly and atmospheric, with visible brush textures, evoking a feeling of quiet solitude and peace.",
  "style": {
    "art_style": "illustrative",
    "influences": [
      "lo-fi aesthetic",
      "Japanese animation"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "illustration",
    "night scene",
    "cat",
    "moonlight",
    "cafe",
    "waterside",
    "atmospheric",
    "digital painting",
    "textured"
  ],
  "use_case": "Training for stylized illustration generation or datasets focused on atmospheric and emotional scenes.",
  "uuid": "b55094a8-7a9b-4e1e-ba85-5e7893761150"
}
```

</details>

<details><summary><b>Serene Yoga and Mindfulness Photography</b></summary>

```text
# Serene Yoga & Mindfulness Lifestyle Photography

## 🧘 Role & Purpose
You are a professional **Yoga & Mindfulness Photography Specialist**. Your task is to create serene, peaceful, and aesthetically pleasing lifestyle imagery that captures wellness, balance, and inner peace.

---

## 🌅 Environment Selection
Choose ONE of the following settings:

### Option 1: Bright Yoga Studio
- Minimalist design with wooden floors
- Large windows with flowing white curtains
- Soft natural light filtering through
- Clean, calming aesthetic

### Option 2: Outdoor Nature Setting
- Garden, beach, forest clearing, or park
- Soft golden-hour or morning light
- Natural landscape backdrop
- Peaceful natural surroundings

### Option 3: Home Meditation Space
- Minimalist room setup
- Meditation cushions and soft furnishings
- Plants and candles
- Soft ambient lighting

### Option 4: Wellness Retreat Center
- Zen-inspired architecture
- Natural materials throughout
- Earth tones and neutral colors
- Peaceful, sanctuary-like atmosphere

---

## 👤 Subject Specifications

### Appearance
- **Age**: 20-50 years old
- **Expression**: Calm, centered, peaceful
- **Skin Tone**: Natural, glowing complexion with minimal makeup
- **Hair**: Natural styling - bun, ponytail, or loose flowing

### Yoga Poses (choose one)
- 🧘 Lotus Position (Padmasana)
- 🧘 Downward Dog (Adho Mukha Svanasana)
- 🧘 Mountain Pose (Tadasana)
- 🧘 Child's Pose (Balasana)
- 🧘 Seated Meditation (Sukhasana)
- 🧘 Tree Pose (Vrksasana)

### OR Meditation Activity
- Breathing exercises with eyes gently closed
- Gentle stretching and mobility work
- Mindful sitting meditation

### Clothing
- **Type**: Comfortable, breathable yoga wear
- **Color**: Earth tones, whites, soft pastels (beige, sage green, soft blue)
- **Style**: Minimalist, flowing, non-restrictive

---

## 🎨 Visual Aesthetic

### Lighting
- Soft, warm, golden-hour natural light
- Gentle diffused lighting (no harsh shadows)
- Professional, flattering illumination
- Warm color temperature throughout

### Color Palette
| Color | Hex Code | Usage |
|-------|----------|-------|
| Sage Green | #9CAF88 | Primary accent |
| Warm Beige | #D4B896 | Neutral base |
| Sky Blue | #B4D4FF | Secondary accent |
| Terracotta | #C45D4F | Warm accent |
| Soft White | #F5F5F0 | Light base |

### Composition
- **Depth of Field**: Soft bokeh background blur
- **Focus**: Sharp subject, blurred peaceful background
- **Framing**: Balanced, centered with breathing room
- **Quality**: Photorealistic, cinematic, 4K resolution

---

## 🌿 Optional Elements to Include

### Props
- Meditation cushions (zafu)
- Yoga mat (natural materials)
- Plants and flowers (orchids, lotus, bamboo)
- Soft candles (unscented glow)
- Crystals (amethyst, clear quartz)
- Yoga straps or blankets

### Natural Materials
- Wooden textures and surfaces
- Stone and earth elements
- Natural fabrics (cotton, linen, hemp)
- Natural light sources

---

## ❌ What to AVOID

- ❌ Bright, harsh fluorescent lighting
- ❌ Cluttered or distracting backgrounds
- ❌ Modern gym aesthetic or heavy equipment
- ❌ Artificial or plastic-looking elements
- ❌ Tension or discomfort in facial expressions
- ❌ Awkward or unnatural yoga poses
- ❌ Harsh shadows and unflattering lighting
- ❌ Aggressive or clashing colors
- ❌ Busy, distracting background elements
- ❌ Modern technology or digital devices

---

## ✨ Quality Standards

✓ **Professional wellness photography quality**  
✓ **Warm, inviting, approachable aesthetic**  
✓ **Authentic, genuine (non-staged) feeling**  
✓ **Inclusive representation**  
✓ **Suitable for print and digital use**

---

## 📱 Perfect For
- Yoga studio websites and marketing
- Wellness app cover images
- Meditation and mindfulness blogs
- Retreat center promotions
- Social media wellness content
- Mental health and self-care materials
- Print materials (posters, brochures, flyers)
```

</details>

<details><summary><b>Serious Man Film Poster</b></summary>

```text
A serious man in a denim jacket standing in a dark urban setting with flashing emergency lights behind him, cinematic lighting, dramatic atmosphere, Persian-English bilingual film poster style
```

</details>

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

<details><summary><b>Snow Leopard on a Himalayan Ridge</b></summary>

```text
A photorealistic wildlife photograph of a snow leopard standing on a snow-dusted rocky ridge high above a sea of clouds at dawn, in a wide landscape 16:9 frame. The snow leopard stands in the left half of the foreground on jagged dark grey rocks lightly covered with fresh snow and frost, its body angled across the frame toward the right while its head on the left turns to look straight into the camera with calm, pale grey-green eyes. Its thick, smoky grey and cream fur is covered with crisp black rosettes and spots, its large paws rest on the rocks, and its long, very thick ringed tail curves down to the right and hangs over the rocks. Behind the ridge, a soft white sea of clouds fills the valleys below. In the distance, a long range of jagged snow-covered Himalayan peaks stretches across the frame, their summits and faces lit pink, peach, and gold by the first light of sunrise, with cool blue shadows in the gullies, and a darker forested slope rising in the lower right. The sky is a clear pale blue fading to soft lavender near the horizon. Telephoto lens look, sharp focus on the leopard's face and fur, natural colors, quiet and majestic mood. No people, no text, no logos.
```

</details>

<details><summary><b>Snowy Mountain Onsen Image to Video</b></summary>

```text
Start from the step 2 image "Steaming Outdoor Hot Spring Beside a Snowy Mountain Inn at Blue Hour" as the exact first frame, and animate it into a calm ${duration:6}-second cinematic shot. Keep the teal hot spring pool, the dark snow-capped rocks around it, the small stone lantern on the left, the larger stone lantern on the right, the two-storey wooden inn with its snowy roofs and warmly lit windows, the snow-laden pine trees, the dark mountain slope, the deep blue twilight sky, and the composition exactly as in the image. The camera makes a slow, gentle push-in toward the pool and the inn. Thick white steam drifts and curls slowly over the water and rises toward the trees. Large soft snowflakes keep falling evenly across the scene. The lanterns and the inn windows glow steadily without flickering. About two thirds of the way through, a small clump of snow slips off a pine branch above the pool and drops straight down into the water near the center, making a small white splash and soft ripples that spread outward and fade. The shot ends calm, with the steam still drifting. Natural, realistic motion, no cuts, no people, no animals, no new objects, no text. Soft sound of bubbling water, a quiet splash, and the hush of falling snow.
```

</details>

<details><summary><b>Snowy Mountain Onsen Scene Brief Builder</b></summary>

```text
Act as a cinematic landscape designer who writes image-ready and motion-ready scene briefs. Help me design one hero shot of a steaming outdoor hot spring (onsen) beside a traditional mountain inn during snowfall at dusk. The shot will first be generated as a still image and then animated into a short video that uses that image as its first frame. Your brief must make the still image rich in elements that can move naturally (steam drifting and curling over the water, snowflakes falling, soft snow slipping off a pine branch, gentle ripples on the pool, the warm glow of lanterns and windows) while keeping the composition calm, balanced, readable, and easy to animate.

My starting idea: ${idea:a steaming rock-lined hot spring in the snow next to an old wooden inn, at blue hour, with stone lanterns}

My starting choices:
- Pool: ${pool:a natural outdoor pool of clear teal water framed by dark volcanic rocks capped with snow, filling the center and foreground}
- Steam: ${steam:thick white steam rising from the water and drifting to one side}
- Inn: ${inn:a two-storey traditional Japanese wooden inn on the right with snow-covered tiled roofs and rows of warmly lit windows}
- Lanterns: ${lanterns:two snow-capped stone lanterns glowing softly, one small on the left rocks and one larger near the inn}
- Trees and mountains: ${trees:snow-laden pine trees behind the pool and a dark forested mountain slope on the left}
- Weather: ${weather:large soft snowflakes falling slowly}
- Time and light: ${time:deep blue twilight just after sunset, warm amber light from the inn and lanterns}
- Visual style: ${style:photoreal travel and landscape photography, natural colors}
- Mood words: ${mood:quiet, warm, peaceful, wintry, inviting}

First ask me, in one short message, for anything missing: the camera height (low near the water, eye level, or slightly raised), how much of the frame the inn should take, how dense the steam and snowfall should be, how bright the windows and lanterns are, whether I want one small natural event in the video (for example a clump of snow sliding off a pine branch into the pool), and anything to avoid (people, bathers, animals, text, signs, logos, or copying a specific real inn, photograph, or named landmark).

Then produce the brief with these sections:

1. **Scene Overview**: two or three sentences on the place, the moment, the light, and the feeling. Describe an imagined mountain hot spring inn in a Japanese spirit, not a copy of a specific real ryokan or a famous photograph.

2. **The Pool and Rocks**: the pool's shape and size in the frame, the water color and clarity, the dark rocks around it and the snow on their tops, and where the water catches warm and cool light.

3. **Steam**: how thick it is, where it rises most, which way it drifts, how it softens the background, and how it should read as warm vapor rather than fog or smoke.

4. **The Inn**: its position, number of storeys, roof shape and the snow on it, the wooden walls, the rows of lit windows, and how much detail is visible through the steam and snow.

5. **Lanterns, Trees, and Mountain**: the two stone lanterns with snow caps and their glow, the snow-laden pines behind the pool (including one branch above the water that could shed snow), and the dark mountain slope against the sky.

6. **Light, Sky, and Snow**: the deep blue twilight sky, the cool ambient light on the snow, the warm amber accents from the windows and lanterns, the size and density of the falling snowflakes, and how soft the shadows are.

7. **Fixed Visual Details**: a numbered list of 8 to 10 details that must stay identical in the still image and in the video (pool shape and position, rock edges, inn position and roofline, window pattern, both lantern positions, pine trees, mountain silhouette, camera position, framing, overall steam zone).

8. **Motion Map**: a table of every element that can move in the video, with columns: element, type of motion, direction, speed (very slow, slow, medium), and how strongly it should move. Include the steam, the snowfall, the water surface, the lantern and window glow, one optional snow clump falling from a pine branch into the pool with a small splash and ripples, and the camera move. Keep total motion subtle and physically plausible, with one gentle air direction.

9. **Prompt Seed A - Hero Still Image**: a ready-to-paste image prompt under 170 words for a wide landscape 16:9 frame, with the steaming hot spring, the snowy inn, and the stone lanterns at blue hour in the first sentence, ending with: no people, no text, no logos.

10. **Prompt Seed B - Image-to-Video Animation**: a ready-to-paste video prompt under 120 words that starts from the hero still as the first frame, describes the steam drifting and curling, snow falling, the steady glow of lanterns and windows, a slow gentle push-in toward the pool and the inn for about 6 seconds, and (if I want it) one clump of snow falling from a pine branch into the pool with a small splash and spreading ripples, and says to keep the pool, rocks, inn, lanterns, trees, and framing exactly as in the image with no new objects.

Rules: no people, bathers, or animals; no text, signs, or logos; no fast camera moves or cuts; and no motion that breaks physics (rocks, lanterns, and the inn never move, steam rises and drifts and does not pour downward, snow falls slowly and evenly, a falling snow clump drops straight down under gravity and makes only a small splash, the light does not flicker or jump). Use short paragraphs and lists.
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

<details><summary><b>Some Silly Moves Anime Comedy Video</b></summary>

```text
References:
@[ref1]: Yuki. Shoulder-length silver-white hair with long bangs, olive-green eyes, small round silver earrings, loose pale camisole, flat deadpan face.
@[ref2]: Sumi. Short black bob with uneven bangs, brown eyes, small gold earrings, cream camisole under an oversized off-white shirt, loud and easily flustered.
@[ref3]: the style reference. Hand-drawn look, line quality and palette only; not its pose or layout.

Visual style: Rough hand-drawn anime sketch, loose black ink lines, flat watercolor washes, muted grey, sage and beige palette, soft indoor daylight. Shot as a phone front camera video: handheld, restless, constantly bobbing and tilting with whoever holds it, quick crash zooms and whip pans.

Avoid: No subtitles. No background music. No slow motion. No other people. Yuki and Sumi never merge or swap faces.

Two friends goof around nonstop with a phone camera through a small apartment, each new spot in front of a different strange painting. Every change of place comes through a whip pan or a cut from the phone itself; nobody stands still. A visible gap always separates their faces. Sound: footsteps, phone rustle, shrieks, laughter, one line. Shot list: 8 shots, about 30 seconds.

Scene 1: Continuous, in front of an orange painting with two huge round owl eyes.
Shot 1 (0-4s): Close two-shot, high angle; the camera bobs quickly with Sumi, who holds the phone with her raised right arm from the top right corner. Yuki springs up into frame from below on screen left and flashes a V sign with both hands, face completely deadpan. Sumi sticks out her tongue and shakes her head side to side, her black bob flying. Cut as Yuki snatches the phone from Sumi's hand; the camera whips left in a blur.

Scene 2: Continuous, in front of a blue-grey blob painting with one black hole for an eye.
Shot 2 (4-8s): Medium shot, eye level; the whip pan lands here, and the camera, now in Yuki's right hand, quickly pans right to follow Sumi. Yuki stays at the bottom left edge of frame, deadpan. Sumi skids across the floor from screen left to screen right in her socks, arms flailing. Cut as Sumi spins and lunges straight at the lens.
Shot 3 (8-11s): Close-up, eye level; the camera, still in Yuki's hand, does a fast crash zoom onto Sumi. Sumi's face is pressed almost against the lens, mouth wide open. Behind her, Yuki does a stiff robot dance with her free arm, still deadpan. Sumi bumps the phone; it tumbles out of Yuki's hand. Cut the instant the phone hits the floor.

Scene 3: Later, in front of a dark green painting of a faded face.
Shot 4 (11-15s): Extreme low angle from the floor; the phone already lies face up, locked-off camera looking at the ceiling. Both girls lean in over the lens from opposite sides, Yuki on screen left, Sumi on screen right. Yuki flips her silver hair forward over her whole face; one big eye peers through a gap. Sumi shrieks and jumps back out of frame, then her hand dives in and grabs the phone. Cut as the phone lifts off the floor.

Scene 4: Continuous, a narrow hallway with a grey wall and a brown smeared painting.
Shot 5 (15-19s): Medium close-up, Sumi holding the phone out in front of her and facing it while she runs backward down the hallway, still running flat out, laughing. Far behind her, at center, Yuki glides after her with her hair still over her face, arms limp, closing the distance. Cut as Sumi swings around a corner; the camera whips right.

Scene 5: Continuous, in front of a beige wall with a round orange painting.
Shot 6 (19-22s): Medium close-up, eye level, handheld; the camera heaves with Sumi's breathing. Sumi, holding the phone in her right hand, presses her back to the wall, panting, eyes darting left and right. Yuki is nowhere in frame. Cut as a white cloth drops in from the top of frame.
Shot 7 (22-25s): Insert, close to the lens; the camera jolts once. A single white bedsheet with two black eye holes lowers from above in front of the lens, held by Yuki's hands.
Yuki's line (flat, deadpan): "Boo."
Shot 8 (25-30s): Wide two-shot, high angle; the camera quickly pulls back, then spins with them. Sumi, phone in her right hand, yanks the sheet with her left; the sheet tangles around both girls and they spin together, laughing, Yuki's hair now neat. Both thrust V signs at the lens. Sumi's index finger is still reaching for the lens when the clip cuts to black as the fingertip covers it.

Style reference used for the character images (Midjourney blend): --sref 1448908625 3123598145 387469134 3207844525 --profile 7v4i3wf --stylize 1000
```

</details>

<details><summary><b>Sophisticated Istanbul Stroll</b></summary>

```text
Full-body cinematic shot of a sophisticated man in his early 30s walking confidently down a historic cobblestone street in Istanbul, Beyoğlu. He features a short beard and dark hair. He is wearing a tailored navy blue wool overcoat, a charcoal grey turtleneck sweater, and black trousers. He is holding a premium brown leather briefcase in one hand and a takeaway coffee cup in the other. He is wearing brown leather Chelsea boots and stylish sunglasses. The background prominently features the iconic Galata Tower rising at the end of the street. Soft natural daylight, high-end fashion photography, realistic anatomical proportions, 8k resolution, highly detailed textures. --ar 9:16
```

</details>

<details><summary><b>Spinning Motion Blur Fashion Portrait</b></summary>

```text
Vertical 9:16 candid fashion portrait of a 
beautiful girl in the picture, with long, messy, loose hair. She spins rapidly while looking back at the camera, arms spread wide and hair flying. SLOW SHUTTER SPEED 1/8–1/15 sec, extreme realistic motion blur, ghost trails on arms and hair, blurred body, recognizable face, horizontal background streaks, slight camera shake, double-exposure effect, heavy 35mm film grain, dreamy, moody, underexposed, photorealistic. No CGI, no frozen motion, no sharp arms or hair.
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

<details><summary><b>Step Inside a Painting: 3D Camera Fly-Through</b></summary>

```text
The video begins from the frame defined by the attached painting and preserves its exact composition, subjects, colors, lighting, and arrangement as a still three-dimensional space.

No person, animal, object, water, foliage, cloud, flame, or any other painted element moves, animates, or changes state. The entire scene remains completely frozen, as if the painting has simply become a solid, motionless diorama.

The camera performs continuous cinematic 3D travel through this frozen scene: it slowly pushes forward, gently orbits, and drifts past the main subjects and spatial layers, revealing depth, parallax, and volumetric form while never altering or animating any content inside the painting.
Only ambient spatial presence accompanies the movement; there is no dialogue, narration, music, or sound effects from any element within the painting.
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

<details><summary><b>Sunbeam in a Sandstone Slot Canyon</b></summary>

```text
A photorealistic photograph of a single beam of sunlight falling into a narrow sandstone slot canyon, tall portrait 3:4. A bright shaft of light pours down from a small crack in the rock at the top center and lands as a glowing round spot on the soft sandy floor near the bottom. Fine dust and sand particles swirl and sparkle inside the beam, making it look solid and misty. The canyon walls rise steeply on both sides in smooth, flowing, wave-like curves and layered stripes, glowing deep orange and red where the light bounces and fading to cool violet and plum in the shadows. The narrow passage curves away behind the beam into darkness. Low, wide-angle view from the canyon floor, long exposure, rich warm colors, high dynamic range, fine detail in the rock texture, quiet, sacred, awe-filled mood. No people, no text, no logos.
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

<details><summary><b>The Breathing Jack-o'-Lantern Horror Short</b></summary>

```text
30 seconds | 16:9 | 4K Ultra HD | 30 FPS | Ultra-photorealistic live-action Halloween horror short.

A terrifying Halloween night unfolds on a rain-soaked wooden porch, where a real adult man discovers that his carved jack-o'-lantern is behaving strangely. With realistic human actors, practical effects, cinematic lighting, and authentic horror atmosphere, an ordinary Halloween decoration becomes something truly sinister.

0–5 seconds: A rain-soaked wooden porch glistens under dim nighttime lighting. A flickering jack-o'-lantern sits beside the front door. A man in a dark flannel shirt and jeans enters carrying Halloween decorations. Suddenly, he notices the pumpkin slowly expanding and contracting as if it were breathing.

5–12 seconds: The camera slowly pushes toward the pumpkin. Its jagged carved smile subtly widens before returning to normal. The internal candle flickers in sync with the movement. The man kneels cautiously as a faint, wet breathing sound emerges from inside.

12–21 seconds: The pumpkin's light abruptly goes out. Complete silence. The man switches on his phone flashlight, revealing two realistic human eyes deep inside the dark pumpkin, staring directly at him. Terrified, he recoils and drops his phone onto the wet wooden floor, leaving its flashlight beam tilted toward the pumpkin.

21–27 seconds: The man slowly reaches toward the pumpkin again. Before he can touch it, the jack-o'-lantern rotates several inches toward him on its own. Its carved smile remains perfectly still. Frozen with disbelief, he slowly backs toward the door.

27–30 seconds: Extreme close-up of the pumpkin. Its internal light suddenly switches back on. A tiny, fresh handprint gradually appears in condensation across its outer surface. Before the viewer can understand what has happened, the screen cuts instantly to black.

Production: Photorealistic live-action visuals, real human actors, consistent character identity, practical pumpkin movement, realistic condensation, natural rain, believable shadows, subtle handheld cinematography, shallow depth of field, cinematic horror lighting, and restrained color grading. Sound design includes rainfall, distant wind, wooden footsteps, soft breathing, subtle fabric movement, a low suspenseful musical rise, and sudden silence before the final reveal.

Negative prompt: No animation, cartoon visuals, CGI-looking characters, artificial environments, changing faces, inconsistent clothing, distorted anatomy, unrealistic pumpkin movement, exaggerated jump scares, gore, dialogue, narration, subtitles, text, logos, watermarks, black bars, or abrupt transitions before the final cut.
```

</details>

<details><summary><b>The Collector's Banquet 1985 Dark Fantasy Film</b></summary>

```text
Create a gripping 30-second dark fantasy film that looks like a forgotten Hollywood sword-and-sorcery movie from 1985, filmed on authentic 35mm with elaborate practical creature effects, handcrafted costumes, theatrical performances, and atmospheric cinematography.

The story follows a ruthless emperor hosting a magnificent banquet inside his ancient palace. He has conquered seven kingdoms and believes no mortal can challenge him. During the celebration, a mysterious hooded servant presents him with a golden chalice containing a strange black liquid. The emperor drinks it to demonstrate his fearlessness, but something horrifying happens. Every guest at the table suddenly freezes, their faces slowly turning toward him. The emperor realizes that the people surrounding him have been dead for centuries, and the mysterious servant has come to collect a debt.

Tell the story through exactly nine cinematic shots, with dramatic close-ups, theatrical camera movements, practical supernatural effects, and a shocking final revelation. Keep the entire film inside one enormous medieval throne hall, allowing the tension to develop naturally through the emperor's arrogance, the mysterious chalice, and the terrifying transformation of the banquet guests.

Include a deep, ominous male narrator delivering short English voiceover lines, alongside natural spoken English dialogue from the emperor and the mysterious servant. All visible dialogue must feature expressive performances and accurate lip synchronization.

[2] GLOBAL SETTING

The entire film takes place inside an enormous medieval imperial throne hall at night. Massive stone columns support a vaulted ceiling, enormous crimson banners hang from the walls, and hundreds of flickering candles illuminate an extravagant banquet table covered with golden goblets, roasted meats, silver platters, and elaborate ceremonial decorations. Heavy velvet curtains frame towering windows overlooking a moonlit kingdom.

The environment resembles a meticulously constructed 1980s fantasy movie set, with practical candlelight, thick atmospheric haze, handcrafted stone architecture, painted background extensions, and rich theatrical lighting.

The Emperor: A commanding adult man in his late fifties with long silver hair, a thick gray beard, piercing blue eyes, and a proud, intimidating expression. He wears an enormous engraved golden crown decorated with red gemstones, elaborate gold ceremonial armor, and a long crimson velvet cloak with fur-lined shoulders. His voice is deep, powerful, and arrogant.

The Mysterious Servant: A tall, unnaturally thin figure wearing a long black hooded robe with elaborate antique embroidery. His face remains mostly concealed beneath the hood, revealing pale skin, sunken eyes, and an unsettling expression. He carries an ancient golden chalice filled with thick black liquid. His movements are unnaturally calm and deliberate, and his voice is quiet, hollow, and mysterious.

The Banquet Guests: Noblemen, noblewomen, knights, and royal advisers wearing elaborate medieval garments, ornate jewelry, embroidered gowns, and ceremonial armor. They initially appear alive and cheerful, but later reveal pale, decaying faces created with detailed practical prosthetic makeup. Their transformations remain non-graphic, resembling theatrical undead creatures from 1980s dark fantasy cinema.

The Ancient Collector: The mysterious servant's true identity, revealed at the end as a supernatural skeletal figure beneath the hood, with glowing amber eyes and a face constructed using elaborate animatronic skull prosthetics.

Cinematography: Authentic 1980s 35mm film photography, vintage anamorphic lenses, warm amber candlelight, rich crimson and gold color grading, deep theatrical shadows, subtle photochemical grain, gentle highlight halation, physical fog, elaborate practical sets, and dramatic fantasy compositions.

Sound: Ominous orchestral score, medieval banquet ambience, distant laughter, clinking goblets, flickering flames, low supernatural whispers, and clear English character dialogue.

[3] TIMESTAMPED STORYBOARD

SHOT 1 | [00:00-00:03] THE CONQUEROR

A magnificent wide cinematic shot reveals the emperor seated at the head of an enormous banquet table, surrounded by laughing nobles and armored knights. Hundreds of candles flicker across golden plates and crimson banners while servants move through the crowded hall.

The camera slowly pushes toward the emperor as he raises a golden goblet above his head.

NARRATOR (deep, ominous voiceover): "He conquered seven kingdoms..."

CUT TO SHOT 2.

SHOT 2 | [00:03-00:06] THE EMPEROR'S PRIDE

A dramatic low-angle close-up captures the emperor laughing arrogantly beneath his enormous golden crown. His silver beard catches the warm candlelight as he slams his goblet against the table, causing the surrounding nobles to fall silent.

EMPEROR (booming voice): "NOT EVEN DEATH CAN COMMAND ME!"

The nobles respond with nervous laughter.

CUT TO SHOT 3.

SHOT 3 | [00:06-00:09] THE UNINVITED GUEST

A slow tracking shot reveals a mysterious hooded servant emerging from the darkness between two enormous stone columns. He approaches the emperor's table carrying an antique golden chalice filled with thick black liquid.

The surrounding guests gradually stop speaking as the servant places the chalice directly in front of the emperor.

SERVANT (quiet, unsettling voice): "Then drink, Your Majesty."

CUT TO SHOT 4.

SHOT 4 | [00:09-00:12] THE FORBIDDEN CHALICE

An intimate close-up shows the emperor studying the black liquid inside the ornate golden chalice. The surface moves unnaturally, reflecting faces that do not belong to anyone standing nearby.

The emperor smirks, lifts the chalice, and drinks its contents in one confident motion.

NARRATOR (voiceover): "But one debt remained unpaid."

The emperor lowers the empty chalice, his smile slowly fading as the banquet hall becomes completely silent.

CUT TO SHOT 5.

SHOT 5 | [00:12-00:16] THE SILENT BANQUET

A wide symmetrical shot reveals the entire banquet table frozen in unnatural stillness. Every noble, knight, and servant has stopped moving, their expressions locked in eerie smiles.

One by one, the guests slowly turn their heads toward the emperor in perfect synchronization.

The emperor looks from side to side, suddenly frightened.

EMPEROR (confused): "What is this?"

The candles flicker violently as a cold wind passes through the hall.

CUT TO SHOT 6.

SHOT 6 | [00:16-00:19] THE DEAD REMEMBER

A terrifying close-up reveals an elderly noblewoman seated beside the emperor. Her once-beautiful face gradually transforms into a pale, ancient corpse through elaborate practical makeup effects. Her cheeks become hollow, her eyes darken, and her expression turns into an unnatural smile.

The camera shifts slightly to reveal other guests undergoing the same transformation, their luxurious clothing remaining unchanged.

NOBLEWOMAN (whispering): "We have waited so long..."

The emperor recoils in horror.

CUT TO SHOT 7.

SHOT 7 | [00:19-00:23] THE TRUTH

A dramatic medium shot shows the emperor rising from his throne, knocking over his chair as he stares at the undead guests surrounding him. The mysterious servant remains perfectly still on the opposite side of the table.

EMPEROR (furious and frightened): "WHO ARE YOU?"

The servant slowly raises his head, revealing pale, hollow features beneath the hood.

SERVANT (calmly): "The one you promised your soul."

The emperor's face drains of color.

CUT TO SHOT 8.

SHOT 8 | [00:23-00:27] THE COLLECTOR

A dramatic close-up captures the mysterious servant slowly pulling back his hood. His face transforms into an ancient skeletal creature through elaborate practical prosthetics and mechanical facial effects. His eyes glow with dim amber light as the surrounding candles extinguish one after another.

The undead guests rise silently from their chairs, forming a motionless circle around the emperor.

NARRATOR (deep voiceover): "And tonight... the collector returned."

The skeletal figure extends one long, bony hand toward the emperor.

CUT TO SHOT 9.

SHOT 9 | [00:27-00:30] THE FINAL PAYMENT

An extreme close-up captures the emperor's terrified face as he backs against his enormous golden throne. His crown slips sideways, and his trembling hands grip the armrests.

The skeletal collector leans close, his glowing eyes reflected in the emperor's frightened gaze.

COLLECTOR (deep whisper): "Your throne is ready... below."

The emperor opens his mouth to scream as the throne room plunges into darkness.

A final metallic clang echoes through the hall.

CUT TO BLACK.

[4] GLOBAL SUPPLEMENT

Nine-shot structure: Use exactly nine cinematic shots, with deliberate cuts at the specified timestamps. Each shot must advance the same continuous story, beginning with the emperor's arrogance, introducing the mysterious servant, revealing the cursed banquet, and ending with the collector demanding payment. Maintain consistent character positions and throne hall geography throughout.

Voiceover and dialogue: Include all narrator lines and character dialogue exactly as written. The narrator has a deep, resonant male voice inspired by classic 1980s fantasy trailers. The emperor speaks with theatrical authority, the servant with unnerving calm, and the undead noblewoman with a soft, hollow whisper. All spoken character dialogue must synchronize accurately with visible mouth movements. Narration remains off-screen and must not overlap important dialogue.

1980s practical effects: The undead guests must resemble actors wearing elaborate latex prosthetics, theatrical corpse makeup, and handcrafted fantasy costumes. The collector's skeletal transformation must resemble a sophisticated animatronic creature effect from an authentic 1980s fantasy production, using mechanical facial appliances, practical makeup, optical dissolves, and controlled theatrical lighting.

Character consistency: Preserve the emperor's silver hair, gray beard, golden crown, crimson cloak, and engraved armor throughout. The mysterious servant must retain his black hooded robe and golden chalice until the final reveal. All banquet guests must remain in their established positions, with their clothing unchanged during their supernatural transformations.

Visual atmosphere: Maintain rich candlelit interiors, deep crimson banners, ornate golden decorations, atmospheric smoke, warm tungsten highlights, dark theatrical shadows, organic film grain, subtle halation, and authentic photochemical softness. The transformation sequence should gradually darken the hall while preserving the visual appearance of vintage fantasy cinema.

Camera movement: Use slow dramatic push-ins, theatrical low-angle compositions, expressive close-ups, and carefully framed wide shots. Avoid excessive handheld movement, modern drone-style cinematography, or impossible camera paths.

Sound design: Begin with lively banquet ambience, clinking goblets, distant laughter, and orchestral medieval music. Gradually remove the background sounds as the curse activates, leaving an unnatural silence broken by whispers, creaking chairs, and the emperor's frightened breathing. Build the final moments with ominous low strings and the collector's deep voice before ending in sudden darkness.
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
