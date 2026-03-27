# Architecture Diagram Mermaid Detailed

This file provides a more detailed Mermaid version of the repository’s architecture.

```mermaid
flowchart TD
    U["Ultimate Frame<br/>first principles / theology / mission / constitutional commitments / moral anthropology"]
    L["Christian Example of U<br/>Logos"]
    A1["AIRCA<br/>Architect / Inform / Rank / Commit / Act"]
    A2["UAIRCA<br/>Ultimate Frame + AIRCA"]
    A3["LAIRCA<br/>Logos-grounded Christian expression of UAIRCA"]

    T["Fractal Taxonomy<br/>recursive classification"]
    O["Fractal Ontology<br/>recursive meaning and relationships"]
    FD["Fractal Decision-Making<br/>recursive decision grammar"]

    MR["Machine-Readable Artifacts<br/>identity / classification / relationships / logic / governance / evidence / provenance / lifecycle / inheritance / interpretation"]
    DL["Decision Ledger / Persistence<br/>problem / options / criteria / decision / expected outcome / actual outcome / review"]
    GR["Governed Action / Review / Feedback"]

    I["Integrations<br/>crosswalks / synthesis / dependency logic / coherence"]

    S["Scale Recurrence<br/>enterprise / function / team / workflow / document / issue / task / node"]

    U --> A2
    L --> A3
    A1 --> A2
    A2 --> A3

    A1 --> FD
    A2 --> FD
    A3 --> FD

    T --> O
    O --> FD

    T --> MR
    O --> MR
    FD --> MR

    MR --> DL
    DL --> GR

    S --> T
    S --> O
    S --> FD
    S --> MR

    I --- U
    I --- L
    I --- A1
    I --- A2
    I --- A3
    I --- T
    I --- O
    I --- FD
    I --- MR
    I --- DL
    I --- GR
    I --- S
