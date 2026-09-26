# Agent Instructions

This repository implements `Knowledge_System`. Before doing anything here, read `system_definition.md` and `README.md` in this same root: they define the system's purpose, boundary, and governing rules. Do not act from this file alone.

## Non-negotiable rules (also mirrored in CLAUDE.md, keep both in sync if edited)

- Do not introduce the Unicode character `U+2014` in prose authored or revised for this repository or in prompts produced for it. Preserve it when it is part of a direct quotation, an official title, bibliographic metadata, code, or other source text whose exact form matters. Use commas, parentheses, colons, or restructure the sentence instead.
- Never create, edit, move, or delete a file in this repository without first showing the person the full content, file name, and path, and getting explicit confirmation.
- Before creating a knowledge note, check whether an equivalent note already exists in the target subfolder of `01_Knowledge/`. If it does, say so and ask whether this is an extension or a distinct topic instead of assuming.
- In a distributable template repository, never add operational knowledge, Inbox items, course projects, bibliographic entries, sources, records, or personal configuration. Follow the boundary defined in `DEPLOYMENT.md`.

## Task Router (progressive disclosure)

Before reading anything beyond this file, classify the user's request using the table below. Read only the files listed for the matching path, in the order given. Escalate to a wider path only when the chosen path's own instructions require it.

| Path | Triggered by | Read, in order | Produces |
|---|---|---|---|
| A. Full systemic audit | A request to analyze or audit the whole repository | `system_definition.md`, `README.md`, every subsystem `README.md` including any README.md it links to (for example `02_Learning/Courses/README.md`); then, depending on which audit is requested (ask if not stated): `04_Templates/Prompts/system_health_audit_prompt.md`, plus `04_Templates/Prompts/traceability_audit_prompt.md` if traceability is in scope, for an operational audit; or `04_Templates/Prompts/template_design_audit_prompt.md` and `DEPLOYMENT.md` for a template-design audit | A diagnosis matching the chosen audit type, recorded with `04_Templates/system_health_report_template.md` or `04_Templates/template_design_audit_report_template.md` |
| B. Placement triage | "Where should this information go", "I have this, where does it belong" | `README.md` section 4 (Where Information Belongs); `00_Inbox/README.md` section 3 if the result is Inbox; `README.md` section 6 if the result is `01_Knowledge/` | A proposed location with justification |
| C. Knowledge note drafting | The destination is already known to be `01_Knowledge/` | `01_Knowledge/README.md` (type and YAML), the matching template in `04_Templates/`, and a duplicate check in the target subfolder | A drafted note, ready for confirmation |
| D. Course design from existing knowledge | "Help me build a course from what I already have" | `02_Learning/README.md`, `04_Templates/course_template.md` (to define purpose, learners, and learning outcomes first), then an index of titles and metadata from `01_Knowledge/` (not full note content) | A course structure referencing existing notes, plus a list of missing knowledge (each one handed to path C's research-request step) |
| E. External knowledge interface | Another project needs to know whether this system already covers something, without exposing its context | `04_Templates/knowledge_requirements_map_template.md`, `04_Templates/knowledge_request_sheet_template.md`; then, per `04_Templates/README.md` section 5 (ask which mode if not stated): `04_Templates/Prompts/knowledge_requirements_analysis_prompt.md` alone for the integrated mode, or `04_Templates/Prompts/external_knowledge_request_prompt.md` followed by `04_Templates/Prompts/knowledge_coverage_analysis_prompt.md` for the separated mode | A coverage map or a generalized knowledge request |

Path C assumes usable material already exists. When it does not, first draft a request for external literature research using `04_Templates/Prompts/literature_research_request_prompt.md`, then continue with `04_Templates/Prompts/knowledge_note_prompt.md`.

If the request does not clearly match one path, ask which path applies before reading anything else. Never default to reading the whole repository.

Every non-negotiable rule above still applies inside every path: show full content before writing, confirm before creating or editing, and check for duplicates before adding a knowledge note.

## Where the rest of the rules live

- Note format, YAML schema, and classification rules: `01_Knowledge/README.md`.
- Bibliographic and source rules: `03_Library/README.md`.
- Inbox capture rules: `00_Inbox/README.md`.
- Course project rules: `02_Learning/README.md`.
- Template selection and the extraction/audit prompt family: `04_Templates/README.md` and `04_Templates/Prompts/`.
- Template distribution, compatibility, and release safety: `DEPLOYMENT.md`.

Follow the normative hierarchy already defined in `README.md`: `system_definition.md → README.md → subsystem README → template`. A lower level can specialize a higher one but never contradict it.
