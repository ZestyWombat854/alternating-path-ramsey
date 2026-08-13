# Referee A report — sealed-49

External referee, blind to referee B and to all other run files. Read only
`data/sealed-49/statement.md` and `data/sealed-49/candidate-proof.md`. Date
2026-08-13.

Claim under review: R_dih(P_a^alt, K_b) = 1+(a-1)(b-1) for all a>=4, b>=1.

Status: COMPLETE. Overall verdict: CONFIRMED, modulo one non-fatal bug in
Lemma 2's b=1 case (see Part 2 and Overall verdict below).

## Statement fidelity

Proof re-derives all definitions (P_a^alt, Dih(a), Gamma-copy, R_dih)
matching statement.md verbatim in substance; no silent quantifier shift.
Proof proves both directions for a>=4, b>=1 as pinned (lower bound actually
proved for a>=2, a superset). Sequence example for P_4^alt in the proof's
own recap matches statement.md's a=4 example. **Verdict: CONFIRMED.**

## Part 0 (orbit of P_a^alt: Lemma 0.1, 0.2)

Lemma 0.1 (P_a^alt = H_{a-1}): direct edge-sum computation on the defining
sequence; checks out by hand (even-index pairs sum to a-1, odd-index pairs
sum to 0 mod a; cardinality count floor(a/2)+ceil(a/2)-1=a-1 matches
|E(P_a^alt)|, forcing equality since one side is a subset of the other of
equal size). Lemma 0.2 (orbit size a, stabilizer size 2, both parities of
a): algebra on the induced action on the index c (tau_1: c->c+2,
tau_2: c->-3-c) checks out; the parity split (odd a: tau_1 alone
transitive; even a: tau_1 covers one parity class, one tau_2 application
switches parity) is the correct mechanism.

**Independent verification** (`code/referee-sealed49-A/part0_orbit.py`,
built ONLY from statement.md's sequence/generator definitions, NOT from the
proof's M_c/H_c machinery): constructed P_a^alt directly from the
alternating sequence, generated Dih(a) by BFS closure of rho,sigma (no
assumed group structure), computed the orbit {gamma(P_a^alt)} and
stabilizer by brute force. For a in {3..14,16,17,20,21} (both parities,
including a bit beyond the statement's anchor range): orbit size = a and
stabilizer size = 2 in every case, orbit*stabilizer = |Dih(a)| = 2a
(orbit-stabilizer sanity) in every case. Matches statement.md's own sanity
anchor and Lemma 0.2 exactly. **Verdict: CONFIRMED.**

## Part 1 (lower bound)

Standard "clique blow-up avoiding a connected graph" construction
(b-1 blocks of size a-1, color 1 within block / color 2 across): color-2
graph is complete (b-1)-partite so no K_b; color-1 graph is a disjoint
union of (a-1)-cliques, so any a-vertex connected pattern (gamma(P_a^alt)
is a Hamiltonian path, hence connected, for every gamma since relabeling
preserves connectivity) must span >=2 blocks and hence have a
cross-block, color-2 edge, killing any monotone color-1 embedding. b=1
base case correct (K_0 vacuously avoids both). Argument is airtight and
is the textbook lower-bound pattern for Ramsey numbers of connected
graphs vs. cliques; no gap found.

**Independent verification**: instantiated the exact construction for
(a,b) in {(4,2),(5,2),(4,3),(5,3),(6,3),(4,4),(6,2),(7,2)} and confirmed,
by direct search over the orbit (`common.py`, built from statement.md
definitions), that it avoids both a color-2 K_b and every color-1
Dih(a)-copy of P_a^alt at n=(a-1)(b-1), for all 8 cells. **Verdict:
CONFIRMED.**

## Part 2 (degree reduction, Lemma 2)

**BUG-FOUND, non-fatal.** Lemma 2's b=1 branch: *"For b=1 take W = any
single vertex (vacuous)."* This is false as literally stated, not
vacuous. At b=1, n=1, so the only nonempty W⊆[1] is W={0}; G restricted to
{0} is a single vertex with 0 possible edges, so its (unique) vertex has
degree exactly 0 within W. The lemma claims this degree is >= a-1, i.e.
>= 3 for a>=4. 0 >= 3 is false. Confirmed by direct computation
(`part2_peeling.py`): for a in {4,5,6,7}, the b=1 case's required
inequality HOLDS=False in every case.

**Why it doesn't break the theorem.** Lemma 2 is invoked exactly once,
in Theorem 7, whose proof begins "let c be any 2-coloring of K_n. If c
has a color-2 K_b we are done." For b=1, a color-2 K_1 trivially exists
for any n>=1 (K_1 has no edges, so the Gamma-copy condition is vacuously
satisfied by statement.md's own definition), so the "Otherwise" branch
that invokes Lemma 2 is never reached when b=1 — Lemma 2's broken case
is dead code from the main theorem's point of view. Re-derived this
independently from statement.md's Gamma-copy definition (not assumed).

**Repairability:** trivial — restrict Lemma 2's statement to b>=2, or
add a sentence noting b=1 needs no separate argument. One-line fix, no
mathematical content changes. Flagging per protocol ("never silently
repair"); not fixed here.

The b>=2 case (independence number <= b-1 forces the (a-1)-core
nonempty via reverse-degeneracy-order greedy (a-1)-coloring) is standard
graph theory and checks out on paper: proper (a-1)-coloring exists by
greedy-reverse-deletion-order (correct, standard degeneracy argument);
pigeonhole then forces an independent set of size ceil(n/(a-1))=b
(arithmetic: n/(a-1)=(b-1)+1/(a-1) strictly between b-1 and b since
a-1>=3, so ceiling is exactly b) if the core were empty, contradicting
alpha(G)<=b-1. No gap found.

**Independent verification** (`part2_peeling.py`): exhaustively enumerated
ALL graphs on n=(a-1)(b-1)+1 vertices for (a,b) in {(4,2),(5,2),(4,3),
(6,2)} (133,501 alpha<=b-1 graphs checked at the largest, (4,3)/n=7),
peeled by removing any current-degree<=a-2 vertex until stable, and
confirmed the resulting core is nonempty whenever alpha(G)<=b-1 in every
case — zero failures. **Verdict: BUG-FOUND at Lemma 2 (b=1 case), assessed
non-fatal/dead-code; b>=2 case CONFIRMED.**

## Part 3 (structural facts: Lemma 3.1, 3.1b, 3.2)

Lemma 3.1 (peel rank 0 -> mirror(P_{p-1}^alt)): sequence-substitution proof
checks out; importantly the proof establishes an EXACT edge-set equality
(not just inclusion), which matters because Lemma 4.2's p'=0 branch later
uses this lemma in the *reverse* direction (reconstructing P_a^alt from a
rank-0 attachment edge + a mirror(P_{a-1}^alt) block), which is only valid
because the decomposition is an iff, not a one-way implication. The proof
text doesn't spell this out as a separate corollary, but the underlying
fact (verified below) supports it — minor exposition gap, not a bug.

Lemma 3.1b (peel far endpoint e=floor(p/2) -> P_{p-1}^alt directly,
rank 0 untouched): direct arithmetic in both parities checks out; the
"e>=1 for p>=2" claim (needed so repeated peeling in Lemma 4.2 never
touches rank 0) verified.

Lemma 3.2 (pivot decomposition of H_c, including the q=0 degeneration at
c=a-2): the sigma-transport argument for part (b), and the bounded-range
no-wraparound argument for why mod-a and mod-q arithmetic agree on the
restricted block, both check out by hand.

**Independent verification** (`part3_structural.py`, built from
statement.md's P_a^alt sequence definition and Part 0's M_c/H_c, checking
exact edge-SET equality, not inclusion): Lemma 3.1 tested for p=2..15,
Lemma 3.1b for p=2..15 (including the sequence-truncation claim), Lemma
3.2 for a=3..15 and every c in {0,...,a-2} (so every q, including all
q=0 boundary instances) — zero failures across all three. **Verdict:
CONFIRMED** (Lemma 3.1's reverse-direction use in Part 4 flagged as an
exposition gap, mathematically sound).

## Part 4 (P(m),Q(m): Lemma 4.1, 4.2)

Re-derived the meaning of Q(m)'s defining condition ("i -> r_{q-1-i}
realizes P_q^alt") from scratch: since i -> r_{q-1-i} is order-REVERSING,
this is equivalent to "the increasing tuple r_0<...<r_{q-1}, via its own
natural order, realizes mirror(P_q^alt)" — consistent with how Lemma 3.1
uses "mirror" elsewhere. Implemented P(m)/Q(m) literally from this
reading (not from Lemma 4.1's recursion) as ground truth.

Lemma 4.1 (windowed recursion, corrected "+1" placement per the
provenance note's Audit 1): re-derived the equivalence independently via
Lemma 3.1 (a length-(q+1) P-witness with first element l exists iff
l~_G r_{q-1} and ranks 1..q realize mirror(P_q^alt), i.e. iff
Q_{(l,m)}(l)>=q) — matches the proof's argument exactly.

Lemma 4.2 (Reduction): traced the p'>=1 branch (repeated Lemma-3.1b
trimming preserves l_0/r_{q-1} as rank 0 throughout, since the deleted
position floor(len/2)>=1 whenever len>=2, so trimming never reaches
length 1 given p'>=1) and the p'=0 branch (uses Lemma 3.1 in reverse, see
Part 3 note above — verified this is valid because Lemma 3.1's proof
gives an exact edge-set decomposition). c=p'-1 stays in the valid
{0,...,a-2} range in both branches. No gap found beyond the Part-3
exposition note.

**Independent verification** (`part4_pq.py`, `part6_extraction.py`, all
graphs on n=0..6 vertices exhaustively — 33,868 graphs total, including
the empty graph, all-isolated-vertex graphs, and |W|<=1 — built P(m)/Q(m)
from the base definition, NOT the recursion):
- Lemma 4.1's recursion formula matches the base-definition P(m) and
  Q(m) exactly on every vertex of every graph: **0 mismatches** (this
  redoes, independently, what the provenance note's "Audit 1" claims —
  and extends it from Audit 1's "5 vertices exhaustive + 200 random on
  6-7" to fully exhaustive through n=6).
- Lemma 4.2's conclusion (some H_c embeds via an increasing map, checked
  by direct orbit search, not via the P/Q construction) verified at every
  one of 56,990 trigger instances (P(m)+Q(m)>=a-1, a in {4,5,6}) across
  all graphs to n=6: **0 failures**.

**Verdict: CONFIRMED.**

## Part 5 (Aggregate Sum Theorem)

This is the most delicate part of the document (per the provenance note,
found in partial form by two agents, completed by a third) and got the
closest hand re-derivation.

**Step A:** correct — M=max(W) can only ever be the LAST (largest)
element of a Q-witness tuple, so P is completely unaffected by removing
M, and Q changes only at neighbors of M.

**Step B — the point I most suspected a bug at:** f(i) restricts P(M)'s
candidate set to {w_{i+1},...,w_d} by evaluating the recursion over the
*ambient window* {u in W' : u>w_i} union {M}. I initially worried this
ambient window is much bigger than {w_{i+1},...,w_d} (it includes all of
W' above w_i, not just M's neighbors above w_i) and that this might
silently change which windowed-Q values get computed for each surviving
candidate. Re-derivation: Lemma 4.1's recursion already filters candidates
to l~_G M internally, so the effective candidate set from that ambient
window is exactly {u in W' : u>w_i, u~_G M} = {w_{i+1},...,w_d} regardless
of the window's extra non-neighbor vertices — the discrepancy is a
red herring. Separately, for a surviving candidate w_j (j>i), does
restricting the *ambient* to {u in W':u>w_i} (rather than all of W')
change w_j's own windowed sub-quantity Q_{(w_j,M)}(w_j)? No: that window
is (w_j,M), already inside {u>w_j} subset {u>w_i} since j>i, so the extra
restriction is vacuous. The proof text makes exactly this second point
explicit ("j>i only restricts which l are eligible, not the window used
to evaluate a fixed l=w_j"); the first point (why the window's non-
neighbor vertices don't matter) is implicit but follows immediately from
Lemma 4.1's own l~_G m filter. Both hold up. No bug.

**Step C:** trivial reindexing of suffix-max >= element, verified by hand
symbol-for-symbol.

**Step D:** re-derived the full telescoping sum independently
(sum Delta(w_i) >= d + sum f(i) - sum q_i, sum_{i=1}^d f(i) =
(d-1)+sum_{i=1}^{d-1} M_i using f(d)=0 and f(i)=1+M_i for i<d, then adding
P_G(M)=f(0)=1+M_0 and applying Step C) — reproduces
"sum Delta(w_i)+P_G(M) >= 2d" exactly, matching the document term for
term.

**Step E:** correct bookkeeping of |E(G)|=|E(G')|+d and Q_G(M)=0 (M is
the max of W, no candidates above it).

**Independent verification:** the aggregate inequality
sum_{m in W}[P(m)+Q(m)] >= 2|E(G)| was checked, using base-definition
P(m)/Q(m) (not the induction), on **all 33,868 graphs on 0..6 vertices**
(`part4_pq.py`) — **0 failures**. Since this checks the theorem's
conclusion directly and exhaustively at every graph size the induction
passes through up to n=6, a bug in the inductive step that didn't already
show up here would have to exactly cancel out on every single graph,
which is not plausible. **Verdict: CONFIRMED.**

## Part 6 (Extraction Lemma, Main Theorem)

Corollary 5.1 (pigeonhole: some m has P(m)+Q(m)>=delta(G)) and Theorem 6
(apply Lemma 4.2 to that m) are immediate and correct given Parts 4-5.
Minor completeness note: Corollary 5.1's "average >= delta(G) so some
term is >= delta(G)" implicitly needs |W|>=1 (a division-by-zero /
vacuous-min edge case at W=empty is never actually stated), and Theorem
6's hypothesis delta(G)>=a-1 on a graph with |W|<a is impossible anyway
(max degree in a k-vertex simple graph is k-1), so W=empty or |W|<a never
actually arise in the one place Theorem 6 is invoked (Lemma 2's W is
always nonempty, and delta>=a-1 forces |W|>=a automatically). Not a bug,
just unstated.

Theorem 7 (Main Theorem): lower bound is Theorem 1. Upper bound
correctly short-circuits b=1 before ever touching the broken branch of
Lemma 2 (see Part 2). For b>=2: Lemma 2 -> nonempty W with delta>=a-1;
Theorem 6 -> some H_c embeds in color 1; Lemma 0.2 -> H_c = gamma(P_a^alt)
for some gamma in Dih(a); this is exactly a Dih(a)-copy of P_a^alt by
statement.md's own "equivalently" clause in the Gamma-copy definition
(explicitly invoked, not silently assumed). Dependency graph across all
six parts is acyclic (0->3->4->5->6, with 1 and 2 feeding into 6 only) —
no circularity found anywhere in the document.

**Verdict: CONFIRMED** (contingent on the Part 2 finding being correctly
assessed as non-fatal, which I verified independently rather than taking
the document's own "vacuous" framing at face value).

## Independent computation

All code in `code/referee-sealed49-A/`, outputs/CNFs in
`data/referee-sealed49-A/`. Everything built from statement.md's
definitions directly (sequence for P_a^alt, rho/sigma generators for
Dih(a), M_c/H_c only where Part 3 is literally about H_c's structure),
not from the proof's constructions, except where noted.

1. **Orbit/stabilizer** (`part0_orbit.py`): BFS-closure Dih(a), brute
   orbit+stabilizer of P_a^alt. a=3..14,16,17,20,21, both parities:
   orbit size = a, stabilizer size = 2, orbit*stab=|Dih(a)| in every case.
2. **Exact R_dih(a,b) values** (`part1_and_exact.py`, `common.py`): 8
   cells — (4,2),(5,2),(4,3),(5,3),(6,3),(4,4),(6,2),(7,2) — via DIMACS
   CNF + kissat: UNSAT at n=1+(a-1)(b-1) in every case (upper bound), and
   Part 1's explicit construction independently confirmed to avoid both
   targets at n=(a-1)(b-1) in every case (lower bound). Cross-validated
   the two smallest cells ((4,2),(5,2)) against full brute-force
   enumeration of all colorings — exact agreement.
3. **P(m),Q(m), Lemma 4.1, Theorem 5** (`part4_pq.py`): all 33,868 graphs
   on 0..6 vertices, exhaustive. 0 recursion mismatches, 0 aggregate-sum
   failures.
4. **Lemma 4.2 / Theorem 6 end-to-end** (`part6_extraction.py`): same
   graph set, a in {4,5,6}: 0 failures across 56,990 + 1,963 trigger
   instances.
5. **Structural lemmas 3.1/3.1b/3.2** (`part3_structural.py`): p,a=2..15
   (resp. 3..15), all c: 0 failures.
6. **Lemma 2 core-nonemptiness** (`part2_peeling.py`): exhaustive for
   (a,b) in {(4,2),(5,2),(4,3),(6,2)}: 0 failures for b>=2; explicit
   refutation of the b=1 branch as literally stated (see Part 2).

One self-caught error along the way: my first version of the Lemma-2
checker had a frozenset/tuple type mismatch that made its independence-set
filter vacuously reject every graph (0 graphs checked). Caught because the
reported "checked" count was implausible for a case with an obvious
witness (K_4), fixed, re-ran.

## Overall verdict

**CONFIRMED**, modulo one genuine but non-propagating bug.

The theorem R_dih(P_a^alt,K_b) = 1+(a-1)(b-1) for all a>=4, b>=1, as
proved in candidate-proof.md, holds up under adversarial re-derivation of
every lemma and exhaustive-to-n=6 / SAT-to-n=11 computational
cross-checking built independently from statement.md's definitions.

One real defect found: **Lemma 2 (Part 2) is false as literally stated
for b=1** — its own "vacuous" framing is wrong; the required degree bound
(>= a-1) fails for the unique candidate W at n=1. This is precisely the
kind of base-case bug the protocol flagged as a priority surface, and it
was not caught by the document's own three internal audit rounds (which
focused on Parts 3-5). It does not propagate: Theorem 7's proof structure
independently and correctly short-circuits b=1 before Lemma 2 is ever
invoked, verified by direct appeal to statement.md's Gamma-copy
definition (a color-2 K_1 trivially exists for any n>=1). Repair is
one line (restrict Lemma 2 to b>=2). Not fixed here per referee
instructions.

One exposition gap noted (Part 3/4 boundary): Lemma 4.2's p'=0 branch
uses Lemma 3.1 in the reverse direction, which is valid only because
Lemma 3.1's *proof* (not its stated conclusion) establishes an exact
edge-set equality — never made explicit as a corollary. Verified
computationally that the equality is indeed exact, so this is safe, but
a fully rigorous write-up should state it.

No other bugs found across Parts 0, 1, 3, 4, 5, 6 after adversarial
re-derivation of every lemma and every listed priority surface (mod-a
odd/even index arithmetic, pivot/decomposition boundary including q=0,
all induction base/empty cases, monotone-embedding index bookkeeping
including the one genuinely subtle windowing point in Theorem 5 Step B,
circularity — dependency graph is acyclic).

```diff
- ===== NOT DONE =====
- I DID NOT attempt a's beyond a=21 (orbit/stabilizer) or n=7+ exhaustive
- graph enumeration (P/Q, aggregate sum, extraction) or b>=5 exact R_dih
- SAT cells, and I did not attempt to formally machine-check the proof in
- a proof assistant (e.g. Lean).
- WHAT IT WOULD CHANGE: none of these were required by the brief (which
- asked for n<=6 exhaustive and >=4 SAT/brute-force cells); they would
- only matter if the theorem were false for some larger, specific (a,b) or
- larger n that happens to lie outside everything checked here — i.e. an
- error that is invisible at every scale tested. Nothing found here points
- toward such an error existing.
```
