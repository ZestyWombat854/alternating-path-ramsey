"""
Adversarial re-derivation, by direct computation, of Part 0 and Part 3's
internal machinery (H_c, mirror, Lemma 3.1, Lemma 3.1b, Lemma 3.2 pivot
decomposition) -- the flagged priority attack surfaces: mod-a index
arithmetic, parity split of the dihedral action, and pivot/decomposition
boundary behavior (q=0 degeneration).

H_c/M_c/mirror are coded directly from Part 0 / Part 3's definitions
(typed in independently here, not imported from any proof-derived
formula), then every stated identity is checked by brute-force set
comparison -- NOT by re-running the proof's own algebraic argument.
P_a^alt itself comes from defs.py (statement.md), so Lemma 0.1
(P_a^alt = H_{a-1}) is also cross-checked here as the anchor linking
the two.
"""
import itertools
from defs import palt_edges

OUT = "../data/lemmas_part3.txt"


def palt_edges_ext(p):
    if p in (0, 1):
        return frozenset()
    return palt_edges(p)


def seq(a):
    """The defining sequence (0,a-1,1,a-2,...) of length a."""
    out = []
    for t in range((a + 1) // 2):
        out.append(t)
        if len(out) < a:
            out.append(a - 1 - t)
    return out[:a]


def M_c(a, c):
    c = c % a
    return frozenset(frozenset((i, j)) for i in range(a) for j in range(a)
                      if i != j and (i + j) % a == c)


def H_c(a, c):
    return M_c(a, c) | M_c(a, c + 1)


def mirror(edges, k):
    return frozenset(frozenset((k - 1 - i, k - 1 - j)) for e in edges for (i, j) in [tuple(e)])


def degree(edges, v):
    return sum(1 for e in edges if v in e)


def main():
    lines = []
    ok_all = True

    # --- Lemma 0.1: P_a^alt = H_{a-1}, for a=3..20 ---
    lines.append("=== Lemma 0.1: P_a^alt == H_{a-1} ===")
    l01_ok = True
    for a in range(3, 21):
        lhs = palt_edges(a)
        rhs = H_c(a, a - 1)
        match = (lhs == rhs)
        l01_ok &= match
        if not match:
            lines.append(f"  MISMATCH a={a}: P_a^alt={sorted(map(sorted,lhs))} H_(a-1)={sorted(map(sorted,rhs))}")
    lines.append(f"Lemma 0.1 holds for a=3..20: {l01_ok}")
    ok_all &= l01_ok
    lines.append("")

    # --- Lemma 3.1: rank-0 peeling ---
    lines.append("=== Lemma 3.1: rank-0 degree 1 (edge to rank p-1); delete+relabel = mirror(P_{p-1}^alt) ===")
    l31_ok = True
    for p in range(2, 21):
        edges = palt_edges_ext(p)
        deg0 = degree(edges, 0)
        edge_ok = (deg0 == 1) and (frozenset((0, p - 1)) in edges)
        remaining = frozenset(e for e in edges if 0 not in e)
        relabeled = frozenset(frozenset((i - 1, j - 1)) for e in remaining for (i, j) in [tuple(e)])
        target = mirror(palt_edges_ext(p - 1), p - 1)
        match = (relabeled == target)
        ok = edge_ok and match
        l31_ok &= ok
        if not ok:
            lines.append(f"  MISMATCH p={p}: deg0={deg0} edge_ok={edge_ok} relabeled={sorted(map(sorted,relabeled))} target={sorted(map(sorted,target))}")
    lines.append(f"Lemma 3.1 holds for p=2..20: {l31_ok}")
    ok_all &= l31_ok
    lines.append("")

    # --- Lemma 3.1b: far-endpoint trimming ---
    lines.append("=== Lemma 3.1b: e=floor(p/2) degree 1, last seq position; delete+order-iso = P_{p-1}^alt directly ===")
    l31b_ok = True
    for p in range(2, 21):
        edges = palt_edges_ext(p)
        e_val = p // 2
        s = seq(p)
        deg_e = degree(edges, e_val)
        last_pos_ok = (s[-1] == e_val) and (s.index(e_val) == p - 1)  # occurs ONLY at last position
        remaining = frozenset(ed for ed in edges if e_val not in ed)

        def phi(x):
            return x if x < e_val else x - 1

        relabeled = frozenset(frozenset((phi(i), phi(j))) for ed in remaining for (i, j) in [tuple(ed)])
        target = palt_edges_ext(p - 1)
        match = (relabeled == target)
        rank0_untouched = (e_val != 0) or (p <= 1)  # e>=1 for p>=2, so rank0 should never equal e_val
        ok = (deg_e == 1) and last_pos_ok and match and (e_val >= 1)
        l31b_ok &= ok
        if not ok:
            lines.append(f"  MISMATCH p={p}: e={e_val} deg_e={deg_e} last_pos_ok={last_pos_ok} match={match} seq={s}")
    lines.append(f"Lemma 3.1b holds for p=2..20: {l31b_ok}")
    ok_all &= l31b_ok
    lines.append("")

    # --- Lemma 3.2: pivot decomposition, a=3..20, all c in {0,...,a-2} (both parities of a and q) ---
    lines.append("=== Lemma 3.2: pivot decomposition H_c, a=3..20, all c in 0..a-2 ===")
    l32_ok = True
    fail_count = 0
    checked = 0
    for a in range(3, 21):
        for c in range(0, a - 1):
            p = c + 1
            q = a - 1 - p
            Hc = H_c(a, c)
            checked += 1

            # (a) restrict to {0,...,p-1}
            sub_a = frozenset(e for e in Hc if all(v < p for v in e))
            target_a = palt_edges_ext(p)
            ok_a = (sub_a == target_a)

            # (b) restrict to {p+1,...,a-1}, relabel down by p+1
            sub_b_raw = frozenset(e for e in Hc if all(v >= p + 1 for v in e))
            sub_b = frozenset(frozenset((i - (p + 1), j - (p + 1))) for e in sub_b_raw for (i, j) in [tuple(e)])
            target_b = mirror(palt_edges_ext(q), q) if q > 0 else frozenset()
            ok_b = (sub_b == target_b)

            # (c) pivot p's edges
            pivot_edges = frozenset(e for e in Hc if p in e)
            if q == 0:
                target_c = frozenset({frozenset((0, p))})
            else:
                target_c = frozenset({frozenset((0, p)), frozenset((p, a - 1))})
            ok_c = (pivot_edges == target_c)

            if not (ok_a and ok_b and ok_c):
                fail_count += 1
                l32_ok = False
                if fail_count <= 15:
                    lines.append(f"  MISMATCH a={a} c={c} (p={p},q={q}): ok_a={ok_a} ok_b={ok_b} ok_c={ok_c}")
                    if not ok_a:
                        lines.append(f"    sub_a={sorted(map(sorted,sub_a))} target_a={sorted(map(sorted,target_a))}")
                    if not ok_b:
                        lines.append(f"    sub_b={sorted(map(sorted,sub_b))} target_b={sorted(map(sorted,target_b))}")
                    if not ok_c:
                        lines.append(f"    pivot={sorted(map(sorted,pivot_edges))} target_c={sorted(map(sorted,target_c))}")
    lines.append(f"Lemma 3.2 checked {checked} (a,c) pairs, a=3..20; ALL PASS: {l32_ok} (failures: {fail_count})")
    ok_all &= l32_ok
    lines.append("")

    lines.append(f"=== GRAND RESULT: Lemma 0.1, 3.1, 3.1b, 3.2 all hold: {ok_all} ===")

    text = "\n".join(lines)
    with open(OUT, "w") as f:
        f.write(text + "\n")
    print(text)
    print("Full output:", OUT)


if __name__ == "__main__":
    main()
