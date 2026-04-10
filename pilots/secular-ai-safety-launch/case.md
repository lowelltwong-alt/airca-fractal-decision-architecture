# Case

## Scenario

A product team has built a customer-facing AI summarization feature for enterprise support workflows.

The feature reduces handling time and improves operator productivity in internal testing. But there are open concerns around:
- hallucinated summaries
- omission of safety-critical details
- inconsistent citation behavior
- weak escalation behavior when confidence is low

## Bounded question

Should the feature ship this quarter?

## Candidate views

### View A — Ship now
The feature is materially useful and should be released broadly on schedule.

### View B — Ship with controls
The feature should launch only with:
- confidence thresholding
- citation display
- human-review fallback for low-confidence cases
- audit logging
- defined rollback trigger

### View C — Delay launch
The feature should not launch until safety and governance controls are stronger.

## Assessments

### Assessment 1 — Value
The feature creates clear productivity upside.

### Assessment 2 — Risk
The feature can distort or omit important case details in some edge cases.

### Assessment 3 — Governance fit
A controlled release with traceability and fallback is more compatible with accountable deployment than an unrestricted launch.

## Current ranked outcome

**Ranked position: View B — Ship with controls**

This preserves momentum without pretending unresolved risk does not matter.

## Why this is a good pilot

This case is small enough to inspect by hand, but rich enough to prove the framework can carry:
- a real question
- multiple positions
- evidence-linked assertions
- a ranked result
- a review path
