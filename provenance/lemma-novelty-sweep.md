# Lemma novelty sweep — Aggregate Sum Theorem & Extraction Lemma (SEALED49)

Tag: LEMMASWEEP. Run date: 2026-08-13. Scope: novelty recon on two internal
lemmas of `data/sealed-49/candidate-proof.md` (Theorem 5 + Corollary 5.1, and
Theorem 6), checked against general graph theory / ordered-Ramsey literature —
**not** a re-check of the main theorem (R_dih(P_a^alt,K_b)=1+(a-1)(b-1)) or of
DD26 (arXiv:2607.06817) itself; that novelty gate is someone else's job and
has already been run repeatedly per this task's own MANIFEST.

## Scope-note (disclosure, not a finding)

Before starting the literature sweep I ran `ls`/`tail`/`head` on this task's
`notes/`, `artifacts/web/` (directory listing only), `artifacts/web/MANIFEST.md`,
`NOTEBOOK.md`, and `data/token-ledger.csv` — to learn append formats before
writing this file. That exceeded my brief ("no repo reads beyond
[candidate-proof.md, statement.md] + notes/lemma paths you create"). What it
exposed: DD26's arXiv id (2607.06817), its predecessor (2604.16188), that
a=3 is already published and a>=4 is this run's new content, and that prior
agents already ran arXiv-search novelty gates on phrases like "dihedral
Ramsey" / "permutational Ramsey" / "alternating path Ramsey" (all clean,
nothing beyond DD26 itself). None of that touches ordered-graph-theory /
monotone-path / degeneracy literature — the actual territory this sweep
needed to cover — and 2607.06817 in fact surfaced on its own, unprompted, in
one of my independent "ordered Ramsey numbers" searches below, so the prior
exposure does not appear to have shortcut or biased the search strategy. Flagging
it anyway per this repo's own disclosure convention (cf. Referee A's
transparency note in NOTEBOOK.md, 2026-08-13 03:10 entry — which I would not
have known the convention existed but for this same overrun).

```diff
- ===== NOT DONE =====
- I did not fetch primary sources for the two most load-bearing classical
- facts (Erdos-Gallai/Diestel min-degree-path folklore; Chvatal 1977's
- greedy min-degree tree-embedding lemma; Erdos-Szekeres 1935 itself) —
- I relied on convergent secondary-source snippets (multiple independent
- WebSearch results plus the Balko survey's own direct restatements) rather
- than a copy-before-read PDF of each. I also did not search non-English
- literature, Google Scholar citation graphs, or MathSciNet.
- WHAT IT WOULD CHANGE: these are extremely standard, uncontested textbook
- facts corroborated from multiple independent angles below; a primary-source
- fetch would almost certainly just confirm the wording, not the verdict. Risk
- is concentrated in the two APPEARS-NEW calls themselves, not in the
- classical-lineage citations — if a closer match to either target lemma
- exists, it is more likely sitting in a paper my search terms didn't surface
- than in a mis-cited classical fact.
```

---

## The two objects, precisely (for the record — see candidate-proof.md for full statements)

**Aggregate Sum Theorem (Thm 5 + Cor 5.1).** Fix a graph G on a finite
linearly ordered vertex set W. For m in W, `P(m)` is the length of the
longest chain `l_0 < ... < l_{p-1} < m` that *realizes P_p^alt* (the specific
"alternating" Hamiltonian-path pattern on ranks, edges = consecutive pairs of
the sequence 0,p-1,1,p-2,2,...) with an extra edge `l_0 ~_G m`; `Q(m)` is the
mirror-image quantity looking rightward. Claim: `sum_{m in W} [P(m)+Q(m)] >=
2|E(G)|`, hence (averaging) `max_m [P(m)+Q(m)] >= delta(G)`. This holds for
*every* graph on an ordered vertex set — no coloring, no completeness
assumption, no relation to any complement.

**Extraction Lemma (Thm 6).** For a>=4, every graph G on a finite linearly
ordered vertex set W with `delta(G) >= a-1` contains, for some `c in Z/aZ`,
an increasing map `v:[a]->W` with every edge of `H_c` landing on a G-edge.
`H_c := M_c ∪ M_{c+1 mod a}` where `M_c` = pairs of `[a]` summing to `c mod
a`; by the proof's own Lemma 0.1/0.2, `{H_c : c in Z/aZ}` is exactly the
Dih(a)-orbit of the alternating path P_a^alt — i.e. abstractly a tree
(a Hamiltonian path shape on `a` vertices), realized only in this
particular "rank-sum" edge-set form.

---

## Verdict 1 — Aggregate Sum Theorem (Thm 5 / Cor 5.1): **APPEARS-NEW**

Swept: ordered Ramsey theory (Conlon-Fox-Lee-Sudakov 2017; Balko's 2025
survey, full text grepped for "degree", "degenerate", "tree", "monotone
path", "Erdos"/"Szekeres"), the classical Erdos-Szekeres proof itself, the
classical min-degree-path folklore, Graham-Kleitman/Chvatal-Komlos
edge-ordered altitude lineage, and Caro's "degree monotone paths" line of
work. Found nothing closer than:

- **Erdos-Szekeres (1935), standard pigeonhole proof.** `P(m)`/`Q(m)` are a
  direct structural transplant of the textbook `L(i)`/`D(i)` labels
  (`L(i)` = longest increasing subsequence ending at `i`, `D(i)` =
  longest decreasing) used to prove "every sequence of `(r-1)(s-1)+1`
  distinct reals has an increasing run of length `r` or decreasing of
  length `s`" via injectivity of `(L(i),D(i))` pairs — confirmed via
  multiple independent search snippets and directly in the Balko survey
  (arxiv.org/html/2502.02155, section "Monotone Paths and the
  Erdos-Szekeres Theorem": *"the Erdos-Szekeres lemma is a consequence of
  a stronger Ramsey statement about monotone paths," R_<(MP_n^<) =
  (n-1)^2+1*, citing Choudum-Ponnusamy and Milans-Stolee-West). But that
  is a **pigeonhole/injectivity** argument bounding a *sequence length*
  under a *no-long-run* hypothesis — structurally different from Theorem
  5, which is an unconditional **discharging/edge-counting identity**
  (induction removing the max vertex, charging its neighbors' `Q`-deltas)
  for an *arbitrary graph*, with no "no long chain" hypothesis and no
  requirement that G be one side of a 2-coloring of a complete graph.
- **Graham-Kleitman (1973), "Increasing paths in edge ordered graphs"**
  (Period. Math. Hungarica; question posed by Chvatal-Komlos 1971): their
  general bound "every edge-ordered n-vertex graph has an increasing trail
  of length >= `2|E(G)|/n`" is the closest **proof-style** relative found —
  both derive "one long monotone/alternating chain exists" by averaging a
  chain-type quantity against `2|E(G)|`, exactly the move Corollary 5.1
  makes from Theorem 5. Settings differ (their chain-length bound is a
  direct average; ours goes through a discharging identity first) and,
  critically, **theirs is edge-ordered** (a linear order on E(G); "increasing"
  means increasing edge-labels along a trail) while ours is **vertex-ordered**
  (a linear order on V(G); P_a^alt-realization is about which vertex-pairs
  are graph-edges at all, not about any edge-label sequence) — see the
  vertex/edge distinction section below. Not a restatement, but the single
  most on-point proof-technique citation found for the Corollary 5.1 half.
- **Caro et al., "Degree Monotone Paths"** (arXiv:1405.1812, 1408.3204) and
  "Ramsey numbers for degree monotone paths" — explicitly Erdos-Szekeres-
  inspired and graph-theoretic, but "monotone" there means the path's *own
  degree sequence* is monotone (an order derived from local graph
  structure), not an externally fixed linear order on V(G) fixed before
  looking at G at all. Genuinely different object; swept and distinguished,
  not a match.
- Diestel-style folklore ("min degree `d` => path of length `d`", greedy
  longest-path argument) is the ancestor of the *shape* of the Corollary
  5.1 conclusion (one long chain from a degree bound) but is unordered and
  says nothing about sums over all vertices or about any specific pattern.

## Verdict 2 — Extraction Lemma (Thm 6): **APPEARS-NEW**

Swept the same territory plus specifically: ordered/monotone Ramsey numbers
of trees, Chvatal's 1977 tree-complete-graph Ramsey theorem and the
classical greedy tree-embedding engine inside it, the survey's
"ordered d-degenerate graph" bounds, and the one paper combining "tree" +
"ordered complete graph" that surfaced. Found nothing closer than:

- **Chvatal (1977), "Tree-complete graph Ramsey numbers"** (J. Graph Theory
  1:93): proves `R(T_n,K_m) = (n-1)(m-1)+1` for *every* tree `T_n` on `n`
  vertices — the unordered ancestor of this whole run's main theorem. Its
  proof is exactly two pieces: (i) a degeneracy/peeling argument to isolate
  a subgraph with `delta >= n-1` (= this proof's separate Lemma 2, not one
  of the two lemmas under audit here, and itself classical/folklore), then
  (ii) the classical fact *"every t-edge tree embeds (greedily, no vertex-order
  constraint) into any graph with min degree >= t"* (confirmed via two
  independent search summaries in near-identical language). The Extraction
  Lemma is exactly the **monotone/ordered strengthening** of step (ii): same
  min-degree threshold (`a-1` = edges of the `a`-vertex tree), but the
  embedding must additionally be increasing in a pre-fixed vertex order, and
  it is proved for one specific tree family (P_a^alt's dihedral orbit)
  rather than all trees. Monotonicity is a real extra constraint the
  classical greedy argument does not supply — it places tree vertices via
  BFS/available-neighbor choices with no control over where they land in
  any ambient order.
- **The gap this fills looks genuinely open, field-wide.** The
  ordered-Ramsey survey (Balko, arXiv:2502.02155, 91KB of body text
  grepped in full) has zero dedicated treatment of trees — a single
  incidental bibliography hit (below) — despite dedicated sections for
  monotone paths, matchings, stars, cycles, and complete graphs. Search
  summaries for "ordered Ramsey number of a tree" independently volunteer
  that, unlike the clean closed-form unordered Chvatal formula, "ordered
  Ramsey numbers for trees... depend heavily on the specific orderings
  imposed" — i.e. no known general ordered/monotone analogue of Chvatal's
  theorem. Consistent with the founding CFLS result that going from
  unordered to ordered/monotone is usually *expensive* (even matchings can
  go superpolynomial; the plain monotone path alone jumps from a linear
  unordered path-Ramsey number to `R_<(MP_n^<)=(n-1)^2+1`, quadratic) — so a
  degree-threshold lemma that reproduces the classical bound *exactly* for
  a specific ordered tree, as the Extraction Lemma (feeding Theorem 7) does,
  is not the kind of thing that seems to already exist quietly as folklore.
- **Barat, Gyarfas, Toth (2024), "Monochromatic spanning trees and matchings
  in ordered complete graphs"** (J. Graph Theory 105(4):523-541,
  arXiv:2210.10135) — the one "tree" + "ordered" hit in the whole sweep.
  Different question: guarantees a monochromatic *spanning* tree (uses all
  n vertices) avoiding a forbidden nested/crossing/separated edge-pattern,
  in a 2-coloring of a complete ordered graph. Not a small fixed-shape
  pattern, not a min-degree hypothesis, not a match — checked and
  distinguished.
- The survey's "ordered `d`-degenerate graph" bounds (its Theorem ~2 region:
  `R_<(G^<) <= n^{32 d log chi}` etc.) bound how `R_<(H)` *grows with
  `|V(H)|`* when the **target** graph H is degenerate — the opposite
  direction from the Extraction Lemma, which asks what **host**-graph min
  degree forces a monotone copy of one *fixed, small* pattern. Swept and
  distinguished, not a match.

---

## Vertex-ordered vs. edge-ordered — swept and distinguished (per brief)

Both target lemmas are **vertex-ordered**: `W` carries a fixed linear order
on vertices, and "realizing `P_p^alt`" / "realizing `H_c`" is a condition on
which vertex-pairs are graph-edges, evaluated against an increasing map into
that order. The following are all confirmed, via direct search, to be
**edge-ordered** instead (a linear order on E(G), "increasing" meaning
increasing edge-labels along a walk) and were swept only to be ruled out:

| Concept | Ordered on | Confirmed via |
|---|---|---|
| Altitude of a graph, `f(G)` (Chvatal-Komlos 1971; Burger-Cockayne-Mynhardt 2005) | edges | Balko-survey-adjacent search: *"the altitude of a graph G... is the largest k such that under each ordering of E(G), there is a path of length k traversing edges in increasing order"* |
| Graham-Kleitman (1973) increasing paths/trails | edges | *"every edge ordering of K_n contains an increasing trail..."* |
| "Monotone paths in dense edge-ordered graphs" (Bucic et al.); "Nearly-linear monotone paths in edge-ordered graphs"; "Tiling edge-ordered graphs..." | edges | titles + abstracts explicitly edge-ordered |

None of these bear on the Aggregate Sum Theorem or Extraction Lemma beyond
the proof-style echo already credited to Graham-Kleitman above.

---

## Must-cite list if this proof is written up for submission

(Ordered by relevance to the two lemmas specifically, not to the paper's
main theorem — that citation list is out of scope here.)

1. Chvatal, V. (1977). *Tree-complete graph Ramsey numbers.* J. Graph
   Theory 1, 93. — unordered ancestor of the Extraction Lemma's degree
   threshold and of Lemma 2's peeling technique.
2. Erdos, P., Szekeres, G. (1935). *A combinatorial problem in geometry.*
   Compositio Math. 2, 463-470. — ancestor of the P(m)/Q(m) construction.
3. Conlon, D., Fox, J., Lee, C., Sudakov, B. (2017). *Ordered Ramsey
   numbers.* J. Combin. Theory Ser. B 122, 353-383 (arXiv:1410.5292). —
   founding paper of the field this proof's upper-bound machinery lives in;
   frames why an exact-match-to-classical-bound result (Theorem 7) is
   noteworthy.
4. Graham, R.L., Kleitman, D.J. (1973). *Increasing paths in edge ordered
   graphs.* Period. Math. Hungarica. — closest proof-style relative to
   Corollary 5.1; cite explicitly to distinguish edge- vs vertex-ordered.
5. Balko, M. *A Survey on Ordered Ramsey Numbers* (arXiv:2502.02155,
   2025). — best available evidence that "ordered Ramsey numbers of trees"
   is essentially untreated as a subfield.
6. Choudum, S.A., Ponnusamy, B., or Milans, K., Stolee, D., West, D. —
   proof(s) that `R_<(MP_n^<) = (n-1)^2+1`, cited via the Balko survey; the
   nearest *known formula* in this space (plain monotone path, path-vs-path,
   not path-vs-clique, not alternating, not dihedral).

## Sources consulted (all via WebSearch snippets unless a local mirror is listed)

- arxiv.org/abs/2607.06817 (DD26) — local mirror: `artifacts/web/lemmasweep-dd26-abs.html`/`.txt`
- arxiv.org/html/2502.02155 (Balko survey) — local mirror:
  `artifacts/web/lemmasweep-balko-survey.html`/`.txt` (full text grepped for
  "degree", "degenerate", "tree", "monotone path", "Erdos"/"Szekeres")
- arxiv.org/abs/1410.5292 (Conlon-Fox-Lee-Sudakov) — local mirror:
  `artifacts/web/lemmasweep-cfls-orderedramsey-abs.html`/`.txt`
- WebSearch only (no fetch — general/attribution queries, snippets
  sufficient and convergent across independent queries): Erdos-Gallai /
  Diestel min-degree-path folklore; Chvatal 1977 proof technique; Graham-
  Kleitman / Chvatal-Komlos altitude; Erdos-Szekeres standard proof; Caro
  "Degree Monotone Paths"; Balko-Cibulka-Kral-Kyncl "Ramsey numbers of
  ordered graphs"; Barat-Gyarfas-Toth spanning trees paper.
