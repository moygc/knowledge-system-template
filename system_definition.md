---
type: system_definition
created: 2026-09-05
updated: 2026-09-14
---

# Knowledge System Definition

## General Purpose

`Knowledge_System` exists to cultivate structured, traceable, and reusable knowledge that supports understanding reality, generating further knowledge, learning, teaching, and informed action.

It transforms questions, documentary sources, reflection, research, and generalized experience into cumulative, verifiable, and applicable understanding. Its purposes may arise from intellectual curiosity, philosophical inquiry, material needs, learning, research, professional practice, or everyday life.

The repository provides a canonical location for each information unit and organizes its relationships without unnecessary duplication. Its structure must be understandable and usable by people, digital tools, artificial intelligence agents, and information retrieval systems.

## Nature of the System

`Knowledge_System` is a **sociotechnical knowledge system**, not merely a collection of folders and files.

Its purposes originate from, or are attributed by, human and social agency. Machines and other artifacts perform operational functions within the system designed to serve those purposes.

The system combines people, information, knowledge notes, documentary sources, metadata, templates, rules, semantic relationships, search tools, artificial intelligence agents, validators, and automations.

## Core Concepts

- **Purpose:** intended state or result established by human or social agents.
- **Function:** observable contribution an element makes within the system.
- **Structure:** elements, relationships, rules, boundaries, and mechanisms that constitute the system.
- **Behavior:** what the system actually does over time.
- **Result:** state or output produced by the system's behavior.

```text
Human purpose
      ↓
Structural design
      ↓
Operational functions
      ↓
System behavior
      ↓
Results
      ↺
Feedback to people and system structure
```

## Functional Architecture

| Component | Primary function |
|---|---|
| `00_Inbox/` | Capture candidate knowledge and sources with low friction before processing. |
| `01_Knowledge/` | Preserve processed, structured, and reusable knowledge. |
| `02_Learning/` | Operate course projects for learning, teaching, or both. |
| `03_Library/` | Preserve documentary sources and their traceability. |
| `04_Templates/` | Standardize the creation of repository artifacts. |
| `system_manifest.yaml` | Declare the identity and compatibility version of the operational structure. |
| YAML metadata | Support semantic classification, retrieval, and automation. |
| Internal links | Express meaningful relationships between knowledge units. |
| README files | Define the rules and operating logic of the system. |
| Agent instruction files | Communicate repository boundaries and operational constraints to compatible artificial intelligence agents. |
| People and agents | Interpret, transform, evaluate, use, and maintain knowledge. |

## System Boundary and Environment

The system contains reusable knowledge, learning structures, documentary sources, templates, metadata, relationships, and its own governance documents. It does not contain the operational documentation of external projects, clients, organizations, or personal situations.

External contexts can use the system and reveal knowledge needs, but they remain in their own repositories. Information crosses into `Knowledge_System` only after it has been converted into a generalizable knowledge candidate or an admissible documentary source.

Real cases may appear as evidence or examples when they are relevant, legally usable, and sufficiently contextualized. A knowledge unit must not depend on knowing the particular case that motivated it.

`02_Learning/` is an internal project subsystem. It may contain a course that a user is taking, a course the user is creating, or a combined teaching-learning project. Course-specific activities, assessments, resources, decisions, and feedback remain in that project. Its documentary references connect to `03_Library/`, while knowledge that becomes sufficiently general, supported, and context-independent moves to `01_Knowledge/`.

The repository itself is also a system under design. Its specific architecture and rules belong in `system_definition.md` and README files. Knowledge learned through its construction belongs in `01_Knowledge/` only after it has been generalized beyond this repository.

Git may support the design, distribution, and improvement of the repository template, but it is outside the operational architecture of a deployed `Knowledge_System`. Operational traceability must therefore remain functional without Git through YAML dates, stable bibliographic identifiers, source locations, citations, documentary records, and internal relationships. Large generated content and source files may remain outside version control when their authorized location and identity remain traceable.

The versioned template contains only functional documentation, canonical templates, prompts, configuration, and required empty structure. Operational knowledge, courses, bibliographic entries, sources, and records belong to the deployed instance and must not enter a public template release. `system_manifest.yaml` identifies the schema shared by the instance; incompatible design changes require an explicit migration rather than silent replacement.

## Information Flows

```text
Curiosity · questions · sources · research · learning · generalized experience
                                  ↓
                  capture → abstraction → validation
                                  ↓
                 Concepts · Frameworks · Methods · Models
                                  ↓
understanding · new knowledge · teaching-learning · research · informed action
                                  ↓
                    questions · evidence · experience
                                  ↺
```

The boundary operates as a filter:

```text
Particular context → extract learning → remove contextual dependency
                  → preserve evidence and limits → admit or reject
```

External project-specific needs can trigger inquiry, but their operational projects are neither the system's primary purpose nor internal components. Course projects are the explicit exception because `02_Learning/` exists to operate teaching-learning activity. The same boundary filter applies to needs arising from curiosity, study, teaching, research, reflection, or daily life.

## Structure and Behavior Principle

The behavior of the repository depends deeply on its structure. Folders, templates, metadata, links, and rules influence how knowledge is captured, processed, found, related, reused, and maintained.

```text
Fragmentation and excessive rules
                ↓
Greater classification and maintenance friction
                ↓
Duplication, inconsistency, and abandonment
```

Conversely:

```text
Canonical location + minimal metadata + clear relationships
                            ↓
                  Simple capture and retrieval
                            ↓
                   Greater knowledge reuse
                            ↓
              Coherent accumulation of knowledge
```

## Structural Principles

- **Flat architecture:** keep the physical structure as shallow as possible while preserving useful functional distinctions.
- **Search-centered retrieval:** use consistent names, metadata, links, and search instead of topic-based folder trees.
- **Maps of content on demand:** create indexes only when volume or complexity makes direct navigation insufficient.
- **Canonical location:** give each information or knowledge unit one primary physical location.
- **Context independence:** preserve reusable knowledge without making it dependent on the project, course, or situation that motivated it.
- **Minimum sufficient complexity:** add structure only when it solves a demonstrated need without disproportionate complexity.

## Feedback and Adaptation

```text
Operational cycle:
Question or source → capture → process → relate → use → review

Structural cycle:
Observe friction → identify cause → modify structure → evaluate

Health cycle:
Measure relevant condition → interpret evidence → decide → review effect
```

The architecture must be stable enough to produce consistency and adaptable enough to respond to evidence from inquiry, learning, research, and actual use. External experience returns as generalized questions, evidence, or learning—not as operational documentation of its original context. Structural changes should solve observed needs rather than hypothetical future needs.

## Decision Criterion

> **Does this element improve the system's sustained ability to cultivate cumulative, verifiable, reusable, and applicable understanding without introducing contextual dependency or disproportionate complexity?**

If the answer is unclear, the element should not be added until a real need can be demonstrated.
