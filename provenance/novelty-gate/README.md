# novelty-gate/ — in-bundle backing for the entry text's dated claims

Two mirrors, copied in from this task's `artifacts/web/` (fetched
2026-08-13, MANIFEST-logged there) so the entry text's "five weeks old"
and "no other paper this week" claims have an in-bundle file behind
them, not just an external, unmirrored URL.

- `2607.06817-abs-2026-08-13.html` — arXiv abstract page for
  Damnjanović–Đorđević, fetched 2026-08-13T14:38Z. Submission history:
  v1 Tue 7 Jul 2026 21:24:10 UTC, v2 Sun 12 Jul 2026 12:54:29 UTC, no v3.
  Backs: "Conjecture 4.9 is five weeks old — first posted 2026-07-07,
  revised 2026-07-12."
- `arxiv-sweep-dihedral-altpath-2026-08-13.xml` — arXiv API listing
  sweep, `abs:"dihedral Ramsey" OR abs:"alternating path Ramsey"`,
  most-recent-first, fetched the same timestamp. One result: 2607.06817
  itself. Backs the implicit "no competing/overlapping paper has
  appeared" novelty claim underlying the whole submission.

This is a snapshot at staging time, not a substitute for the
immediate pre-post re-check the submission note's checklist calls for
separately (novelty can move between staging and actual posting).
