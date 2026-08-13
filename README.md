# Dihedral Ramsey numbers of the alternating a-path versus K_b, a >= 4

Evidence bundle for R_dih(P_a^alt, K_b) = 1 + (a-1)(b-1), every a >= 4,
b >= 1 — the a >= 4 slice of Conjecture 4.9 (Damnjanović–Đorđević,
arXiv:2607.06817). Staged by PREP49, 2026-08-13. This bundle is the full content of the
dedicated evidence repo ZestyWombat854/alternating-path-ramsey (owner
decision 2026-08-13: a sibling repo of the a = 3 entry's
[ZestyWombat854/dihedral-ramsey](https://github.com/ZestyWombat854/dihedral-ramsey),
not a subfolder of it; the two entries cross-link).

Not yet posted anywhere. The entry text lives in the producing task's
submission note (internal, not shipped here); its scope is R_dih only —
the cyclic analogue for a >= 4 is explicitly untouched. The partial
Lean 4 formalization IS included (`lean/`, with its own coverage map,
axiom audit, and an independent statement-fidelity audit); what remains
before posting is owner review and the immediate pre-post novelty
re-check.

## Layout

```
proof-final.md                 candidate proof, both referee-found issues
                                repaired INLINE (each marked [REPAIR ...]),
                                plus a provenance note at the top
proof-original-with-errata.md  the untouched original: verbatim copy of
                                the sealed run's own candidate-proof.md
                                (body as audited; errata appended, not
                                folded in — diff the two files to see
                                every edit, exactly)
statement.md                   the pinned problem (verbatim copy)
referees/A/report.md           referee A's full report
referees/A/code/*.py           referee A's verification scripts (7 files)
referees/A/data/*.cnf          referee A's SAT instances (8 cells)
referees/B/report.md           referee B's full report
referees/B/code/*.py           referee B's verification scripts (7 files)
referees/B/data/*.txt          referee B's verification outputs (6 files)
closure/                       PREP49's independent closure of referee B's
                                one declared gap (see closure/README.md)
provenance/                    the sealed run's own research record:
                                registry.md, blocked.md,
                                round-0{1,2,3}-synthesis.md
hygiene.sh                     escape-hatch grep pass (sorry/admit/axiom/
                                native_decide) over this whole bundle
CLAIMS.md                      claim-by-claim audit: every sentence of the
                                entry text mapped to a file here
provenance/lemma-novelty-sweep.md  the dated novelty sweep behind the
                                entry's "Where these sit in the
                                literature" paragraph
lean/                          partial Lean 4 formalization: sources,
                                pinned toolchain, verify.sh,
                                FORMALIZATION_MAP.md, AXIOM_AUDIT.md,
                                statement-audit.md (independent)
```

## Re-run commands and expected output

All computational claims below are independently re-runnable. Dependencies:
Python 3 (stdlib only, except `referees/B/code/verify_R_dih_small.py`
which needs `numpy`), and a `kissat` binary on PATH (or `KISSAT=/path`)
for the two scripts that call it. Every command below was actually
re-run, from these exact bundle paths, while staging this bundle
(2026-08-13); the output shown is real, not transcribed from the
referee reports.

**Path neutralization (2026-08-13, staging).** All six of referee B's
runnable scripts and two of referee A's (`part1_and_exact.py`,
`part6_extraction.py`) originally referenced hardcoded absolute paths
from the machine that produced this bundle (module lookup and output
copies). Those absolute prefixes identify the producing machine, so in
this bundle's copies — and only here — they have been rewritten to
bundle-relative paths (`.` for the script's own directory, `../data`
for its referee's data directory). This path rewrite is the only edit
made to any referee file, it was applied at staging time for
pseudonymity, and the task-side originals retain their original paths
for audit. The shipped outputs in `referees/{A,B}/data/` are untouched.
As a check, one neutralized verifier
(`referees/B/code/verify_rho_sigma_action.py`) was re-run from its
bundle location after the rewrite and reproduced its shipped output
byte-for-byte.

Because the paths are now relative, run each script from inside its own
`code/` directory. Four scripts reference no paths at all and run from
anywhere: `referees/A/code/part0_orbit.py`, `part2_peeling.py`,
`part3_structural.py`, `part4_pq.py`.

### referees/A/code/ (run from that directory)

| Command | Expected output (tail) |
|---|---|
| `python3 part0_orbit.py` | `ALL_OK: True` (orbit size = a, stabilizer size = 2, a=3..14,16,17,20,21) |
| `python3 part1_and_exact.py` | writes CNFs to `../data/`; 8 cells, each `UNSAT (theorem OK)` |
| `python3 part2_peeling.py` | `a=4 b=3 n=7: exhaustive=yes graphs_with_alpha<=b-1=133501 failures=0` (and 3 more cells, all `failures=0`); b=1 probe shows `HOLDS=False` (the bug referee A found, now repaired in `proof-final.md`) |
| `python3 part3_structural.py` | `ALL_PASS: True` (Lemmas 3.1, 3.1b, 3.2, p/a up to 15, zero failures) |
| `python3 part4_pq.py` | `n=0..6: total graphs checked = 33868` / `Lemma 4.1 P-recursion mismatches: 0` / `Q-recursion mismatches: 0` / `Theorem 5 aggregate-sum failures: 0` / `ALL_PASS: True` (~1.1s) |
| `python3 part6_extraction.py` | `Lemma 4.2 trigger instances checked: 56990, failures: 0` / `Theorem 6 trigger instances checked: 1963, failures: 0` / `ALL_PASS: True` (~1.0s) |

(`common.py` is a shared library, not run directly.)

### referees/B/code/ (run from that directory)

| Command | Expected output (tail) |
|---|---|
| `python3 verify_orbit_stabilizer.py` | `ALL PASS (a=3..25): True` |
| `python3 verify_rho_sigma_action.py` | `Checked 322 (a,c) pairs, a=3..25.` / `... hold in ALL cases: True` |
| `python3 verify_lemmas_part3.py` | `GRAND RESULT: Lemma 0.1, 3.1, 3.1b, 3.2 all hold: True` |
| `python3 verify_extraction.py` | `TOTAL graphs with delta>=3 checked: 1885, failures: 0` / `THEOREM 6 (a=4) HOLDS ON ALL REACHABLE CASES (n<=6): True` |
| `python3 verify_PQ_aggregate.py` | `Total graphs checked (n=0..6): 33868` / `GRAND RESULT -- Lemma 4.1 exact match AND Theorem 5 AND Corollary 5.1 hold on ALL graphs to n=6: True` (~1.1s) |
| `python3 verify_R_dih_small.py` | needs `numpy`; `ALL CELLS CONFIRM R_dih(P_a^alt,K_b)=1+(a-1)(b-1) EXACTLY: True` (5 cells, <1s) |

(`defs.py` is a shared library, not run directly.)

### closure/ (referee B's (5,3)-gap closure — independent of both referees' code)

See `closure/README.md` for the full account.

```
python3 closure/encode_5_3_gap.py closure/
```

Output directory is a command-line argument, no setup needed. Expected: `n=8: ... verdict=SAT
independent_witness_check=True`, `n=9: ... verdict=UNSAT`, final
`VERDICT: R_dih(P_5alt,K_3) = 9 -- both legs independently confirmed
... referee B's gap is closed`. Ran in 0.07s wall time against the
20-minute cap.

### hygiene.sh

```
./hygiene.sh
```

Greps this whole bundle for the usual escape-hatch words. See its own
header for the exact exclusions. Output recorded in the producing
task's notebook (internal, not shipped) and summarized in CLAIMS.md.
The Lean project has its own stricter scan inside `lean/verify.sh`.

## What was NOT changed

Exactly two kinds of files in this bundle differ from their
source-of-record; everything else — both referee reports, all referee
data and outputs, the provenance files, `statement.md` — is a
byte-verbatim copy of what the sealed run and its referees actually
produced.

1. `proof-final.md`: differs from `proof-original-with-errata.md` by
   four edits, each marked `[REPAIR ...]` — diff the two files to see
   the complete, exact set.
2. Eight referee scripts (all six of B's, plus A's `part1_and_exact.py`
   and `part6_extraction.py`): differ from the referees' originals by
   the path neutralization described above — hardcoded absolute paths
   from the producing machine rewritten to bundle-relative ones, for
   pseudonymity. Nothing else in any script was touched; the task-side
   originals keep the original paths for audit; one neutralized
   verifier was re-run and reproduced its shipped output
   byte-for-byte.

An earlier staging pass of this README deliberately disclosed the
absolute paths rather than patching them, on the
never-silently-repair-a-referee's-checker principle (see
`provenance/registry.md`). Pseudonymity forced the edit; this note is
what keeps it a disclosed repair rather than a silent one.

## lean/ (appended 2026-08-13, post-LEAN49)

Partial Lean 4 formalization, added after the LEAN49 run landed. Contents:
sources (`Sealed49.lean`, `Sealed49/{Defs,Orbit,Aggregate,AxiomAudit}.lean`),
toolchain pins (`lean-toolchain` = leanprover/lean4:v4.30.0,
`lakefile.toml` + `lake-manifest.json` pinning mathlib tag v4.30.0, rev
c5ea003), `verify.sh` (one command: build + whole-word escape-hatch
scan — sorry / admit / native_decide / unsafe / axiom / set_option /
nolint — + axiom audit), the formalization's own `README.md`,
`FORMALIZATION_MAP.md` (source-to-Lean coverage table with SHA-256 pins
of the statement and proof of record), `AXIOM_AUDIT.md` (trust boundary
and scan list, in prose), and `statement-audit.md` — an independent
statement-fidelity audit (verdict FAITHFUL-WITH-NOTES, zero deviations,
16/16 items FAITHFUL).

Exact boundary, matching the entry text verbatim: kernel-checked are the
full definitional layer plus four theorems (Lemma 0.1 orbit
identification, both dihedral generator computations, Lemma 3.1 in
pointwise form); NOT formalized are the Aggregate Sum Theorem, the
Extraction Lemma, and the final assembly — for those the dual-blind
referee reports in `referees/` are the verification. The `.lake/` build
directory is not shipped; `lake exe cache get` restores it (~8459 files)
before `./verify.sh`.

## Status, authorship, and identity (appended at staging, 2026-08-13)

- **Review status:** the theorem has NOT received human peer review. Its
  verification is the dual-blind AI referee process documented in
  `referees/` (both verdicts CONFIRMED), the machine checks shipped
  there, and the partial Lean formalization in `lean/` — exactly as the
  public entry text states, no more.
- **AI assistance:** the proof was produced, refereed, and formalized by
  Claude (Anthropic) agents under the sealed-run protocol documented in
  `provenance/`; this bundle itself was assembled and audited by the
  same means. Disclosed here in the repo as well as in the entry text.
- **Pseudonymity:** this work is published under the vibemathed-assigned
  pseudonym ZestyWombat854. Absolute machine paths in eight referee
  scripts were rewritten to bundle-relative form at staging (see "Path
  neutralization" above); no other identifying material ships here.
- **Renamings:** every place the Lean names or shapes an object
  differently from the prose source is listed in
  `lean/FORMALIZATION_MAP.md` § Renamings and reformulations.
