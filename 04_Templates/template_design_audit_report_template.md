# Template Design Audit Report

## Purpose and Scope

[State the template version, repository state, and release or design decision this audit should support.]

## Snapshot

- **Review date:** YYYY-MM-DD
- **Schema version:** [value from system_manifest.yaml]
- **Reviewer:** [person or agent]
- **Repository state reviewed:** [commit, tag, archive, or working tree]
- **Important limitations:** [unavailable evidence or checks not performed]

## Design Checks

| Area | Expected condition | Evidence | Result | Significance |
|---|---|---|---|---|
| Purpose | Functional documents support the declared system purpose | [evidence] | [pass, fail, or not measured] | [effect] |
| Consistency | Normative documents, subsystem rules, and templates agree | [evidence] | [result] | [effect] |
| Distribution | Only paths admitted by the distribution contract are published | [evidence] | [result] | [effect] |
| Compatibility | Schema version and migration requirements are explicit | [evidence] | [result] | [effect] |
| Safety | Prompts define trust and modification boundaries | [evidence] | [result] | [effect] |
| Operability | A clean instance can be initialized and used without Git | [evidence] | [result] | [effect] |

## Findings

| ID | Fact | Interpretation | Risk or opportunity | Recommendation |
|---|---|---|---|---|
| D-01 | [observed fact] | [meaning] | [system effect] | [minimal response] |

## Experiments

| Experiment | Hypothesis | Procedure | Observed signal | Decision |
|---|---|---|---|---|
| [name] | [causal expectation] | [reversible test] | [result] | [adopt, revise, reject, or continue] |

## Release Decision

- **Decision:** [ready, conditionally ready, or not ready]
- **Blocking findings:** [IDs or none]
- **Required follow-up:** [actions and owners]

Remove unused rows and do not infer operational effectiveness from the quantity of example content in the design repository.
