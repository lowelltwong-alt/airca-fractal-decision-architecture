# Architecture Diagram Mermaid

This file provides a text-renderable Mermaid version of the repository’s core architecture.

```mermaid
flowchart TD
    U["Ultimate Frame<br/>theology / first principles / mission / constitutional commitments<br/>Christian example: Logos"]
    D["Decision Spine<br/>AIRCA / UAIRCA / LAIRCA"]
    T["Fractal Taxonomy<br/>recursive classification"]
    O["Fractal Ontology<br/>recursive meaning and relationships"]
    F["Fractal Decision-Making<br/>recursive decision structure"]
    M["Machine-Readable Artifacts<br/>identity / classification / relationships / logic / governance / lifecycle / inheritance / interpretation"]
    G["Governed Action, Review, and Persistence"]
    I["Integrations<br/>crosswalks / synthesis / dependency logic / system coherence"]

    U --> D
    D --> F
    T --> O
    O --> F
    T --> M
    O --> M
    F --> M
    M --> G

    I --- U
    I --- D
    I --- T
    I --- O
    I --- F
    I --- M
    I --- G
