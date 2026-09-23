# Literature Research Request Prompt

## Purpose

Draft a request for an external AI research tool (for example NotebookLM or a
general-purpose assistant) to extract and structure literature on a topic,
before that material enters this repository through the Knowledge Note Prompt
or the Source Analysis section within it.

## Required Inputs

- Topic to research.
- Target note type, if already known: concept, model, method, or framework
  (optional; the external tool can also help determine this).
- Whether the material will support a course, if pedagogical framing is needed.

## Prompt

```text
I need literature-based material on: [TOPIC].

If a target note type is already known, structure the material to answer that
type's primary question:
- concept: What is it?
- model: How can it be represented?
- method: How is it done?
- framework: How should the problem or knowledge be organized?
If the type is not yet known, present the material so the type is identifiable:
definition-only material suggests a concept, a representation with elements and
relationships suggests a model, a repeatable procedure suggests a method, an
organizing structure suggests a framework.

Return, for each source you use:
- a full, verifiable citation (author, year, title, publisher or venue, and a
  stable identifier such as a DOI or URL when available);
- the specific claims you attribute to it, with page, section, or location
  when possible;
- whether each claim is explicitly stated by the source or your own synthesis
  across sources.

Do not invent citations, page numbers, or claims not present in the material
you found. State explicitly when the literature is sparse, contradictory, or
inconclusive on a point, rather than smoothing it over.

If this material will support a course, also identify prerequisite knowledge a
learner would need before this topic, and natural checkpoints where a learner
could self-assess understanding.

Keep the material free of any project, client, or organizational context; it
should stand on its own.
```

## Next Step

Paste the returned material, with its citations, into the Source Analysis
section of `knowledge_note_prompt.md` (or directly into the matching type
subsection, if the type and scope are already clear) to continue on path C.
