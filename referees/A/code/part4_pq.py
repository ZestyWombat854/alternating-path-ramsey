"""Machine-check Part 4 (P(m),Q(m), Lemma 4.1 recursion) and Part 5
(Aggregate Sum Theorem) directly from the BASE DEFINITIONS in the proof's
Part 4 (not from the recursion itself), on all graphs up to n=6 incl.
degenerate cases (empty graph, isolated vertices, |W|<=1).
"""
import itertools
from functools import lru_cache


@lru_cache(maxsize=None)
def p_alt_edges(p):
    if p == 0:
        return ()
    seq = []
    for t in range((p + 1) // 2):
        seq.append(t)
        if len(seq) < p:
            seq.append(p - 1 - t)
    seq = seq[:p]
    edges = set()
    for i in range(p - 1):
        edges.add(tuple(sorted((seq[i], seq[i + 1]))))
    return tuple(edges)


def all_graphs(n):
    verts = list(range(n))
    pairs = list(itertools.combinations(verts, 2))
    for bits in itertools.product((0, 1), repeat=len(pairs)):
        E = frozenset(p for p, b in zip(pairs, bits) if b)
        yield verts, E


def edge_in(E, x, y):
    a, b = (x, y) if x < y else (y, x)
    return (a, b) in E


def realizes_as_P(E, tup, p):
    for i, j in p_alt_edges(p):
        if not edge_in(E, tup[i], tup[j]):
            return False
    return True


def realizes_as_Q(E, tup, q):
    for i, j in p_alt_edges(q):
        if not edge_in(E, tup[q - 1 - i], tup[q - 1 - j]):
            return False
    return True


def P_of(E, m, ambient):
    cand = [v for v in ambient if v < m]
    for p in range(len(cand), 0, -1):
        for tup in itertools.combinations(cand, p):
            if realizes_as_P(E, tup, p) and edge_in(E, tup[0], m):
                return p
    return 0


def Q_of(E, m, ambient):
    cand = [v for v in ambient if v > m]
    for q in range(len(cand), 0, -1):
        for tup in itertools.combinations(cand, q):
            if realizes_as_Q(E, tup, q) and edge_in(E, tup[q - 1], m):
                return q
    return 0


def P_recursion(E, m, W):
    best = 0
    for l in W:
        if l >= m or not edge_in(E, l, m):
            continue
        window = [v for v in W if l < v < m]
        val = 1 + Q_of(E, l, window)
        best = max(best, val)
    return best


def Q_recursion(E, m, W):
    best = 0
    for r in W:
        if r <= m or not edge_in(E, r, m):
            continue
        window = [v for v in W if m < v < r]
        val = 1 + P_of(E, r, window)
        best = max(best, val)
    return best


def run(nmax):
    mismatches_41P = []
    mismatches_41Q = []
    agg_failures = []
    total_graphs = 0
    for n in range(0, nmax + 1):
        for W, E in all_graphs(n):
            total_graphs += 1
            Ps = {m: P_of(E, m, W) for m in W}
            Qs = {m: Q_of(E, m, W) for m in W}
            for m in W:
                rp = P_recursion(E, m, W)
                if rp != Ps[m]:
                    mismatches_41P.append((n, list(E), m, Ps[m], rp))
                rq = Q_recursion(E, m, W)
                if rq != Qs[m]:
                    mismatches_41Q.append((n, list(E), m, Qs[m], rq))
            total = sum(Ps[m] + Qs[m] for m in W)
            if total < 2 * len(E):
                agg_failures.append((n, list(E), total, 2 * len(E)))
    return total_graphs, mismatches_41P, mismatches_41Q, agg_failures


if __name__ == "__main__":
    import sys
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    tg, m1, m2, af = run(nmax)
    print(f"n=0..{nmax}: total graphs checked = {tg}")
    print(f"Lemma 4.1 P-recursion mismatches: {len(m1)}")
    for x in m1[:5]:
        print("  ", x)
    print(f"Lemma 4.1 Q-recursion mismatches: {len(m2)}")
    for x in m2[:5]:
        print("  ", x)
    print(f"Theorem 5 aggregate-sum failures (sum < 2|E|): {len(af)}")
    for x in af[:5]:
        print("  ", x)
    print("ALL_PASS:", len(m1) == 0 and len(m2) == 0 and len(af) == 0)
