# Course Projects

## Purpose

`Courses/` stores projects whose primary function is learning, teaching, or both.

## Operating Boundary

Each course project has its own folder and begins from `04_Templates/course_template.md`. It may preserve course-specific notes, activities, assessments, resources, decisions, and feedback.

Documentary references belong in `03_Library/references.bib`. Generalizable knowledge does not move directly from a course into `01_Knowledge/`; it first becomes a context-independent candidate in `00_Inbox/` and passes the normal review and validation process.

Operational projects whose primary purpose is not teaching-learning remain outside `Knowledge_System`.

## Minimum Structure

```text
Courses/
└── course_name/
    └── README.md
```

Add `Lessons/`, `Activities/`, `Assessments/`, or `Resources/` only when the course project can no longer remain clear and usable as one document.
