from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator


REQUIRED_FRAMEWORK_FILES = [
    Path("framework/docs/core-schema-spec.md"),
    Path("framework/schemas/core/classes.yaml"),
    Path("framework/schemas/core/edges.yaml"),
    Path("framework/schemas/extensions/religious.yaml"),
    Path("framework/schemas/extensions/secular.yaml"),
    Path("framework/validation/shacl/core.shacl.ttl"),
    Path("framework/examples/religious-justification.ttl"),
    Path("framework/examples/secular-ai-safety.ttl"),
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def load_schema(root: Path) -> dict:
    schema_path = root / "schemas" / "artifact.schema.json"
    return json.loads(schema_path.read_text(encoding="utf-8"))


def validate_artifacts(root: Path) -> list[str]:
    schema = load_schema(root)
    validator = Draft202012Validator(schema)
    errors: list[str] = []
    seen_ids: dict[str, Path] = {}

    for artifact_path in root.glob("**/artifact.json"):
        data = json.loads(artifact_path.read_text(encoding="utf-8"))

        for err in validator.iter_errors(data):
            location = ".".join(str(part) for part in err.path) or "<root>"
            errors.append(f"{artifact_path}: schema error at {location}: {err.message}")

        artifact_id = data.get("artifact_id")
        if artifact_id:
            prior = seen_ids.get(artifact_id)
            if prior:
                errors.append(
                    f"duplicate artifact_id '{artifact_id}' in {artifact_path} and {prior}"
                )
            else:
                seen_ids[artifact_id] = artifact_path

        for doc in data.get("source_docs", []):
            if not (root / doc).exists():
                errors.append(f"{artifact_path}: referenced source doc missing: {doc}")

    return errors


def validate_framework_files(root: Path) -> list[str]:
    errors: list[str] = []
    for rel_path in REQUIRED_FRAMEWORK_FILES:
        if not (root / rel_path).exists():
            errors.append(f"missing framework file: {rel_path}")
    return errors


def validate_roadmap(root: Path) -> list[str]:
    roadmap_path = root / "ROADMAP.md"
    if not roadmap_path.exists():
        return ["ROADMAP.md is missing"]
    first_line = roadmap_path.read_text(encoding="utf-8").splitlines()[0].strip()
    if first_line.lower() != "# roadmap":
        return ["ROADMAP.md should begin with '# ROADMAP'"]
    return []


def main() -> int:
    root = repo_root()
    errors: list[str] = []
    errors.extend(validate_artifacts(root))
    errors.extend(validate_framework_files(root))
    errors.extend(validate_roadmap(root))

    if errors:
        print("Repository validation failed:\n")
        for err in errors:
            print(f"- {err}")
        return 1

    artifact_count = len(list(root.glob("**/artifact.json")))
    print(f"Validation passed. Checked {artifact_count} artifact.json files and framework starter files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
