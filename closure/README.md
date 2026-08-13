# closure/ — independent closure of referee B's (5,3) gap

Referee B's report (`../referees/B/report.md`, section 3, the NOT-DONE
block under task 3b) explicitly did not complete a two-sided verification
of R_dih(P_5alt, K_3) at n=9: the upper-bound leg (UNSAT of "no colour-1
Dih(5)-copy of P_5alt and no colour-2 K_3" at n=9) was left unchecked
mechanically, because brute force over 2^36 colourings was outside B's
budget and B did not substitute a SAT solver.

`encode_5_3_gap.py` is a fresh, independent encoding of exactly that
cell, written from `../statement.md`'s definitions only. It shares no
code with either referee's encoder (`../referees/A/code/*.py`,
`../referees/B/code/*.py`) — see the script's own docstring for the
encoding and the independence argument in detail.

## What it found

Both legs run (n=8 self-check, n=9 target):

| n | leg | kissat exit | verdict | extra check |
|---|---|---|---|---|
| 8 | lower bound | 10 | **SAT** | witness independently re-checked by a second, brute-force code path in the same script — clean (no colour-1 Dih(5)-copy of P_5alt, no colour-2 K_3) |
| 9 | upper bound (the gap) | 20 | **UNSAT** | — |

**R_dih(P_5alt, K_3) = 9, confirmed.** Referee B's gap is closed.

Run: `results.json` (machine-readable summary), `5_3_n8.cnf` /
`5_3_n9.cnf` (DIMACS instances), `5_3_n8.kissat.log` / `5_3_n9.kissat.log`
(full solver output), `5_3_n8.witness.txt` (decoded SAT witness + the
independent-checker verdict). kissat 4.0.4, both legs solved in well
under a second — nowhere near the 20-minute cap this closure was run
under.

**No DRAT certificate for the n=9 UNSAT leg** — noted explicitly, per the
task brief ("no DRAT needed for staging; note it"). kissat's exit code 20
and the full log are the evidence kept here. If this closure is later
promoted from staging-completeness to a fully certified artifact (the bar
the `../theorem-b-cert-debt/` and referee A's own cells meet), re-run
kissat with `--no-binary 5_3_n9.cnf 5_3_n9.drat` and check with
`drat-trim 5_3_n9.cnf 5_3_n9.drat`.

## Context: this is not the only independent confirmation of this cell

Referee A's own SAT sweep (`../referees/A/report.md`, part 2) independently
covered **the same cell**, (5,3), among its 8: see
`../referees/A/data/cnf_5_3.cnf` (36 vars, 714 clauses — about half this
script's 1344, because A's encoding dedups by the `a`-element orbit
{H_c} rather than iterating all `2a` elements of Dih(5); both are valid
encodings of the same statement.md definition, cross-checked here by the
clause-count arithmetic matching exactly under that hypothesis:
126·5+84=714). So R_dih(P_5alt,K_3)=9 already had one independent SAT
confirmation before this script ran; what was actually missing was
narrower — referee B's *own* report had an open NOT-DONE item for a cell
its co-referee had in fact covered. This script closes it a second way,
directly, so B's report and the bundle as a whole no longer rest on
"another referee happened to cover this."

## Re-run

```
python3 closure/encode_5_3_gap.py closure/
```

Expected: `n=8: ... verdict=SAT independent_witness_check=True`,
`n=9: ... verdict=UNSAT`, final line `VERDICT: R_dih(P_5alt,K_3) = 9 --
both legs independently confirmed ... referee B's gap is closed`, exit
code 0. No dependencies beyond Python 3 stdlib and a `kissat` binary on
PATH (or `KISSAT=/path/to/kissat` in the environment).
