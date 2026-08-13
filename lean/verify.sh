#!/usr/bin/env bash
# Verification script for the Sealed49 Lean project (run SEALED49, LEAN49
# formalization pass). Checks, in order:
#   1. the project builds clean (lake build Sealed49);
#   2. none of our own .lean files use a placeholder-proof escape hatch
#      (grep hygiene, excluding the vendored .lake/packages dependencies);
#   3. the axiom audit reports only the target axiom set.
# Exits nonzero on any failure.
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")"

echo "== [1/3] lake build Sealed49 =="
lake build Sealed49

echo "== [2/3] grep hygiene (our .lean files, excluding .lake/) =="
# Whole-word scan for every escape hatch: placeholder proofs (sorry,
# admit), kernel bypasses (native_decide, unsafe), custom axiom
# declarations, elaborator overrides (set_option), and linter
# suppression (nolint). -w keeps '#print axioms' and prose like
# "admits" clean.
HITS=$(find . -name "*.lean" -not -path "./.lake/*" -print0 \
  | xargs -0 grep -lnw -e 'sorry' -e 'admit' -e 'native_decide' \
      -e 'unsafe' -e 'axiom' -e 'set_option' -e 'nolint' || true)
if [ -n "$HITS" ]; then
  echo "FAIL: forbidden token found in:"
  echo "$HITS"
  exit 1
fi
echo "clean."

echo "== [3/3] axiom audit =="
AUDIT_OUT=$(lake env lean Sealed49/AxiomAudit.lean)
echo "$AUDIT_OUT"
BAD=$(echo "$AUDIT_OUT" | grep -v '\[propext, Classical.choice, Quot.sound\]' || true)
if [ -n "$BAD" ]; then
  echo "FAIL: axiom audit reported something outside the target set:"
  echo "$BAD"
  exit 1
fi
echo "clean: every audited theorem depends only on [propext, Classical.choice, Quot.sound]."

echo "== verify.sh: ALL CHECKS PASSED =="
