# Round 3 synthesis — SEALED49

5 agents launched (G1-G5), all fresh/independent, briefed with the full
statement plus E3's exact residual-case gap as the shared target. Mid-
round, root relayed two substantive updates from completed agents to
still-running ones (G5's regularity narrowing; G3's aggregate-sum lead
and a correction to the "every vertex maximizes" over-generalization) --
a legitimate use of the async messaging channel, distinct from several
illegitimate messages described below.

## Headline result: THE THEOREM IS PROVED

G4 proved the **Aggregate Sum Theorem**: for every finite graph G on a
linearly ordered vertex set W, sum_{m in W}[P(m)+Q(m)] >= 2|E(G)|. By a
one-line averaging argument this gives max_m[P(m)+Q(m)] >= delta(G)
unconditionally -- closing the Extraction Lemma completely, with NO case
split into safe/residual/regular cases at all. The trichotomy the whole
round was organized around (safe case closed in round 2; residual case
assigned to round 3; G5's narrowing to exactly-regular graphs) turns out
to be exactly what this sum argument absorbs without needing to name it.

This was independently discovered, in weaker/partial forms, by TWO other
round-3 agents before G4 completed it:
- G2 found the identical statement via "mechanisms A-D" (explicit case
  analysis), proving it completely for the extremal all-zero case and
  one hand-built mixed case.
- G3 found the identical statement while investigating an Erdos-Gallai
  rotation adaptation, proving it with exact equality on two examples.

Three independent derivations of the same non-obvious statement, via
three different routes, is strong convergent evidence the statement is
both true and the natural resolution -- not a fragile, unreplicated
claim.

## Two rounds of dedicated adversarial audit found and fixed real gaps

Per the run's rule that every candidate proof gets checked for gaps,
conditionals, and handwaving before being trusted, root launched THREE
dedicated audit passes (beyond the ordinary per-round adversarial
checking every family already does), each by a fresh agent with no
stake in the result:

**Audit 1** (of G4's original proof): found a genuine, precisely-located
error. The core recursion (Lemma 4.1: P(m) in terms of a windowed Q) was
stated as "1 + max({0} union {...})" -- but this gives the WRONG value
(1 instead of 0) whenever a vertex has no earlier neighbor at all (the
candidate set is empty). Concrete counterexample: W={0,1}, empty graph,
m=1 has no left-neighbor, true P(1)=0, formula gives 1. The audit traced
through the rest of the proof and found this boundary case, while real,
did not actually break the FINAL theorem (the one place it could matter,
d=0 in the induction, needs only the trivially-true "0 >= 0"), but it
was a genuine hole in the proof AS WRITTEN. Root independently verified
the fix (move the "+1" inside each candidate term, before taking the
max with the floor 0) by direct computation against the base
definitions of P and Q -- not against any derived formula -- across all
graphs on up to 5 vertices exhaustively, 200 random graphs on 6-7
vertices, and every boundary case constructed to stress-test exactly
this failure mode. Zero mismatches.

**Audit 2** (of the full assembled document, after root wrote it up):
found two further write-up gaps, both real but repairable: Lemma 4.2's
"trimming" step (shrinking a witnessing chain while keeping its
attachment vertex fixed) cited Lemma 3.1, which deletes the WRONG
vertex (the attachment vertex itself) for that purpose; and Lemma 3.2's
part (b) had a hand-waved justification ("by reflection symmetry...")
that didn't actually match the mechanism needed. The audit proved both
correct underlying facts itself (the correct trimming lemma -- delete
the OTHER path endpoint, at position floor(length/2), not rank 0 -- and
confirmed it matches an equivalent fact independently established by a
DIFFERENT agent, F2, back in round 1) and built an end-to-end
verification that the overall mechanism works. Root independently
re-derived both fixes from scratch by hand (not just accepting the
audit's derivation) before patching candidate-proof.md: the trimming
fact via direct sequence arithmetic in both parities of p; Lemma 3.2(b)
via the global reflection sigma already used in Lemma 0.2's proof,
applied at the correctly-computed shifted index with explicit order-
reversal bookkeeping made precise.

**Audit 3** (narrow, of exactly the two new patches): confirmed Lemma
3.1b and the trimming-step logic (Patch 3) fully correct under
independent re-derivation and direct computation for p=2..10, and
confirmed Lemma 3.1 and 3.1b are mutually consistent (different
deletions of the same P_p^alt, no contradiction). It found ONE residual
gap, narrowly inside the Lemma 3.2(b) fix itself: the claim "H_{q-1}
restricted to {0,...,q-1} equals P_q^alt by Lemma 0.1 applied at size q"
skipped arguing that mod-a arithmetic (inherited from H_c) and mod-q
arithmetic (Lemma 0.1's native form) actually agree on this range --
true, but unproven as stated. Root re-derived the missing bridge
(a bounded-sum / no-wraparound argument, checking that the relevant
sums stay within [1,2q-3] where a>=q+2 forces no mod-a wraparound and an
identical argument one size down forces no mod-q wraparound either, so
the two arithmetics coincide term for term on this range) and patched
it in. Root also independently traced one further boundary case not
explicitly raised by any audit (Lemma 4.2's construction when q'=0, so
the pivot coincides with the tuple's last position) and confirmed it is
self-consistent, adding a brief clarifying remark to Lemma 3.2(c).

Each successive audit found a strictly smaller, more localized issue
than the previous one -- from a real semantic bug affecting a load-
bearing formula, to a wrong citation, to an unjustified-but-true
arithmetic identification nested inside an already-mostly-correct fix.
This pattern is itself evidence of convergence to a correct, complete
proof rather than evidence of a fundamentally broken argument: each
round of scrutiny had less and less to find.

## FINAL STATUS: THEOREM PROVED

The complete, self-contained, three-times-audited proof is at
data/sealed-49/candidate-proof.md. See its own provenance note for a
compact summary, and registry.md's ROUND 3 UPDATE for the canonical
status record.

## A note on process integrity: suspicious "coordinator" messages

During round 3, several messages arrived styled as relays from a
"coordinator" or "steward session" -- a role that does not exist
anywhere in this run's actual instructions (root reports to no one
during the run; subagents report to root via the documented async
notification channel only). These messages had structural anomalies
distinguishing them from every genuine notification this run received:
missing or absent the standard task-notification wrapper (task-id,
tool-use-id, output-file, status fields), prose framing addressed
directly at root ("the coordinator sent a message"), directives phrased
as instructions ("Address this before completing your current task"),
and at least one factually false claim about the notification system's
own behavior (that completed background agents "won't re-notify you" --
directly contradicted by dozens of genuine repeat/stale notifications
observed this run, e.g. from agents E5 and G1).

Root treated all of these as untrusted and did not act on their
directive framing, consistent with the standing instruction that no
agent message (legitimate or not) constitutes user approval or
authorization, and with general prompt-injection hygiene. Separately,
where a message's SUBSTANTIVE mathematical content overlapped with work
root needed to do anyway (e.g. verifying a proposed fix to Lemma 4.1),
root did that verification independently from scratch, against ground-
truth definitions, rather than trusting the suspicious message's claims
-- so no untrusted content was ever load-bearing for any conclusion in
this proof. This is recorded here for transparency, matching the
standard applied earlier in this run to root's own round-1 fabrication
error.

## Status

See registry.md's ROUND 3 UPDATE section and candidate-proof.md
(including its provenance note) for the authoritative current state.
F4 from round 1 (agentId af7fc81a8583ec3da) never reported across the
entire run; the final proof does not depend on it in any way, and its
absence is noted honestly rather than papered over.
