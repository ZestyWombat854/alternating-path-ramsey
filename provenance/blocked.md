# SEALED49 blocked routes

A route is listed here when it stalls at a theorem-strength missing lemma.
Reopen only when a new agent proposes a materially new mechanism, invariant,
or construction (recorded under "reopen condition").

## After round 1

These are narrow MECHANISMS shown insufficient for the Extraction Lemma
(EL), not whole families — the families that found them (F2,F3,F4,F5,F6,F7)
remain PROMISING/converged and should not repeat these specific mechanisms
without a genuinely new idea attached.

- **Single fixed gamma (literal P_a^alt only, no rotation/reflection
  flexibility).** BLOCKED. F4 gave an explicit coloring (a=4,b=3,n=7)
  where identity fails but a rotation succeeds. Reopen condition: n/a,
  this is a permanent structural fact, not a stalled lemma — any EL proof
  must use the flexibility across c.
- **Local density/connectivity on a single fixed a-subset** (as the sole
  mechanism, e.g. "this subset is connected/2-connected so it must realize
  some H_c"). BLOCKED. F6 (4-cycle) and F2 (triangle+pendant) gave explicit
  small counterexamples. Reopen condition: an argument that aggregates
  across MANY overlapping subsets, or a genuinely global invariant, not a
  per-subset local claim.
- **Naive single-pivot Chvátal-style induction on b** (split by one
  vertex's color-2-degree, recurse on both sides as independent smaller
  instances of the SAME theorem with no shared structure exploited).
  BLOCKED for a,b>=3. F7 proved (root-verified independently) an exact
  algebraic shortfall of (a-2)(b-2) vertices versus the target bound — not
  "unexplored," numerically incompatible with the linear target as stated.
  Reopen condition: a version that extracts and reuses EXTRA structure
  between the two cases (e.g. color-1 edges from the pivot into both sides
  jointly), not two independent black-box recursive calls.
- **Naive Turán-edge-count peeling to a min-degree subgraph** (repeatedly
  delete low-degree vertices, standard degeneracy argument). BLOCKED as
  the route to a MIN-DEGREE hypothesis with the tight constant. F5 showed
  it costs a factor of ~2 versus the true threshold. Reopen condition:
  none needed — F5 already supplied the fix (Erdos-Gallai's sharp
  longest-path bound, proved from scratch, gives the tight constant
  directly). Use Erdos-Gallai, not naive peeling, whenever this edge-count
  route is wanted.
- **Single-vertex "large forward/one-sided-degree" as an anchor for a
  direct construction.** BLOCKED. F7 gave an explicit interval/proximity
  graph where every vertex's forward-degree is capped far below what such
  an argument needs, yet alpha(G) can still be forced to b-1. F2 similarly
  found the EL-witnessing copy need not be anchored in any single tight
  vertex's neighborhood. Reopen condition: an argument using SEVERAL
  vertices' structure jointly, not one vertex's degree in one direction.
- **RETRACTED (was never a real result): F7's "Obstruction B"** — claimed
  K_{a-1,a-1} (complete bipartite, sorted halves) defeats every dihedral
  realization. FALSE. Root found explicit counterexamples a=4..9 by direct
  computation. Do not cite or rely on this claim.

## After round 2

- **Global counting/averaging over any order-or-cardinality-defined tuple
  family** (uniform over all C(n,a) tuples, any reweighting keyed only to
  position/order, not to G's actual edges). BLOCKED PERMANENTLY (this is a
  proved impossibility, not a stalled attempt — see E1's Theorem B).
  Disjoint union of K copies of K_a sits at EL's exact degree threshold
  (delta=a-1) yet average badness over ALL tuples converges to the MAXIMUM
  possible value (not just short of the pigeonhole threshold) as K grows;
  survives adversarial reordering and passage to connected sparse
  examples. Reopen condition: only if someone finds a weighting scheme
  that is genuinely G-adjacency-aware without presupposing the witness
  already found (E1 showed this collapses into the structural/graph-
  traversal approach, i.e. stops being a "counting" argument at all).
- **Bounded-reach probabilistic sampling models** (uniform random subset,
  fixed contiguous blocks, sliding windows of any FIXED size, locally-
  adaptive models that only inspect a bounded neighborhood). BLOCKED
  PERMANENTLY — proved impossibility, see E4's Theorems 1-3. The
  LRB(a,m,K) construction (clique blocks + matchings reaching K blocks
  forward) sits at EL's threshold, has no trivial K_a shortcut, and its
  unique witnesses have spread growing unboundedly with K, invisible to
  any model committing in advance to a bounded window/reach. Reopen
  condition: none — E4 showed any fix requires the sampling distribution
  to already know where the witness is, which is circular.
- **Peeling both global extremes of W simultaneously toward one fixed
  target c** (E6's literally-assigned mechanism). BLOCKED — proved
  impossible for any a>=4 (E6 Corollary 4: no single H_c has both rank 0
  and rank a-1 as its two path endpoints). Reopen condition: none needed;
  E6 already showed the natural repair collapses into the already-known
  (and already-stalling) alternating min/max construction, not a new
  mechanism.
- **The 2-shape claim {Id_a, Delta_a} suffices universally.** REFUTED (not
  merely blocked) — see E5, 5 explicit counterexamples a=4..8, two of them
  exhaustive complete-graph proofs. Do not revisit; "full flexibility
  across all c" is now PROVED necessary (E5 + E7 jointly: no fixed subset
  of shapes can ever work for every graph, since different extremal graphs
  provably need disjoint shape-subsets).
- **Plain edge-count/degeneracy-peeling as a route to a min-degree
  hypothesis with the tight constant**, carried over from round 1, remains
  blocked; still use Erdos-Gallai instead.

## RESOLVED in round 3 (was: open target, see registry.md ROUND 2 UPDATE)

E3's residual-case gap (for G edge-minimal with delta(G)>=1, in the case
where the degree-exactly-delta vertex set T induces a subgraph of minimum
degree >= 1, prove some m in W has P(m)+Q(m) >= delta(G) rather than just
delta(G)-1) is RESOLVED -- not by closing that specific case, but by G4's
Aggregate Sum Theorem, which proves the needed conclusion (max_m[P(m)+
Q(m)] >= delta(G)) unconditionally, for every graph, with no case split
into safe/residual/regular at all. The narrower case-based framing this
round was organized around turned out to be unnecessary once the right
invariant (a SUM, not a max, tracked through the induction) was found.
See registry.md ROUND 3 UPDATE and candidate-proof.md.

## Unresolved (not blocked, informational leads for round 3+)

- E2/E7 complementarity: circulant/short-range graphs resolved via the
  min-bandwidth shape c* (E2); bipartite/long-range graphs resolved via
  the opposite-extreme shapes {a-2,a-1} (E7). A dichotomy argument
  covering both regimes has not been attempted. Held in reserve as a
  second track if the E3 residual-case route stalls.
- E2's own gap (is the circulant family a genuine global minimizer? — a
  compression/exchange argument stalled on a degree-floor issue similar in
  flavor to E3's gap) — not separately assigned in round 3 but may turn
  out to be the same underlying obstruction; worth revisiting if E3's
  route closes and a cleaner writeup is wanted, or if E3's route stalls
  further.
