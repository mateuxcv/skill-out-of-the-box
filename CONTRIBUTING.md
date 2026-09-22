# Contributing to Out of the Box

Help improve the quality of product and architecture decisions while keeping the instructions concise and proportional to the task.

## Valuable contributions

- Creative methods grounded in real B2B jobs.
- Better evidence and compatibility checks for library composition.
- Concrete design, accessibility, and architecture improvements.
- Reproducible cases of false activation, shallow novelty, or unsupported claims.
- Clearer installation, documentation, and validation.

## Report an issue

Include the goal, original prompt, expected behavior, observed behavior, and a minimal example. Record the model, harness version, and available tools when known. Remove credentials and private data from traces.

Separate observations from hypotheses about their cause. An issue should explain a problem, not just request more instructions.

## Submit a focused change

1. Create a fork and a descriptive branch.
2. Identify the observed problem and the smallest coherent improvement.
3. Write public documentation, skill content, examples, and evaluation cases in English. Runtime conversation can follow the user's language.
4. Keep `SKILL.md` below 500 lines and load detailed references conditionally.
5. Preserve the simple frontmatter convention: a plain `name` and a double-quoted `description`. Update the validator deliberately if expanding that supported subset.
6. Update affected examples and evaluation cases without embedding desired outputs as fake results.
7. Run:

   ```bash
   python scripts/validate_skill.py
   python -m unittest discover -s tests -v
   ```

8. For behavioral changes, compare relevant cases in fresh sessions when possible. Restart OpenCode after changing an installed skill.
9. Submit a pull request with the problem, change, evidence, and remaining limitations.

## Evaluation conventions

Case definitions live in [.opencode/skills/out-of-the-box/evals/evals.json](.opencode/skills/out-of-the-box/evals/evals.json). Follow the [evaluation guide](.opencode/skills/out-of-the-box/references/evaluation.md).

- `context` describes setup the evaluator must actually supply.
- `files` contains fixture paths relative to the skill root; empty means no bundled fixture.
- Assertions should distinguish useful behavior, not require exact wording.
- Negative trigger controls should run without explicitly forcing the skill to load.
- Store actual results separately from definitions and name the revision and environment.
- Label author walkthroughs honestly. Do not report them as independent fresh-session runs.

| Result field | Record |
| --- | --- |
| Environment | Model, date, revision, tools, and supplied context. |
| Evidence | Actual output or relevant tool events. |
| Grade | Pass, fail, or not observed for each assertion. |
| Limitations | Missing setup, unavailable tools, or untested assumptions. |

## Editorial principles

Prefer observable mechanisms to vague adjectives. Keep the native/existing-stack alternative in view. Avoid mandating a framework, package, or architecture. Explain the purpose of constraints and distinguish documentation, experiments, and measurements.

Add tests for meaningful validator behavior, not for every sentence of prose. Passing CI establishes package integrity; improved agent behavior requires separate evidence.
