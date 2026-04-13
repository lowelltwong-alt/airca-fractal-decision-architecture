from __future__ import annotations

import argparse

from .publish import publish_artifact


def main() -> None:
    parser = argparse.ArgumentParser(description="Publish AIRCA decision artifacts as white-paper-style markdown")
    parser.add_argument("artifact", help="Path to the AIRCA decision artifact JSON file")
    parser.add_argument(
        "--output-dir",
        default="papers/generated",
        help="Directory where generated paper files will be written",
    )
    args = parser.parse_args()

    paper_path, summary_path = publish_artifact(args.artifact, args.output_dir)
    print(f"Generated {paper_path}")
    print(f"Generated {summary_path}")


if __name__ == "__main__":
    main()
