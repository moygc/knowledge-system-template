# Agent Instructions

This repository implements `Knowledge_System`. Before doing anything here, read `system_definition.md` and `README.md` in this same root: they define the system's purpose, boundary, and governing rules. Do not act from this file alone.

## Non-negotiable rules (also mirrored in CLAUDE.md, keep both in sync if edited)

- Do not introduce the Unicode character `U+2014` in prose authored or revised for this repository or in prompts produced for it. Preserve it when it is part of a direct quotation, an official title, bibliographic metadata, code, or other source text whose exact form matters. Use commas, parentheses, colons, or restructure the sentence instead.
- Never create, edit, move, or delete a file in this repository without first showing the person the full content, file name, and path, and getting explicit confirmation.
- Before creating a knowledge note, check whether an equivalent note already exists in the target subfolder of `01_Knowledge/`. If it does, say so and ask whether this is an extension or a distinct topic instead of assuming.
- In a distributable template repository, never add operational knowledge, Inbox items, course projects, bibliographic entries, sources, records, or personal configuration. Follow the boundary defined in `DEPLOYMENT.md`.

## Where the rest of the rules live

- Note format, YAML schema, and classification rules: `01_Knowledge/README.md`.
- Bibliographic and source rules: `03_Library/README.md`.
- Inbox capture rules: `00_Inbox/README.md`.
- Course project rules: `02_Learning/README.md`.
- Template selection and the extraction/audit prompt family: `04_Templates/README.md` and `04_Templates/Prompts/`.
- Template distribution, compatibility, and release safety: `DEPLOYMENT.md`.

Follow the normative hierarchy already defined in `README.md`: `system_definition.md → README.md → subsystem README → template`. A lower level can specialize a higher one but never contradict it.
