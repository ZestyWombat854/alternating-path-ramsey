# Formalization map

Source-to-Lean coverage map for the Sealed49 project. Practice adapted
from the formalization-map convention in jinshanmu/CrouzeixConjecture
(commit 9df0783).

## Source identity (pinned)

- **Statement of record**: `statement.md` — 47 lines, SHA-256
  `3560d2950a8b335e118be2fa94fcf165e2123e8fd07bfcac37e490f2d49e8a69`.
  In the evidence bundle this file sits at the repo root; it is
  byte-identical to the sealed run's pinned statement (task source:
  `data/sealed-49/statement.md`).
- **Proof of record**: `proof-final.md` — 598 lines, SHA-256
  `883c7d653e8f064a95d0b0ed0310c5e55d87f31580f08be39bd9bd340ef90e4a`
  (referee repairs marked `[REPAIR ...]`); its pre-repair original
  ships as `proof-original-with-errata.md` — 561 lines, SHA-256
  `dde673fa43b67b0513bae653d3f0d6fd41557358f4d87eda596d80e76ac74ffd`.
  Lean docstrings cite this file under its task-side name,
  `candidate-proof.md`; the lemma statements formalized here are
  identical in both forms (the repairs touch a `b = 1` lemma branch and
  a proof aside, neither formalized).
- **Toolchain**: Lean `leanprover/lean4:v4.30.0`; mathlib tag `v4.30.0`
  (rev `c5ea00351c28e24afc9f0f84379aa41082b1188f`), per `lean-toolchain`
  / `lakefile.toml` / `lake-manifest.json`.

Statuses: **proved** = checked proof term, in the axiom audit;
**defined** = faithful encoded object (fidelity independently checked in
`statement-audit.md`); **not formalized** = no Lean counterpart exists —
deliberately absent rather than stubbed (this project ships zero
placeholder proofs).

## Statement objects (statement.md, 47 lines)

| Source | Object | Lean declaration(s) | Status |
|---|---|---|---|
| lines 7–10 | vertex set `[m]`; the alternating sequence `s_{2t}=t`, `s_{2t+1}=a−1−t`; the path `P_a^alt` | `altSeqVal`, `Palt` (via `SimpleGraph.fromRel` over consecutive pairs) | **defined**, plus **proved** characterization `palt_adj_iff` (`x≠y ∧ (x+y=a−1 ∨ x+y=a)`) |
| line 15 | rotation `ρ(i)=i+1`, reflection `σ(i)=m−1−i`, the group `Dih(m)=⟨ρ,σ⟩` | `rhoPerm = finRotate`, `sigmaPerm = Fin.revPerm`, `Dih = Subgroup.closure {ρ,σ}` | **defined** (mathlib-source match confirmed in `statement-audit.md`) |
| line 22 | relabeled graph `γ(H)` | `actGraph γ H = H.comap γ.symm` | **defined** |
| lines 17–26 | "contains a Γ-copy" (first of the statement's two equivalent forms: the `(v,γ)`-pair form, `v` increasing) | `GammaCopy` (`Fin m ↪o Fin n` order-embedding) | **defined** |
| lines 27–31 | 2-colorings of `E(K_n)`; the number `R_dih` | one-graph convention (`G` = color 1, `Gᶜ` = color 2); `Rdih` via `Nat.sInf`; `Kgraph = ⊤` | **defined** |
| lines 33–47 | **the theorem**: `R_dih(P_a^alt, K_b) = 1+(a−1)(b−1)` for all `a≥4, b≥1` | — (would be `Main.lean`) | **not formalized** |

## Proof of record (proof-final.md, by part)

| Source | Claim | Lean declaration(s) | Status |
|---|---|---|---|
| Part 0 (lines 40–79) | `M_c`, `H_c` (`c ∈ Z/aZ`), mirror | `Mgraph`, `Hgraph`, `mirrorGraph` | **defined**, plus **proved** `mgraph_adj_iff`, `hgraph_adj_iff` |
| Part 0, Lemma 0.1 | `P_a^alt = H_{a−1}` for `a ≥ 3` | `palt_eq_Hgraph` | **proved** — by a direct adjacency characterization, a different but equivalent route to the source's cardinality count |
| Part 0, Lemma 0.2 (computational core) | `ρ(H_c) = H_{c+2}`, `σ(H_c) = H_{−3−c}` | `actGraph_rho_hgraph` (hyp `2 ≤ a`), `actGraph_sigma_hgraph` (no hyp) | **proved** — hypotheses weaker than the source's blanket `a ≥ 3`; strict generalizations |
| Part 0, Lemma 0.2 (remainder) | extension from the two generators to all of `Dih(a)`; the index orbit is all of `Z/aZ`; exactly `a` distinct graphs; stabilizer order 2 | — | **not formalized** |
| Part 1 (lines 80–108), Theorem 1 | lower bound `R_dih ≥ 1+(a−1)(b−1)` (block-partition construction) | — | **not formalized** |
| Part 2 (lines 109–145), Lemma 2 | degree reduction to a min-degree core | — | **not formalized** |
| Part 3 (lines 146–271), Lemma 3.1 | rank 0's unique edge; deleting it gives `mirror(P_{p−1}^alt)` | `realizes_palt_succ_iff` (hyp `1 ≤ q`, i.e. `p ≥ 2`, matching the source) | **proved** — in the equivalent pointwise-adjacency form; see "Renamings and reformulations" below |
| Part 3, Lemmas 3.1b, 3.2 | pivot decomposition | — | **not formalized** |
| Part 4 (lines 272–368) | the quantities `P(m)`, `Q(m)` (longest alternating chains) | `PWitness`/`P`, `QWitness`/`Q` via `Nat.findGreatest`; supporting `Realizes`, `degreeOn`, `minDegreeOn` | **defined** — directly over the "largest p with a witness tuple" predicate, not via Lemma 4.1's recursion |
| Part 4, Lemmas 4.1, 4.2 | the windowed recursion for `P(m)`; window transfer | — | **not formalized** |
| Part 5 (lines 369–463), Theorem 5 + Cor 5.1 | **Aggregate Sum Theorem** `Σ_m [P(m)+Q(m)] ≥ 2·E(G)`; averaging corollary | — | **not formalized** |
| Part 6 (lines 464–503), Theorem 6 | **Extraction Lemma**; assembly of the upper bound; the main theorem | — | **not formalized** |

## Renamings and reformulations (all disclosed)

- `realizes_palt_succ_iff` states Lemma 3.1 as a pointwise iff — "a
  `(q+1)`-tuple realizes `P_{q+1}^alt` iff its endpoints are adjacent
  and its tail realizes `mirror(P_q^alt)`" — rather than as the
  source's induced-subgraph equality. This is the exact shape in which
  the source's own Lemma 4.1 proof invokes Lemma 3.1; the independent
  audit (`statement-audit.md` item 16) verified the two are the same
  fact and ruled the labeling honest. The carrier is generalized from
  increasing tuples to arbitrary maps; the generalization is unused.
- A "2-coloring of `K_n`" is one `G : SimpleGraph (Fin n)` (color 1),
  with color 2 as `Gᶜ` — a bijection with 2-colorings, no generality
  lost (`statement-audit.md` item 9).
- `Palt` is built from the sequence `altSeqVal`, not from `H_c`;
  Lemma 0.1 (`palt_eq_Hgraph`) is the proved bridge between the two.

## Trust

Axiom audit: `AxiomAudit.lean` + `AXIOM_AUDIT.md`. Independent
statement-fidelity audit: `statement-audit.md` (verdict
FAITHFUL-WITH-NOTES, 16/16 items FAITHFUL, zero deviations).
Authoritative check: `./verify.sh`.
