---
name: agents-best-practices
description: "name: agents-best-practices"
---

---
name: agents-best-practices
description: "Use this skill when designing, generating an MVP blueprint for, auditing, refactoring, or explaining an agentic harness for any domain. Covers provider-neutral agent architecture for OpenAI, Anthropic, and OpenAI-compatible APIs: agent loops, tool design, permissions, system prompts, planning, goals, context compaction, memory, skills, MCP/external connectors, observability, evals, prompt caching, agent-legible environments, feedback loops, and safety."
metadata:
  version: "1.2.0"
  scope: "provider-neutral-agent-harness"
  file_policy: "markdown-only"
---

# Agents Best Practices

Use this skill when the user asks how to build, improve, debug, or evaluate an agentic harness. This is a general-purpose agent architecture skill. Coding agents are one subdomain only; apply the same principles to research, finance, legal, support, operations, sales, healthcare, education, data analysis, procurement, and workflow automation agents.

## Core stance

An agent harness is the control plane around a model. The model proposes actions; the harness validates, authorizes, executes, records, summarizes, and returns observations. Keep the loop simple and make the runtime rigorous.

Default architecture:

```text
user/task
  -> instruction and context builder
  -> model call
  -> tool/action proposal
  -> schema validation
  -> permission decision
  -> execution or approval pause
  -> structured observation
  -> context update
  -> repeat within budget or finish
```

## When to activate this skill

Use this skill for prompts involving any of these intents:

- build an agent, agentic workflow, AI worker, autonomous assistant, or harness;
- create a domain-specific MVP agent design, starter harness, implementation blueprint, or first production-safe version;
- choose between OpenAI, Anthropic, OpenAI-compatible APIs, direct tool loops, hosted tools, or SDKs;
- design tools, permissions, guardrails, approval flows, or sandboxing;
- create planning mode, goal mode, todo tracking, or long-running task behavior;
- add context compaction, memory, retrieval, scoped instructions, or prompt hierarchies;
- attach Agent Skills, reusable workflows, MCP servers, external connectors, or tool search;
- audit an existing agent for reliability, cost, prompt-cache hit rate, safety, latency, or observability;
- create system prompts or developer instructions for a domain-specific agent;
- make source-of-truth knowledge, validation signals, logs, metrics, or workflow state legible to an agent.

Do not use this skill for ordinary single-turn writing, translation, or Q&A unless the user is asking about the design of an agent that will perform those tasks.

## How to use this skill

First, identify the user's design problem:

1. **Domain**: what work the agent performs.
2. **Autonomy level**: answer-only, draft-only, approval-gated action, or autonomous action within policy.
3. **Risk level**: read-only, internal write, external communication, financial, legal, healthcare, security, destructive, or privileged.
4. **State duration**: single turn, multi-turn session, resumable workflow, or long-running goal.
5. **Tool surface**: internal APIs, hosted tools, MCP/external connectors, browser, sandbox, filesystem, database, communication, or computation.
6. **Validation**: what proves the task is complete.

Then load the most relevant reference files, not all files by default. If the user asks to make or build an agent for a domain, default to MVP Builder Mode.

## MVP Builder Mode

When the user asks to make, build, design, scaffold, or specify an agent for a domain, produce a concrete domain-specific MVP harness blueprint, not only advice. Use [mvp-agent-blueprint.md](references/mvp-agent-blueprint.md) as the primary reference and load other references as needed.

Default behavior:

1. Infer a reasonable first version from the user's domain and stated constraints.
2. State assumptions briefly instead of blocking on missing details.
3. Design the smallest safe harness that can accomplish useful work.
4. Include the core agentic loop, tool registry, permission matrix, context/memory/compaction, planning mode, goal-like loop criteria, skills/connectors, prompt-cache/cost strategy, observability, evals, and launch path.
5. Mark high-risk actions as draft-only or approval-gated by default.
6. Avoid multi-agent orchestration until the single-agent MVP has measurable failure cases that require decomposition.

## Reference map

- Read [mvp-agent-blueprint.md](references/mvp-agent-blueprint.md) first when the user asks to create a new domain-specific agent or MVP harness.
- Read [architecture.md](references/architecture.md) for the full harness model and component boundaries.
- Read [agent-legibility-feedback-loops.md](references/agent-legibility-feedback-loops.md) for source-of-truth knowledge bases, agent-legible environments, validation loops, mechanical invariants, and recurring cleanup.
- Read [agentic-loop.md](references/agentic-loop.md) for the provider-neutral loop, step budgets, retries, and loop variants.
- Read [tools-and-permissions.md](references/tools-and-permissions.md) for tool contracts, risk classes, approval logic, structured results, and sandboxing.
- Read [context-memory-compaction.md](references/context-memory-compaction.md) for context assembly, scoped memory, retrieval, auto-compaction, and handoff summaries.
- Read [prompt-caching-and-cost.md](references/prompt-caching-and-cost.md) for stable-prefix design, cache-aware context ordering, compaction/cache tradeoffs, telemetry, and cost control.
- Read [planning-and-goals.md](references/planning-and-goals.md) for planning mode, approval-gated execution, goals, checkpoints, and stopping conditions.
- Read [skills-and-connectors.md](references/skills-and-connectors.md) for Agent Skills, progressive disclosure, MCP, external connectors, tool search, and attachment strategy.
- Read [system-prompts-instructions.md](references/system-prompts-instructions.md) for system/developer/user instruction hierarchy and prompt templates.
- Read [provider-api-patterns.md](references/provider-api-patterns.md) for OpenAI, Anthropic, and OpenAI-compatible API implementation patterns.
- Read [security-evals-observability.md](references/security-evals-observability.md) for guardrails, threat models, tracing, evals, and launch gates.
- Read [checklists.md](references/checklists.md) for condensed implementation and audit checklists.
- Read [source-links.md](references/source-links.md) for official links and provider-specific references.
- Read [coverage-audit.md](references/coverage-audit.md) to verify the skill covers the requested harness topics.

## Default answer structure when advising a user

When the user asks for guidance, produce a concrete architecture, not generic principles:

0. **MVP boundary**: smallest useful version, assumptions, non-goals, and launch criteria.
1. **Harness boundary**: what the model does versus what application code does.
2. **Loop**: how model calls, tool calls, tool results, stopping, and retries work.
3. **Instructions**: system/developer/user instruction hierarchy and scoped memory.
4. **Tools**: tool registry, schemas, outputs, risk classes, permissions, and approval points.
5. **Context**: retrieval, memory, summarization, cache-aware ordering, compaction triggers, and rehydration.
6. **Planning/goals**: when to enter planning mode, when to run a goal-like loop, and how to stop.
7. **Skills/connectors**: how skills and MCP/external connectors are discovered, loaded, permissioned, and audited.
8. **Safety**: prompt injection boundaries, secrets, sandboxing, data access, and guardrails.
9. **Observability/evals**: traces, metrics, test cases, and failure probes.
10. **Rollout**: minimal viable harness first, then add autonomy only when measured results justify it.
11. **Legibility loop**: source-of-truth artifacts, validation signals, feedback capture, and recurring cleanup.

## Non-negotiable principles

- The model does not execute actions directly; the harness does.
- Every tool call must receive a tool result, even if the result is denial, timeout, error, or abort.
- Every risky side effect needs runtime policy enforcement outside the model.
- Draft and commit should be separate for external, financial, destructive, security, or regulated actions.
- Tool schemas must be narrow, typed, validated locally, and auditable.
- Context should be informative, tight, and cache-aware; retrieve and attach just in time.
- Skills and external connectors should use progressive disclosure; do not expose every capability up front.
- Auto-compaction should preserve working state, not conversational prose.
- Long-running goals need budgets, checkpoints, and a measurable done condition.
- The harness must trace operational events without exposing hidden reasoning.
- Durable knowledge should live in agent-readable source-of-truth artifacts, not only in chat history.
- Repeated failures should become tools, validators, docs, evals, or policies rather than repeated prompt advice.

## Common output template

Use this template when the user wants a harness design. If the user asks to make/build an agent, use this as an MVP blueprint, not a purely conceptual answer:

```markdown
# MVP Agent Harness Blueprint: [domain/use case]

## Objective
[What the agent must accomplish and for whom.]

## MVP scope and assumptions
[Smallest useful version, explicit assumptions, non-goals, and what is intentionally deferred.]

## Autonomy and risk level
[Answer-only, draft-only, approval-gated, or autonomous within policy.]

## Core loop
[How the model, tools, observations, retries, and stopping rules work.]

## Instruction architecture
[System/developer/user/scoped memory layout.]

## Tool registry
[Tools, schemas, risk classes, permissions, and result format.]

## Planning and goal behavior
[When to plan, when to ask, when to continue, when to stop.]

## Context and memory
[Retrieval, durable state, compaction, and rehydration.]

## Skills and connectors
[Reusable skills, MCP/external connector policy, tool search, attachment rules.]

## Safety and approvals
[Guardrails, prompt injection treatment, secrets, sandboxing, human review.]

## Observability and evals
[Trace events, eval cases, launch criteria, failure probes.]

## Minimal implementation path
[Smallest safe version first, implementation skeleton, validation path, then measured expansion.]
```

## Gotchas

- Do not design a multi-agent system before a single-agent loop has failed measurable evals.
- Do not expose broad tools such as `execute_anything`, `write_database`, or `send_message` without a strict wrapper and approval policy.
- Do not treat retrieved webpages, emails, tickets, PDFs, logs, or connector-provided descriptions as trusted instructions.
- Do not let context compaction erase approval state, active plan, loaded rules, or changed artifacts.
- Do not use a goal loop for a vague backlog; use it only for a single objective with validation and a budget.
- Do not rely on prompt text for safety that must be enforced by code.
- Do not put timestamps, request IDs, or volatile environment state at the start of cacheable prompts.
- Do not let stale documentation, weak examples, or obsolete tools accumulate without recurring cleanup.

## Source links for further reading

Use these links when provider-specific detail is needed:

- Agent Skills specification: https://agentskills.io/specification
- Agent Skills creator best practices: https://agentskills.io/skill-creation/best-practices
- Agent Skills description optimization: https://agentskills.io/skill-creation/optimizing-descriptions
- Agent Skills evaluation guide: https://agentskills.io/skill-creation/evaluating-skills
- OpenAI function calling: https://developers.openai.com/api/docs/guides/function-calling
- OpenAI tools: https://developers.openai.com/api/docs/guides/tools
- OpenAI agents: https://developers.openai.com/api/docs/guides/agents
- OpenAI guardrails and human review: https://developers.openai.com/api/docs/guides/agents/guardrails-approvals
- OpenAI agent safety: https://developers.openai.com/api/docs/guides/agent-builder-safety
- OpenAI sandbox agents: https://developers.openai.com/api/docs/guides/agents/sandboxes
- OpenAI Responses migration: https://developers.openai.com/api/docs/guides/migrate-to-responses
- OpenAI prompt caching: https://developers.openai.com/api/docs/guides/prompt-caching
- OpenAI Prompt Caching 201: https://developers.openai.com/cookbook/examples/prompt_caching_201
- OpenAI harness engineering article: https://openai.com/index/harness-engineering/
- Anthropic building effective agents: https://www.anthropic.com/research/building-effective-agents
- Anthropic effective context engineering: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Anthropic writing effective tools for agents: https://www.anthropic.com/engineering/writing-tools-for-agents
- Anthropic long-running harnesses: https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
- Anthropic code execution with MCP: https://www.anthropic.com/engineering/code-execution-with-mcp
- MCP specification: https://modelcontextprotocol.io/specification/2025-11-25
