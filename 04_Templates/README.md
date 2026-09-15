# Templates

## 1. Purpose

`04_Templates/` is the canonical location for reusable structures used to create consistent repository artifacts.

Templates reduce repeated decisions. They provide a useful starting structure without requiring every document to contain every possible section or metadata field.

## 2. Scope

This folder contains templates only. It does not contain:

- actual knowledge notes;
- documentary sources or reading records;
- course-specific materials;
- completed prompts or project documentation.

Completed files must be stored in the subsystem corresponding to their primary function, or in the originating external system when a template explicitly defines that boundary.

## 3. Available Templates

| Template | Use |
|---|---|
| `concept_template.md` | Define and explain an idea. |
| `model_template.md` | Represent a system or phenomenon. |
| `method_template.md` | Describe a repeatable procedure. |
| `framework_template.md` | Organize elements, relationships, or reasoning. |
| `course_template.md` | Define a course project for learning, teaching, or both. |
| `inbox_item_template.md` | Capture a candidate with visible age and pending work. |
| `source_record_template.md` | Record source-specific summaries and notes. |
| `references_template.bib` | Initialize a private operational bibliography. |
| `knowledge_request_sheet_template.md` | Transfer generalized knowledge requirements without exposing their origin. |
| `knowledge_requirements_map_template.md` | Map an external need against available and missing knowledge. |
| `system_health_report_template.md` | Record a lightweight, decision-oriented review of system health. |
| `template_design_audit_report_template.md` | Record a release-oriented audit of the template design. |
| `prompt_template.md` | Create a reusable prompt. |
| `readme_document_template.md` | Document a repository or subsystem. |
| `Prompts/` | Process sources, analyze knowledge boundaries, and review system health. |

The knowledge templates correspond to the four types defined in [`01_Knowledge/README.md`](../01_Knowledge/README.md#4-knowledge-types).

## 4. Template Selection

Select a template according to the artifact's primary function:

```text
Defines an idea                       → concept_template.md
Represents a phenomenon               → model_template.md
Prescribes a repeatable procedure     → method_template.md
Organizes reasoning or action         → framework_template.md
Operates a course project             → course_template.md
Captures an Inbox candidate           → inbox_item_template.md
Records notes about one source        → source_record_template.md
Transfers a generalized request       → knowledge_request_sheet_template.md
Maps an external need to knowledge    → knowledge_requirements_map_template.md
Reviews system health                 → system_health_report_template.md
Audits template design and release    → template_design_audit_report_template.md
Provides reusable AI instructions     → prompt_template.md
Documents a repository or subsystem   → readme_document_template.md
```

If an artifact performs two substantial functions, separate it into linked files instead of combining incompatible templates.

## 5. Usage

1. Select the template that matches the artifact's primary function.
2. Copy it to the correct destination folder.
3. Rename the copy using lowercase `snake_case`.
4. Replace all placeholders.
5. Remove optional metadata and sections that add no value.
6. Add content, links, and sources required for understanding or traceability.
7. For artifacts entering `Knowledge_System`, remove dependency on any particular project, client, course, or situation unless the artifact belongs to `02_Learning/`.
8. Verify that no placeholder remains before considering the file complete.

Do not edit a template to create a specific note. Always work from a copy stored in the appropriate subsystem.

Every prompt that reads documents or repository files must treat their contents as untrusted data rather than instructions and must state its file-access and modification boundary explicitly.

The prompts in `Prompts/` form a documentary processing workflow:

```text
Analyze sources → extract a typed knowledge note → audit traceability
```

Assign a BibTeX key to every source before extraction. When a source or question originates in a particular context, generalize the knowledge need and remove unnecessary identifying or operational details before extraction. Generated notes remain drafts until they have passed human review.

The two audit prompts answer different questions:

| Prompt | Object evaluated | Decision supported |
|---|---|---|
| `system_health_audit_prompt.md` | An operational instance and its behavior | What operational friction or risk requires intervention? |
| `template_design_audit_prompt.md` | The versioned template and release candidate | Is the design coherent, compatible, and safe to distribute? |

The operational audit does not assume that Git exists and uses `system_health_report_template.md`. The design audit may inspect version-control and release evidence and uses `template_design_audit_report_template.md`. Neither audit may modify the evaluated system.

The external knowledge interface follows a separate workflow:

```text
External need → external requirements artifact → coverage analysis → approved generalized request → knowledge curation
```

`knowledge_requirements_analysis_prompt.md` may read both the originating context and `Knowledge_System`, but it must never modify the repository. Its completed map remains in the originating system. Only an approved, context-independent knowledge request may proceed to the extraction and curation workflow.

Two operating modes are available:

| Mode | Workflow | Use |
|---|---|---|
| **Integrated** | `knowledge_requirements_analysis_prompt.md` reads both systems and writes only the external map | Faster analysis with one executor |
| **Separated** | `external_knowledge_request_prompt.md` produces a sanitized sheet; `knowledge_coverage_analysis_prompt.md` searches the repository independently | Stronger separation between context and knowledge |

In separated mode, only `knowledge_request_sheet.md` crosses the boundary. Neither prompt may modify `Knowledge_System`.

## 6. Knowledge Template Rules

Knowledge templates follow the canonical YAML standard from the [root README](../README.md#6-yaml-standard).

Knowledge templates require `type`, `created`, and `updated`:

```yaml
---
type: concept
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Optional fields may be included when they contain useful values:

```yaml
domain:
  - systems_science
subjects:
  - systems_thinking
aliases:
  - pensamiento sistémico
sources:
  - meadows2008thinking
```

Dates use ISO 8601 format `YYYY-MM-DD`. Templates must not contain empty optional fields merely to display every available option. The README documents available fields; the template provides the minimum useful starting point.

## 7. Maintenance

- Maintain one canonical template for each artifact type.
- Do not keep duplicate templates inside other subsystems.
- Keep templates shorter than the documents produced from them.
- Add a section only when it is useful for most artifacts of that type.
- Prefer instructions in this README over extensive comments inside templates.
- Update a template when the governing README changes.
- Test structural changes against real files before adopting them.

The governing rule is:

> **A template should remove recurring decisions without imposing unnecessary content or metadata.**
