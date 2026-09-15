# Library

## 1. Purpose

`03_Library/` preserves the documentary sources that support knowledge, research, learning, and professional practice.

Its primary function is **bibliographic traceability**: connecting knowledge claims with identifiable sources without duplicating synthesized knowledge from `01_Knowledge/`.

## 2. Scope

This subsystem can contain:

- bibliographic metadata;
- legally stored source files;
- summaries and reading notes about individual sources.

It does not contain:

- reusable conceptual synthesis, which belongs in `01_Knowledge/`;
- temporary captures awaiting evaluation, which belong in `00_Inbox/`;
- course-specific materials, which belong in `02_Learning/`;
- templates, which belong in `04_Templates/`.
- operational documentation, deliverables, and working files from external projects or organizations.

A documentary source may study or report a real project or case when it is legitimately used as evidence. This does not make the originating project part of `Knowledge_System`. Internal project files remain in their own systems unless they have independently become admissible documentary sources.

## 3. Architecture

```text
03_Library/
├── Sources/
├── Records/
├── references.bib
└── README.md
```

| Component | Function |
|---|---|
| `references.bib` | Canonical bibliographic metadata and citation keys. |
| `Sources/` | Optional local copies of source documents. |
| `Records/` | Optional summaries, reading notes, and annotations. |
| `README.md` | Operating rules for the library subsystem. |

`references.bib` is the bibliographic source of truth. Source files and records are optional extensions connected through the same citation key. This traceability model does not depend on Git or require every source file to be stored inside the repository.

In a new operational instance, copy [`04_Templates/references_template.bib`](../04_Templates/references_template.bib) to `03_Library/references.bib`. The operational file is private content and is intentionally excluded from template versioning.

## 4. Canonical Identifier

Every bibliographic work is identified by a unique and stable BibTeX key.

Recommended pattern:

```text
authorYYYYshorttitle
```

Examples:

```text
meadows2008thinking
bertalanffy1968general
turton2018analysis
```

Rules:

- use lowercase ASCII letters and numbers;
- do not use spaces, accents, or file extensions;
- use the first author's family name;
- keep the key short but recognizable;
- add a stable suffix such as `a` or `b` when needed;
- do not change a key after it has been referenced, except to correct an error.

The key connects the library components:

```text
meadows2008thinking
        ├── entry in references.bib
        ├── Sources/meadows2008thinking.pdf
        ├── Records/meadows2008thinking.md
        └── sources: meadows2008thinking
```

## 5. BibTeX

`references.bib` stores canonical bibliographic metadata using standard BibTeX entry types and fields.

Example:

```bibtex
@book{meadows2008thinking,
  author    = {Meadows, Donella H.},
  title     = {Thinking in Systems: A Primer},
  year      = {2008},
  publisher = {Chelsea Green Publishing}
}
```

Use the BibTeX type that best represents the source, such as:

- `@book`;
- `@article`;
- `@incollection`;
- `@inproceedings`;
- `@techreport`;
- `@phdthesis`;
- `@mastersthesis`;
- `@misc` when no more specific type applies.

Prefer standard BibTeX fields. Add optional fields only when the information exists and improves identification, retrieval, or citation.

Do not reproduce BibTeX metadata in Markdown YAML.

## 6. Source Files

`Sources/` stores a local source file only when keeping that file is useful and legally permitted. A source may instead remain in an authorized external location when its BibTeX metadata and, when needed, its documentary record preserve enough information to identify and retrieve it.

Name the primary file with its BibTeX key:

```text
Sources/meadows2008thinking.pdf
```

If several files belong to the same work, append a short functional qualifier:

```text
meadows2008thinking.pdf
meadows2008thinking_supplement.pdf
meadows2008thinking_data.csv
```

Rules:

- preserve the original file format when practical;
- do not rename the file independently of its BibTeX key;
- do not store unauthorized copies;
- do not duplicate the same source in multiple folders;
- a BibTeX entry does not require a local file.
- do not assume that local source files are versioned; establish an appropriate backup or external preservation mechanism when losing them would matter.

## 7. Documentary Records

`Records/` contains optional Markdown notes about individual sources.

A record is useful when a source requires:

- a summary;
- reading notes;
- key ideas;
- interpretation or criticism;
- relevance to current knowledge, research, or learning.

Name the record with the corresponding BibTeX key:

```text
Records/meadows2008thinking.md
```

Recommended minimal structure:

```markdown
# Thinking in Systems

## Summary

## Key Ideas

## Notes
```

Do not copy author, year, publisher, DOI, or other bibliographic fields into the record. Those fields belong only in `references.bib`.

A record describes or interprets one source. Reusable knowledge synthesized from one or more sources belongs in `01_Knowledge/`.

## 8. Relationship with Knowledge Notes

Knowledge notes reference sources through BibTeX keys:

```yaml
sources:
  - meadows2008thinking
  - bertalanffy1968general
```

The `sources` field identifies works supporting the note as a whole. A specific claim that requires attribution should cite the corresponding key in its context.

```text
references.bib
      ↓ identifies
Documentary source
      ↓ supports
Knowledge note
```

Do not use a source record as a substitute for a knowledge note, and do not copy the full synthesis into both locations.

Source records may describe cases contained in a source, but they must not become repositories for the operational history of an external project.

## 9. Basic Workflow

1. Initialize `references.bib` from its template when creating a new operational instance.
2. Check whether the work already exists in `references.bib`.
3. Create a unique and stable BibTeX key.
4. Add and verify the bibliographic entry.
5. Store the source in `Sources/` only when useful and permitted.
6. Create a record in `Records/` only when source-specific notes add value.
7. Reference the BibTeX key from relevant knowledge notes.
8. Correct the canonical entry when bibliographic information improves.

## 10. Maintenance

- Keep one BibTeX entry per cited work or edition.
- Avoid duplicate keys and duplicate bibliographic entries.
- Preserve keys that are already in use.
- Periodically detect missing citations and orphaned files or records.
- Keep bibliographic metadata in BibTeX and interpretation in Markdown.
- Add fields, folders, or indexes only when actual use justifies them.

The governing rule is:

> **One stable citation key connects bibliographic metadata, source files, records, and knowledge notes.**
