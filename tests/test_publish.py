from pathlib import Path

from airca.publish import publish_artifact


def test_publish_artifact_generates_markdown_files(tmp_path: Path):
    artifact = tmp_path / "decision.json"
    artifact.write_text(
        """
{
  \"schema_version\": \"0.1.0\",
  \"generated_at\": \"2026-04-03T09:30:00Z\",
  \"decision\": {
    \"id\": \"test-decision\",
    \"title\": \"Test Decision\",
    \"question\": \"What should happen?\",
    \"context\": \"Testing publish output.\",
    \"status\": \"committed\",
    \"chosen_option\": \"Option A\",
    \"rationale\": \"Best available choice.\",
    \"action_items\": [\"Do the thing\"],
    \"roles\": {
      \"architect\": \"Owner\",
      \"inform\": [],
      \"rank\": [],
      \"commit\": \"Owner\",
      \"act\": []
    },
    \"options\": [
      {
        \"name\": \"Option A\",
        \"description\": \"Preferred option\",
        \"scores\": {\"clarity\": 5},
        \"total_score\": 5,
        \"evidence\": [\"Clear\"]
      }
    ],
    \"metadata\": {}
  }
}
        """.strip(),
        encoding="utf-8",
    )

    paper_path, summary_path = publish_artifact(artifact, tmp_path / "papers")

    assert paper_path.exists()
    assert summary_path.exists()
    assert "Decision Paper: Test Decision" in paper_path.read_text(encoding="utf-8")
