---
artifact: true
artifact_type: technical_crosswalk
status: proposed
canon_status: not_canon_until_approved
authority: explanatory_only
review_cycle: 6 months
stale_after: 2026-11-29
---

# Shannon Information Theory and Decision Capacity

Status: Non-canonical concept note.
Authority: Explanatory only. AIRCA is not a communication theorem; Shannon is used here as a reliability lens for decision architecture, not as a derivation of doctrinal authority or as a flagship claim.

## BLUF

AIRCA's central wager is that **as AI makes answers cheaper, the scarce resource becomes decision capacity**. Information theory makes that claim precise. Decision capacity has the same structural meaning as channel capacity: a finite rate at which a workflow + reviewer + governance loop can absorb evidence, reduce uncertainty, and commit. The AIRCA stages — **Architect, Inform, Rank, Commit, Act** — map directly onto channel definition, mutual-information gathering, distortion-bounded compression, residual-uncertainty acceptance, and transmission. This note explains the mapping. It does **not** re-rank AIRCA as a flagship, alter LAIRCA/Logos theological claims, or introduce new doctrinal artifacts.

Conceptual lineage: this note draws on Shannon (1948), Cover & Thomas (*Elements of Information Theory*), and MacKay (*Information Theory, Inference, and Learning Algorithms*); see the **References** section. No file outside this repository is required to read this note.

## Boundary

This note does **not**:

- claim AIRCA is the operational consequence of Shannon math;
- alter the AIRCA / UAIRCA / LAIRCA stack or its definitions;
- promote AIRCA to flagship status (LawFirm OS remains the flagship architecture per the profile portfolio);
- propose new artifact classes, ontology entries, or governance rules;
- define theological truth, Logos ordering, or Ultimate Frame content (those belong upstream of AIRCA);
- introduce new metrics as required runtime numbers — anything quantitative below is conceptual.

The AIRCA / Ultimate Frame distinction stated elsewhere in this repo is preserved.

## AIRCA stage → Shannon function

| AIRCA stage | Shannon function | What it does in decision architecture |
|---|---|---|
| **Architect** | define source $X$, channel, receiver, destination, authority boundaries | name what the decision is about, who decides, what counts as authoritative input |
| **Inform** | gather $Y$ to reduce $H(X \mid Y)$ via mutual information | acquire evidence valued by its uncertainty reduction, not its volume |
| **Rank** | rate-distortion compression: choose the smallest representation that preserves the decision-relevant distinctions | shortlist options, compress alternatives while preserving forbidden distortions |
| **Commit** | accept residual uncertainty consistent with Fano-style error bounds | choose under residual uncertainty; do not pretend certainty the channel did not deliver |
| **Act** | transmit the commitment downstream + record provenance for future channels | execute and write durable decision memory so the next loop can compare $P_{\text{predicted}}$ vs $P_{\text{observed}}$ |
| **Review / Exception** | detect distortion across the chain; trigger error correction | catch upstream errors before chaos-amplification; route through governed correction |

## Real math used

Notation:

- $X$ = the decision-relevant variable (the thing the institution actually needs to decide).
- $Y$ = the evidence assembled during *Inform*.
- $A$ = the action alternatives ranked during *Rank*.
- $\hat{A}$ = the action committed to and acted on.
- $D$ = an accepted distortion budget on the compression performed during *Rank*.

### Entropy as decision uncertainty

```math
H(X) = -\sum_{x} p(x)\,\log_2 p(x)
```

AIRCA interpretation:

- Decision uncertainty is what *Architect* names and what *Inform* + *Rank* + *Commit* progressively reduce. High $H(X)$ is the condition under which a deliberate fractal decision architecture matters at all — when $H(X)$ is near zero, the institution does not have a decision; it has a transaction.

### Mutual information as the value of evidence

```math
I(X;Y) = H(X) - H(X \mid Y)
```

AIRCA interpretation:

- *Inform* should optimize $I(X;Y)$, not document volume. A 200-page intake packet that does not reduce $H(X \mid Y)$ is high-cost noise. A 3-page packet that resolves the decision-critical ambiguity is the right unit of work.

### Channel capacity as decision capacity

```math
C = \max_{p(x)} I(X;Y)
```

AIRCA interpretation (the central analogy):

- Decision capacity $C$ is set by the weakest link in the loop: reviewer bandwidth, the institution's classification clarity, the AI tool's grounding reliability, the audit/review surface. AIRCA's higher-order claim — *answers are cheap, decisions are scarce* — is the AI-era statement that $C$, not $I(X;Y)$ per evidence packet, is now the binding constraint.

### Rate-distortion as the *Rank* tradeoff

```math
R(D) \;=\; \min_{p(\hat{x} \mid x):\ \mathbb{E}[d(X,\hat{X})] \le D}\; I(X;\hat{X})
```

AIRCA interpretation:

- *Rank* is a compression operation: take the alternatives and produce a shortlist (or a recommendation) at a defined distortion budget. The institutional question is: **which distortions are forbidden?** Acceptable distortion examples: dropping a marginally-worse alternative from the shortlist. Forbidden distortion examples: silently dropping an alternative the Ultimate Frame requires, omitting a stakeholder, hiding adverse evidence.

### Data processing inequality as the AIRCA boundary

If $X \to Y \to A \to \hat{A}$ is a Markov chain:

```math
I(X; \hat{A}) \;\le\; I(X;Y)
```

AIRCA interpretation (the structural rule):

- The committed action $\hat{A}$ cannot carry more information about the canonical decision variable $X$ than the *Inform*-stage evidence preserved. **No amount of polished commit-stage prose creates information that the channel did not deliver upstream.** This is why AIRCA insists on architecture-before-inform and inform-before-rank: each later stage is downstream in the Markov chain and cannot recover what the upstream channel dropped.

### Fano-style honesty at *Commit*

For a finite alternative set $\mathcal{A}$ and a committed action $\hat{A}$ with error probability $P_e$:

```math
H(X \mid \hat{A}) \;\le\; h_2(P_e) \;+\; P_e \log_2(|\mathcal{A}| - 1)
```

AIRCA interpretation:

- If residual decision uncertainty stays high, the probability of a wrong commit cannot be small. *Commit* should expose that — through stated assumptions, reversibility design, and review triggers — not paper over it with rhetorical certainty.

### Optional drift gauge (data-dependent)

```math
D_{\mathrm{KL}}(P_{\text{observed outcomes}} \,\Vert\, P_{\text{predicted outcomes}})
```

AIRCA interpretation:

- If post-decision outcome distributions are recorded, $D_{\mathrm{KL}}$ between predicted and observed becomes a candidate calibration / decision-quality signal. Use only with explicit baselines and zero-count smoothing; **not implemented in any AIRCA artifact today**.

## Integration implications

These are conceptual implications, not new doctrine:

1. **Decision capacity is a hard constraint, not a preference.** Capacity floors are set by reviewer bandwidth and classification clarity. Adding more AI-generated synthesis without raising the floor does not raise $C$.
2. **The Ultimate Frame is the *Architect* decision.** Naming the frame is exactly the Shannon step of defining source / channel / authority boundary. Skipping it is starting transmission without knowing what is being transmitted.
3. **Inform must justify volume by mutual information.** Long context packets that do not reduce $H(X \mid Y)$ are channel noise, not channel signal.
4. **Rank must declare its forbidden distortions.** Without that declaration, rate-distortion has no concrete meaning and compression silently drops what the frame would have preserved.
5. **Commit must respect residual uncertainty.** Fluent confidence is not lower error probability.
6. **Act preserves decision memory for future channels.** Provenance and outcome records are the redundancy that lets the next AIRCA loop detect drift.
7. **Review/Exception catches chaos-style cascades.** Small architecture-stage errors amplify through the AIRCA chain. Upstream correction is structurally cheaper than downstream rework.

## Safe design questions

For each AIRCA-style decision under consideration:

1. **Architect**: What is the authoritative source for this decision, and what Ultimate Frame governs it?
2. **Inform**: What evidence reduces $H(X \mid Y)$ for the decision-relevant variable, vs adds volume?
3. **Inform**: Where can channel noise enter (retrieval, summarization, ambiguous source, late-stage prompts)?
4. **Rank**: What distortions are tolerable in compression, and what distortions are forbidden by the frame?
5. **Commit**: What residual uncertainty remains, and is the reversibility/escalation design consistent with it?
6. **Act**: What provenance and outcome record will let the next loop measure drift?
7. **Review**: What error-correction path covers upstream architecture errors, not just downstream commit errors?

## Non-goals

- This note does not propose AIRCA as a Shannon theorem.
- This note does not promote AIRCA to flagship; LawFirm OS remains flagship in the public portfolio.
- This note does not modify LAIRCA / Logos doctrinal claims. Theological framing is upstream; this note only treats Shannon as a downstream reliability lens.
- This note does not introduce new artifact classes, ontology entries, or governance rules.

## References

Conceptual only.

- Claude E. Shannon, "A Mathematical Theory of Communication," *Bell System Technical Journal*, 1948.
- Thomas M. Cover and Joy A. Thomas, *Elements of Information Theory*, Wiley (especially rate-distortion and Fano's inequality).
- David J. C. MacKay, *Information Theory, Inference, and Learning Algorithms*, Cambridge University Press.
- For AIRCA / UAIRCA / LAIRCA semantics, derivations, and Ultimate Frame content: this repo's own canonical files. Shannon is not consulted for those.
