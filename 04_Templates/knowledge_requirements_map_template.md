# Knowledge Requirements Map

## Purpose

Identify the knowledge required by an external context, determine what `Knowledge_System` already provides, and define how each gap should be treated without transferring operational context into the repository.

The completed map belongs in the external system that originated the need. This template remains in `04_Templates/` as the canonical reusable structure.

## 1. External Context

- **Originating system:** [project, research activity, personal inquiry, professional practice, or other context]
- **Purpose:** [decision, capability, understanding, design, or action to be supported]
- **Scope:** [what this analysis covers and excludes]
- **Knowledge System consulted:** [repository or version examined]

External details may be recorded here when necessary for the originating system, but they must not be copied into a knowledge note unless they are admissible evidence or a relevant example.

## 2. Boundary Rules

- The external context may reference and apply canonical knowledge.
- `Knowledge_System` must not receive operational files or unnecessary identifying or sensitive information.
- A particular need must be translated into a context-independent knowledge question before it can become a knowledge candidate.
- Generalization must preserve evidence, assumptions, applicability conditions, and limitations.
- The completed map remains outside `Knowledge_System`, except when its primary function belongs to `02_Learning/`.

## 3. Requirements Map

Use these coverage values: `available`, `partial`, `missing`, or `uncertain`.

Use these treatment values: `reuse`, `adapt_externally`, `update_candidate`, `new_candidate`, `research_needed`, or `external_only`.

| ID | External need | General knowledge question | Required knowledge unit | Type | Coverage | Priority |
|---|---|---|---|---|---|---|
| KR-01 | [contextual need] | [question independent of the originating context] | [knowledge sought] | [concept/framework/method/model] | [coverage] | [high/medium/low] |

## 4. Coverage and Action Register

| ID | Existing knowledge and evidence | Exact gap | Gap class | Treatment | Expected result |
|---|---|---|---|---|---|
| KR-01 | [exact note names and relevant sections, or none] | [what is absent, insufficient, or uncertain] | [knowledge/evidence/context_data/decision/adaptation] | [treatment] | [usable external or general result] |

Interpret gap classes as follows:

| Gap class | Meaning | Normal destination |
|---|---|---|
| `knowledge` | A reusable concept, framework, method, or model is absent or incomplete | Candidate for knowledge curation |
| `evidence` | Documentary or empirical support is insufficient | Research and source evaluation |
| `context_data` | Measurements or facts are required only for the external situation | Originating system |
| `decision` | A preference, criterion, constraint, or authorization is missing | Originating system |
| `adaptation` | General knowledge exists but must be configured for the situation | Originating system |

## 5. Generalized Knowledge Requests

Complete this section only for `update_candidate`, `new_candidate`, or `research_needed`. It is the only part intended to cross into a knowledge-curation workflow.

### [KR-XX — Proposed Knowledge Unit]

- **General question:** [context-independent question]
- **Proposed type:** [concept/framework/method/model]
- **Intended scope:** [general systems or situations covered]
- **Existing knowledge to reuse:** [exact canonical note names]
- **Evidence required:** [sources, observations, comparisons, or validation needed]
- **Conditions and limits to preserve:** [applicability boundaries]
- **Context that must not cross:** [identifiers, operational details, private data, or case-specific decisions]

## 6. External Application and Feedback

| ID | Knowledge applied or generated | External configuration or result | Evidence from use | Generalizable learning candidate |
|---|---|---|---|---|
| KR-01 | [canonical note or external work product] | [how it was used] | [observation or result] | [generalized learning, or none] |

The project or originating system may reference knowledge created or used. Canonical knowledge must not link back to or depend on this completed map.

## Completion Check

- Every external need has been translated into a general knowledge question.
- Existing knowledge was inspected rather than inferred only from file names.
- Coverage and gaps are supported by explicit evidence.
- Context-specific data, decisions, and adaptations remain external.
- Proposed knowledge requests contain no unnecessary contextual dependency.
- No change to `Knowledge_System` has been made through this mapping activity.
