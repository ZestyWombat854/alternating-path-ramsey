# Referee B report — SEALED49

Reviewer: external referee B (fresh agent, no connection to the producing
team). Read exactly two files: `data/sealed-49/statement.md` and
`data/sealed-49/candidate-proof.md`. No other file in the repository was
read for mathematical content (see the format-only exception noted at the
end of this report). No web access. Date: 2026-08-13.

**Overall verdict: CONFIRMED.** No bug found in the proof as currently
written, after (1) a full independent line-by-line re-derivation of every
lemma from the stated definitions, prioritizing the attack surfaces named
in the brief, and (2) six independent computational verification scripts
built from scratch, none of which found a discrepancy. One cosmetic
arithmetic erratum was found in a supporting aside (does not affect any
downstream conclusion; detailed below). One requested verification cell
was only partially completed; see the NOT DONE block under §3.

---

## 1. Statement fidelity

The proof's Theorem 7 states exactly the pinned claim — "For all integers
a>=4 and b>=1: R_dih(P_a^alt,K_b)=1+(a-1)(b-1)" — with no shifted
quantifiers or silently narrowed range.

The one fidelity point worth real scrutiny: statement.md's Γ-copy
definition requires only that H's *edges* map to color-r pairs under
`v∘γ` (no induced-subgraph condition on H's non-edges). The proof's
internal notion, "realizing H_c entirely in E(G)" (used throughout Parts
2–6), is the same non-induced notion, and I checked the *exact* algebraic
translation at the point where the two languages meet (end of Theorem
7's proof): "for every edge {i,j} of H_c=γ(P_a^alt), {v_i,v_j} has color
1" unwinds — via H_c's edge set being `{{γ(i),γ(j)}:{i,j}∈E(P_a^alt)}` —
to exactly statement.md's "{v_{γ(i)},v_{γ(j)}} has color r for every
edge {i,j} of H". This is a precise match, not an approximate one.
Verdict: **CONFIRMED**, no drift between the proof's working language and
the pinned definitions.

## 2. Lemma-by-lemma adversarial re-derivation

Every lemma below was re-derived by hand from the definitions (not by
checking the proof's algebra step matches itself), then cross-checked
against the written proof.

- **Lemma 0.1** (P_a^alt = H_{a-1}): re-derived the edge-sum argument
  independently; confirmed against both worked examples in statement.md
  (a=4, a=5). **CONFIRMED**.
- **Lemma 0.2** (orbit size a, stabilizer 2): re-derived the τ₁(c)=c+2,
  τ₂(c)=-3-c index action and the odd/even parity-sweep argument by hand;
  correct. One terse spot: "disjointness of the M's forces
  {c,c+1}={c',c'+1}" skips the (true, easy) fact that every M_c is
  nonempty for a>=3 — needed to make "forces" rigorous. Not a bug, just
  under-argued. **CONFIRMED** (with a noted terseness, not an error).
- **Theorem 1** (lower bound, a>=2,b>=1): the block-coloring construction
  and the "connected graph has an edge crossing every nontrivial
  partition" argument are both correct and standard. **CONFIRMED**.
- **Lemma 2** (degree reduction): the b=1 case ("take W = any single
  vertex (vacuous)") looks wrong on first read — a lone vertex has degree
  0, not >=a-1 — until you notice n=1 when b=1, and a color-2 K_1 is
  *trivially* satisfied by any single vertex (0 edges to check), so the
  hypothesis "no color-2 K_b" is unsatisfiable at b=1, making the lemma
  vacuously true. Confirmed this reading is correct (§3, general
  mechanism test, not hard-coded). The b>=2 degeneracy-ordering /
  greedy-(a-1)-coloring argument is a standard, correctly-executed
  argument. **CONFIRMED**.
- **Lemma 3.1** (rank-0 peeling): conclusion re-derived and correct.
  Found one arithmetic slip in the supporting parenthetical: solving
  s_{2j+1}=p-1-j=0 gives j=p-1, so the out-of-range position is
  k=2j+1=**2p-1**, not the stated "2p-3". This does not affect the
  conclusion — 2p-1 exceeds p-1 for all p>=1 (even more robustly than the
  stated 2p-3, which only exceeds p-1 for p>=3, hence the proof's own
  "p=2 checked directly" patch). Nothing downstream cites this specific
  number. **CONFIRMED, cosmetic erratum noted, not repaired** (per
  instructions, bugs are reported, not silently fixed).
- **Lemma 3.1b** (far-endpoint trimming, e=floor(p/2)): re-derived both
  parity cases of s_{p-1}=e directly; correct, including "occurs only at
  the last position" and the order-isomorphism relabeling. **CONFIRMED**.
- **Lemma 3.2** (pivot decomposition, parts a/b/c): this is where three
  earlier audit rounds found real bugs (per the provenance note), so I
  re-derived it fully independently rather than checking the given
  algebra. Part (a): confirmed via the mod-c/mod-p wraparound argument.
  Part (b): re-derived the σ=mirror∘τ identity from scratch; independently
  re-derived the "bounded-sum/no-wraparound" range argument
  (i+j∈[1,2q-3] excludes both the mod-a and mod-q wraparound points given
  a>=q+2) and confirmed it holds, including the q∈{0,1} vacuous
  boundary. One point I checked carefully because it looked suspicious:
  at q=0 the stated reduction "-p-2 mod a = a-p-2 = q-1" produces the
  *non-canonical* representative -1 rather than a-1 — but since H_c is
  only ever defined up to congruence mod a (Part 0: "for c in Z/aZ"), any
  integer representative denotes the same graph, so this is not an error,
  just a non-canonical label. Part (c) (pivot's edges, degenerating to
  one edge when q=0): confirmed. **CONFIRMED** for all three parts.
- **Lemma 4.1** (windowed recursion, the "corrected" form): re-derived
  from Part 4's raw definition using Lemma 3.1's peeling fact, independent
  of the proof's own derivation. The equivalence "(q+1)-tuple witnesses
  P(m) with first element l" ⟺ "Q_{(l,m)}(l)>=q" checks out exactly, and
  the "+1 attached per-candidate before taking max with the {0} floor"
  placement (the thing Audit 1 fixed) is the one that is actually
  necessary — confirmed both by hand and exhaustively (§3). **CONFIRMED**.
- **Lemma 4.2** (reduction): re-derived the clipping-via-3.1b argument
  (preserves rank 0, terminates at length p'>=1 whenever nontrivial, so
  never needs the undefined-by-statement.md P_0^alt/P_1^alt edge case in
  a load-bearing way) and the pivot assembly, including the p'=0 (⟹q'=a-1)
  degenerate branch via direct citation of Lemma 3.1. Note: Lemma 4.2
  reuses the symbols "p,q" for both P(m)/Q(m) *values* and, after
  clipping, as Lemma 3.2's own pivot parameters — a notational collision
  that could confuse a reader but is not incorrect (the correspondence
  p'↔Lemma 3.2's p, c=p'-1, is made explicit). **CONFIRMED**.
- **Theorem 5** (Aggregate Sum): the most complex and highest-value part
  of the proof, so I reconstructed the entire induction independently —
  Steps A through E — rather than verifying the given algebra in place.
  Step A (P unaffected by removing the max vertex M, Q monotone and
  exactly-equal off N(M)): confirmed. Step B (the windowed quantity f(i)
  really does equal both "candidates restricted to {w_{i+1..d}}" and the
  genuinely-windowed P_{(w_i,M)}(M), because G-adjacency itself does the
  candidate filtering either way): this is the subtlest point in the
  whole proof and I verified it explicitly by hand — confirmed, no gap.
  Step C (elementary max-vs-sum fact): confirmed trivially. Step D (the
  d=0 isolated-vertex base case, and the d>=1 telescoping sum): both
  reconstructed independently and match exactly, including the
  index-shift `sum_{i=1}^d f(i) = (d-1)+sum_{i=1}^{d-1}M_i` step. Step E
  (assembly, Q_G(M)=0): confirmed. **CONFIRMED** — I found no error
  anywhere in Part 5, despite treating it as the highest-suspicion target
  going in.
- **Corollary 5.1, Theorem 6, Theorem 7**: averaging argument, and the
  final assembly into the main theorem, both confirmed as stated, with
  the H_c↔Dih-copy translation checked precisely (§1). **CONFIRMED**.

## 3. Independent computation

All code in `code/referee-sealed49-B/`, all outputs in
`data/referee-sealed49-B/`. `defs.py` implements P_a^alt, Dih(a),
γ(H), and Γ-copy checking **from statement.md's definitions only** (not
via the proof's H_c/mirror machinery); it was validated against both of
statement.md's own worked examples (a=4, a=5) before use.

- **Orbit/stabilizer (task 3a)** — `verify_orbit_stabilizer.py`: direct
  group-action computation (not H_c-based), a=3..25, both parities.
  Reproduces the a=3..14 sanity anchor exactly and extends it: orbit
  size = a, |Stab| = 2, in all 23 cases. **PASS**.
- **R_dih exhaustive small cells (task 3b)** — `verify_R_dih_small.py`:
  vectorized brute force (not a SAT solver — "exhaustive or own-encoded
  SAT" per the brief; exhaustive was chosen as the stronger, solver-free
  option) over **every** 2-coloring of K_n, using the orbit-based
  Γ-copy check built from statement.md only. Both directions checked at
  each cell: zero avoiding colorings at n (upper bound), >=1 avoiding
  coloring at n-1 (lower bound). Ran in under 1 second total:

  | (a,b) | n | upper: bad colorings at n | lower: bad colorings at n-1 |
  |---|---|---|---|
  | (4,2) | 4 | 0 / 64 | 1 / 8 |
  | (4,3) | 7 | 0 / 2,097,152 | 10 / 32,768 |
  | (5,2) | 5 | 0 / 1,024 | 1 / 64 |
  | (6,2) | 6 | 0 / 32,768 | 1 / 1,024 |
  | (7,2) | 7 | 0 / 2,097,152 | 1 / 32,768 |

  All five cells confirm R_dih=1+(a-1)(b-1) exactly. The b=1 degenerate
  case was additionally checked **through the same general (non-special-
  cased) code path** at a=4, n=0,1,2: bad_count=1 at n=0, 0 at n=1,
  matching R_dih(P_4^alt,K_1)=1. **PASS**.

  ```diff
  - ===== NOT DONE =====
  - I did NOT complete a full two-sided (upper+lower, exhaustive-or-SAT)
  - verification at (5,3) (n=9, 2^36 colorings — infeasible by brute
  - force within the politeness budget; no actual SAT solver was used as
  - the alternative). I substituted a partial check: Theorem 1's explicit
  - lower-bound construction was directly verified to avoid both targets
  - at (5,3), (4,4), and (6,3) (n up to 10), which confirms the LOWER
  - bound only at those three cells, not the upper bound.
  - WHAT IT WOULD CHANGE: if the upper bound failed specifically at
  - (5,3) — i.e. some coloring of K_9 avoided both targets — that would
  - be a direct counterexample to the theorem. I consider this low risk
  - given the upper bound was confirmed exhaustively, with zero
  - exceptions, at five other cells including the adjacent (4,3) and
  - (5,2), and given the fully independent re-derivation of Theorem 7's
  - general argument in §2 found no step that could plausibly hold at
  - those cells while failing at (5,3) specifically — but it is not
  - mechanically checked, and the task asked for it "if feasible."
  ```

- **P(m)/Q(m) and Aggregate Sum, exhaustive to n=6 (task 3c)** —
  `verify_PQ_aggregate.py`: two independent implementations — brute force
  straight from Part 4's definition, and Lemma 4.1's stated recursion,
  coded independently from each other — cross-checked on **every vertex
  of every one of 33,868 labeled graphs on [n], n=0..6** (all degenerate
  cases — empty graph, isolated vertices, n<=1 — included by
  construction, since the sweep is exhaustive, not sampled). Zero
  mismatches. Theorem 5 (sum[P+Q]>=2|E(G)|) and Corollary 5.1
  (max[P+Q]>=delta(G)) both hold on all 33,868 graphs, zero violations,
  minimum observed slack 0 (tight at the trivial n=1 base case, as
  expected). Ran in 1.1 seconds. **PASS**.
- **Extraction Lemma, end-to-end (bonus, beyond the literal ask)** —
  `verify_extraction.py`: for a=4, checked **directly** (via the
  statement.md-only orbit checker, bypassing the P/Q machinery entirely)
  that every graph on n<=6 with delta(G)>=3 actually contains a Dih(4)-
  copy of P_4^alt as a subgraph. 1,885 such graphs exist among n=4..6;
  zero failures. **PASS**.
- **ρ(H_c)=H_{c+2}, σ(H_c)=H_{-3-c} (supporting Lemma 3.2(b) and Lemma
  0.2)** — `verify_rho_sigma_action.py`: checked via two independent
  codepaths (H_c from Part 0's raw definition, ρ/σ as statement.md's own
  generators via defs.py), a=3..25, all c: 322 pairs, zero mismatches.
  **PASS**.
- **Lemma 0.1, 3.1, 3.1b, 3.2, pivot decomposition (priority attack
  surface: mod-a arithmetic, parity split, pivot boundary)** —
  `verify_lemmas_part3.py`: H_c/mirror coded independently from Part 0/3's
  definitions. Lemma 0.1 for a=3..20; Lemma 3.1, 3.1b for p=2..20; Lemma
  3.2 (all three parts) for a=3..20, every c in {0,...,a-2} (189 pairs,
  covering the q=0 pivot-degeneration boundary at every a). Zero
  mismatches anywhere. **PASS**.

Format note: to append the required NOTEBOOK.md entry and
token-ledger.csv row in the existing schema, I checked only the
structural format (tail of NOTEBOOK.md, header comments and a few
numeric rows of token-ledger.csv) via shell, not the Read tool, and did
not read any research content beyond the two assigned files.

## 4. Verdict summary

| Part | Verdict |
|---|---|
| Statement fidelity | CONFIRMED |
| Part 0 (orbit/stabilizer) | CONFIRMED |
| Part 1 (lower bound) | CONFIRMED |
| Part 2 (degree reduction) | CONFIRMED |
| Part 3 (peeling, trimming, pivot decomposition) | CONFIRMED (1 cosmetic erratum, no effect) |
| Part 4 (P/Q recursion, reduction) | CONFIRMED |
| Part 5 (Aggregate Sum Theorem) | CONFIRMED |
| Part 6 (Extraction, main theorem) | CONFIRMED |
| **Overall** | **CONFIRMED** |

No bug found; no repair performed or needed. The one erratum (Lemma 3.1's
proof: "k=2p-3" should read "k=2p-1") is reported, not silently fixed,
per instructions — it is inconsequential to the proof's validity.
