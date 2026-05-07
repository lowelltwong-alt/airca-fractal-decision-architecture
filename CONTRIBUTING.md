# Contributing to AIRCA

Thanks for contributing.

AIRCA is being developed as a practical, AI-native decision architecture with machine-readable artifacts.

## Good first contributions

Helpful first contributions include:

- improving the Python examples
- tightening the JSON schema
- adding validators and tests
- creating more decision templates
- improving docs and diagrams
- adding integrations with GitHub, LangGraph, or policy engines

## Development workflow

1. Fork or branch from `main`
2. Create a feature branch
3. Make your change
4. Run the example and tests
5. Open a pull request with a clear description

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python examples/python/task_prioritization_demo.py
```

## Design principles

When contributing, prefer changes that make AIRCA:

- easier to understand
- easier to adopt
- machine-readable
- human-auditable
- GitHub-native
- useful with or without LLMs

## Attribution

Please preserve the distinction between:

- historical collaborative origins where explicitly noted in the existing theory materials
- new repository-specific implementation, packaging, schema, and productization work added by Lowell T. Wong

Do not broaden attribution for new implementation work unless it is explicitly warranted.
