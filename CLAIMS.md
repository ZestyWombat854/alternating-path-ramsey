# CLAIMS.md — claim-by-claim audit

Every factual sentence of the entry text and result note (the text
posted on vibemathed; drafted in the producing task's internal notes,
not shipped here), mapped to the bundle file(s) that back it. Built
against the producing run's submission-trust checklist, gate 1: "No
file -> add the file or cut the sentence." Every row below resolved to
an in-bundle file; nothing here was left as a bare assertion.

## Entry text

| # | Claim | Backed by | Note |
|---|---|---|---|
| 1 | R_dih(P_a^alt, K_b) = 1+(a-1)(b-1) for every a>=4, b>=1 | `proof-final.md` Theorem 7 (statement + proof); `referees/A/report.md` + `referees/B/report.md` (independent CONFIRMED verdicts) | The theorem itself |
| 2 | Definitions of P_a^alt, Dih(a), R_dih as used | `statement.md` | Verbatim pinned problem |
| 3 | Resolves Conjecture 4.9 for every a>=4 | `statement.md` (statement.md's own header ties the pinned problem to Conjecture 4.9); `proof-final.md` | statement.md is this run's restatement of the paper's Conjecture 4.9, dihedral case only |
| 4 | Combined with the a=3 case, resolves Conjecture 4.9 in full for a>=3 | External: the live a=3 entry (linked, not in this bundle) + this bundle's `proof-final.md` | The a=3 half of this claim is NOT re-verified by this bundle — it rests on the already-posted, already-refereed sibling entry |
| 5 | This is R_dih only; cyclic (R_cyc) is untouched for a>=4 | `statement.md` (defines R_dih only; no R_cyc definition anywhere in this bundle); `proof-final.md` (Theorem 7's proof never invokes a cyclic-group argument) | Absence claim: verified by the definition simply not existing in either file |
| 6 | Dih(3)=Sym(3) (a=3 accident); for a>=4, \|Dih(a)\|=2a<a! | `referees/A/code/part0_orbit.py` + `referees/B/code/verify_orbit_stabilizer.py` (both compute \|Dih(a)\|=2a directly, a up to 21/25) | 2a<a! for a>=4 is elementary arithmetic (2·4=8<24), not separately certified by any script here |
| 7 | Conjecture 4.9 first posted 2026-07-07, revised 2026-07-12, no v3 as of 2026-08-13 | `provenance/novelty-gate/2607.06817-abs-2026-08-13.html` | Fresh fetch, this staging pass |
| 8 | Conjecture 4.9 has no independent citations yet | Not re-verified in this bundle | See NOT-DONE block below |
| 9 | Closed form 1+(a-1)(b-1) is the source paper's own conjecture | `statement.md` (states the target formula, sourced from the paper); `provenance/novelty-gate/2607.06817-abs-2026-08-13.html` | |
| 10 | Lower bound is the standard block-partition construction | `proof-final.md` Theorem 1; `referees/A/report.md` Part 1 ("textbook lower-bound pattern... no gap found"); `referees/B/report.md` §2 ("standard") | |
| 11 | Degree-reduction / degeneracy-peeling step is standard graph theory | `proof-final.md` Lemma 2; `referees/A/report.md` Part 2 ("standard, correctly-executed"); `referees/B/report.md` §2 | |
| 12 | Aggregate Sum Theorem: sum_m[P(m)+Q(m)] >= 2\|E(G)\| | `proof-final.md` Theorem 5; `referees/A/code/part4_pq.py`; `referees/B/code/verify_PQ_aggregate.py` + `referees/B/data/PQ_aggregate.txt` (33,868 graphs, n<=6, 0 violations, both independently coded) | |
| 13 | Proved by an induction mentioning no a, P_a^alt, or Dih(a) | `proof-final.md` Part 5 (read the statement and proof text directly — self-verifying by inspection) | |
| 14 | Extraction Lemma follows by one-line averaging; is the entire remaining content | `proof-final.md` Theorem 6, Corollary 5.1; `provenance/registry.md` ("EL ITSELF IS THE ENTIRE REMAINING CONTENT OF THE THEOREM") | |
| 15 | Proof produced by sealed multi-agent process, 3 rounds, no shared context within a round | `provenance/registry.md`, `provenance/round-01-synthesis.md`, `round-02-synthesis.md`, `round-03-synthesis.md` | |
| 16 | Two referees, dual-blind, structurally separated, zero shared context | `referees/A/report.md` line 1 ("blind to referee B and to all other run files"); `referees/B/report.md` line 1 ("fresh agent, no connection to the producing team... No other file... was read") | |
| 17 | Both independently wrote their own verification code | `referees/A/code/*.py` vs `referees/B/code/*.py` — visibly disjoint implementations (diff the two directories; zero shared files) | |
| 18 | Orbit/stabilizer structure checked, a up to 25 | `referees/B/code/verify_orbit_stabilizer.py` + `referees/B/data/orbit_stabilizer.txt` (a=3..25) | referee A's own version covers a up to 21 only (`part0_orbit.py`) — the "up to 25" figure is B's |
| 19 | Exact SAT/UNSAT confirmation at 8 (a,b) cells, 6 confirmed two ways | `referees/A/data/*.cnf` (8 files); `referees/B/data/R_dih_small_cells.txt` (5 cells, exhaustive); `closure/results.json` ((5,3) a third way) | See union computation below |
| 20 | Aggregate Sum inequality checked exhaustively, 33,868 graphs to n=6, 0 violations, both referees | `referees/A/code/part4_pq.py`; `referees/B/code/verify_PQ_aggregate.py` + `referees/B/data/PQ_aggregate.txt` | Independently re-run by PREP49 while staging (see README.md); identical results |
| 21 | Both referees' overall verdict: CONFIRMED | `referees/A/report.md` (Overall verdict section); `referees/B/report.md` §4 (verdict table) | |
| 22 | One non-fatal bug found (Lemma 2, b=1 branch); doesn't propagate | `referees/A/report.md` Part 2; `proof-final.md` (repaired inline, marked `[REPAIR, referee A ...]`, two locations) | |
| 23 | One cosmetic arithmetic slip found (Lemma 3.1 proof aside); no effect | `referees/B/report.md` §2 (Lemma 3.1 bullet); `proof-final.md` (repaired inline, marked `[REPAIR, referee B ...]`) | |
| 24 | Both repaired inline in the submitted proof; pre-repair original kept | `proof-final.md` vs `proof-original-with-errata.md` — diff the two | |
| 25 | One referee (B) flagged a verification cell (5,3) it hadn't finished; already had independent SAT coverage from A; now closed a second way | `referees/B/report.md` §3 NOT-DONE block; `referees/A/data/cnf_5_3.cnf`; `closure/results.json`, `closure/README.md` | |
| 26 | No human peer review was obtained | Not verifiable by a file (absence claim about the real world, not this repo) | Stated on the run's own word, same as the a=3 debut's identical claim |
| 27 | Lean formalization: [placeholder] | `code/lean-49/` (outside this bundle; LEAN49's separate, parallel deliverable) | **Must be resolved before posting — see README.md and the submission note's checklist** |

## Result note

| # | Claim | Backed by | Note |
|---|---|---|---|
| 28 | R_cyc(P_a^alt,K_b), a>=4, not addressed by this entry | Same as row 5 | |
| 29 | This entry + a=3 sibling resolve Conjecture 4.9 (dihedral) for a>=3 | Same as row 4 | |
| 30 | a=1,2 not checked by either entry | Not checked in this bundle (by construction — `proof-final.md` Theorem 7 states a>=4; the a=3 entry states a=3 only) | Honest scope disclaimer, not a claim requiring positive evidence |
| 31 | Entry is amendable if Lean status changes after posting | Process claim, not a factual/mathematical one | No file needed |

## The "eight cells" arithmetic (row 19), spelled out

```
A (SAT, kissat):        (4,2) (5,2) (4,3) (5,3) (6,3) (4,4) (6,2) (7,2)   -- 8 cells
B (exhaustive):         (4,2)       (4,3)             (6,2) (7,2)         -- 5 cells, all subset of A
closure (independent):                    (5,3)                           -- 1 cell, subset of A
-----------------------------------------------------------------------
union: 8 distinct cells (A's own list); 6 of them ((4,2),(4,3),(5,2),(5,3),(6,2),(7,2))
confirmed at least twice; (5,3) specifically confirmed three independent ways.
```

(An earlier draft of the entry text said "nine cells combined" — wrong;
corrected to "eight... six of them confirmed two independent ways"
after this table caught the arithmetic. Left here as a record of the
audit actually doing its job, not smoothed over.)

## hygiene.sh result

Run over this entire bundle (2026-08-13): 0 occurrences of the usual
escape-hatch words (see `hygiene.sh`'s own header for exactly which
four, and its exclusion list). Also run over the full `staging/` tree
(this bundle plus `../theorem-b-cert-debt/`): 0 occurrences. Full output
in `../../NOTEBOOK.md` (PREP49's closing entry).

```diff
- ===== NOT DONE =====
- I DID NOT independently verify claim 8 (Conjecture 4.9 has zero
- independent citations) or claim 26 (no human peer review was obtained)
- against any file in this bundle -- both are absence claims about the
- outside world (citation databases, who has read this proof) that no
- local file can prove. Claim 8 rests on this run's own citation-count
- history (Semantic Scholar checks throughout the task, most recently
- pre-dating this bundle -- see the task's own artifacts/web/MANIFEST.md
- for the trail, not reproduced inside this bundle) rather than a fresh
- citation recheck run specifically for this staging pass.
- WHAT IT WOULD CHANGE: if either turns out false at posting time (a
- citation appeared, or some reviewer already privately read a draft),
- the entry's "skeptic's case" framing would need a one-line update, not
- a retraction -- neither claim is load-bearing for the theorem itself,
- only for how the entry frames its own novelty and review history.
```
| "Where these sit in the literature" paragraph (ES lineage; Graham–Kleitman edge-ordered distinction; Chvátal 1977 ordered strengthening; Balko survey absence; novelty claim basis) | provenance/lemma-novelty-sweep.md (sweep report, shipped in this bundle; verdicts APPEARS-NEW for both lemmas) |

## Lean formalization rows (appended 2026-08-13, post-LEAN49)

| Claim in entry text | Backing in this bundle |
|---|---|
| "Lean formalization: partial ... zero sorry, zero native_decide ... axioms exactly [propext, Classical.choice, Quot.sound]" | lean/ (full sources + toolchain pins); re-run: `cd lean && lake exe cache get && ./verify.sh` — build + hygiene grep + axiom audit, all three must pass (verified 2026-08-13 by the authoring agent, independently by the orchestrator, and a third time by the statement-fidelity auditor, all exit 0) |
| "every object in the pinned statement ... plus four theorems" (orbit identification; both generator computations; path-peeling Lemma 3.1) | lean/Sealed49/{Defs,Orbit,Aggregate}.lean — palt_eq_Hgraph, actGraph_rho_hgraph, actGraph_sigma_hgraph, realizes_palt_succ_iff; per-theorem axiom listing in lean/Sealed49/AxiomAudit.lean |
| "What is NOT formalized: the Aggregate Sum Theorem, the Extraction Lemma, and the final assembly" | Honest-boundary statement — no Lean file claims these; Extraction.lean/Main.lean deliberately absent rather than stubbed (zero placeholder proofs anywhere) |
| "an independent statement-fidelity audit of the Lean definitions" | lean/statement-audit.md — independent auditor, forbidden from reading the author's rationale; verified Lean terms against mathlib SOURCE (finRotate, Fin.revPerm, fromRel, comap), 16/16 items FAITHFUL, verdict FAITHFUL-WITH-NOTES, zero deviations; includes the honesty ruling on calling realizes_palt_succ_iff "Lemma 3.1 in equivalent pointwise form" |
