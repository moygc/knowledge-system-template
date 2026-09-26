# Knowledge_System

> A personal system for cultivating structured, traceable, and reusable knowledge for understanding, learning, inquiry, and informed action.

## 1. Purpose

`Knowledge_System` supports the cumulative development of knowledge for understanding reality, generating further knowledge, learning, research, teaching, decision-making, professional practice, and everyday life.

It is a sociotechnical system: people establish its purposes and interpret its contents, while files, metadata, search tools, agents, and automations perform supporting functions.

The complete purpose, principles, and decision criterion are defined in [`system_definition.md`](system_definition.md).

## 2. Architecture

```text
Knowledge_System/
├── 00_Inbox/
├── 01_Knowledge/
├── 02_Learning/
├── 03_Library/
├── 04_Templates/
├── AGENTS.md
├── CLAUDE.md
├── DEPLOYMENT.md
├── README.md
├── system_manifest.yaml
└── system_definition.md
```

| Component | Function | Boundary |
|---|---|---|
| `00_Inbox/` | Capture admissible knowledge candidates and sources before processing. | Not permanent storage or an entry point for external project files. |
| `01_Knowledge/` | Preserve processed and reusable knowledge. | Does not store complete sources, courses, or temporary material. |
| `02_Learning/` | Organize course projects for learning, teaching, or both. | Keeps course-specific work while transferring generalizable knowledge to `01_Knowledge/`. |
| `03_Library/` | Preserve documentary sources and bibliographic traceability. | Does not replace synthesized knowledge. |
| `04_Templates/` | Maintain canonical templates. | Does not contain actual knowledge notes. |
| `AGENTS.md` and `CLAUDE.md` | Communicate repository constraints to compatible AI agents. | Do not replace the normative hierarchy or grant authority beyond the user's request. |
| `DEPLOYMENT.md` | Define the boundary between the versioned template and private operational instances. | Does not govern knowledge content. |
| `README.md` | Provide the global operating guide. | Does not duplicate subsystem instructions. |
| `system_manifest.yaml` | Declare machine-readable system identity and schema compatibility. | Does not replace operating documentation. |
| `system_definition.md` | Define the system's purpose and governing principles. | Does not contain operational procedures. |

Root folders represent stable **functions**, not subjects, disciplines, or projects.

## 3. Information Flow

```text
00_Inbox ──processing──→ 01_Knowledge ──application──→ 02_Learning
                              ▲
                              │ support and evidence
                              │
                         03_Library

04_Templates ──standardization──→ repository artifacts
```

This is a dominant flow, not a mandatory linear pipeline. A source can enter `03_Library/` directly, and learning structures can reference both knowledge and sources.

The repository also exchanges information with its environment:

```text
Questions · sources · research · learning · generalized experience
                              ↓
                    Knowledge_System
                              ↓
understanding · new knowledge · teaching-learning · research · informed action
                              ↺
```

External projects and situations may consume knowledge or reveal a knowledge gap, but their operational documentation remains outside the repository. Only sources and knowledge candidates that satisfy the system boundary may enter.

## 4. Where Information Belongs

| Question | Location |
|---|---|
| Is it unprocessed or temporary? | `00_Inbox/` |
| Is it understood and reusable knowledge? | `01_Knowledge/` |
| Was it created specifically for learning or teaching? | `02_Learning/` |
| Is it a documentary or bibliographic source? | `03_Library/` |
| Is it a reusable structure for creating files? | `04_Templates/` |
| Is it operational documentation from an external project or situation? | Keep it in its originating system. |

When an item could belong in several places, identify its primary function, store it in one canonical location, and connect other contexts through links or metadata.

## 5. Global Conventions

### 5.1 Folder Names

- Root folders use an ordering number and a functional English name in PascalCase.
- Subfolders use PascalCase and are normally plural when they represent collections.
- Subfolders are not numbered unless order or sequence carries real meaning.

```text
01_Knowledge/
├── Concepts/
├── Models/
├── Methods/
└── Frameworks/
```

### 5.2 File Names

- Use lowercase `snake_case`.
- Avoid spaces, accents, dates, versions, and lifecycle states.
- Prefer short, descriptive, and stable names.
- `README.md` is the defined naming exception.

```text
system.md
system_purpose.md
system_representation.md
```

### 5.3 Language

- Structural names, YAML keys, and controlled values use English.
- Document content and aliases may use the language most appropriate to the knowledge.
- Add genuine aliases in another language when they materially improve retrieval; do not translate mechanically or duplicate the title without a real search need.
- A semantic file name may preserve another language when translation would reduce precision.

### 5.4 Document Format

Repository documents use Markdown (`.md`) with Obsidian-compatible extensions for wiki links and LaTeX-compatible mathematical notation.

Use:

- ATX headings (`#`, `##`, `###`) to represent document hierarchy, beginning with a single level-one title.
- Standard Markdown paragraphs, emphasis, blockquotes, ordered and unordered lists, and tables.
- Fenced code blocks with a language identifier when the language is known.
- Wiki links (`[[note_name]]`) for relationships between canonical knowledge notes.
- Standard Markdown links for repository documentation, files, and external resources.
- Single dollar-sign delimiters for mathematical notation within a line: `$y = f(x)$`.
- Double dollar-sign delimiters on separate lines for displayed equations:

  ```latex
  $$
  y = f(x)
  $$
  ```

Mathematical expressions use LaTeX-compatible syntax. Dollar-sign delimiters represent mathematics, not currency; write currency with an explicit currency code or escaped symbol when ambiguity is possible.

Use raw HTML only when Markdown cannot express the required structure clearly and the target renderer supports it.

## 6. YAML Standard

YAML applies to knowledge notes in `01_Knowledge/`. README files and other system documentation do not require it.

### 6.1 Required Fields

Knowledge notes require `type`, `created`, and `updated`:

```yaml
---
type: concept
created: 2026-09-14
updated: 2026-09-14
---
```

Accepted values are:

- `concept`: defines and explains an idea;
- `model`: represents a system or phenomenon;
- `method`: explains how to perform an operation;
- `framework`: organizes elements, relationships, or reasoning.

### 6.2 Optional Fields

```yaml
---
type: concept
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

| Field | Function |
|---|---|
| `created` | Date on which the knowledge note was first created. |
| `updated` | Date of the latest substantive change to its knowledge content or structure. |
| `domain` | Broad and stable field of knowledge. |
| `subjects` | Specific topics addressed by the note. |
| `aliases` | Genuine alternative names or synonyms. |
| `sources` | BibTeX keys supporting the note. |

Dates use ISO 8601 format `YYYY-MM-DD`. `created` remains stable; `updated` changes only after a substantive revision, not after formatting-only operations. Optional fields are omitted when they have no values. Collections always use multiline YAML lists.

`sources` is required when substantive claims depend on documentary evidence. It may be omitted for an original definition, observation, or synthesis only when the note states the relevant basis, assumptions, and limits needed to evaluate and reuse it.

The canonical schema excludes `status`, `tags`, and `related`:

- Contextual links express relationships more clearly than `related`.
- `domain` and `subjects` replace generic tags.
- Maturity states create unnecessary manual maintenance.

A deprecated note may use `status: deprecated` as an explicit exception.

### 6.3 Controlled Vocabularies

`type` is a closed vocabulary. It should be extended only when several real notes cannot be classified correctly.

Initial `domain` values are:

- `systems_science`;
- `process_systems_engineering`;
- `techno_economic_analysis`;
- `knowledge_management`.

`domain` is controlled but extensible. New domains must be broad, stable, reusable, and justified by actual content.

`subjects` uses flexible `snake_case` values. `aliases` is free text. `sources` uses unique and stable keys from `03_Library/references.bib`.

## 7. Operating Rules

### 7.1 Canonical Location

Each information unit has one primary physical location. Use links and metadata instead of creating copies.

### 7.2 Flat Architecture

Keep the folder structure as shallow as possible. Add a folder only when it represents a demonstrated functional difference.

### 7.3 Search-Centered Retrieval

Use clear names, search, metadata, and contextual links instead of deep topic-based folder trees.

### 7.4 Maps of Content

Create an index or map of content only when the volume or complexity of an area makes direct navigation and search insufficient.

### 7.5 Minimum Sufficient Complexity

Add a folder, field, template, rule, or automation only when it solves an observed need and its value exceeds its maintenance cost.

### 7.6 Context Independence

Canonical knowledge must remain understandable and reusable without knowing the project, client, course, or situation that motivated it. Particular experience must be abstracted and validated before entering; retain relevant evidence, assumptions, and limits while removing contextual dependency and sensitive information.

### 7.7 Operational Independence from Git

Git may be used to design, distribute, or improve this repository template, but it is not an operational dependency of `Knowledge_System`. A deployed personal or shared instance may grow without versioning its generated knowledge, course projects, or source files.

Traceability depends on stable BibTeX keys, admissible source locations, documentary records, contextual citations, internal links, and YAML dates. When source files are too large or unsuitable for repository storage, `references.bib` and related records must preserve enough information to identify and retrieve them from their authorized location.

The versioned template and an operational instance follow the distribution and update contract in [`DEPLOYMENT.md`](DEPLOYMENT.md). The template uses `system_manifest.yaml` as the instance-level compatibility marker. Its integer `schema_version` changes only when an update requires migration of operational structure, metadata, identifiers, or interpretation rules.

## 8. Basic Workflow

1. Convert a question, source, or experience into an admissible knowledge candidate before capture.
2. Capture the candidate in `00_Inbox/` or register an admissible source directly in `03_Library/`.
3. Decide whether to process, relocate, preserve as a source, or delete it.
4. Convert understood, supported, and context-independent information into a note in `01_Knowledge/`.
5. Add only metadata, links, and sources that improve retrieval or traceability.
6. Use `02_Learning/Courses/` for a course project being taken, created, or both; register its sources in `03_Library/` and transfer only generalizable knowledge to `01_Knowledge/`.
7. Review system health when inquiry or use reveals friction, duplication, missing knowledge, or accumulated Inbox material.

## 9. Subsystem Documentation

Global rules belong in this README. Each subsystem documents only its internal rules.

| Document | Responsibility |
|---|---|
| [`01_Knowledge/README.md`](01_Knowledge/README.md) | Knowledge types, classification, and knowledge-note requirements. |
| [`03_Library/README.md`](03_Library/README.md) | Sources, BibTeX, documentary records, and bibliographic management. |
| [`00_Inbox/README.md`](00_Inbox/README.md) | Capture, admission, and processing rules. |
| [`02_Learning/README.md`](02_Learning/README.md) | Teaching-learning systems and course architecture. |
| `04_Templates/README.md` | Template selection and maintenance. |
| [`DEPLOYMENT.md`](DEPLOYMENT.md) | Template distribution, private-content boundary, compatibility, and updates. |
| [`AGENTS.md`](AGENTS.md) and [`CLAUDE.md`](CLAUDE.md) | Agent instructions and task router; see section 2 (Architecture) for their responsibility and boundary. |

The normative hierarchy is:

```text
system_definition.md
        ↓
README.md
        ↓
Subsystem README
        ↓
Template
```

A lower level can specialize a higher-level rule but cannot contradict it.

## 10. System Feedback and Audit

Use the audit that matches the object and decision. Mixing them produces invalid conclusions because a design repository is not expected to contain a mature body of personal knowledge, while an operational instance is not expected to expose Git or release evidence.

### 10.1 Operational Health

Review health with the minimum measurements needed to support a decision. The canonical structure is [`04_Templates/system_health_report_template.md`](04_Templates/system_health_report_template.md).

Useful measurements include:

- Inbox item count and oldest known capture date;
- knowledge notes with valid required YAML, resolvable links, and traceable sources when documentary claims are present;
- duplicate or orphaned BibTeX keys, source files, and documentary records;
- active course projects with explicit purpose, outcomes, assessment, and feedback;
- generalized knowledge candidates produced by course projects and the decisions made about them;
- unresolved findings from previous reviews.

Measurements are diagnostic signals, not performance targets by themselves. Add a metric only when it can reveal a decision, risk, bottleneck, or useful intervention.

### 10.2 Template Design and Release

Review the versioned design with [`04_Templates/Prompts/template_design_audit_prompt.md`](04_Templates/Prompts/template_design_audit_prompt.md) and record the result with [`04_Templates/template_design_audit_report_template.md`](04_Templates/template_design_audit_report_template.md).

This audit evaluates normative consistency, schema compatibility, prompt safety, structural completeness, and the distribution boundary. It must not use note quantity or topical coverage as evidence that the template succeeds or fails operationally.

## 11. System Evolution

The repository evolves from evidence of use, not anticipated complexity.

Before adding structure, ask:

> Does this change improve the system's ability to cultivate cumulative, verifiable, reusable, and applicable understanding without introducing contextual dependency or disproportionate complexity?

If the value is unclear, do not add the change yet.
