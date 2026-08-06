---
name: pragmatic-programmer
description: "Pragmatic Programmer Agent Rules"
---

Pragmatic Programmer Agent Rules
Source: https://github.com/ciembor/agent-rules-books (2026, 778 stars)
Based on Andrew Hunt and David Thomas, "The Pragmatic Programmer".
Converted into binding engineering policy for AI coding agents.
------------------------------------------------------------------

## Purpose

This repository follows **The Pragmatic Programmer** in the sense of Andrew Hunt and David Thomas:
work pragmatically, take responsibility for quality, automate what is repetitive, and keep code and process adaptable.

All code generation, edits, and reviews must optimize for:
- clear ownership and responsibility
- DRY at the knowledge level
- orthogonality
- incremental delivery
- ruthless feedback
- automation of repetitive work
- code that is easy to change and easy to reason about

This file is a binding engineering policy: `MUST` is binding, `SHOULD` is a strong default, and `MUST NOT` is forbidden.

---

## Primary Directive

Be pragmatic, not dogmatic.

When uncertain, choose the option that:
1. reduces knowledge duplication
2. keeps concerns independent
3. shortens feedback loops
4. leaves the system easier to change
5. makes intent clearer to future maintainers

Do not follow style or process rituals that do not improve outcomes.

---

## Core Pragmatic Principles

### Own the Result
1. Take responsibility for the quality and changeability of the code you touch.
2. Do not blame tooling, framework defaults, or "existing style" for avoidable bad design.
3. Surface trade-offs, risks, and uncertainty explicitly.

### Think Beyond the Local Edit
1. Every change affects future maintainability.
2. Small quick fixes that multiply future cost are usually a bad bargain.
3. Leave the area better than you found it.

### Favor Adaptability
1. Build systems that are easy to observe, test, and change.
2. Prefer flexible boundaries over brittle cleverness.
3. Avoid premature commitment when requirements are still moving.

---

## DRY Rules

DRY means **do not duplicate knowledge**, not merely do not duplicate text.

1. A business rule should have one authoritative representation.
2. Validation logic for the same concept should not be scattered.
3. Status semantics, mappings, and calculations should not be copied across layers.
4. Configuration and schema meaning should not be repeated inconsistently.
5. Avoid duplicated process steps that can be automated.

Anti-patterns (MUST NOT):
- the same rule encoded in UI, API, service, and DB trigger with no ownership
- copy/paste with minor edits for "just this one case"
- duplicated manual deployment or testing steps
- one concept with multiple partially aligned implementations

---

## Orthogonality Rules

1. Keep components independent so one change does not force unrelated changes elsewhere.
2. Minimize hidden couplings through globals, ambient context, or shared mutable state.
3. Avoid overlapping responsibilities between modules.
4. Separate policy from mechanism, data from presentation, orchestration from computation.

Anti-patterns (MUST NOT):
- one change requiring edits in many unrelated places
- one module knowing too much about internal details of others
- shared utility modules creating sideways coupling everywhere

---

## Tracer Bullets and Iterative Delivery

1. Prefer a thin end-to-end slice over a pile of isolated pieces.
2. Use tracer bullets to validate architecture, integration, and assumptions early.
3. Keep the first slice simple but real enough to prove the path.
4. Refine from working feedback instead of predicting everything up front.

Anti-patterns (MUST NOT):
- building many layers before anything runs end to end
- treating prototypes as production without hardening
- waiting for perfect certainty before integrating

---

## Prototyping Rules

1. Use prototypes to learn, not to pretend you are done.
2. Be explicit about what a prototype proves and what it does not.
3. Do not let experimental shortcuts silently become production defaults.
4. Carry forward only the lessons or code that still deserve to survive.

---

## Automation Rules

1. Automate repetitive, error-prone, or easy-to-forget tasks.
2. Prefer repeatable scripts over tribal-knowledge commands.
3. Build, test, lint, format, package, and deploy steps should be reproducible.
4. Keep local automation aligned with CI/CD behavior.

Anti-patterns (MUST NOT):
- "works on my machine" build steps
- manual release rituals with many hidden prerequisites
- documentation that describes what a script should do instead of having the script

---

## Feedback Loop Rules

1. Shorten the time between change and feedback.
2. Run relevant tests early and often.
3. Use static analysis, linters, and type checks where they reduce real risk.
4. Make failure visible fast.
5. Prefer a cheap early signal over a late expensive surprise.

---

## Design by Contract and Assertions

1. Make assumptions explicit in code.
2. Use assertions or invariant checks where they clarify impossible states.
3. Distinguish between programmer errors, contract violations, and expected domain failures.
4. Keep contracts close to the abstraction they protect.

Anti-patterns (MUST NOT):
- relying on comments for critical preconditions
- hiding invariant assumptions in scattered callers
- returning nonsense values for impossible states

---

## Error Handling and Recovery

1. Detect errors close to their source.
2. Do not discard useful error context.
3. Let callers distinguish retryable, recoverable, and permanent failures where relevant.
4. Fail loudly enough to diagnose, but with boundaries that prevent system-wide collapse.

---

## Naming and Communication Rules

1. Code is communication first.
2. Use names that reflect domain meaning and developer intent.
3. Prefer clarity over cleverness.
4. Write comments or docs where they convey decision rationale, contracts, or non-obvious behavior.
5. Writing is part of engineering, not overhead.

---

## Text and Data Rules

1. Favor plain text and open formats for long-lived automation and integration where practical.
2. Make scripts and configs inspectable and diffable.
3. Keep serialization and config formats explicit and version-aware.
4. Avoid opaque binary or framework-specific lock-in unless justified.

---

## State and Concurrency Rules

1. Treat shared mutable state as expensive.
2. Prefer immutability, isolation, or explicit synchronization when state is shared.
3. Keep concurrency assumptions visible.
4. Do not add asynchronous complexity unless it clearly earns its cost.

---

## Estimation and Increment Rules

1. Break work into pieces that can be reasoned about, tested, and corrected.
2. Keep plans and estimates honest about uncertainty.
3. Prefer small deliverable increments to large hidden progress.
4. Make risk visible early.

---

## Tooling Rules

1. Know and use the tools that amplify correctness and speed.
2. Do not hand-do tasks that should be scripted.
3. Keep editor, formatter, lint, tests, and local scripts aligned with team standards.
4. Improve the toolchain when repeated friction appears.

---

## Broken Windows Rule

1. Do not normalize local decay.
2. Fix small quality problems before they signal that nobody cares.
3. Tidy the code you touch where the cost is low and the value is immediate.
4. Avoid leaving behind "temporary" hacks with no cleanup plan.

---

## Review Rules

When reviewing code, actively look for:
- duplicated knowledge, not just duplicated lines
- hidden couplings
- missing automation opportunities
- long feedback loops
- local fixes that worsen future changeability
- unclear contracts or assumptions
- non-repeatable manual processes
- brittle integration points
- code that communicates poorly

---

## Forbidden Patterns

### Cargo-Cult Process
- rituals followed with no benefit
- documentation and checklists replacing automation

### Knowledge Duplication
- same rule in many places
- copied logic because "layers need it too"

### Non-Orthogonal Design
- modules with overlapping responsibilities
- changes leaking across boundaries by default

### Manual Everything
- repeated human steps for build, test, release, setup, or validation
- hidden local environment assumptions

### Prototype Fossilization
- experimental code promoted to production without redesign or hardening

---

## Code Generation Rules

When generating code, default to:
1. one clear source of truth for each rule
2. orthogonal responsibilities
3. fast local feedback
4. automation over repeated manual work
5. explicit contracts and assumptions
6. readable names and communication
7. incremental end-to-end slices when building new capabilities

Avoid by default:
- copy/paste rule duplication
- tangled modules
- fragile manual workflows
- overcommitting to an architecture before the first end-to-end path works

---

## Testing Rules

1. Keep tests runnable quickly and often.
2. Prefer tests that align with the business or technical contract being protected.
3. Use automation so validation is habitual, not heroic.
4. Keep flaky or environment-dependent tests out of the critical feedback path where possible.

---

## Review Checklist

Before finalizing any change, verify:
- Did we reduce duplicated knowledge?
- Are responsibilities more orthogonal after the change?
- Did we improve or preserve fast feedback?
- Did we automate anything repetitive that was hurting reliability?
- Are contracts and assumptions clearer?
- Is the code easier to communicate about?
- Did we avoid prototype shortcuts becoming silent production defaults?
- Did we fix at least one small "broken window" if it was in the touched area?

If any answer is no, revise before shipping.

---

## Final Instruction

When uncertain, choose the option that:
1. removes duplicated knowledge
2. keeps concerns orthogonal
3. shortens feedback loops
4. improves automation
5. leaves the codebase easier to change tomorrow

Be pragmatic, and make the right thing the easy thing.
