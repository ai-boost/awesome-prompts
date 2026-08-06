---
name: adhd-parallel-ideation-skill
description: "name: adhd"
---

---
name: adhd
description: Parallel divergent ideation for coding agents. Spawns N isolated branches under different cognitive frames (regulator, biology, speedrunner, 10-year-old, $0 budget), scores, clusters, prunes traps, and deepens top survivors. Use on /adhd, "ADHD mode", brainstorm/ideate intents, or open-ended design, architecture, naming, API/SDK surface, and fuzzy-debugging decisions. Skip for syntax, lookups, bugs with known root cause, or closed phrasing ("quick", "standard", "canonical", "textbook"). Full pre-flight gate is in the skill body.
license: MIT
---

# ADHD

Stop picking the textbook answer. The first three answers the model would
give are the answers a senior engineer would give in thirty seconds.
Correct. Forgettable. The interesting answers live past number three, in
the awkward middle nobody walks into. This skill makes the model walk
there.

## Pre-flight (run before Phase 1)

This skill is expensive. About 10 Agent calls, 30 to 90 seconds wall clock,
5 to 10x a single answer. Do not pay that cost when a direct answer is
better. Run this gate before Phase 1.

**Step 1. Explicit invocation check.**

If the user typed `/adhd` or explicitly asked for ADHD mode, "use the
adhd skill", or "run ADHD on this", **SKIP the rest of this section and go
straight to Phase 1**. The user opted in. Do not second-guess.

**Step 2. Self-judge (only if Step 1 did not match).**

Ask yourself three questions. If the answer to any is no, ABORT.

1. **Open-ended?** Would a senior engineer give multiple viable answers
   here, or is there one canonical answer? If canonical, abort.
2. **High-stakes?** Is the cost of the obvious answer being wrong actually
   high? Architecture decisions, public API surfaces, naming a real
   product, fuzzy bugs with no known root cause, schema design = yes.
   Side project at 11pm = no.
3. **Open phrasing?** Did the user avoid words like "quick", "standard",
   "canonical", "textbook", "just", "one-line"? If they used any of those,
   they want the direct answer. Abort.

If all three checks pass, proceed to Phase 1.

If any fails, ABORT and answer the question directly. Optionally append
one sentence: *"If you want a wider exploration under parallel cognitive
frames with explicit trap detection, run `/adhd <your problem>`.*"

## When to trigger (summary)

Strong signals to invoke:

- explicit `/adhd <problem>` or "use ADHD mode" (unconditional)
- *"give me a few ways to…"*, *"brainstorm…"*, *"what are some approaches"*
- *"the obvious answer feels wrong"*, *"I'm stuck on X"*
- architecture or design decision on something that ships
- fuzzy bug, no known root cause, user wants hypothesis classes
- naming for a public product, API, SDK surface

Strong signals to NOT invoke:

- factual lookup, syntax help, "what is X"
- bug fix with a known root cause
- "quick", "standard", "canonical", "textbook", "just show me"
- inner-loop / per-keystroke work
- the answer is one search query away

## The loop

Two strict phases. Mixing them kills idea quality, because the critic
strangles the generator.

### Phase 1 — Diverge (no critic)

For the problem P:

1. Pick 5 cognitive frames from the table below. Bias toward engineering
   tags when the problem is code-shaped. Always include at least one wild
   frame to keep range.

2. Spawn 5 **parallel** Agent/Task tool calls. One per frame. Each Agent
   gets only:
   - the problem P
   - any context the user provided
   - the chosen frame's vantage prompt
   - a system instruction that forbids evaluation

   The exact instruction to give each Agent:

   > You are in DIVERGENT mode. You are a generator, not a critic.
   > Generate 6 short distinct ideas under this frame. Each idea is one
   > phrase or one sentence. Do not evaluate. Do not rank. Do not hedge.
   > The first three obvious answers everyone would give are banned.
   > Push past them into the awkward middle.
   > Output a JSON array only. No prose before or after.
   > `[{"text": "...", "rationale": "..."}, ...]`

3. **Critical invariant.** The Agent calls must be parallel and isolated.
   Do NOT serialize them. Do NOT pass one branch's output as context to
   another. Branches that see each other anchor each other and the whole
   method collapses to a wider single thought.

### Phase 2 — Focus (critic on)

After all branches return:

1. **Score.** Rate each idea on three axes 0 to 10: novelty (distance from
   the obvious default), viability (could it actually ship), fit (does it
   address the stated problem). For any idea that looks attractive but is
   a trap (hidden cost, false economy, will not scale, premature
   abstraction), flag it with a one-line reason.

2. **Cluster.** Group ideas into 3 to 6 clusters by their underlying angle,
   not by surface keywords. Label clusters by angle: "remove the server
   plays", "cache-shaped plays", "batched-window plays", "race-multiple-
   backends plays".

3. **Deepen the top 3.** Rank by weighted score (novelty 0.35 + viability
   0.40 + fit 0.25), exclude traps, take top 3. For each, spawn one Agent
   call that produces:
   - a 4 to 8 sentence sketch of how the idea works
   - the load-bearing risk
   - the first concrete step a builder would take
   - 3 to 5 child ideas (variations, hybrids, unlocks)

   Deepen Agent instruction:

   > You are in FOCUS mode. Take one promising idea and connect dots.
   > Sketch how it would actually work in 4 to 8 sentences. Name the
   > load-bearing risk. Name the first concrete step a coder would take.
   > Then generate 3 to 5 sub-ideas that branch off (variations,
   > combinations with other domains, things this unlocks).
   > Output JSON only.

## Frames

Pick 5 per run.

| Frame | Vantage prompt | Tags |
|---|---|---|
| **hardware engineer** | You think in latency, memory layout, and physical constraints. Re-ask this as a hardware/firmware problem. What does the bus topology, cache, timing budget tell you? | code, wild |
| **regulator** | You audit systems for compliance and failure modes. What must be provable, traceable, or refusable here? | design, general |
| **10-year-old** | You are a curious 10 year old who has never seen software. Describe naive but unencumbered approaches. Ignore convention. | general, wild |
| **competitor trying to break it** | You are a hostile competitor or attacker. Generate approaches that exploit, fail, or sabotage the obvious solution. Then invert into ideas. | code, design |
| **biology** | Transplant a mechanism from biology (immune systems, neural plasticity, cell signaling, evolution, gut flora). Force-fit it onto this engineering problem. | code, wild |
| **logistics** | Steal mechanisms from logistics: queues, batching, just-in-time, hub-and-spoke, returns, last-mile. Apply them literally. | code, design |
| **game design** | Approach this as a game designer. What are the loops, rewards, friction, save-states, speedrun tricks? Treat the user as a player. | design, general |
| **markets** | Treat the problem as a market. Buyers, sellers, market-makers. What does an auction, a futures contract, a clearing house look like here? | design, wild |
| **inversion** | Ask the OPPOSITE question. If goal is X, brainstorm how to guarantee NOT X. Then negate each answer back. | code, design, general |
| **extreme: $0 budget, 1 hour** | No money, no team, one hour. What is the crudest version that still does the load-bearing thing? | code, general |
| **extreme: infinite budget, 10 years** | Infinite compute, infinite engineers, a decade. What is the maximalist version? | design, wild |
| **remove the load-bearing assumption** | Name the thing everyone treats as fixed (framework, database, request-response model, network). Imagine it is gone. What is possible? | code, design, wild |
| **speedrunner** | You are a speedrunner. Find glitches, skips, out-of-bounds tricks, frame-perfect shortcuts. What is the abusive-but-legal path? | code, wild |
| **ant colony** | No central planner. Many dumb agents, local rules, pheromone trails. How does the problem solve itself emergently? | code, wild |
| **3am on-call** | You are the on-call engineer woken at 3am when this breaks. What design would let you not get paged? | code, design |

### Picking frames

For code-shaped problems: pick 4 frames tagged `code` or `design`, plus 1
tagged `wild`. For open product or strategy problems: a mix from all tags.
Vary the picks across sessions so the same problem produces different
candidate sets when re-run.

## Output shape

After Phase 2, render in this order. Do not collapse it into a wall of
prose. The structure is the point.

1. **Brief.** One or two lines confirming the problem and any reframe used.
2. **Wide set.** Full pool grouped by cluster. Each cluster labeled by
   underlying angle. Each idea is one short phrase. Show score chips like
   `[N7 V8 F9]` next to each.
3. **Converge.** A 2 to 4 idea shortlist. State why each is on the list.
   Mark the non-obvious-but-viable pick explicitly with ★. List traps
   separately, each with the one-line reason it is a trap.
4. **Focus.** The 3 deepened branches. For each: the sketch, the load-
   bearing risk, the first concrete step, and the child ideas.
5. **Provocation.** One wildcard question or idea that opens a new
   direction the user can push into if nothing landed.

## Anti-patterns

These are how this skill goes wrong. Watch for them.

- **Convergence disguised as divergence.** Ten minor variations of one idea
  is not breadth. If every candidate shares the same underlying assumption,
  you have not diverged. You have decorated.
- **Weird-for-weird's-sake with no convergence.** A pile of 30 unsorted
  absurdities is as useless as one safe answer. Always converge.
- **Walls of equally-weighted prose.** Cluster, label, pull out the best.
  Structure is half the value.
- **Refusing to commit.** After diverging, take a position on what is
  actually promising. "Here are 20 ideas, you decide" is a cop-out.
  Generate wide, but converge with a real opinion.
- **Skipping the isolation invariant.** If you simulate parallel branches
  by writing them sequentially in one context, you have not done ADHD. You
  have done a wider single thought. The Agent/Task tool gives each branch a
  fresh context. Use it.

## Calibration

- **How many ideas?** Scale to stakes. Quick "name this function" =
  3 frames × 4 ideas. "How should I position this product" = 5 frames ×
  8 ideas. Default is 5 × 6 = 30.
- **How weird?** Read the room. Serious strategy work: flag the wild cards
  clearly so they do not read as unserious. Open brainstorming or play:
  let it run loose. Absurd ideas earn their place by seeding viable ones.
- **When to stop diverging?** Stop when new candidates start repeating the
  shape of existing ones. The space is mapped. Do not pad to hit a number.

## Cost

5 diverge + 1 score + 1 cluster + 3 deepen ≈ 10 Agent calls per run.
About 5 to 10x a single-shot answer. Not for every keystroke. For decision
points where the cost of the obvious answer is high.

## Companion library and CLI

There is a Node/TS implementation that does the same loop with structured
JSON parsing, score weighting, and a CLI. Use it when running outside
Claude Code or in batch.

    npm install -g adhd-agent
    adhd "your problem here"

Code, paper, evals, and contributing guide at
https://github.com/UditAkhourii/adhd. The skill above gives you the same
loop inside Claude with no install required.

## Source spec

This skill operationalises a written spec on divergent ideation. The
original prose is preserved in `SOURCE-SPEC.md` for reference. The
implementation choices made here (parallel isolated Agent calls,
mechanical generator/critic split, frame-based branching) follow from
that spec.
