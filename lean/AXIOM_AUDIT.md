# Axiom audit

Prose companion to `Sealed49/AxiomAudit.lean`. Practice adapted from the
axiom-audit convention in jinshanmu/CrouzeixConjecture (commit 9df0783).

## Trust boundary

Every theorem this project proves depends on exactly the ordinary
mathlib foundations and nothing else:

    [propext, Classical.choice, Quot.sound]

Classical reasoning enters only through mathlib's standard lemmas (this
project's own files contain no `open Classical` and no explicit choice
invocations). No custom axiom is declared anywhere in the project.

## What is audited

`Sealed49/AxiomAudit.lean` runs `#print axioms` on exactly the four
theorems the project claims to prove — no more, no fewer:

- `Sealed49.palt_eq_Hgraph` (Lemma 0.1),
- `Sealed49.actGraph_rho_hgraph` (Lemma 0.2, ρ computation),
- `Sealed49.actGraph_sigma_hgraph` (Lemma 0.2, σ computation),
- `Sealed49.realizes_palt_succ_iff` (Lemma 3.1, pointwise form).

Definitions carry no proof obligations; their faithfulness to the
pinned statement is the subject of the independent audit in
`statement-audit.md` and the coverage map in `FORMALIZATION_MAP.md`.

## What the scans prohibit

`./verify.sh` step 2 scans every project `.lean` file (the vendored
`.lake/` dependencies excluded) for escape hatches, matching whole
words:

- placeholder proofs: `sorry`, `admit`;
- kernel bypasses: `native_decide`, `unsafe`;
- custom `axiom` declarations;
- elaborator overrides: `set_option`;
- linter suppression: `nolint`.

A hit on any of these fails verification. One disclosed exception
outside the `.lean` files: `lakefile.toml` disables mathlib's *style*
linter set (`weak.linter.mathlibStandardSet = false`) — copyright-header
and formatting cosmetics only; it suppresses no proof-relevant check.

## What is deliberately absent

Unproved material has no Lean counterpart at all: there is no
`Extraction.lean` or `Main.lean`, and no stubbed or `sorry`d statement
anywhere. What is not proved is absent, never faked. The independent
audit noted one unused proved lemma (`altSeqVal_lt`, dead code); it is
inside the scanned files and carries the same trust boundary.

## Authoritative procedure

    ./verify.sh

runs, serially: (1) `lake build Sealed49`; (2) the whole-word escape-
hatch scan above; (3) the axiom audit, failing if any audited theorem
reports anything outside `[propext, Classical.choice, Quot.sound]`.
