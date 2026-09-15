# Inbox

## 1. Purpose

`00_Inbox/` is the temporary entry point for admissible knowledge candidates and sources that have not yet been fully evaluated or processed.

Its function is to make capture easy without weakening the permanent structure of the repository.

## 2. What Belongs Here

- quick notes and ideas;
- incomplete drafts;
- exploratory or project-produced knowledge drafts that still require generalization, sources, or validation;
- information awaiting classification;
- references awaiting bibliographic registration;
- material that requires review before deciding its value.

The Inbox does not require complete knowledge-note YAML, polished writing, or definitive classification. It does require enough queue metadata to make age and pending work visible.

## 3. Minimum Queue Metadata

Every Inbox item begins with:

```yaml
---
captured: YYYY-MM-DD
pending_reason: [concise reason this item still requires a decision or transformation]
---
```

`captured` records when the item entered the Inbox. `pending_reason` is concise free text rather than a controlled vocabulary; it should identify the missing decision or transformation, not restate the topic.

Add `review_after: YYYY-MM-DD` only when review has been intentionally deferred until a meaningful date. It is not a deadline required for every item.

Use [`04_Templates/inbox_item_template.md`](../04_Templates/inbox_item_template.md) when a structured capture is useful. A minimal quick capture may contain only the required metadata, a title, and enough content to make the pending decision understandable.

## 4. What Does Not Belong Here

- processed and reusable knowledge;
- registered documentary sources;
- active course structures;
- canonical templates;
- operational files, deliverables, or identifiable records from external projects;
- sensitive contextual information unnecessary for developing reusable knowledge;
- material kept indefinitely without a defined reason.

An external experience may generate an Inbox item only after its potential learning has been expressed as a general question, observation, hypothesis, or knowledge candidate. The originating project or situation remains in its own system.

A course project may also generate an Inbox item after its potentially reusable learning has been separated from course-specific activities, assignments, decisions, and learner context.

## 5. Processing Decisions

Every item should eventually receive one decision:

```text
Inbox item
    ├── process into reusable knowledge → 01_Knowledge/
    ├── use for teaching or learning    → 02_Learning/
    ├── register or preserve as source  → 03_Library/
    ├── move to another appropriate system
    └── delete when it has no continuing value
```

Moving an item means integrating it into the destination subsystem, not merely relocating an unprocessed file.

## 6. Basic Workflow

1. Verify that the item belongs within the repository boundary.
2. Remove unnecessary project, client, organizational, or personal identifiers.
3. Capture it with enough conceptual and evidential context to understand it later.
4. Review it when processing the Inbox.
5. Determine its primary function and continuing value.
6. Process, relocate, or delete it.
7. Remove the original Inbox item after successful integration.

## 7. Minimum Rules

- Prefer descriptive temporary names when practical.
- Add a source or context when it may otherwise be forgotten.
- Preserve `captured` and keep `pending_reason` aligned with the actual unresolved work.
- Preserve evidence and limits, but not unnecessary contextual dependency.
- Do not organize the Inbox with topic-based subfolders.
- Do not duplicate an item when processing it.
- Keep only material that still requires a decision or transformation.
- Review the Inbox before accumulated material becomes difficult to evaluate.

The governing rule is:

> **Capture admissible candidates quickly, then process them deliberately. The Inbox is a queue, not an archive.**
