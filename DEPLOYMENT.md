# Deployment and Template Versioning

## 1. Purpose

This document defines how to distribute and update the `Knowledge_System` template without placing operational knowledge, courses, sources, or personal records under version control.

The design repository and an operational instance have different functions:

```text
Versioned template repository
        ↓ instantiate or update
Operational Knowledge_System
        ↓ produces
Private knowledge, courses, sources, and records
```

Git versions the design of the system. It is not the storage, traceability, or backup mechanism for operational content.

## 2. Distribution Contract

A distributable template contains only:

- `README.md`, `system_definition.md`, `DEPLOYMENT.md`, `system_manifest.yaml`, `AGENTS.md`, and `CLAUDE.md`;
- repository configuration required for safe distribution;
- subsystem README files;
- canonical files under `04_Templates/`;
- empty functional directories represented by `.gitkeep` when necessary.

It must not contain:

- Inbox items other than `00_Inbox/README.md`;
- knowledge notes other than `01_Knowledge/README.md`;
- actual course projects;
- an operational `03_Library/references.bib`;
- source files or documentary records;
- credentials, local application state, caches, or personal configuration.

This contract is based on path and function, not file extension. A Markdown or BibTeX file can still contain private operational content.

## 3. Operational Initialization

After creating an instance from the template:

1. Keep `system_manifest.yaml` at the root as the instance compatibility marker.
2. Copy `04_Templates/references_template.bib` to `03_Library/references.bib`.
3. Create knowledge, course, source, and record files only in their operational folders.
4. Establish a backup mechanism appropriate to the value and volume of operational content.
5. Do not rely on Git history for knowledge traceability; use the identifiers, dates, citations, records, and links defined by the system.

The operational `references.bib` is deliberately excluded from template versioning even though the empty starter lives under `04_Templates/`.

## 4. Schema Compatibility

`system_manifest.yaml` declares the schema version used by the complete instance:

```yaml
system_id: knowledge_system
schema_version: 1
```

The schema version changes only when an update requires an operational instance to migrate its folders, metadata, identifiers, or interpretation rules. Documentation corrections and backward-compatible additions do not require a schema change.

Before applying a template update:

1. compare the instance schema version with the new template;
2. read the release notes or migration instructions;
3. back up operational content;
4. apply only functional files from the distribution contract;
5. verify the instance with the operational health audit.

Never replace an operational folder wholesale with the corresponding folder from a template release.

## 5. Version-Control Policy

The distributable repository uses a closed allowlist. Everything is ignored by default, and only functional paths are explicitly admitted.

The intended policy is:

```text
Tracked:   system definition, manifest, operating and agent documentation,
           templates, prompts, distribution configuration, empty structure

Ignored:   Inbox candidates, knowledge notes, course projects,
           references, sources, records, and local application state
```

Do not use extension-wide exceptions such as allowing every `*.md` or `*.bib` file. They defeat the boundary because most operational content uses those formats.

## 6. Release Verification

Before publishing a template release:

1. generate it in a new directory with no inherited Git history;
2. inspect the complete list of files prepared for version control;
3. verify that every tracked path satisfies the distribution contract;
4. search for credentials, personal identifiers, operational citations, and real course or knowledge content;
5. test internal Markdown links, prompt boundaries, and template consistency;
6. confirm that the operational folders remain usable after private files are created and ignored;
7. create the release only after the clean export passes these checks.

Changing `.gitignore` does not remove information from previous commits. A public template must begin from a clean exported directory or from a history that has been deliberately sanitized.

## 7. Update Principle

Template updates flow from design to operation. Operational content never flows back into a public release automatically.

```text
Observed operational friction
          ↓ generalized, non-sensitive requirement
Private design and testing
          ↓ verified functional change
Clean template release
          ↓ controlled adoption
Operational instance
```

The governing rule is:

> **Distribute the system's capabilities and constraints, never the user's accumulated content.**
