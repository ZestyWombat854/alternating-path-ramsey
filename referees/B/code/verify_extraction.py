"""
End-to-end check of Theorem 6 (Extraction Lemma): for a=4, every graph G
on n<=6 vertices with delta(G) >= a-1 = 3 must contain a Dih(4)-copy of
P_4^alt (as an uncolored subgraph: an increasing v and gamma in Dih(4)
with every edge of gamma(P_4^alt) an edge of G).

This uses ONLY defs.py (statement.md's own Gamma-copy definition, via
the orbit formulation) -- it does NOT go through the proof's P(m)/Q(m)
or H_c machinery at all. It is an independent, direct test of the
theorem's practical conclusion, exhaustive over all graphs with the
hypothesis satisfied at every reachable n.
"""
import itertools
from defs import palt_edges, dihedral_group, orbit_of_graph

OUT = "../data/extraction_a4.txt"


def has_orbit_copy(orbit, a, n, adj):
    for v in itertools.combinations(range(n), a):
        for H in orbit:
            if all(adj[v[i]][v[j]] for e in H for (i, j) in [tuple(e)]):
                return True
    return False


def main():
    a = 4
    edges = palt_edges(a)
    G = dihedral_group(a)
    orbit = orbit_of_graph(edges, a, G)
    assert len(orbit) == a

    lines = []
    lines.append(f"Extraction Lemma (Theorem 6) direct check, a={a} (delta>=a-1={a-1}).")
    lines.append("For every graph on n<=6 with min degree >= 3, does a Dih(4)-copy of")
    lines.append("P_4^alt exist as an (uncolored) subgraph? Checked via statement.md's")
    lines.append("own orbit-based Gamma-copy definition (defs.py), independent of the")
    lines.append("proof's P(m)/Q(m) machinery.")
    lines.append("")

    total_checked = 0
    total_failed = 0
    fail_examples = []

    for n in range(4, 7):
        edge_list = list(itertools.combinations(range(n), 2))
        E = len(edge_list)
        checked_n = 0
        failed_n = 0
        for mask in range(1 << E):
            adj = [[False] * n for _ in range(n)]
            for idx, (i, j) in enumerate(edge_list):
                if (mask >> idx) & 1:
                    adj[i][j] = adj[j][i] = True
            deg = [sum(adj[x]) for x in range(n)]
            if min(deg) < a - 1:
                continue
            checked_n += 1
            ok = has_orbit_copy(orbit, a, n, adj)
            if not ok:
                failed_n += 1
                fail_examples.append((n, mask))
        total_checked += checked_n
        total_failed += failed_n
        lines.append(f"n={n}: graphs with delta>={a-1}: {checked_n:5d}   failures: {failed_n}")

    lines.append("")
    lines.append(f"TOTAL graphs with delta>={a-1} checked: {total_checked}, failures: {total_failed}")
    lines.append(f"THEOREM 6 (a=4) HOLDS ON ALL REACHABLE CASES (n<=6): {total_failed == 0}")
    if fail_examples:
        lines.append(f"Failure examples (n,mask): {fail_examples[:10]}")

    text = "\n".join(lines)
    with open(OUT, "w") as f:
        f.write(text + "\n")
    print(text)
    print("Full output:", OUT)


if __name__ == "__main__":
    main()
