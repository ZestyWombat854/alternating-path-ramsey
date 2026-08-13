#!/usr/bin/env bash
# hygiene.sh -- grep this bundle for the usual escape-hatch words (sorry,
# admit, axiom, native_decide), per submission-trust-checklist.md gate 3:
# "a naive grep by a reviewer must come back clean."
#
# Word-bounded (-w), so "admittedly" does not match "admit". Case-sensitive
# (these are Lean/Coq keywords and conventional markers, not English
# prose words we're trying to catch loosely).
#
# Exclusions, and why:
#   - this script itself: it necessarily contains the four words, as the
#     literal strings it searches for.
#   - README.md (this bundle's, and closure/'s, and any other subfolder's):
#     they discuss the hygiene process and this exact exclusion list, which
#     requires naming the words. No README claims 0 occurrences while
#     containing a real one -- if it did, that would itself be a bug.
#
# The Lean formalization is now included (lean/, added 2026-08-13 after
# LEAN49 landed). Its actual sources (*.lean) ARE scanned here -- and are
# clean -- and are additionally scanned by lean/verify.sh's stricter
# whole-word list. Five more files are excluded for the same
# mention-vs-use reason as the READMEs:
#   - lean/verify.sh: names its own scan words as literal strings;
#   - lean/AXIOM_AUDIT.md, lean/FORMALIZATION_MAP.md,
#     lean/statement-audit.md: audit/coverage documentation that must
#     name the prohibited words and the axiom set to describe them;
#   - CLAIMS.md: quotes the public entry text verbatim, which itself
#     says "zero sorry, zero native_decide".
# None of these five contains a real escape hatch; each names the words
# to document the scanning of the files that could.
#
# Usage: ./hygiene.sh [root-dir]   (default: this script's own directory)
# Exit code: 0 iff every word's count is 0.

set -euo pipefail
ROOT="${1:-$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)}"
cd "$ROOT"

WORDS=(sorry admit axiom native_decide)
total=0
clean=1

echo "hygiene.sh: scanning $ROOT"
echo

for w in "${WORDS[@]}"; do
  matches=$(grep -rIn -w \
    --exclude-dir=.git \
    --exclude-dir=.lake \
    --exclude="hygiene.sh" \
    --exclude="README.md" \
    --exclude="verify.sh" \
    --exclude="AXIOM_AUDIT.md" \
    --exclude="FORMALIZATION_MAP.md" \
    --exclude="statement-audit.md" \
    --exclude="CLAIMS.md" \
    "$w" . 2>/dev/null || true)
  count=$(printf '%s\n' "$matches" | grep -c . || true)
  if [ -z "$matches" ]; then
    count=0
  fi
  echo "$w: $count occurrence(s)"
  if [ "$count" -gt 0 ]; then
    clean=0
    printf '%s\n' "$matches" | sed 's/^/    /'
  fi
  total=$((total + count))
done

echo
echo "TOTAL: $total occurrence(s) of sorry/admit/axiom/native_decide"
if [ "$clean" -eq 1 ]; then
  echo "CLEAN: 0 occurrences of the usual escape hatches."
  exit 0
else
  echo "NOT CLEAN -- review the matches printed above."
  exit 1
fi
