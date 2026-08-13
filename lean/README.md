# Sealed49

Lean 4 formalization of run SEALED49: `R_dih(P_a^alt, K_b) = 1+(a-1)(b-1)`
for all `a ≥ 4, b ≥ 1`. Sources of record:
`../../data/sealed-49/statement.md` (definitions) and
`../../data/sealed-49/candidate-proof.md` (proof, errata-repaired).
Current status: **PARTIAL** — see `../../notes/LEAN49-status.md` for the
full per-file breakdown and exactly which lemmas remain.

## Toolchain (pinned, no rc)

- Lean: `leanprover/lean4:v4.30.0` (`lean-toolchain`).
- mathlib: tag `v4.30.0` (`lakefile.toml`'s `[[require]]`), resolving to
  rev `c5ea00351c28e24afc9f0f84379aa41082b1188f` — matches the Lean
  toolchain exactly (mathlib4 tags track Lean releases 1:1).

## Build

```sh
lake exe cache get   # downloads the mathlib .olean cache (~5G)
lake build Sealed49
```

First build (cold cache download + full mathlib import): a few minutes.
Incremental single-file rebuilds after that: ~35-40s (dominated by
re-elaborating the mathlib import chain each `lean` invocation, not by
this project's own ~460 lines).

## Verify

```sh
./verify.sh
```

Runs the build, checks none of this project's own `.lean` files (i.e.
excluding the vendored `.lake/packages` dependencies) use a placeholder-
proof escape hatch, and runs the axiom audit
(`Sealed49/AxiomAudit.lean`), failing if anything outside
`[propext, Classical.choice, Quot.sound]` shows up.

## Files

- `Sealed49/Defs.lean` — every definition from statement.md (`P_a^alt`,
  `Dih(m)`, Γ-copy, `R_dih`, `K_b`) plus `H_c`/`M_c` from
  candidate-proof.md Part 0, cited line-by-line in the docstrings.
- `Sealed49/Orbit.lean` — Part 0 (orbit of `P_a^alt`): Lemma 0.1 complete;
  Lemma 0.2's two generator computations (`ρ(H_c)=H_{c+2}`,
  `σ(H_c)=H_{-3-c}`) complete, full closure/cardinality argument not
  attempted.
- `Sealed49/Aggregate.lean` — Part 4-5 (`P(m)`, `Q(m)`, the Aggregate Sum
  Theorem): `P`/`Q` definitions complete; a direct reformulation of Lemma
  3.1 complete; Lemma 4.1 and Theorem 5 not attempted.
- `Sealed49/AxiomAudit.lean` — `#print axioms` for every theorem actually
  proved above.
- No `Extraction.lean` or `Main.lean` yet (not started — see status doc).

## Source pins (staging addition, 2026-08-13)

The exact prose this project formalizes, frozen by content hash:

- statement of record: 47 lines, SHA-256
  `3560d2950a8b335e118be2fa94fcf165e2123e8fd07bfcac37e490f2d49e8a69`;
- proof of record (repaired form, `[REPAIR]`-marked): 598 lines, SHA-256
  `883c7d653e8f064a95d0b0ed0310c5e55d87f31580f08be39bd9bd340ef90e4a`;
- pre-repair original: 561 lines, SHA-256
  `dde673fa43b67b0513bae653d3f0d6fd41557358f4d87eda596d80e76ac74ffd`.

Coverage map: `FORMALIZATION_MAP.md`. Trust boundary and scan list:
`AXIOM_AUDIT.md`. The hygiene scan in `verify.sh` was widened at staging
(whole-word: sorry / admit / native_decide / unsafe / axiom /
set_option / nolint) and re-run — all checks pass.

## Bundle path note

This copy ships inside the evidence bundle. The task-relative source
paths above resolve here as: `../../data/sealed-49/statement.md` → the
bundle root's `statement.md` (byte-identical, hash above);
`../../data/sealed-49/candidate-proof.md` → the bundle root's
`proof-final.md` (repaired form; pre-repair original alongside);
`../../notes/LEAN49-status.md` (internal status doc, not shipped) → its
content is superseded here by `FORMALIZATION_MAP.md`.
