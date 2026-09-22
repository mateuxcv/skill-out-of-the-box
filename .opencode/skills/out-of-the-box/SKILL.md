---
name: out-of-the-box
description: "Use when asked to think outside the box, design a distinctive B2B or SaaS experience, or discover and combine libraries for a business application. Turns creative exploration, GitHub Trending research, and technical experiments into a useful product with a lean architecture. Also use when explicitly asked to improve this skill using itself. Do not activate for mechanical edits, isolated bug fixes, or documentation lookups without a creative product or architecture decision."
---

# Out of the Box

**Explore broadly. Select rigorously. Build simply.**

Turn a business problem into a distinctive, useful experience. Search beyond familiar tools, combine complementary capabilities, and choose the smallest architecture that preserves the value of the idea.

## Operating contract

- Follow the user's constraints and repository conventions. This skill grants no permissions and requires no additional agents.
- Ask only when missing information could materially change the decision. State reversible assumptions and continue otherwise.
- Match the requested deliverable: a proposal needs a decision; a build request needs implementation and verification, not just a plan or spike.
- Share conclusions, evidence, alternatives, and trade-offs rather than private step-by-step reasoning.
- Keep skill files in English; communicate with the user in their preferred language unless asked otherwise.

## Choose the depth

| Mode | Use when | Minimum useful process |
| --- | --- | --- |
| **Focused** | One interaction or a tight deadline | Baseline + one meaningful alternative; investigate only the uncertainty that could change the choice. |
| **Explore** | A new product, workflow, or significant technical choice | Baseline + two different mechanisms; current discovery; compare finalists; prove the riskiest assumption. |
| **Prove** | A costly migration or uncertain integration | Explore, then test the decisive contract in the target environment before committing to it. |

These are defaults, not output quotas. Keep the visible brief short. Do not stretch a small task into a research ceremony.

## 1. Frame the job

Inspect relevant project instructions, manifests, lockfiles, components, domain code, integrations, and checks before picking a stack.

Capture: **actor → recurring job → current friction → desired observable outcome → constraints → decisive uncertainty**. Distinguish operator, buyer, and administrator when their needs differ. Identify what the current solution already does well.

State a baseline and a success criterion. If neither has been measured, label them as hypotheses or proposed targets. Do not invent customer interviews, business metrics, or enterprise requirements.

## 2. Generate mechanisms, not cosmetic variants

Read [creative methods](references/creative-methods.md) when generating directions.

For an Explore or Prove task, consider:

1. **Baseline:** the best small improvement using existing capabilities.
2. **Transfer:** a useful mechanism borrowed from a different domain.
3. **Recombination:** complementary capabilities that remove a step or enable a new outcome.

Include one **bold but feasible** direction that challenges a workflow assumption. Do not eliminate it just because the baseline is familiar; test whether its incremental value pays for its complexity. Hard constraints still apply.

Use this idea card: **pain → mechanism → expected benefit → what disappears → main risk → cheapest falsifying test**.

**Diversity gate:** if the directions only change colors, layout, vendors, or framework names, regenerate an alternative. Change the unit of work, decision sequence, interaction, or coordination model instead.

## 3. Discover and verify

Read [research and selection](references/research-and-selection.md) before external discovery or dependency decisions.

- In Explore and Prove, consult current [GitHub Trending](https://github.com/trending?since=weekly), problem-oriented search, and established alternatives. In Focused mode, research when it can affect the choice; honor an explicit research request.
- Search for **capability + constraint**, not just favorite library names. A relevant discovery can inform an interaction pattern without becoming a dependency.
- Open primary sources for finalists: official documentation, repository, releases, package registry, and applicable license.
- Keep evidence attached to the claim: **source + access date + version if relevant + observation + uncertainty**.
- Distinguish **discovered**, **documented**, **tested**, and **measured**. Reading an API does not prove two packages work together.
- If web access fails, disclose it and continue with local evidence and provisional candidates. Do not fabricate current research.

Default to a short discovery pass and a small shortlist. Stop once a viable finalist, a strong alternative, and a test for the decisive uncertainty exist. Reopen research only if a failed test or changed constraint could change the decision.

## 4. Compose capabilities; subtract complexity

For each proposed combination, complete:

> A owns __. B owns __. Together they enable __. Their contract is __. The added cost is __. Removing B would lose __.

Check runtime and version compatibility, data contracts, state ownership, rendering, failure behavior, and overlapping responsibilities. Verify rather than assume integration.

**Subtraction test:** compare the combination with existing dependencies, a native API, and a small implementation. If removing a component preserves the distinctive value and required behavior, remove it.

Treat technical or license incompatibility with a hard requirement as a blocker to adoption. An unresolved critical claim remains an experiment, not a production recommendation. Respect explicit dependency constraints; explain conflicts rather than silently replacing the user's requirements.

## 5. Make the experience and architecture concrete

Read [B2B design and architecture](references/b2b-design-and-architecture.md) for interface or system design.

Choose a direction by useful differentiation, user value, feasibility, total cost, and evidence confidence. Compare it with the strongest alternative, not a deliberately weak strawman.

Define:

- **Signature interaction:** one observable moment that makes the job easier or enables a better decision.
- **Experience:** primary journey, information hierarchy, visual character, realistic content, keyboard path, and relevant states.
- **Architecture:** cohesive responsibilities, sources of truth, essential dependencies, integration boundaries, and an exit path for uncertain components.
- **Decision boundary:** the evidence that would make you change your mind.

Prefer the existing structure and a cohesive application. Add layers, services, queues, and abstractions only for demonstrated needs. Simplicity means low total complexity, not the fewest files at any cost.

## 6. Run the smallest decisive experiment; finish the work

Before building, state **hypothesis → experiment → observable pass/fail condition → fallback**. Test the assumption most likely to invalidate the direction, not the easiest detail to demonstrate.

Implement the smallest vertical slice connecting the interaction, business rule, and necessary data. For visual-only work, prototype the flow and its states without unrelated infrastructure.

- Use actual versions and representative synthetic data for technical experiments.
- Run the project's relevant checks. Cover important contracts, transitions, and recovery behavior.
- Inspect the interface with browser tools when available; otherwise state that visual verification was not performed.
- Do not call a mock a live integration, an expected gain a measurement, or an unexecuted check a pass.
- When the experiment fails, revise or simplify the direction instead of stacking patches and libraries around a broken assumption.
- Complete the requested scope after the spike. Do not stop at the experiment when implementation was requested.

## Deliver a compact decision, not a process transcript

Lead with the chosen solution. Include its distinctive value, the strongest alternative, essential evidence, architecture trade-off, and what was actually built and verified. Name unresolved assumptions that affect adoption.

Use the [decision brief](assets/decision-brief.md) only for substantial decisions or requested documentation. Small tasks can use a few paragraphs; do not create process files by default.

## Final gates

- **Value:** would the idea still matter without the technology names?
- **Novelty:** does the chosen mechanism change the work, not just its appearance?
- **Simplicity:** does every component preserve necessary value after the subtraction test?
- **Evidence:** is each important claim supported at the level required for adoption?
- **Usability:** can the user complete and recover the primary workflow?
- **Delivery:** did the work reach the requested scope, with honest verification?

## Improving this skill itself

When explicitly requested, apply the same loop to this repository: inspect a real correction or execution trace, compare improvement directions, research relevant primary sources, change the smallest coherent set of instructions, and validate the result. Record the observed problem separately from the expected benefit.

Read [evaluation guidance](references/evaluation.md) and the [evaluation cases](evals/evals.json) when evaluating this skill. They are not normal product-task context. Compare old and new versions in fresh sessions when available; an author self-review is useful evidence but not an independent benchmark.
