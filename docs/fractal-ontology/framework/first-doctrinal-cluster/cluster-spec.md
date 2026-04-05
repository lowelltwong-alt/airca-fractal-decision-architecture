# Cluster Spec: Justification

## Scope

This pilot cluster models the doctrine of justification as a bounded doctrinal field with multiple views, competing claims, baseline-specific judgments, and coherence consequences.

The goal is not to flatten traditions into one verdict. The goal is to make the doctrinal field machine-readable, reviewable, and coherence-aware.

## Core topic

- `doctrine.justification`

Definition:

Justification concerns how a sinner is accounted righteous before God, on what ground, by what means or instrument, and in what relation to sanctification, sacramental life, grace, and final judgment.

## Modeling layers

This cluster uses the repository's framework split:

1. **Topic layer**
   - the doctrinal question itself
2. **View layer**
   - a concrete doctrinal answer
3. **Assertion layer**
   - provenance-bearing claims about what a view depends on, contradicts, or reinforces
4. **Assessment layer**
   - baseline-specific judgments such as affirmed, rejected, disputed, or false doctrine
5. **Coherence layer**
   - penalties, bonuses, and propagation rules that allow ripple effects to be measured

## Included pilot views

### 1. `view.justification.forensic_imputation`
God justifies by a declarative act in which the believer is counted righteous on the basis of Christ's righteousness, received by faith rather than by intrinsic merit.

### 2. `view.justification.infused_righteousness`
God justifies through grace that makes the believer actually righteous, with justification and renewal more tightly joined than in strictly forensic accounts.

### 3. `view.justification.synergistic_participation`
Justification is framed through covenantal or participatory union in which grace initiates and enables, while the believer's response is not treated as merely passive.

### 4. `view.justification.moral_reduction`
Justification is reduced to God's recognition of moral improvement, exemplary imitation, or ethical reform without adequate grounding in grace, divine action, or Christ's objective saving work.

### 5. `view.justification.antinomian_distortion`
Justification is distorted into a denial that obedience, sanctification, or moral seriousness matter at all for the Christian life.

## Included baselines

### `baseline.reformed_confessional`
Used to model a classic Reformed confessional evaluation.

### `baseline.catholic_tridentine`
Used to model a Roman Catholic Tridentine evaluation.

### `baseline.ecumenical_minimum`
Used as a lighter shared boundary for identifying views that fall inside or outside broad historical orthodoxy.

## Design rules for this pilot

- A topic is never itself labeled false doctrine.
- A specific view can be labeled `false_doctrine` only inside a stated baseline.
- Contradiction edges are typed and weighted, not merely implied.
- Dependencies are modeled separately from affirmations.
- Coherence scoring is downstream from ontology; ontology does not silently perform the norming work.
- Human review remains authoritative for assessment changes.

## What this pilot demonstrates

This cluster demonstrates that the repository can represent:

- one doctrine with multiple views
- baseline-specific orthodoxy judgments
- explicit false doctrine handling
- coherence penalties for contradiction
- coherence penalties for broken dependencies
- AIRCA-compatible review and commitment points

## Planned expansions

- add scriptural interpretation nodes
- add theologian and confession lineage nodes
- add named-graph or provenance partitions by tradition
- add temporal overlays for historical shifts
- add scoring implementation examples
