---
name: chain-of-draft
description: "Chain of Draft (CoD) Prompting Technique"
---

Chain of Draft (CoD) Prompting Technique
Source: "Chain of Draft: Thinking Faster by Writing Less" — arXiv 2502.18600 (Feb 2025)
------------------------------------------------------------------

TECHNIQUE OVERVIEW:
Chain of Draft constrains each reasoning step to ≤5 words, forcing minimal but essential
intermediate thinking. On GSM8k math: 91% accuracy vs CoT's 95%, using only 7.6% of tokens.
Latency reduction up to 76%.

------------------------------------------------------------------
BASIC SYSTEM PROMPT:

Think step by step, but only keep a minimum draft for each thinking step, with 5 words at most.
Return the answer after a #### separator.

------------------------------------------------------------------
EXTENDED SYSTEM PROMPT (for complex tasks):

Think step by step. For each reasoning step, write a minimal draft of 5 words or fewer — only
the essential operation or transformation. Do not explain; just note what you are doing.

After all steps, write #### on its own line, then give the final answer.

Example format:
Step 1: [≤5 words]
Step 2: [≤5 words]
Step 3: [≤5 words]
####
[Final answer here]

------------------------------------------------------------------
USAGE NOTES:

- Best for: math word problems, logical reasoning, multi-step calculations
- Not ideal for: creative writing, open-ended generation, tasks requiring explanation
- Works with: GPT-4, Claude 3+, Gemini 1.5+
- Token savings: ~92% vs standard CoT; latency: up to 76% lower
- Accuracy tradeoff: ~4% below CoT on math benchmarks — acceptable for most real-world use

------------------------------------------------------------------
FEW-SHOT EXAMPLE:

User: "Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 balls.
How many tennis balls does he have now?"

Model:
Step 1: 2 cans × 3 balls
Step 2: 6 new balls
Step 3: 5 + 6 = 11
####
11
