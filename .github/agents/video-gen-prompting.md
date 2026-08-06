---
name: video-gen-prompting
description: "AI Video Generation Prompt Guide & Templates"
---

AI Video Generation Prompt Guide & Templates
Sources: OpenAI Sora 2 Cookbook (2025), Runway Gen-3 official docs, Kling 2.6 community guide,
         Medium/@creativeaininja model-specific strategies (2025-2026)
------------------------------------------------------------------

CORE PHILOSOPHY:

Treat a video prompt like a cinematographer's brief to a director.
Specify: WHAT is happening, HOW the camera moves, WHAT the light does, and WHEN things change.
Vagueness yields randomness. Specificity yields control.

Each model has a distinct "personality":
  Runway Gen 4.5  → kinetic sculptor; obsessed with physics and camera movement
  Kling 2.6       → audio-visual choreographer; generates synced sound + video
  Veo 3 / 3.1     → rendering engine; loves structured data and reference images
  Sora 2          → physics simulator; models cause, effect, and inertia

------------------------------------------------------------------
UNIVERSAL PROMPT STRUCTURE (works across all models):

[STYLE INTENT] — cinematic short film | documentary | commercial | music video
[SHOT TYPE + FRAMING] — wide establishing shot | medium close-up | aerial
[CAMERA MOVEMENT] — slow dolly-in | handheld ENG | crane boom up | static
[SUBJECT + ACTION] — described in beats/counts, not vague adjectives
[ENVIRONMENT] — foreground, midground, background, weather
[LIGHTING] — source, direction, quality, color palette anchors
[DURATION HINT] — 4s / 8s / 12s (models follow shorter clips more reliably)

Rule: One camera move + one subject action per shot.

------------------------------------------------------------------
SHOT TYPE VOCABULARY:

Wide establishing shot, eye level
Aerial wide shot, slight downward angle
Medium shot, straight on
Medium close-up, slight angle from behind
Close-up (face / object), tight framing
Extreme close-up, macro detail
Two-shot, over-the-shoulder

------------------------------------------------------------------
CAMERA MOVEMENT VOCABULARY:

Horizontal:  pan left / pan right | truck left / truck right
Vertical:    tilt up / tilt down | boom up / boom down | crane shot
Depth:       dolly in / dolly out | zoom in / zoom out
Complex:     tracking shot | whip pan | handheld ENG | gimbal smooth
Modifiers:   slow | fast | steady | shaky | floating | rapid

------------------------------------------------------------------
LIGHTING VOCABULARY:

Quality:    soft diffuse | hard directional | volumetric | HDR specular
Source:     practical window light | neon sign | overhead fluorescent |
            candle | morning sun | golden hour | blue hour
Direction:  45° key right | rim from behind | flat fill | negative fill
Palette:    "warm amber + cream + walnut" | "teal + coral + concrete grey" |
            "cool daylight 5600K with tungsten practicals"

------------------------------------------------------------------
STRONG vs WEAK — COMPARISON TABLE:

Weak                          Strong
----                          ------
"Beautiful street at night"   "Wet asphalt, zebra crosswalk, neon reflections
                               pooling in puddles"
"Person moves quickly"        "Cyclist pedals three times, brakes hard at
                               crosswalk, front wheel skids"
"Cinematic look"              "Anamorphic 2.0x lens, shallow DOF, volumetric
                               light shafts, grain at ISO 800"
"A car crash"                 "Heavy sedan at high velocity impacts concrete
                               barrier. Hood crumples with resistance; glass
                               shatters with momentum; chassis recoils."
"Brightly lit room"           "Soft window light with warm lamp fill, cool rim
                               from hallway; palette: amber, cream, walnut brown"

------------------------------------------------------------------
SORA 2 — SPECIFIC TECHNIQUES:

Best for: physics-heavy action, fluid dynamics, complex object interactions.

Causal chain technique — explain WHY things happen:
  "Glass tipped by elbow. Liquid breaches rim, impacts table, shatters from
   impact force, milk spreads with surface tension holding droplets on wood grain."

Scaffolded multi-shot template:
  [Scene headline]
  Shot 1 (0-5s): [Angle] + [Action]
  Shot 2 (5-10s): [New angle] + [Action continuation]
  Shot 3 (10-15s): [Close-up] + [Resolution]
  Physics Notes: [Global rules — e.g. "low gravity", "wet surfaces"]

API-only parameters (must be set outside prompt text):
  model: sora-2 or sora-2-pro
  size: 1280x720 | 720x1280 | 1920x1080 (pro only)
  seconds: 4 | 8 | 12 | 16 | 20

Characters API: reuse character references across shots (max 2 per generation).

Physics glitch fixes:
  Object morphing      → "remains solid and rigid throughout"
  Weightless motion    → include weight descriptors: heavy, dense, solid
  Unrealistic impact   → specify: "baseball hits window creating spiderweb crack"
  Floating objects     → negative: "no clipping, no defiance of gravity"

------------------------------------------------------------------
RUNWAY GEN 4.5 — SPECIFIC TECHNIQUES:

Best for: commercials, VFX, product shots, physics-heavy scenes.

Force-reaction syntax:
  Not: "A car drives fast"
  Use: "Vehicle moving at high velocity, tires spray water as chassis leans
        into curve, inertia carries weight, gravel pings undercarriage."

Camera control tokens (use exactly):
  Camera pan left | Camera pan right
  Camera tilt up | Camera tilt down
  Truck left | Truck right
  Zoom in | Zoom out
  Dolly in | Dolly out
  Boom up | Boom down

Motion Brush workflow (in-tool):
  1. Paint foreground with motion vector left (-3)
  2. Paint background with vector right (+1)
  3. Reinforce in text: "Camera trucking right, foreground moves past quickly"

Common fixes:
  Morphing objects → "remains solid and rigid throughout"
  Weightless motion → add weight terms: heavy, dense, hollow, solid
  Jerky camera → "smooth dolly in" or "steady pan right"
  Motion blur artifacts → lower brush strength, add "crisp motion"

------------------------------------------------------------------
KLING 2.6 — SPECIFIC TECHNIQUES:

Best for: music videos, dialogue scenes, narrative with spoken lines.

Timeline script template:
  Cinematic [aspect ratio], [visual style]

  Beat 0-4s:  [Camera angle] + [Scene description]
  Beat 4-8s:  [Camera change] + [Action]
  Beat 8-10s: [Final shot or reaction]

  Audio:
    0-4s: [Ambient sound]
    4.5s: SFX: [Sound effect synchronized to action]
    8s:   Dialogue ([Character name], [Tone]): "Line here"

Lip sync rules:
  Keep dialogue under 5 seconds per line
  Format: "Beat 5-8s: Close-up. Detective (Male, Weary): 'I don't believe
           in coincidences.'"
  Tone descriptors: (whispering) | (shouting) | (breathy) | (resigned)

Negative prompts (use the negatives field, not in main prompt):
  Audio:   "no background music, no mumble, no overlapping speech, no distortion"
  Visual:  "no text overlays, no blurring, no morphing, no extra limbs"

Character consistency: use Elements feature — upload reference image, tag as
Element, reference by name in all future prompts.

------------------------------------------------------------------
VEO 3 / 3.1 — SPECIFIC TECHNIQUES:

Best for: brand-consistent series, personalized campaigns, multi-shot automation.

Structured prompt (JSON-style):
  Project: [Cinematic Commercial / Documentary / etc.]
  Aspect ratio: 16:9
  Cinematography:
    Camera gear: Alexa Mini LF
    Lens: Anamorphic 35mm
    Shot type: Medium close-up
    Movement: Slow dolly in
    Lighting key: Softbox 45° right
    Lighting fill: Negative fill left
    Contrast ratio: High contrast 8:1
  Subject:
    Description: [person, age, attire]
    Action: [beat-by-beat action description]
    Expression: [start state → end state]
  Audio:
    Dialogue: [labeled by character name]
    Ambience: [room tone, environment]

Interpolation feature: provide start frame + end frame as image uploads;
Veo fills the motion between them — best for seamless scene transitions.

Masked editing: regenerate only a specific region without re-creating entire scene.

Ingredients workflow: upload Midjourney keyframes as reference images for
visual consistency across a series.

------------------------------------------------------------------
SORA 2 — FULL REUSABLE PROMPT TEMPLATE:

[Plain language scene description: characters, costumes, scenery, weather]

Cinematography:
  Camera shot: [framing + angle]
  Mood: [overall tonal intent]

Actions:
  - [Beat 1: specific action with count or timing]
  - [Beat 2: distinct next beat]
  - [Beat 3: resolution or reaction]

Dialogue (if any):
  [Character (Tone)]: "Natural, concise line"

Background Sound:
  [Ambient sound cue — rhythm guide, not full soundtrack]

------------------------------------------------------------------
ULTRA-DETAILED PRODUCTION TEMPLATE (for maximum control):

Format & Look:    [emulated film stock: Kodak Vision3, Fuji Eterna | grain level |
                   shutter angle: 180° for standard, 45° for stutter effect]
Lens & Filter:    [focal length + anamorphic ratio + filter: diffusion, polarizer]
Color Grade:      [highlights: warm amber | mids: neutral | shadows: deep teal |
                   overall contrast: high / low]
Lighting:         [key source + angle | bounce | negative fill | practicals |
                   atmospheric: haze, smoke, dust motes]
Location:         [foreground element | midground action | background depth]
Wardrobe/Props:   [specific textures, colors, materials]
Sound:            [diegetic: footsteps, door, engine | added: score, SFX]
Shot breakdown:
  Shot 1 [duration]: [purpose — establish location] — [description]
  Shot 2 [duration]: [purpose — introduce character] — [description]
  Shot 3 [duration]: [purpose — reveal/payoff] — [description]

------------------------------------------------------------------
HYBRID WORKFLOW (professional pipeline):

Step 1 — Keyframe generation:    Midjourney (full art direction control)
Step 2 — Motion synthesis:       Veo 3.1 interpolation (start + end frame upload)
Step 3 — Dialogue / audio sync:  Kling 2.6 with timeline script
Step 4 — Upscaling:              Topaz Video AI → 4K output

Audio-first music video workflow:
  1. Generate audio in Suno or ElevenLabs
  2. Export beat timestamps
  3. Map timeline script beats to audio timestamps in Kling
  4. Enable lip-sync mode with character reference

------------------------------------------------------------------
MODEL SELECTION GUIDE:

Model           Best use case
-----           -------------
Runway Gen 4.5  Commercials, VFX, physics-heavy action, product shots
Kling 2.6       Music videos, dialogue scenes, narrative with spoken lines
Veo 3.1         Brand-consistent series, automation, reference-image anchoring
Sora 2          Physics simulation, fluid dynamics, complex interactions

------------------------------------------------------------------
COMMON FAILURE PATTERNS + FIXES:

Problem                         Fix
-------                         ---
Inconsistent style across shots Create master style reference, use as ingredient
                                 or Element in every generation
Quality degrades on iterations  Don't iterate in-tool — regenerate from upscaled still
Runway: motion blur artifacts   Lower brush strength; add "crisp motion"
Kling: dialogue bleed           Use explicit [Character Name] brackets per line
Veo: reference image ignored    Mention the reference explicitly in prose too
Sora: physics glitches          Break into simpler sub-scenes; add causal chain
All models: morphing objects     "remains solid and rigid throughout"
All models: weightless motion    Use weight-specific nouns: heavy, dense, hollow

Duration note: all models follow shorter clips more reliably.
For 8s of action, consider generating two 4s clips and stitching.
