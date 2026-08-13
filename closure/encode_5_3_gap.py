#!/usr/bin/env python3
"""
encode_5_3_gap.py -- PREP49's independent closure of referee B's declared
NOT-DONE gap: the (5,3) cell's UPPER leg, R_dih(P_5^alt, K_3) <= 9, i.e.
UNSAT of "no colour-1 Dih(5)-copy of P_5^alt and no colour-2 K_3" at n=9.

Referee B (report.md in this bundle, section 3, NOT-DONE block) completed
the lower-bound leg at (5,3) (Theorem 1's explicit construction, avoids
both targets at n=8) but explicitly did not complete the upper-bound leg
at n=9 (2^36 colourings, called infeasible by brute force within their
budget; no SAT solver was substituted). Referee A's own 8-cell SAT sweep
-- (4,2),(5,2),(4,3),(5,3),(6,3),(4,4),(6,2),(7,2) -- already includes
(5,3) (data/cnf_5_3.cnf in referees/A/data/ in this bundle), so the
upper leg already had ONE independent SAT confirmation before this
script ran. This script is a SECOND, independent one, written fresh for
the bundle rather than reused, so the cell that referee B flagged as its
own gap has independent SAT coverage from a source outside both
referees' own code (per the task brief: "do NOT reuse the referees'
encoders -- independence").

Written from data/sealed-49/statement.md's definitions ONLY (the copy of
that file living beside this one, at ../statement.md). Does not import,
read, or share a single line with referees/A/code/*.py or
referees/B/code/*.py -- verified by construction (typed fresh below, no
shared helper module).

ENCODING. One Boolean CNF variable x_{u,v} per unordered pair {u,v} of
[n] (u<v), TRUE iff {u,v} has colour 2, FALSE iff colour 1.

Family 1 (forbid a colour-1 Dih(5)-copy of P_5alt): for every increasing
map v:[5]->[n] (i.e. every increasing 5-tuple, one per 5-subset of [n])
and every gamma in Dih(5): a clause with one POSITIVE literal per edge
{i,j} of P_5alt, evaluated as the pair {v(gamma(i)), v(gamma(j))} --
exactly statement.md's Gamma-copy definition, applied literally (not via
any H_c/mirror reformulation). This clause is satisfiable only if at
least one such image pair is colour 2, i.e. it forbids that specific
(v,gamma) witnessing an all-colour-1 copy.

Family 2 (forbid a colour-2 K_3): statement.md notes K_b's Gamma-copy
notion is group/shape-independent and coincides with an ordinary
monochromatic clique for every Gamma -- so no group machinery is needed
here at all. For every 3-subset S of [n]: a clause with one NEGATIVE
literal per edge of the complete graph on S.

n = 1+(5-1)(3-1) = 9. Theorem 7 predicts UNSAT at n=9 (upper bound) and
SAT at n=8 (lower bound, Theorem 1's construction). Both legs are run
below: n=8 first, as a self-check (if n=8 were also UNSAT, that would
mean this encoding is bugged -- over-constrained -- and the n=9 verdict
would not be trustworthy either), then n=9, the actual target. The n=8
SAT witness is additionally validated by an independently-written
brute-force checker (a second code path from the clause generator, so an
encoding bug would have to appear identically in both to go undetected).

No DRAT certificate is produced for the n=9 UNSAT leg (per the task
brief: "no DRAT needed for staging; note it"). kissat's own exit code
(20 = UNSAT) and full log are the evidence retained here; a DRAT proof
could be added later if this closure is promoted from staging-completeness
to a certified artifact at the same rigor as the theorem-b-cert-debt/ and
referees/A cells (which trim-verify their UNSAT legs).

Usage: python3 encode_5_3_gap.py [outdir]
Exits 0 iff n=8 is SAT (self-check passes) and n=9 is UNSAT (gap closed).
"""
import itertools
import math
import os
import subprocess
import sys
from datetime import datetime, timezone

A = 5
B = 3

KISSAT = os.environ.get("KISSAT") or "kissat"
TIMEOUT_S = 20 * 60  # 20 minute cap per the task brief


# ---------------------------------------------------------------------------
# Objects, built fresh from statement.md's definitions only.
# ---------------------------------------------------------------------------

def alt_path_edges(a):
    """P_a^alt: edges are the consecutive pairs of the sequence
    (0, a-1, 1, a-2, 2, a-3, ...) -- statement.md's own wording, typed
    directly (not copied from any proof/referee helper)."""
    seq = [0]
    lo, hi = 1, a - 1
    take_hi = True
    while len(seq) < a:
        if take_hi:
            seq.append(hi)
            hi -= 1
        else:
            seq.append(lo)
            lo += 1
        take_hi = not take_hi
    assert sorted(seq) == list(range(a)), (a, seq)
    return [tuple(sorted((seq[i], seq[i + 1]))) for i in range(a - 1)]


def identity_perm(m):
    return tuple(range(m))


def compose(p, q):
    """(p after q): apply q first, then p."""
    return tuple(p[q[i]] for i in range(len(q)))


def dihedral_group(m):
    """Dih(m) = <rho, sigma>, rho(i)=i+1 (mod m), sigma(i)=m-1-i --
    statement.md's own generators, closed by BFS (no assumed size)."""
    rho = tuple((i + 1) % m for i in range(m))
    sigma = tuple((m - 1 - i) for i in range(m))
    seen = {identity_perm(m)}
    frontier = [identity_perm(m)]
    while frontier:
        nxt = []
        for p in frontier:
            for g in (rho, sigma):
                q = compose(g, p)
                if q not in seen:
                    seen.add(q)
                    nxt.append(q)
        frontier = nxt
    return sorted(seen)


# Sanity checks against statement.md's own worked examples, before anything
# else runs.
assert set(map(frozenset, alt_path_edges(4))) == {frozenset(e) for e in
                                                    [(0, 3), (3, 1), (1, 2)]}
assert set(map(frozenset, alt_path_edges(5))) == {frozenset(e) for e in
                                                    [(0, 4), (4, 1), (1, 3), (3, 2)]}
_dih5_check = dihedral_group(5)
assert len(_dih5_check) == 10, len(_dih5_check)  # |Dih(5)| = 2*5


# ---------------------------------------------------------------------------
# CNF construction.
# ---------------------------------------------------------------------------

def build_cnf(n):
    pairs = list(itertools.combinations(range(n), 2))
    vid = {p: i + 1 for i, p in enumerate(pairs)}
    base_edges = alt_path_edges(A)
    dih_a = dihedral_group(A)

    clauses = []
    for v in itertools.combinations(range(n), A):
        for gamma in dih_a:
            lits = []
            for (i, j) in base_edges:
                u1, u2 = v[gamma[i]], v[gamma[j]]
                pair = (u1, u2) if u1 < u2 else (u2, u1)
                lits.append(vid[pair])
            clauses.append(lits)
    for s in itertools.combinations(range(n), B):
        clauses.append([-vid[(x, y)] for (x, y) in itertools.combinations(s, 2)])

    expected = math.comb(n, A) * len(dih_a) + math.comb(n, B)
    assert len(clauses) == expected, (len(clauses), expected)
    return vid, pairs, clauses


def write_dimacs(path, nvars, clauses, comment):
    with open(path, "w") as f:
        f.write(f"c {comment}\n")
        f.write(f"p cnf {nvars} {len(clauses)}\n")
        for c in clauses:
            f.write(" ".join(map(str, c)) + " 0\n")


def parse_model(kissat_stdout):
    lits = []
    for line in kissat_stdout.splitlines():
        if line.startswith("v "):
            lits.extend(int(x) for x in line[2:].split())
    return {abs(l): (l > 0) for l in lits if l != 0}


# ---------------------------------------------------------------------------
# Independent brute-force checker (separate code path from build_cnf, for
# validating the n=8 SAT witness -- catches encoding bugs that a
# self-consistent-but-wrong CNF generator would not catch on its own).
# ---------------------------------------------------------------------------

def colour1_has_dih5_copy(colour2_pairs, n):
    """True iff some increasing v:[5]->[n], gamma in Dih(5) has every
    P_5alt edge landing on a pair NOT in colour2_pairs (i.e. colour 1)."""
    base_edges = alt_path_edges(A)
    dih_a = dihedral_group(A)
    for v in itertools.combinations(range(n), A):
        for gamma in dih_a:
            ok = True
            for (i, j) in base_edges:
                u1, u2 = v[gamma[i]], v[gamma[j]]
                pair = (u1, u2) if u1 < u2 else (u2, u1)
                if pair in colour2_pairs:
                    ok = False
                    break
            if ok:
                return True, v, gamma
    return False, None, None


def colour2_has_k3(colour2_pairs, n):
    for s in itertools.combinations(range(n), B):
        if all((x, y) in colour2_pairs for (x, y) in itertools.combinations(s, 2)):
            return True, s
    return False, None


# ---------------------------------------------------------------------------
# Driver.
# ---------------------------------------------------------------------------

def run_leg(n, outdir, expect):
    vid, pairs, clauses = build_cnf(n)
    base = os.path.join(outdir, f"5_3_n{n}")
    write_dimacs(base + ".cnf", len(pairs), clauses,
                 f"PREP49 independent closure: (P_5alt,Dih(5)) vs K_3, n={n}; "
                 f"expect {expect}; encoded fresh from statement.md, not the "
                 f"referees' encoders")
    try:
        proc = subprocess.run([KISSAT, "--no-binary", base + ".cnf"],
                               capture_output=True, text=True, timeout=TIMEOUT_S)
        rc, out = proc.returncode, proc.stdout + proc.stderr
        timed_out = False
    except subprocess.TimeoutExpired as e:
        rc, out = None, (e.stdout or "") + (e.stderr or "")
        timed_out = True
    with open(base + ".kissat.log", "w") as f:
        f.write(out)

    result = {"n": n, "vars": len(pairs), "clauses": len(clauses),
              "kissat_exit": rc, "timed_out": timed_out, "expect": expect}

    if rc == 10:  # SAT
        model = parse_model(out)
        colour2 = {p for p in pairs if model.get(vid[p], False)}
        has_p5, wit_v, wit_g = colour1_has_dih5_copy(colour2, n)
        has_k3, wit_s = colour2_has_k3(colour2, n)
        independent_check_clean = (not has_p5) and (not has_k3)
        result["verdict"] = "SAT"
        result["independent_witness_check"] = independent_check_clean
        with open(base + ".witness.txt", "w") as f:
            f.write(f"c n={n}: decoded witness (colour1=default, colour2=marked)\n")
            f.write(f"c colour-2 pairs: {sorted(colour2)}\n")
            f.write(f"c independent brute-force check (separate code path): "
                    f"no colour-1 Dih(5)-copy of P_5alt: {not has_p5}; "
                    f"no colour-2 K_3: {not has_k3}\n")
            if has_p5:
                f.write(f"c !! FALSE WITNESS: v={wit_v} gamma={wit_g}\n")
            if has_k3:
                f.write(f"c !! FALSE WITNESS: K_3 on {wit_s}\n")
    elif rc == 20:  # UNSAT
        result["verdict"] = "UNSAT"
        result["independent_witness_check"] = None  # n/a; no witness to check
    else:
        result["verdict"] = f"INCONCLUSIVE (exit={rc}, timed_out={timed_out})"
        result["independent_witness_check"] = None

    return result


def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
    os.makedirs(outdir, exist_ok=True)

    print("Self-check leg: n=8 (lower bound, Theorem 1's construction), expect SAT")
    r8 = run_leg(8, outdir, "SAT (lower bound: R_dih(P_5alt,K_3) > 8)")
    print(f"  n=8: kissat exit={r8['kissat_exit']} verdict={r8['verdict']} "
          f"independent_witness_check={r8['independent_witness_check']}")

    print("Target leg: n=9 (upper bound -- referee B's declared gap), expect UNSAT")
    r9 = run_leg(9, outdir, "UNSAT (upper bound: R_dih(P_5alt,K_3) <= 9)")
    print(f"  n=9: kissat exit={r9['kissat_exit']} verdict={r9['verdict']}")

    gap_closed = (r8["verdict"] == "SAT" and r8["independent_witness_check"] is True
                  and r9["verdict"] == "UNSAT")

    summary = {
        "script": "encode_5_3_gap.py",
        "run_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "purpose": "Close referee B's declared NOT-DONE gap: (5,3) cell upper leg",
        "kissat_binary": KISSAT,
        "n8_selfcheck": r8,
        "n9_target": r9,
        "gap_closed": gap_closed,
        "conclusion": ("R_dih(P_5alt,K_3) = 9 -- both legs independently confirmed "
                        "(n=8 SAT with a brute-force-validated witness, n=9 UNSAT); "
                        "referee B's gap is closed" if gap_closed else
                        "INCOMPLETE -- see legs above"),
        "note": "No DRAT certificate generated for the n=9 UNSAT leg (staging-only "
                "closure per the task brief; kissat's exit code 20 and full log are "
                "the evidence retained here).",
    }
    import json
    with open(os.path.join(outdir, "results.json"), "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nVERDICT: {summary['conclusion']}")
    print(f"Artifacts in {outdir}/")
    return 0 if gap_closed else 1


if __name__ == "__main__":
    sys.exit(main())
