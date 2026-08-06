---
name: flux-image-gen
description: "Flux Image Generation Prompt Guide & Template"
---

Flux Image Generation Prompt Guide & Template
Source: Black Forest Labs official guide + community best practices (2025)
------------------------------------------------------------------

CORE TEMPLATE:

{camera} at {aperture}: {subject + action}, {environment & atmosphere},
{lighting}, {style reference}.

EXAMPLE:

Hasselblad X2D 100C with 90mm lens at f/4: a woman emerges from morning mist
on a mountain ridge, crystalline frost formations catching early light,
golden alpenglow with deep teal shadows, inspired by Ansel Adams,
cinematic depth of field, wide aspect ratio.

------------------------------------------------------------------
WORD ORDER — MOST IMPORTANT FIRST:

Flux weights earlier tokens more heavily. Structure as:
1. Main subject + action
2. Critical style element
3. Environment/setting
4. Lighting
5. Secondary details

------------------------------------------------------------------
TECHNICAL LAYER (include in every prompt):

Camera body:    Hasselblad, Leica, Sony A7R4, Nikon Z9, Canon R5, Pentax 645Z
Lens focal:     35mm (wide/environmental), 50mm (natural), 85mm (portrait),
                135mm (compressed), 200mm (telephoto isolation)
Aperture:       f/1.2–f/2 (shallow blur), f/4 (balanced), f/8–f/11 (sharp),
                f/16 (landscape, all in focus)
Lighting:       golden hour, blue hour, overcast diffuse, Rembrandt,
                backlighting, practical neon, strobe, bioluminescent

------------------------------------------------------------------
STYLE REFERENCES:

Photographers:  Ansel Adams (landscape), Annie Leibovitz (portrait),
                Gregory Crewdson (cinematic), Hiroshi Sugimoto (minimalist),
                Steve McCurry (documentary), Peter Lik (nature)
Art styles:     art deco, bauhaus, ukiyo-e, brutalist, cyberpunk,
                solarpunk, dark academia, cottagecore
Film palettes:  "Blade Runner 2049" (teal-orange), "The Grand Budapest Hotel"
                (pastel), "Mad Max: Fury Road" (desaturated orange),
                "Moonlight" (blue-gold)

------------------------------------------------------------------
PROMPT LENGTH GUIDE:

10–30 words:   Quick iteration, exploring concepts
30–80 words:   Standard — best for most projects
80–120 words:  Detailed scenes with many specific elements
120+ words:    Complex compositions; diminishing returns past ~150 words

------------------------------------------------------------------
LANGUAGE RULES:

✓ Use action verbs:     "emerges through mist" not "mountain with mist"
✓ Use flowing prose:    avoid comma-separated keyword lists
✓ Be specific:          "Hasselblad at f/4" not "professional camera"
✓ Text in images:       use quotation marks: "the text you want"
✗ Avoid negative terms: describe what you want, not what to exclude
✗ Avoid "high quality", "best", "ultra HD" — they rarely help

------------------------------------------------------------------
ATMOSPHERE MODIFIERS:

Weather:     "rain-slicked streets", "swirling snowstorm", "heat haze shimmer",
             "sea fog rolling in", "lightning on horizon"
Time:        "30 minutes before sunrise", "golden hour last light",
             "blue hour just after sunset", "3am city quiet"
Mood:        "melancholic stillness", "charged anticipation",
             "serene isolation", "electric tension"

------------------------------------------------------------------
QUICK REFERENCE — COPY AND FILL:

[Camera model] with [focal length]mm lens at [aperture]:
[subject] [action verb], [environmental detail],
[atmospheric condition], [lighting description],
inspired by [photographer/artist], [mood adjective] tone.

------------------------------------------------------------------
FLUX vs DALL-E vs MIDJOURNEY:

Flux:        Best for photorealism, follows long complex prompts precisely,
             camera/lens terminology works especially well
DALL-E 3:    Best for illustrated/stylized, auto-optimizes your prompt,
             literal and precise interpretation of unusual requests
Midjourney:  Best for stylized artistic output, use --ar --s --chaos params,
             shorter prompts often outperform long ones
