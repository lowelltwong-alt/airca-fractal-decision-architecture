# Decision Paper: Choose AIRCA packaging direction

## Abstract
This paper documents a structured AIRCA decision and converts it into a public-facing record that can be reviewed, reused, and improved over time.

## Problem
How should AIRCA be packaged first to maximize usability and GitHub adoption?

## Context
The project needs a practical first release that is easy to run, easy to explain, and strong enough to generate future papers and examples.

## Options Considered
### Option 1: Python package + publish pipeline
Ship a usable package and turn decisions into white-paper-style outputs.
- Total score: 15
- Evidence: Fast time to value, GitHub-native, Content engine

### Option 2: Theory docs only
Keep expanding conceptual docs without productized outputs.
- Total score: 4
- Evidence: Low immediate value, Harder to attract users

## Evaluation Criteria
- adoption
- clarity
- usability

## Decision
Python package + publish pipeline

## Rationale
This path balances speed, clarity, and real-world usefulness while creating a direct path from decisions to reusable public knowledge.

## AIRCA Roles
- Architect: Lowell T. Wong
- Inform: Potential contributors, GitHub users
- Rank: Maintainer, Developer advisor
- Commit: Lowell T. Wong
- Act: Repository maintainer

## Implications
- Ship publish pipeline
- Add more examples
- Use generated papers as public artifacts

## Human Review
- Required: true
- Reviewer: Lowell T. Wong
- Status: approved
- Notes: Approved after reviewing risk, maintainability, and onboarding impact.

## Future Review
30 days

## Learning Signals
- Watch onboarding time for new contributors
- Track artifact reuse in future architecture decisions
- Review whether human review reduced ambiguity

## Assumptions
- People adopt tools faster than abstract frameworks
- Reusable outputs increase repository desirability

## Uncertainties
- How quickly contributors will adopt the paper workflow
- Which use case will resonate most first

## Publication Notes
This white-paper-style document was generated from an AIRCA decision artifact.
