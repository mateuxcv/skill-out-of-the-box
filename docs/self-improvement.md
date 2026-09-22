# Applying Out of the Box to itself

## Context

**Date:** 2026-09-21. **Baseline:** `7b6960b`.

The user requested English documentation and asked the agent to use the current out-of-the-box skill to improve it. The current skill was loaded and applied in the authoring session.

This record is an **author self-review and implementation decision**, not a controlled behavioral benchmark.

## Job, friction, and constraints

- **Job:** give users a portable, understandable method for creative B2B product work and justified technical composition.
- **Observed correction:** the public README and skill materials were in Portuguese; the user requires English.
- **Observed structure:** the baseline had a concise main skill, on-demand references, six packaged files, prose evaluation scenarios, and a standard-library validator.
- **Review findings:** alternative diversity was described but had no explicit regeneration gate; evidence labels did not sharply distinguish documented and tested claims; scenarios were not machine-readable; the validator did not inspect evaluation-case structure or maintainer-document links.
- **Constraints:** preserve OpenCode discovery, keep the package lightweight, retain a no-new-dependencies option, and make verification claims match actual work.

The review findings are inspection-based opportunities. They do not prove that the previous version failed every corresponding agent task.

## Directions considered

| Direction | Mechanism | Benefit | Cost or limitation |
| --- | --- | --- | --- |
| Translation-only baseline | Translate existing instructions without changing the workflow. | Satisfies the language correction with minimal change. | Leaves review and evaluation gaps intact. |
| Expanded tooling platform | Add a research aggregator, dependency catalog, and automated multi-agent evaluator. | Could automate repeated discovery and grading. | Adds tools and operational assumptions without observed demand for them. |
| Decision contracts and reusable evaluation data | Transfer falsifiable experiments into idea selection; combine evidence levels, subtraction tests, and structured cases. | Makes creative and technical choices easier to inspect while preserving the current architecture. | Behavioral benefit still requires fresh-session comparison. |

**Selected:** decision contracts and reusable evaluation data, alongside the required English translation.

**Bold but feasible challenger:** use explicit evidence levels and a falsifying experiment to challenge the agent's own preferred idea, rather than simply adding more brainstorming techniques.

**Signature improvement:** a recommendation states what would invalidate it and what can be removed without losing its distinctive value.

## Research performed

Sources were accessed on **2026-09-21**. These observations describe the consulted sources; they are not performance measurements.

| Source | Observation | Decision impact |
| --- | --- | --- |
| [GitHub Trending, weekly](https://github.com/trending?since=weekly) | The returned page included agent tooling and `addyosmani/agent-skills`. | Used for discovery; rankings did not become adoption criteria. |
| [Agent Skills best practices](https://agentskills.io/skill-creation/best-practices.md) | Recommends grounding skills in real corrections, conditional references, calibrated detail, and execution feedback. | Keep the core lean; use this real language correction and repository inspection as the starting point. |
| [Agent Skills evaluation guide](https://agentskills.io/skill-creation/evaluating-skills.md) | Describes structured `evals/evals.json`, fresh contexts, baseline comparisons, and evidence-backed assertions. | Add reusable case data and distinguish author review from behavioral evaluation. |
| [skills-ref README](https://github.com/agentskills/agentskills/blob/main/skills-ref/README.md) | Provides validation and metadata utilities; explicitly describes itself as a demonstration library. | Retain the local validator for its narrow repository-specific contract rather than adding this dependency. |
| [Agent-skills repository root](https://github.com/addyosmani/agent-skills) via GitHub Contents API | Root listing includes separate skills, references, scripts, and evals directories. | Structural comparison only; no claim about that project's behavioral quality or integration compatibility. |

The alternatives were an existing native implementation, a reference validator library, and broader tooling patterns. None required importing external implementation code for this revision.

## Composition and subtraction

- **Core Markdown** owns the workflow and decision gates.
- **References** own conditional detail.
- **JSON cases** own reusable evaluation inputs and assertions.
- **Python validator and tests** own structural checks; they do not grade creativity.
- **Shared contract:** stable relative paths, skill metadata, and a checked case schema.

Removing an external framework preserves the intended value, so none was added. Removing structured cases would make comparisons harder to reuse; removing evidence distinctions would blur documented capability and verified integration.

## Implemented changes

- English README, skill, references, decision template, and contribution guidance.
- A meaningful-diversity gate and one bold, feasible challenger.
- Claim-level evidence: discovered, documented, tested, measured.
- Explicit composition ownership and a subtraction test.
- An inspectable design contract and falsifiable experiment format.
- Twelve structured cases: the original ten concerns plus focused-effort and evidence-level cases.
- Validation of case integrity and maintainer-document file links, with unit coverage of failure cases.

## Verification boundaries

Local checks executed during this revision:

- `python scripts/validate_skill.py`: passed; seven packaged files, metadata, local file links, and evaluation-case structure checked.
- `python -m unittest discover -s tests -v`: all 16 validator tests passed.
- `git diff --check`: passed with no whitespace errors.
- The core skill contains 126 lines, compared with 137 in the baseline. This is a line-count observation, not a measured token or latency improvement.

The static walkthrough below checks instruction/case consistency. CI outcomes are associated with the published commit and reported separately.

| Case | Author walkthrough finding | Evidence kind |
| --- | --- | --- |
| No new dependencies | The workflow requires the existing-stack baseline and a subtraction test; the case checks preservation of the restriction. | Static instruction/case review. |
| Focused interaction | Focused mode permits one alternative and decision-changing research only, avoiding a mandatory broad discovery pass. | Static instruction/case review. |
| Documentation is not integration | Evidence levels and the composition contract require a target-environment test before claiming integration readiness. | Static instruction/case review. |

No fresh-session old-versus-new comparison or independent design review was performed as part of this authoring record. No improvement percentage, customer outcome, or benchmark score is claimed.

**What would change this decision:** if fresh-session comparisons show that the new gates increase ceremony without producing better mechanisms or better-supported decisions, shorten or remove them. If repeated runs need the same executable helper, add that helper only after the repetition is observed.
