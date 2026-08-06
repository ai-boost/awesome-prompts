---
name: classic-software-engineering-canon
description: "Classic Software Engineering Canon Agent Rules"
---

Classic Software Engineering Canon Agent Rules
Source: https://github.com/ciembor/agent-rules-books (2026, 1.4k+ stars)
Based on Clean Code / Clean Architecture (Robert C. Martin), Domain-Driven Design
Distilled (Vaughn Vernon), and Designing Data-Intensive Applications (Martin Kleppmann).
Converted into binding engineering policy for AI coding agents.
------------------------------------------------------------------

## Purpose

This repository follows the canonical software engineering canon: code that humans
can read and reason about, architectures that protect business rules from volatile
details, domain models that align with business language and boundaries, and
data-intensive systems that treat failure, inconsistency, and evolution as normal
inputs rather than exceptions.

All code generation, edits, and reviews must optimize for:
- local reasoning and precise naming
- inward dependencies and replaceable details
- bounded contexts and explicit domain language
- explicit data ownership, consistency, and durability contracts

This file is a binding engineering policy: `MUST` is binding, `SHOULD` is a strong
default, and `MUST NOT` is forbidden.

---

## Clean Code — Readability & Local Reasoning

### Decision Rules
- Treat cleanliness as part of delivery. Preserve behavior and leave touched code
cleaner within scope.
- Write for local reasoning. A reader MUST understand the path without
reconstructing hidden state, wide jumps, or naming trivia.
- Use precise names and one term per concept. Rename when vocabulary hides intent,
overloads meaning, or forces comments to compensate.
- Keep functions small, focused, and at one level of abstraction. Tell the story
top-down so intent appears before detail.
- Keep parameters few and meaningful. Avoid boolean flags, output parameters, and
grab-bag argument lists; model the concept instead.
- Separate commands from queries and eliminate hidden side effects. A function that
answers MUST NOT mutate behind the reader's back.
- Keep the happy path readable. Isolate error handling, invalid-state handling, and
cleanup; prefer explicit optionality or typed results over null-like sentinel flow.
- Use comments only for rationale, constraints, warnings, or external contracts. Do
not narrate code instead of improving it.
- Treat tests as production code: readable, deterministic, aligned with the behavior
or contract they protect.

### Trigger Rules
- When a function mixes setup, validation, computation, and side effects, split the
phases.
- When a comment explains control flow, simplify names or structure before keeping
the comment.
- When a function both mutates and answers, or hides a mode switch behind a flag,
separate the responsibilities.
- When duplication, repeated switches, or primitive clusters appear, name the
concept with an argument object, polymorphism, special case, or small abstraction.

---

## Clean Architecture — Dependency Direction & Boundaries

### Decision Rules
- Source dependencies MUST point inward toward higher-level policy. Domain and use
cases MUST NOT import frameworks, databases, web handlers, queues, external service
clients, UI types, or other details.
- Put enterprise rules and invariants in entities or equivalent domain objects; put
application-specific orchestration in focused use cases.
- Pass plain request and response models across use-case boundaries. Do not pass web
requests, framework contexts, ORM rows, database-bound structures, or framework
response objects into or out of core policy.
- Treat frameworks, databases, web delivery, messaging, filesystems, clocks, service
clients, networks, devices, and vendors as outer-layer details behind ports,
gateways, presenters, mappers, or adapters.
- Inner layers own the interfaces they need; outer layers implement them. Object
construction and concrete wiring belong in the composition root or other outer-layer
main component.
- Keep adapters humble. Controllers, endpoints, presenters, gateway adapters, service
listeners, and hardware adapters translate external formats to use-case calls and
back; they do not own business decisions.
- Organize by use case, feature, or business capability before generic technical
buckets. The structure SHOULD reveal domain intent and application actions.
- Test entities, use cases, and boundary contracts first, without the real
framework, database, network, external service, or target hardware. Test adapters
separately at the seams.

### Trigger Rules
- When framework annotations, request/response objects, serializers, ORM rows,
schemas, vendor SDKs, or transport formats enter core policy, move translation
outward.
- When controllers, jobs, handlers, views, presenters, gateways, repositories, SQL,
service listeners, or hardware adapters contain business branching or validation,
move the rule inward.
- When a use case instantiates infrastructure, calls a volatile dependency directly,
or depends on a concrete implementation, introduce a policy-owned port and wire the
concrete detail at the edge.

---

## Domain-Driven Design — Model, Language & Boundaries

### Decision Rules
- Before designing code, identify the business capability, classify the subdomain as
Core, Supporting, or Generic, define the Bounded Context, use its Ubiquitous
Language, and choose only tactical patterns that earn their cost.
- Give every meaningful model one explicit Bounded Context. The context owns its
language, rules, semantics, code structure, tests, and integration contracts.
- Treat the same word in different contexts as potentially different concepts.
Translate at context boundaries instead of sharing domain classes or leaking foreign
language into the local model.
- Use Entities when identity and lifecycle matter; make identity explicit and protect
meaningful state transitions rather than exposing unrestricted setters.
- Use immutable, self-validating Value Objects when primitives hide domain meaning.
- Use Aggregates only as invariant and transactional consistency boundaries. Keep
them small, modify through the root, reference other Aggregates by identity, avoid
large object graphs, and usually change one Aggregate per transaction.
- Use Domain Events for meaningful past-tense business facts that clarify
collaboration or integration; do not publish noisy field-change events.
- Application Services coordinate use cases by loading Aggregates, invoking domain
behavior, saving results, and triggering integration work. They MUST NOT become the
real domain model.
- Keep frameworks, persistence mechanics, transport formats, REST representations,
and infrastructure types out of the domain model.

### Trigger Rules
- When language is fuzzy, generic, overloaded, or imported from another context,
pause coding and sharpen the local Ubiquitous Language.
- When one model spreads across billing, identity, catalog, fulfillment, support,
permissions, or other separate concerns, split or translate instead of reusing
shared domain classes.
- When a request wants to load and mutate a large graph or several Aggregate roots,
revisit the invariant boundary and ask whether eventual consistency is acceptable.
- When controllers, helpers, services, or transport-shaped application services
contain business decisions, move behavior into the domain model or name the missing
concept.

---

## Data-Intensive Systems — Correctness, Durability & Evolution

### Decision Rules
- Make core trade-offs explicit: source of truth, consistency expectation, retry
behavior, duplicate and reordered work, partial failure, data evolution, and whether
state is durable, cached, derived, or ephemeral.
- Treat crashes, partial writes, duplicate work, timeouts, stale reads, and unknown
downstream success as normal inputs. Distinguish accepted, persisted, applied, and
durable success.
- Choose data models, query models, and ownership boundaries from relationships,
access patterns, consistency needs, update locality, evolution pressure, and whether
data is primary or derived.
- Treat indexes, caches, search copies, read models, materialized views, and
denormalized copies as derived data with explicit propagation, lag, observability,
repair, and rebuild paths.
- Make commands, jobs, events, batch jobs, and stream processors safe under retry
and replay with deduplication keys, naturally idempotent transitions, or an explicit
transactional recovery contract.
- Preserve only the ordering the business logic actually needs. Scope it per key,
stream, partition, record, entity history, or stronger contract.
- Separate commands, events, durable logs, streams, and materialized views. Events
describe facts; consumers MUST tolerate lag, duplicates, restart, replay, stable
identifiers, correlation metadata, and versioned payloads.
- Design schemas, encodings, APIs, messages, events, and database changes as
evolving contracts across old readers, old writers, old data, in-flight messages,
rolling upgrades, and cross-service formats.
- Match transactions and isolation to invariants. Make atomicity scope, commit
behavior, recovery, reconciliation, lost-update, write-skew, phantom, and
side-effect repair semantics explicit.
- Treat network delay, packet loss, partitions, duplicate messages, pauses, stale
leaders, timeouts, wall-clock uncertainty, leases, locks, majorities, and leadership
as assumptions needing a fault model.

### Trigger Rules
- When changing a write path, state the source of truth, consistency boundary,
durability point, visibility point, downstream effects, rollback or repair path, and
behavior after timeout or unknown success.
- When adding or changing a cache, index, projection, search copy, read model,
warehouse, or denormalized field, define ownership, propagation, staleness, write
cost, lag visibility, rebuild, and repair.
- When changing a schema, API, message, event, enum, status, or payload meaning,
plan compatibility for old readers, old writers, old stored data, old messages, new
writers, rollout, and migration.
- When adding retries, jobs, consumers, queues, CDC, event sourcing, stream
processors, or replayable batch work, prove duplicate, replay, ordering, retention,
side-effect, and recovery safety.
- When choosing transaction isolation or weakening consistency, map each anomaly to
the invariant it can break and add compensating design where needed.

---

## Unified Review Checklist

Before finalizing any change, verify:
- Can a reader follow the change locally without reconstructing hidden state?
- Are names and APIs carrying meaning without narration?
- Do dependencies point inward, with ports owned by inner policy?
- Is the domain language visible in code, tests, and APIs?
- Are Aggregates small, root-protected, and not graph-shaped?
- Is the source of truth explicit, and are derived representations tracked?
- Are retries, duplicates, replay, reordering, timeouts, crashes, and unknown
success handled?
- Do schemas, APIs, messages, and events evolve safely across mixed versions?
- Did framework, persistence, vendor, and construction details stay behind
boundaries?
- Did I remove at least one smell from the touched area?
- Do tests protect the changed behavior or contract without needing real
infrastructure?

If any answer is no, revise before shipping.

---

## Final Instruction

When uncertain, choose the option that:
1. improves local reasoning and precise naming
2. keeps dependencies pointing inward and details replaceable
3. sharpens the domain model and its explicit boundaries
4. makes data ownership, consistency, and failure handling explicit
5. leaves the codebase easier to change tomorrow

Be pragmatic, and make the right thing the easy thing.
