"""Direct checks of Lemma 3.1, 3.1b, 3.2 (Part 3)."""
import itertools


def p_alt_seq(p):
    seq = []
    for t in range((p + 1) // 2):
        seq.append(t)
        if len(seq) < p:
            seq.append(p - 1 - t)
    return seq[:p]


def p_alt_edges(p):
    seq = p_alt_seq(p)
    return frozenset(frozenset((seq[i], seq[i + 1])) for i in range(p - 1))


def mirror(edges, size):
    return frozenset(frozenset((size - 1 - i, size - 1 - j)) for e in edges for i, j in [tuple(e)])


def degree(edges, v):
    return sum(1 for e in edges if v in e)


def neighbors(edges, v):
    return {list(e - {v})[0] for e in edges if v in e}


def check_lemma31(p):
    E = p_alt_edges(p)
    d0 = degree(E, 0)
    n0 = neighbors(E, 0)
    ok1 = d0 == 1 and n0 == {p - 1}
    # delete vertex 0, relabel {1..p-1}->{0..p-2} (subtract 1)
    E2 = frozenset(frozenset((i - 1, j - 1)) for e in E if 0 not in e for i, j in [tuple(e)])
    target = mirror(p_alt_edges(p - 1), p - 1) if p >= 2 else frozenset()
    ok2 = E2 == target
    return ok1 and ok2, (p, d0, n0, ok1, ok2)


def check_lemma31b(p):
    seq = p_alt_seq(p)
    e = p // 2
    E = p_alt_edges(p)
    d_e = degree(E, e)
    ok1 = d_e == 1
    ok2 = seq[-1] == e and e not in seq[:-1]
    # delete e via order-isomorphism, compare to P_{p-1}^alt directly
    below = sorted(v for v in range(p) if v != e)
    relabel = {v: i for i, v in enumerate(below)}
    E2 = frozenset(frozenset((relabel[i], relabel[j])) for e_ in E if e not in e_ for i, j in [tuple(e_)])
    target = p_alt_edges(p - 1) if p >= 2 else frozenset()
    ok3 = E2 == target
    # also: resulting sequence = original sequence with last term dropped, relabeled
    ok4 = [relabel[x] for x in seq[:-1]] == p_alt_seq(p - 1)
    return ok1 and ok2 and ok3 and ok4, (p, e, d_e, ok1, ok2, ok3, ok4)


def M(a, c):
    return frozenset(frozenset((i, j)) for i, j in itertools.combinations(range(a), 2) if (i + j) % a == c)


def H(a, c):
    return M(a, c) | M(a, (c + 1) % a)


def check_lemma32(a):
    results = []
    for c in range(0, a - 1):
        p = c + 1
        q = a - 1 - p
        Hc = H(a, c)
        # (a) restrict to {0,...,p-1}
        restrict_left = frozenset(e for e in Hc if all(x < p for x in e))
        target_left = p_alt_edges(p)
        ok_a = restrict_left == target_left
        # (b) restrict to {p+1,...,a-1}, relabel down by p+1
        restrict_right_raw = frozenset(e for e in Hc if all(x > p for x in e))
        restrict_right = frozenset(frozenset((i - (p + 1), j - (p + 1))) for e in restrict_right_raw for i, j in [tuple(e)])
        target_right = mirror(p_alt_edges(q), q) if q >= 1 else frozenset()
        ok_b = restrict_right == target_right
        # (c) pivot p's edges
        pivot_edges = frozenset(e for e in Hc if p in e)
        if q >= 1:
            expected_pivot = frozenset({frozenset((0, p)), frozenset((p, a - 1))})
        else:
            expected_pivot = frozenset({frozenset((0, p))})
        ok_c = pivot_edges == expected_pivot
        results.append((c, p, q, ok_a, ok_b, ok_c))
    return results


if __name__ == "__main__":
    print("=== Lemma 3.1 (peel rank 0 -> mirror(P_{p-1}^alt)) ===")
    fail31 = [check_lemma31(p)[1] for p in range(2, 16) if not check_lemma31(p)[0]]
    print("tested p=2..15, failures:", fail31)

    print("=== Lemma 3.1b (peel e=floor(p/2) -> P_{p-1}^alt directly) ===")
    fail31b = [check_lemma31b(p)[1] for p in range(2, 16) if not check_lemma31b(p)[0]]
    print("tested p=2..15, failures:", fail31b)

    print("=== Lemma 3.2 (pivot decomposition of H_c) ===")
    all_fail32 = []
    for a in range(3, 16):
        for row in check_lemma32(a):
            c, p, q, ok_a, ok_b, ok_c = row
            if not (ok_a and ok_b and ok_c):
                all_fail32.append((a,) + row)
    print("tested a=3..15, all c in 0..a-2, failures:", all_fail32)

    print("ALL_PASS:", not fail31 and not fail31b and not all_fail32)
