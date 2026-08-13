"""Black-box check of Lemma 4.2 (Reduction) and Theorem 6 (Extraction Lemma)
end-to-end conclusions, independent of the P(m)/Q(m) construction: given
P(m)+Q(m)>=a-1 (resp. delta(G)>=a-1), directly search the WHOLE graph for
an increasing embedding of some gamma(P_a^alt), gamma in Dih(a).
"""
import itertools
import sys

sys.path.insert(0, ".")
from common import dih_orbit_edges
from part4_pq import all_graphs, edge_in, P_of, Q_of


def graph_has_Hc_embedding(E, W, orbit_edges):
    for edges in orbit_edges:
        a = max(max(e) for e in edges) + 1
        for v in itertools.combinations(W, a):
            if all(edge_in(E, v[i], v[j]) for i, j in edges):
                return True
    return False


def min_degree(E, W):
    if not W:
        return None
    deg = {w: 0 for w in W}
    for x, y in E:
        deg[x] += 1
        deg[y] += 1
    return min(deg.values())


def run(nmax, avals):
    orbit_cache = {a: dih_orbit_edges(a) for a in avals}
    lemma42_checked = 0
    lemma42_fail = []
    thm6_checked = 0
    thm6_fail = []
    for n in range(0, nmax + 1):
        for W, E in all_graphs(n):
            Ps = {m: P_of(E, m, W) for m in W}
            Qs = {m: Q_of(E, m, W) for m in W}
            for a in avals:
                if n < a:
                    continue
                orbit = orbit_cache[a]
                # Lemma 4.2: any m with P+Q>=a-1 should force an H_c embedding.
                if any(Ps[m] + Qs[m] >= a - 1 for m in W):
                    lemma42_checked += 1
                    if not graph_has_Hc_embedding(E, W, orbit):
                        lemma42_fail.append((n, a, list(E)))
                # Theorem 6: delta(G)>=a-1 should force an H_c embedding.
                d = min_degree(E, W)
                if d is not None and d >= a - 1:
                    thm6_checked += 1
                    if not graph_has_Hc_embedding(E, W, orbit):
                        thm6_fail.append((n, a, list(E)))
    return lemma42_checked, lemma42_fail, thm6_checked, thm6_fail


if __name__ == "__main__":
    nmax = int(sys.argv[1]) if len(sys.argv) > 1 else 6
    avals = [4, 5, 6]
    c42, f42, c6, f6 = run(nmax, avals)
    print(f"Lemma 4.2 trigger instances checked: {c42}, failures: {len(f42)}")
    for x in f42[:5]:
        print("  ", x)
    print(f"Theorem 6 trigger instances checked: {c6}, failures: {len(f6)}")
    for x in f6[:5]:
        print("  ", x)
    print("ALL_PASS:", len(f42) == 0 and len(f6) == 0)
