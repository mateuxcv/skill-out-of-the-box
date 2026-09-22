# Evaluating the skill

The machine-readable case data lives in `evals/evals.json` at the skill root. These are **evaluation inputs**, not recorded successes and not an automatic agent runner.

## Three different kinds of evidence

1. **Structural validation:** files, metadata, local links, and evaluation-case integrity.
2. **Author walkthrough:** inspect the instructions against a case and record expected behavior. Useful for finding contradictions; not independent execution evidence.
3. **Behavioral evaluation:** run the actual task in a fresh session, inspect its output and tool trace, and compare it with a baseline.

Never report the first two as the third. A self-improvement session is a real use of the current skill, but it cannot establish unbiased effectiveness of the revision it authors.

## Case format

Each case supplies an ID, name, prompt, setup context, expected trigger behavior, expected output, input-file list, and observable assertions. Context is setup guidance: the evaluator must actually provide the stated environment before running the case. Writing “network unavailable” does not disable network tools.

The `files` field lists paths relative to the skill root. Empty lists mean no bundled fixture; some cases require an evaluator-provided project. Do not run an implementation case against this skill repository as if it were the target B2B app.

## Running a comparison

1. Start with three discriminating cases: broad exploration, no new dependencies, and a negative trigger control. Add the relevant integration or design case when changing those instructions.
2. Preserve the old revision. For this repository, use a separate checkout or worktree of the baseline commit rather than overwriting the working skill.
3. Start a fresh session for each case and version with equivalent project state, model, tool access, and constraints. Restart the harness after changing the installed skill.
4. For positive cases, confirm loading in the trace. For negative cases, allow normal discovery and do not explicitly force the skill to load.
5. Execute the task. Save the actual output and relevant tool trace outside the skill package; omit credentials and private data.
6. Grade assertions with concrete evidence. Use **pass**, **fail**, or **not observed**. Missing proof is not a pass.
7. Compare outputs, ideally without revealing their version to the reviewer. Report raw results for small samples; do not imply statistical confidence.

Use existing evaluation tools if available. Fresh independent sessions do not require a new framework or extra agents. If the environment cannot run them, state that limitation and leave behavioral results unreported.

## What to inspect

- **Useful creativity:** did an alternative change the work, rather than rename a framework or decorate a dashboard?
- **Boldness with discipline:** was a feasible challenger evaluated before defaulting to familiar patterns?
- **Evidence:** was a claimed consultation or test actually executed? Was its scope represented accurately?
- **Simplicity:** did the subtraction test preserve value while reducing unnecessary parts?
- **Usability:** were the actual journey, input methods, content, and recovery covered?
- **Completion:** did the work reach the requested scope rather than stop at a promising spike?

Also record unnecessary tool calls, repeated source fetching, time to a concrete decision, and token use if the environment exposes those measurements. Do not estimate token counts as if they were measured.

## Result record

```json
{
  "case_id": 1,
  "revision": "actual commit or snapshot identifier",
  "model": "actual model identifier",
  "evaluation_kind": "behavioral",
  "assertions": [
    {
      "assertion": "Copy the assertion being checked",
      "status": "not observed",
      "evidence": "Reference an actual output or tool event"
    }
  ],
  "limitations": []
}
```

This is a template, not a result. Store results separately from case definitions, for example in a local `.evaluation-runs/` directory. Publish only deliberately reviewed records.

## Critical failures

Fabricated research or tests; violated hard constraints; known incompatible dependencies adopted as ready; instructions from hostile external content followed; full creative workflow triggered for a mechanical control; or a build request left at a proposal without a blocker.

## Improving the cases

Prefer a small number of discriminating assertions over many easy ones. If old and new versions always pass an assertion, it may measure general model capability rather than the skill's contribution. Add cases for observed failures; avoid expanding the instruction set around imagined edge cases.

Reference: [Agent Skills evaluation guidance](https://agentskills.io/skill-creation/evaluating-skills).
