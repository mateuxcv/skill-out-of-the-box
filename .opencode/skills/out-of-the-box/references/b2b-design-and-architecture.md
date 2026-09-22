# B2B design and lean architecture

Apply the criteria relevant to the actual workflow. This is not a mandatory feature checklist for every business application.

## Organize around a decision

- Identify the unit of work: order, account, document, incident, or exception.
- Distinguish operator, buyer, and administrator when their needs differ.
- Make the primary workspace answer: what needs attention, why, and what can I do now?
- Use tables for comparison and ordering; use timelines, graphs, or cards when their structure improves the actual decision.
- Support progressive depth: triage summary, investigation detail, and action in the appropriate context.
- Consider saved views, bulk actions, keyboard navigation, import/export, and task resumption for repeated work.
- Account for adoption cost: a technically superior interface may fail if it breaks indispensable integrations and habits.

## Make the visual direction inspectable

Before building a screen, specify a compact **design contract**:

1. **Character:** e.g. editorial and analytical, compact and operational, or precise and technical; tie it to users and brand.
2. **Composition:** navigation, work surface, evidence, and detail proportions.
3. **Hierarchy:** the information that drives the decision and the primary action.
4. **Tokens:** typography, spacing, semantic color, density, borders, and elevation consistent with the existing system.
5. **Signature interaction:** the demonstrable moment that makes the job easier.
6. **States and input:** realistic content, keyboard route, responsive behavior, and recovery.

For a substantial redesign, compare two distinct compositions with a sketch, wireframe, or prototype before polishing. A text-only task may use an annotated layout description. Do not claim a visual comparison if none was performed.

Use domain-shaped content: long company names, missing values, conflicting records, and realistic amounts or dates. A layout that only works with short placeholder text has not demonstrated usability.

Gradients, large cards, illustration, and motion are choices, not a universal style. Motion should explain state changes or preserve orientation; honor reduced-motion preferences. Preserve the existing identity when evolving a product.

## States are part of the product

Cover relevant initial, loading, empty, partial, no-results, error, success, conflict, and insufficient-access states.

- Explain failure and the next action without losing the user's work.
- Offer undo where feasible; request confirmation at the necessary point for irreversible actions.
- Use semantic controls, labels, focus order, adequate contrast, and information conveyed beyond color.
- Provide keyboard alternatives to drag-and-drop. Test focus behavior when virtualizing content.
- Match the actual device: field work on a phone and a dense desktop operations console need different compositions.
- Verify a complete path from entry through decision to recovery, not only the ideal screenshot.

## Use AI for a specific capability

AI is useful when ambiguity, language, or synthesis makes a deterministic alternative inadequate.

Define the assisted action, acceptable quality, latency, cost, and correction path. Show supporting evidence for factual suggestions when available. Preserve workflow continuity during errors or outages. Separate suggestions from consequential actions according to the actual authorization model.

Do not automatically add chat, a vector database, or an agent framework. Compare with rules, search, direct manipulation, and sensible defaults.

## Keep architecture proportional

Work within existing conventions. For a new product, start with a cohesive application and capability-oriented modules when appropriate.

```text
features/
  reconciliation/
    ui/
    use-cases/
    domain/
    integrations/
```

This is a conceptual example, not a mandatory folder tree. A small feature may fit in a few files. Separate meaningful business rules from volatile implementation details when the boundary helps evolution or testing.

- Give each datum a source of truth and each module a clear responsibility.
- Isolate external integrations where replacement, failure, or a contract warrants the boundary.
- Avoid competing owners of global state, UI systems, or validation logic without a specific reason.
- Add asynchronous processing when duration, reliability, or workload requires it.
- Prefer simple deployment and operation until requirements justify distribution.
- Count integration glue, duplicated state, migration work, and operational burden as complexity—not just package count.

## Spend complexity where the value lives

Keep commodity capabilities conventional. Concentrate experimentation on the signature interaction or capability that differentiates the workflow.

For an uncertain component, specify its boundary, fallback, and removal condition. Do not build a generic abstraction platform merely because a dependency might change someday.

When the application serves multiple companies, enforce tenant isolation and authorization on the server. Model authorship and history when approvals or traceable changes require them. SSO, elaborate roles, extensive audit, residency, and multiple regions should follow actual requirements.

## Choose a test that could disprove the idea

| Hypothesis | Useful experiment | Example falsifier |
| --- | --- | --- |
| Exception queues reduce context switching | Complete representative cases against the current flow. | Evidence still requires the same external navigation. |
| Two libraries enable direct editing | Exercise selection, editing, filtering, and recovery in the target runtime. | Focus or state diverges between components. |
| Virtualization is necessary | Compare representative workloads with and without it. | Pagination already meets the target with less complexity. |
| Automation saves work | Use normal, ambiguous, and incorrect inputs. | Correction costs exceed manual handling for the target cases. |
| Visual hierarchy improves scanning | Inspect realistic content at relevant densities and sizes. | Users cannot identify the next action or important exception. |

Set actual thresholds from context before running the test; these examples are not benchmarks. Technical feasibility does not prove adoption, revenue, or customer preference.
