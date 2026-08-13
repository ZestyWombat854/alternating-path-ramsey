# Round 2 synthesis — SEALED49

7 agents launched (E1-E7), all fresh/independent, briefed with the full
statement plus the round-1-established EL reduction as shared context (this
was legitimate since the reduction is proven, not "a favored approach" —
see registry.md). F4 from round 1 (agentId af7fc81a8583ec3da) still has not
reported; folded in separately whenever it arrives, not backdated here.

## Headline result: EL is now reduced to one narrow, precisely-stated gap

**E3 nearly closed the Extraction Lemma.** New machinery:

- **Pivot Decomposition (E3 Lemma 1, fully proved, all a,c):** every H_c
  splits around pivot vertex p=c+1 into a left block realizing P_p^alt
  exactly (on {0,...,p-1}) and a right block realizing mirror(P_q^alt)
  exactly (on {p+1,...,a-1}, q=a-1-p), with the pivot's only two H_c-edges
  going to the two OUTER extremes (0 and a-1) of the whole tuple, not to
  its immediate neighbors. This is new structure beyond anything in round 1.

- **P(m), Q(m):** for m in W, P(m) = longest left-chain (below m, ending in
  an edge to m) realizing P_p^alt for its own length; Q(m) = longest
  right-chain (above m, ending in an edge to m) realizing mirror(P_q^alt).

- **Reduction (E3 Lemma 3, fully proved):** if some m has P(m)+Q(m) >= a-1,
  EL holds (splice the two chains at m via the Pivot Decomposition run in
  reverse).

- **Near-miss (E3 Lemma 4, fully proved):** max_m[P(m)+Q(m)] >= delta(G)-1
  ALWAYS, by a clean induction on |W| (remove any vertex, degrees drop by
  at most 1, recurse).

- **The gap, confirmed real (not a proof artifact) by exhaustive
  computation at a=4:** the sharp truth needed is max_m[P(m)+Q(m)] >=
  delta(G), i.e. ONE MORE than Lemma 4 gives. E3 isolated exactly where the
  induction loses its "+1": when deleting vertex v costs the bound, it's
  because v has a neighbor u with deg(u) = delta exactly (a "tight"
  vertex). Working with G edge-minimal (WLOG), let T = {tight vertices}.
  Deleting v in T with no T-neighbor costs nothing (safe case, closes with
  no loss). THE RESIDUAL, UNRESOLVED CASE: every vertex of T has a
  T-neighbor, i.e. G[T] has minimum degree >= 1 (T induces no isolated
  vertices). E3 tried several natural fixes (paired removal, seeding at a
  T-T edge, nested induction) and could not close this case, but the gap is
  now about as narrow as a remaining lemma can be.

**THIS IS THE NEW SINGLE TARGET for round 3**, stated with full precision:

  For every graph G on a finite linearly ordered set W with delta(G)>=1,
  in the case where G is edge-minimal subject to its degree floor and the
  degree-minimum vertex set T induces a graph of minimum degree >= 1
  (every tight vertex has a tight neighbor): some m in W has
  P(m) + Q(m) >= delta(G) (not just delta(G)-1).

Root's own analysis while processing this (recorded for round 3's benefit,
NOT independently verified, offered as a lead not a result): P(m) and Q(m)
as E3 defined them require the chains to realize the SPECIFIC canonical
shape (P_p^alt / its mirror) exactly — more rigid than "any orbit shape
with the right endpoint role." Relaxing P(m)/Q(m) to allow ANY compatible
H_c'-type shape at the appropriate smaller modulus (not just the rigid
identity/mirror pair) might supply exactly the missing flexibility in the
tight-tight-edge residual case, analogous to how the original problem
needed flexibility across all c rather than a single fixed shape. This is
a hypothesis for round 3 to test, not a proven direction.

## E1, E4: two independent, rigorous impossibility results (define the
## boundary of what CANNOT work — do not revisit without new ideas)

- **E1 (global counting):** Theorem B — a disjoint union of K copies of
  K_a sits exactly at EL's degree threshold, yet the AVERAGE badness over
  ALL C(n,a) tuples converges to the maximum possible value a (not just
  short of threshold) as K grows, via a "rainbow tuple" argument. Survives
  adversarial reordering and passage to connected sparse examples. No
  order-based or cardinality-based averaging scheme can prove EL.
- **E4 (probabilistic):** an explicit "long-range block" construction
  (LRB(a,m,K): clique blocks with matchings reaching K blocks forward)
  sits at the EL threshold, has bounded clique number (no trivial K_a
  shortcut), and its UNIQUE witnesses have spread growing unboundedly with
  K — provably invisible to any bounded-reach sampling model (uniform
  subsets, fixed blocks, sliding windows of any fixed size, locally-
  adaptive variants). No bounded-reach probabilistic method can prove EL.
- Both independently conclude: the correct mechanism must follow G's
  actual adjacency structure with UNBOUNDED reach — exactly what the
  peeling/induction machinery (E2, E3, E6, and round 1's F2/F3/F5) already
  aims at. This closes off "statistical" approaches to EL as a category,
  not just as individual failed attempts.

## E2: full resolution of an entire natural extremal family, plus a
## striking complementarity with E7

- **Bandwidth Theorem (E2 Theorem 3, fully proved, all a):** the minimum
  possible "jump" (rank-distance) among all a orbit shapes is exactly
  ceil((a-1)/2), achieved uniquely at c* = floor((a-3)/2).
- Using this, **E2 completely proves EL for the entire natural
  (a-1)-regular circulant/banded graph family** (both parities of a,
  explicit witness constructions) — a full sub-case now closed, not just
  tested.
- E2 also sharpened the Survival Lemma to an exact iff-criterion (Theorem
  2, via independent sets in the a-cycle — strictly sharper than the
  original pigeonhole threshold).
- **Complementarity with E7 (see below):** E2's circulant family (only
  short-range edges) is resolved via the MINIMUM-bandwidth shape H_c*.
  E7's bipartite-block family (only long-range/cross-split edges) is
  resolved via the two shapes at the OPPOSITE extreme, {a-2,a-1}. These
  are two structurally opposite regimes, each closed by a different
  specific shape. FLAGGED AS A PROMISING SYNTHESIS LEAD for a future
  round: a dichotomy argument ("G has enough short-range structure
  somewhere -> use c*; else enough long-range/bipartite structure
  somewhere -> use {a-2,a-1}") might cover all cases. Not attempted yet.
- E2's own remaining gap (showing the circulant family is a genuine global
  minimizer, via a compression/exchange argument) stalled on the same kind
  of degree-floor-violation issue as E3's Lemma 4 gap — worth noting the
  two gaps may be related.

## E5: decisively refutes F1's round-1 "2 shapes suffice" claim

Five explicit counterexamples (a=4,5 exhaustively proved by full graph
enumeration; a=6,7,8 verified single instances) where EL's conclusion
holds via some H_c but NEITHER H_{a-1} (Id_a) NOR H_{a-2} (Delta_a) works.
F1's narrower claim is FALSE. Secondary, well-caveated finding: the
minimal universal-per-a subset size grows slowly with a (2 at a=4-6, 3 at
a=7-8, 4 at a=13-20, open at a=27) rather than staying fixed — evidence,
not proof, and explicitly flagged by E5 as fragile (several early
"confirmed" candidates broke under harder adversarial testing). The
"full flexibility across all c" formulation five round-1 agents used
remains the safe, justified default.

## E7: exhaustive resolution of the bipartite-block family + Survival
## Lemma is provably not tight

- Exhaustively checked (not sampled) ALL interleavings of the
  disjoint-K_{a-1,a-1}-blocks family, a=4..12: realizing ANYTHING there is
  exactly equivalent to realizing BOTH H_{a-2} and H_{a-1} (never just
  one, never neither). Minimum realized-shape-count found anywhere in
  extensive adversarial search: exactly 2 (never 0).
- In this same extremal graph, EVERY increasing a-tuple exceeds the
  Survival Lemma's pigeonhole threshold by 4-6x, yet EL still holds — the
  missing pairs are numerous but not evenly spread across candidate
  shapes. Proves (a third independent way, after E1 and E4) that pure
  counting cannot be the whole mechanism; positional/structural alignment
  is essential.
- Combined with E5: no fixed subset of shapes can EVER work universally,
  since E7's extremal graph needs exactly {a-2,a-1} and nothing else,
  while E5's counterexamples need OTHER shapes with {a-2,a-1} both
  failing — the intersection is empty. Full flexibility across all c is
  not just currently-unavoidable but PROVABLY necessary.

## E6: rigorous impossibility of its own literal assigned mechanism, plus
## reusable structure

- **Corollary 4 (fully proved):** no single H_c has BOTH rank 0 and rank
  a-1 as its two path endpoints (for any a>=4) — so "peel both global
  extremes of W toward one fixed target c" is combinatorially impossible
  as literally stated. Honest, clean negative result specific to E6's
  assigned mechanism.
- Showed the natural repair collapses back to the already-known
  alternating min/max construction (not a new mechanism) and precisely
  isolated what's missing: a potential function handling "gap-fill" and
  "c-switching" repairs during a stall, with the open risk being whether
  such repairs cascade.
- Reusable new lemmas: non-crossing chord decomposition of each M_c
  (Lemma 2); explicit path-traversal formula for every H_c generalizing
  the peeling identities to all c, not just c=a-1 (Lemma 3).

## Metric-reconciliation note (avoid confusion in future rounds)

E2 section 6 and E7 Task 1 both report "minimum realized count" numbers
that look inconsistent (E2: growing with n, e.g. 5,6,7,8; E7: flat at 2).
They are measuring DIFFERENT quantities: E2 tracked TOTAL realized (T,c)
incidence pairs (which naturally scales with graph size/vertex count), E7
tracked the number of DISTINCT c-values realized ANYWHERE in the graph
(the quantity that actually matters for EL, since EL only needs one c to
work somewhere). No actual conflict.

## Registry status changes

E1, E4 -> mechanism-class CLOSED (rigorous impossibility proofs; see
blocked.md). E2 -> PROMISING, full sub-case (circulant family) DONE,
compression-argument gap open. E3 -> PROMISING, MOST ADVANCED: complete
proof chain modulo one precisely-isolated residual-case lemma. E5 ->
DONE (adjudication complete, definitive answer). E6 -> PROMISING but its
literal assigned mechanism is proved impossible; contributed reusable
structure. E7 -> ongoing support, delivered decisive complementary data
(bipartite-block family, Survival Lemma non-tightness). F4 -> still
PENDING.

## Round 3 plan

Concentrate heavily on closing E3's exact residual-case gap (see above) —
this is now the single most promising path to a complete proof, with
several genuinely different sub-approaches assigned (shape-flexibility
relaxation, direct structural analysis of the tight-vertex-induced
subgraph, paired/simultaneous removal, and an explicit attempt to adapt
Erdos-Gallai's own rotation-to-cycle trick, which the pivot-decomposition
structure now closely resembles). One agent continues computational
support, targeted at this specific gap. E2's dichotomy lead (circulant
c* vs bipartite {a-2,a-1}) and E2's own compression-argument gap are held
in reserve as a second track if the E3 track stalls, not dropped.
