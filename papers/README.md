# AIRCA Papers

This folder contains white-paper-style outputs generated from AIRCA decision artifacts.

## Why this folder exists

AIRCA should not rely on abstract promises alone.

It should generate:

- publishable markdown papers
- short decision summaries
- reusable knowledge from real choices

## Workflow

1. Create or update a decision artifact
2. Add human review where needed
3. Add learning signals
4. Publish with:

```bash
python -m airca.publish_cli examples/artifacts/architecture-decision.json
```

## Goal

Every strong AIRCA decision can become:

- a white paper
- a blog post draft
- an internal memo
- a case study
