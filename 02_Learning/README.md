# Learning

## 1. Purpose

`02_Learning/` contains course projects designed to support learning, teaching, or both.

Its primary purpose is to organize knowledge, activities, assessment, and feedback so that learners can develop observable and transferable understanding or capabilities.

## 2. Core Principle

A course is a **teaching-learning system**, not merely a sequence of content.

```text
Learning purpose
       ↓
Knowledge + learner + activities + assessment + feedback
       ↓
Relationships organized over time
       ↓
Understanding + capability + transfer
```

The desired result is not content delivery. It is the learner's ability to understand, remember, apply, integrate, and transfer knowledge.

## 3. Scope

This subsystem can contain projects in three modes:

- `learning`: the user is taking or studying a course;
- `teaching`: the user is designing or delivering a course;
- `hybrid`: the same project integrates learning and course creation.

A course project can contain:

- courses;
- learning paths;
- lessons;
- activities and exercises;
- assessments;
- feedback mechanisms;
- teaching and self-learning resources.

It does not contain:

- canonical knowledge notes, which belong in `01_Knowledge/`;
- complete documentary sources, which belong in `03_Library/`;
- unprocessed information, which belongs in `00_Inbox/`;
- reusable repository templates, which belong in `04_Templates/`.

Learning artifacts should reference canonical knowledge instead of copying it. Course-specific explanations, examples, activities, instructions, notes, assignments, decisions, and assessments remain inside the course because their function depends on its learning context.

Courses may include learning projects, cases, and simulations when their primary function is to develop or assess learning. Operational projects whose primary purpose exists outside teaching-learning remain outside the repository.

Sources used by a course are registered in `03_Library/references.bib`. A local source file may remain outside version control or outside the repository when its BibTeX entry and authorized location preserve retrieval. Knowledge discovered or produced through a course enters `01_Knowledge/` only after it becomes generalizable, supported, and understandable without the course context.

## 4. Architecture

```text
02_Learning/
├── Courses/
└── README.md
```

`Courses/` is the collection of course projects. Each course has its own folder and a `README.md` that defines both the project and its teaching-learning system:

```text
Courses/
└── course_name/
    └── README.md
```

Additional folders such as `Lessons/`, `Activities/`, `Assessments/`, or `Resources/` are created only when the volume and structure of a real course justify them.

## 5. Course Project Metadata

Each course-project `README.md` begins with:

```yaml
---
type: course_project
mode: learning
status: active
created: 2026-09-14
updated: 2026-09-14
---
```

Accepted `mode` values are `learning`, `teaching`, and `hybrid`. Accepted `status` values are `planned`, `active`, `paused`, and `completed`. Dates use ISO 8601 format `YYYY-MM-DD`. These controlled values belong only to course projects and do not extend the knowledge-note vocabulary.

## 6. Course as a System

Every course should define the following components:

| Component | Guiding question |
|---|---|
| Purpose | What capability should the course develop? |
| Learners | Who will learn and what do they already know? |
| Context | Under what conditions will learning occur? |
| Knowledge | What canonical knowledge is required? |
| Structure | How should learning progress over time? |
| Activities | What will learners do to construct and apply understanding? |
| Assessment | What evidence will demonstrate learning? |
| Feedback | How will learners and the course adapt from evidence? |

Knowledge notes from `01_Knowledge/` are content elements, but they are not the complete course. Learning emerges from how knowledge interacts with objectives, sequence, practice, assessment, feedback, learners, and context.

## 7. Design Relationships

Course behavior depends primarily on the relationships among its elements.

Important relationships include:

- prior knowledge → new knowledge;
- learning objective → activity;
- activity → evidence of learning;
- evidence → feedback;
- feedback → learner adjustment;
- assessment results → course improvement;
- concept → example → practice → transfer;
- simple structures → integrated and complex structures.

The essential alignment is:

```text
Learning outcomes
        ↕
Learning activities
        ↕
Assessment evidence
```

If these components are not aligned, the course may present information without producing the intended capability.

## 8. Learning Principles

Course design should use the minimum pedagogical structure necessary to support effective learning.

High-value principles include:

- activate relevant prior knowledge;
- make learning outcomes explicit;
- manage cognitive load through coherent segmentation;
- connect explanation with examples and practice;
- use active retrieval and appropriately spaced practice;
- provide timely and actionable feedback;
- evaluate application and transfer, not only recall;
- support planning, self-monitoring, and reflection;
- adapt the design using evidence from learner performance.

These principles guide design but do not impose one universal teaching sequence. Their application depends on the learner, subject, context, modality, and intended capability.

## 9. Knowledge and Source Flow

```text
Course project ──uses──→ references.bib and authorized sources
      │
      ├──keeps──→ course-specific activities, notes, and assessments
      │
      └──reveals──→ generalizable knowledge candidate
                          ↓
                     00_Inbox
                          ↓ review and validation
                     01_Knowledge
```

Do not move raw course notes directly into `01_Knowledge/`. First convert them into a context-independent candidate, preserve evidence and limits, and process them through the normal knowledge workflow.

## 10. Minimum Course Definition

A course can begin with a single `README.md` containing:

```markdown
---
type: course_project
mode: learning
status: active
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Course Project Name

## Project Mode and Scope

## Purpose

## Learners and Context

## Learning Outcomes

## Prerequisite Knowledge

## Knowledge Structure

## Learning Sequence

## Activities and Practice

## Assessment and Feedback

## Sources

## Generalizable Knowledge Candidates
```

Create additional files only when the course can no longer remain clear and usable as one document.

## 11. Basic Workflow

1. Define the capability the course should develop.
2. Identify learners, prior knowledge, context, and constraints.
3. Select the project mode and create its folder from `04_Templates/course_template.md`.
4. Select required knowledge from `01_Knowledge/` and register documentary sources in `03_Library/references.bib`.
5. Map prerequisites and relationships among knowledge elements.
6. Organize a coherent learning progression.
7. Perform or design activities that require learners to use the knowledge.
8. Define observable evidence and assessment criteria.
9. Provide feedback to learners and improve the course structure.
10. Send potentially reusable learning to `00_Inbox/` as generalized candidates; curate it separately before admission to `01_Knowledge/`.

## 12. Maintenance

- Keep canonical knowledge in `01_Knowledge/`.
- Preserve only course-specific content inside the course.
- Prefer references over duplicated explanations.
- Keep course-project status and `updated` current while the project is active.
- Review generalizable knowledge candidates before closing a course project.
- Keep the initial course structure flat.
- Add folders only when navigation or maintenance requires them.
- Revise courses using evidence from learner performance and feedback.
- Do not add pedagogical mechanisms without a clear learning function.

The governing rule is:

> **Design every course as a system whose structure and relationships produce evidence of meaningful and transferable learning.**
