# Knowledge

## 1. Purpose

`01_Knowledge/` is the canonical location for knowledge that has been processed, understood, and structured sufficiently to be reused.

Its function is to preserve understanding independently of the source, project, course, or situation in which it originated.

## 2. Scope

This subsystem contains:

- concepts;
- models;
- methods;
- frameworks.

It does not contain:

- unprocessed or temporary information, which belongs in `00_Inbox/`;
- complete documentary sources, which belong in `03_Library/`;
- course-specific exercises or assessments, which belong in `02_Learning/`;
- reusable templates, which belong in `04_Templates/`.

A knowledge note may use a real case as evidence or illustration, but it must not depend on an external project, client, course, or situation. Operational documentation and context-specific decisions remain in their originating systems.

## 3. Architecture

```text
01_Knowledge/
├── Concepts/
├── Models/
├── Methods/
├── Frameworks/
└── README.md
```

These folders classify knowledge by its primary cognitive function, not by topic or discipline. Topics are represented through metadata, search, and contextual links.

## 4. Knowledge Types

### 4.1 Concept

A `concept` defines and explains an idea.

Primary question:

> **What is it?**

A concept normally explains its meaning, function, behavior, relationships, or implications.

Examples: system, feedback, audit, uncertainty.

### 4.2 Model

A `model` represents a system, phenomenon, or situation in a simplified form for description, explanation, exploration, or prediction.

Primary question:

> **How can it be represented?**

A model normally identifies what it represents, its elements, relationships, assumptions, and limitations.

Examples: stock-and-flow model, process model, cost model.

### 4.3 Method

A `method` defines a repeatable way to perform an operation or obtain a result.

Primary question:

> **How is it done?**

A method normally identifies its purpose, inputs, procedure, outputs, and limitations.

Examples: audit method, sensitivity analysis, optimization procedure.

### 4.4 Framework

A `framework` organizes elements, relationships, or questions to guide reasoning, representation, or action.

Primary question:

> **How should the problem or knowledge be organized?**

A framework normally identifies its purpose, scope, components, relationships, and operating logic. It guides application without necessarily prescribing a fixed sequence.

Examples: system representation framework, system operations framework.

## 5. Classification Rules

Classify a note by its **primary function**:

```text
Defines an idea                       → concept
Represents a phenomenon               → model
Prescribes a repeatable procedure     → method
Organizes reasoning or action         → framework
```

Use these rules for ambiguous cases:

- A principle or theory expressed as an explanatory idea is a `concept`.
- A technique or procedure is a `method`.
- A representation with assumptions and relationships is a `model`.
- An organizing structure that permits different application paths is a `framework`.
- A framework may contain methods or models without becoming one of them.
- A note that performs two substantial functions should normally be separated into two linked notes.

The four types form the initial closed vocabulary. Add a new type only when several real notes cannot be classified correctly and the new distinction improves use or retrieval.

## 6. YAML Metadata

Knowledge notes follow the global YAML standard defined in the [root README](../README.md#6-yaml-standard).

Knowledge notes require `type`, `created`, and `updated`:

```yaml
---
type: concept
created: 2026-09-14
updated: 2026-09-14
---
```

Optional fields are added only when they contain useful information:

```yaml
---
type: concept
created: 2026-09-14
updated: 2026-09-14
domain:
  - systems_science
subjects:
  - systems_thinking
aliases:
  - pensamiento sistémico
sources:
  - meadows2008thinking
---
```

Dates use ISO 8601 format `YYYY-MM-DD`. Preserve the original `created` value and change `updated` after a substantive revision. Do not add empty optional fields. Do not use metadata as a substitute for clear content and contextual relationships.

## 7. Relationships and Sources

Express relationships through links placed in explanatory sentences:

```markdown
The [[system_representation]] framework organizes ways to represent a [[system]].
```

Contextual links are preferred over a `related` YAML field because they explain why two notes are connected.

Use `sources` for documentary traceability. Each value must be a stable BibTeX key defined in:

```text
03_Library/references.bib
```

```yaml
sources:
  - meadows2008thinking
```

The `sources` field identifies the works supporting the note as a whole. When a specific claim requires attribution, cite the corresponding key in the relevant passage.

Use `sources` whenever substantive claims depend on documentary evidence. A note based on original observation or synthesis may omit it only when its evidential basis, assumptions, and limits are explicit enough to evaluate and reuse the knowledge responsibly.

## 8. Knowledge Note Requirements

Information is ready to enter `01_Knowledge/` when it has:

- a clear and descriptive title;
- one identifiable primary knowledge type;
- valid `created` and `updated` dates;
- a coherent explanation of the essential idea, representation, procedure, or structure;
- enough context to be understood outside its original source or project;
- no unnecessary identifying, operational, or sensitive information from an external context;
- explicit evidence, assumptions, and limits when they affect validity or transfer;
- no unnecessary duplication of an existing canonical note.

Metadata, examples, links, and sources are added only when they improve understanding, retrieval, or traceability.

A note does not need to be exhaustive or final. It needs to be understandable, supported, context-independent, and useful.

The admission test is:

> **Can this note be understood and reused without knowing the particular project, client, course, or situation that motivated it?**

Generalization must not erase important conditions or overstate transferability. Remove contextual dependency while preserving the evidence and limits needed to apply the knowledge responsibly.

## 9. Basic Workflow

1. Determine whether the information has been understood sufficiently to be reusable.
2. Check whether a canonical note already exists.
3. Identify its primary type.
4. Create the note from the corresponding template in `04_Templates/`.
5. Write the minimum coherent explanation.
6. Add useful metadata, contextual links, and BibTeX sources.
7. Revise the existing note when understanding changes instead of creating a duplicate.

## 10. Maintenance

- Keep one canonical note per knowledge unit.
- Prefer revising and linking over copying.
- Use search and metadata instead of topic-based subfolders.
- Keep folder depth minimal.
- Remove obsolete metadata and broken relationships.
- Preserve deprecated knowledge only when its history or traceability remains useful.
- Add new folders, types, or rules only when actual use demonstrates a recurring need.

The governing criterion is:

> **Preserve the minimum structure required to make knowledge understandable, retrievable, traceable, and reusable.**
