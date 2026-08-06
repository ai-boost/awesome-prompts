---
name: reasoning-model-prompting
description: "Reasoning / Extended Thinking Model Prompting Guide & Templates"
---

Reasoning / Extended Thinking Model Prompting Guide & Templates
Sources: Anthropic Claude Prompting Best Practices (platform.claude.com, 2025-2026),
         OpenAI o3/o4-mini Function Calling Guide (developers.openai.com, 2025),
         Helicone thinking model guide, OpenAI Reasoning Best Practices docs
------------------------------------------------------------------

WHAT MAKES REASONING MODELS DIFFERENT:

Reasoning models (o1, o3, o4-mini, Claude 3.7/Sonnet 4.6 adaptive thinking,
Gemini 2.0 Flash Thinking) run an internal chain-of-thought BEFORE producing
their response. This internal CoT is hidden — you never see it directly.

Implications:
  - They self-plan. You do not need to tell them how to think.
  - Explicit CoT instructions ("think step by step") interfere with their
    native reasoning and degrade performance.
  - They excel on 5+ step problems. They are overkill for simple queries.
  - They are slower and more expensive per token. Use them when it matters.
  - Few-shot examples often hurt rather than help (they constrain the
    model's natural reasoning path).

Mental model: treat them as a senior colleague who figures out the approach
themselves when you clearly state the goal — not a junior who needs
step-by-step instructions.

------------------------------------------------------------------
THE GOLDEN RULES:

DO:
  - State the goal clearly and completely
  - Provide all relevant context upfront (long context at TOP of prompt)
  - Use XML tags or markdown sections to separate distinct inputs
  - Set explicit output format constraints (what the final answer should look like)
  - Use "think thoroughly" or "reason carefully" over prescribed plans
  - For Claude: control depth via the effort parameter (low / medium / high / max)
  - For o3/o4: use developer messages to set role + boundaries + tool rules
  - Ask for self-verification: "Before finalizing, verify your answer against [criteria]"
  - Break multi-shot problems into well-defined sub-tasks

DON'T:
  - "Think step by step" — redundant, often harmful
  - "Let's think about this carefully before answering" — same problem
  - "First do X, then do Y, then do Z" — prescribing the reasoning path
  - Provide many few-shot examples — use zero-shot first
  - Use structured output requests (JSON, tables) — these models perform worse;
    use standard LLMs for format-heavy tasks or add strict schema enforcement
  - Give vague goals and expect inference — be explicit
  - Overload context with irrelevant detail — quality over quantity
  - Use these models for tasks with fewer than 3 reasoning steps — wasteful

------------------------------------------------------------------
WHEN TO USE REASONING MODELS vs STANDARD MODELS:

Use reasoning models for:
  Complex multi-step problems (5+ steps)
  Math, logic, code debugging, legal/medical analysis
  Agentic tasks with tool use across many steps
  Problems where accuracy matters more than speed/cost
  Ambiguous tasks requiring judgment about the right approach

Use standard models (GPT-4.1, Claude Haiku, Gemini Flash) for:
  Simple queries (< 3 reasoning steps)
  Structured output generation (JSON, CSV, templates)
  Tasks where few-shot examples are critical
  High-volume, latency-sensitive workloads
  Basic summarization, translation, extraction

------------------------------------------------------------------
CLAUDE ADAPTIVE THINKING (Sonnet 4.6 / Opus 4.6) — SPECIFIC GUIDE:

How it works: Claude dynamically decides when and how much to think based on
the `effort` parameter and query complexity. On simple queries it skips thinking
entirely. On complex queries it reasons deeply.

API configuration:
  thinking={"type": "adaptive"}
  output_config={"effort": "high"}   # low | medium | high | max

Effort settings:
  low     → high-volume, latency-sensitive tasks, simple queries
  medium  → most production applications (recommended default)
  high    → agentic coding, multi-step tool use, complex reasoning
  max     → hardest long-horizon problems (cost: significant)

Prompt guidance for effort calibration:
  To increase thinking: "Take your time and reason carefully about this."
  To reduce thinking:   "Extended thinking adds latency and should only be used
                         when it meaningfully improves answer quality. When in
                         doubt, respond directly."
  To prevent over-exploration: "Choose an approach and commit to it. Avoid
                         revisiting decisions unless you encounter new
                         information that directly contradicts your reasoning."

Interleaved thinking (after tool use):
  "After receiving tool results, carefully reflect on their quality and
   determine optimal next steps before proceeding."

Self-check pattern:
  "Before you finish, verify your answer against [specific test criteria]."

Note on extended thinking with budget_tokens: still functional on Sonnet/Opus 4.6
but deprecated. Prefer adaptive thinking + effort parameter.

------------------------------------------------------------------
OPENAI o3 / o4-MINI — SPECIFIC GUIDE:

How it works: o-series models convert system prompts to "developer messages"
automatically. They reason internally before every response and every tool call.
Do NOT instruct them to plan before calling tools — they already do this.

System prompt → developer message (auto-converted). Same format, different semantic:
  Purpose: set role, define available actions, establish tool-calling order,
           set usage boundaries.

Developer message structure:
  1. Role definition + scope of available actions
  2. Function-call ordering rules (if multi-step tool use)
  3. Tool usage boundaries (when to use which tool, when NOT to)
  4. Proactiveness / confirmation guidance

Function description rules:
  - Clarify invocation criteria explicitly ("Only call if directory exists")
  - Add argument construction rules upfront ("Do not overwrite without using
    file_delete or file_update first")
  - Use few-shot examples only for complex argument formats
  - Flat argument schemas outperform deeply nested ones
  - Up to ~100 tools and ~20 arguments per tool stays within training distribution

Anti-patterns specific to o3/o4:
  - "Plan before calling tools" → redundant, degrades performance
  - Lazy behavior accumulation → start fresh conversations for unrelated topics;
    discard irrelevant past tool calls; summarize instead
  - Hallucinating future tool calls → "Do NOT promise function calls later.
    Only call a function when you are ready to execute it."

Structured output enforcement: use `strict: true` in tool schema for validation.

Persist reasoning between tool calls (Responses API):
  include=["reasoning.encrypted_content"]
  This maintains CoT context across calls, improving tool-selection decisions.

------------------------------------------------------------------
REUSABLE SYSTEM PROMPT TEMPLATE (Claude adaptive thinking):

<system>
You are [role description].

<task_scope>
[Clear description of what you are responsible for and what is out of scope.]
</task_scope>

<output_requirements>
[Exact format, length, structure of the expected output. Be specific.]
</output_requirements>

<constraints>
[Hard limits: what you must never do, what data you must not access, etc.]
</constraints>

<quality_standard>
Before finalizing any response, verify it against:
- [Criterion 1]
- [Criterion 2]
Only respond when you are confident your answer meets these criteria.
</quality_standard>
</system>

------------------------------------------------------------------
REUSABLE DEVELOPER MESSAGE TEMPLATE (OpenAI o3/o4-mini):

You are [role]. You can help users with: [action 1], [action 2], [action 3].

Tool usage rules:
- Use [tool A] for [specific purpose].
- Use [tool B] only when [condition].
- If both [tool A] and [tool B] could apply, prefer [tool A] for [reason].
- Do NOT call any tool unless you are ready to execute it now.
- Do NOT promise future tool calls.

Execution order for [complex workflow]:
1. Call [tool A] to [retrieve/validate X]
2. Only if X is confirmed, call [tool B] with the result
3. Summarize outcome to user

When uncertain about user intent, ask one clarifying question before acting.

------------------------------------------------------------------
PROMPT PATTERNS BY TASK TYPE:

Complex analysis / reasoning:
  "Analyze [problem]. Consider [dimension 1], [dimension 2], [dimension 3].
   Provide a final recommendation with your confidence level and the
   main uncertainty you could not resolve."

Code debugging (Claude):
  "Debug this function. After your analysis, verify the fix by mentally
   tracing through [specific test case]. Only return the corrected code."

Multi-step research (o3/o4):
  "Research [topic]. For each finding, note your confidence level.
   Identify the key uncertainty that most affects the final answer.
   Do not speculate beyond available evidence."

Decision under ambiguity:
  "I need a decision on [X]. Constraints: [list]. If you need to make an
   assumption, state it explicitly and flag it so I can correct it.
   Give me your recommendation and the single most important caveat."

Agentic coding (Claude high effort):
  "Complete [task]. Use tests to verify correctness at each step.
   Do not remove or skip tests to make them pass — fix the implementation.
   After completing, summarize what you changed and why."

------------------------------------------------------------------
THINKING BUDGET / COST MANAGEMENT:

Claude (adaptive):
  Low effort:    fastest, cheapest — use for high-volume chat, simple queries
  Medium effort: best default — balances quality and cost
  High effort:   agentic coding, tool chains, complex reasoning
  Max effort:    large-scale migrations, deep research, long-horizon agents

  Prevent runaway cost:
    "Extended thinking should only be used when it meaningfully improves
     answer quality. When in doubt, respond directly without extended reasoning."

OpenAI o3/o4:
  Use o4-mini-high for most reasoning tasks (cost-efficient)
  Use o3 for the hardest problems where o4-mini falls short
  Do not use reasoning models for classification, extraction, or templating —
  those are standard model tasks

------------------------------------------------------------------
COMMON MISTAKES AND THEIR SYMPTOMS:

Mistake                         Symptom
-------                         -------
"Think step by step"            Verbose, constrained reasoning; worse answers
Too many few-shot examples      Model mimics example format instead of reasoning
Prescribing the reasoning path  Model gets locked into suboptimal approach
Using for simple tasks          Slow, expensive, often worse than GPT-4.1 / Haiku
Structured output request       Inconsistent, malformed JSON/table output
Vague goal statement            Confident-sounding but wrong answer
Over-prompting tool use         Tool overtriggering; irrelevant calls accumulate
"Explain your reasoning"        Adds output tokens without improving answer quality

------------------------------------------------------------------
QUICK REFERENCE — DO / DON'T:

DO                                        DON'T
--                                        -----
State goals clearly and completely        Prescribe reasoning steps
Use XML tags to separate input sections   Use "think step by step"
Set explicit output format requirements   Add many few-shot examples
Use effort / budget parameters            Request structured output (JSON)
Ask for self-verification at the end      Use for simple < 3-step tasks
Zero-shot first, few-shot only if needed  Over-explain the reasoning process
