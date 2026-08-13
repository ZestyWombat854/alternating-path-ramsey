"""
Task 3(c): machine-check the proof's per-vertex quantities P(m), Q(m)
(Part 4) and its aggregate inequality (Theorem 5) on ALL labeled graphs
to n=6, including degenerate cases (empty graph, isolated vertices,
n<=1).

Two INDEPENDENT implementations of P(m), Q(m) are cross-checked against
each other on every vertex of every graph:
  (1) brute_P / brute_Q: direct brute-force search over all witnessing
      tuples, straight from Part 4's Definition (not using Lemma 4.1).
  (2) rec_P / rec_Q: Lemma 4.1's windowed recursion formula, coded
      independently from the lemma's stated (corrected) form.
Agreement on every vertex of every graph on n=1..6 is a strong
mechanical check of Lemma 4.1. We also check Theorem 5's aggregate
inequality sum[P(m)+Q(m)] >= 2|E(G)| and Corollary 5.1's
max[P(m)+Q(m)] >= delta(G) on the same exhaustive graph set.

P_p^alt for p in {0,1} (needed at the recursion's base) is not formally
defined by statement.md (which requires a>=2) but is an unambiguous
trivial extension (0 vertices/0 edges, 1 vertex/0 edges) used only as
proof-internal recursion machinery, not as a claim about the pinned
objects.
"""
import itertools
import sys
sys.path.insert(0, ".")
from defs import palt_edges

OUT = "../data/PQ_aggregate.txt"


def palt_edges_ext(p):
    if p == 0 or p == 1:
        return frozenset()
    return palt_edges(p)


def make_adj(n, mask, edge_list):
    adj = [[False] * n for _ in range(n)]
    for idx, (i, j) in enumerate(edge_list):
        if (mask >> idx) & 1:
            adj[i][j] = adj[j][i] = True
    return adj


def realizes(tuple_vals, patt_edges, adj):
    """For every edge {i,j} of patt_edges (indices into tuple_vals),
    check {tuple_vals[i],tuple_vals[j]} in E(G)."""
    for e in patt_edges:
        i, j = tuple(e)
        if not adj[tuple_vals[i]][tuple_vals[j]]:
            return False
    return True


def brute_P(m, candidates, adj):
    """candidates: sorted list of vertices, all < m (ambient-restricted
    already by caller). Largest p>=0 with a p-tuple l_0<...<l_{p-1} from
    candidates realizing P_p^alt with l_0~_G m."""
    best = 0
    k = len(candidates)
    for p in range(k, 0, -1):
        patt = palt_edges_ext(p)
        found = False
        for combo in itertools.combinations(candidates, p):
            if not adj[combo[0]][m]:
                continue
            if realizes(combo, patt, adj):
                found = True
                break
        if found:
            best = p
            break
    return best


def brute_Q(m, candidates, adj):
    """candidates: sorted list of vertices, all > m. Largest q>=0 with
    m<r_0<...<r_{q-1} from candidates, i->r_{q-1-i} realizes P_q^alt,
    r_{q-1}~_G m."""
    best = 0
    k = len(candidates)
    for q in range(k, 0, -1):
        patt = palt_edges_ext(q)
        found = False
        for combo in itertools.combinations(candidates, q):
            if not adj[combo[-1]][m]:
                continue
            rev = tuple(reversed(combo))
            if realizes(rev, patt, adj):
                found = True
                break
        if found:
            best = q
            break
    return best


def rec_P(m, verts, adj, memo):
    """Lemma 4.1: P(m) = max({0} U {1+rec_Q(l, window(l,m)) : l<m, l~_G m}),
    verts = full ambient vertex list (already restricted to the current
    window by caller)."""
    key = ("P", m, tuple(verts))
    if key in memo:
        return memo[key]
    best = 0
    for l in verts:
        if l >= m or not adj[l][m]:
            continue
        window = [u for u in verts if l < u < m]
        val = 1 + rec_Q(l, window, adj, memo)
        if val > best:
            best = val
    memo[key] = best
    return best


def rec_Q(m, verts, adj, memo):
    key = ("Q", m, tuple(verts))
    if key in memo:
        return memo[key]
    best = 0
    for r in verts:
        if r <= m or not adj[m][r]:
            continue
        window = [u for u in verts if m < u < r]
        val = 1 + rec_P(r, window, adj, memo)
        if val > best:
            best = val
    memo[key] = best
    return best


def check_graph(n, mask, edge_list, lines_bad):
    adj = make_adj(n, mask, edge_list)
    verts = list(range(n))
    mismatches = []
    total_PQ = 0
    E = bin(mask).count("1")
    max_PQ = 0
    for m in verts:
        below = [u for u in verts if u < m]
        above = [u for u in verts if u > m]
        bp = brute_P(m, below, adj)
        bq = brute_Q(m, above, adj)
        memo = {}
        rp = rec_P(m, verts, adj, memo)
        rq = rec_Q(m, verts, adj, memo)
        if bp != rp or bq != rq:
            mismatches.append((m, bp, bq, rp, rq))
        total_PQ += bp + bq
        max_PQ = max(max_PQ, bp + bq)
    agg_ok = total_PQ >= 2 * E
    deg = [sum(adj[v]) for v in verts]
    delta = min(deg) if n > 0 else None
    cor_ok = (delta is None) or (max_PQ >= delta)
    if mismatches or not agg_ok or not cor_ok:
        lines_bad.append(f"n={n} mask={mask:0{len(edge_list)}b} mismatches={mismatches} "
                          f"sumPQ={total_PQ} 2E={2*E} agg_ok={agg_ok} maxPQ={max_PQ} delta={delta} cor_ok={cor_ok}")
    return (len(mismatches) == 0), agg_ok, cor_ok, total_PQ, 2 * E, max_PQ, delta


def main():
    lines = []
    bad_lines = []
    lines.append("Exhaustive P(m)/Q(m) brute-force vs Lemma-4.1-recursion cross-check,")
    lines.append("plus Theorem 5 (aggregate sum) and Corollary 5.1 (max>=delta),")
    lines.append("over ALL labeled graphs on [n], n=0..6.")
    lines.append("")

    grand_ok = True
    min_slack = None
    min_slack_witness = None
    graphs_checked = 0

    for n in range(0, 7):
        edge_list = list(itertools.combinations(range(n), 2))
        E = len(edge_list)
        n_graphs = 1 << E
        all_lemma41_ok = True
        all_agg_ok = True
        all_cor_ok = True
        for mask in range(n_graphs):
            if n == 0:
                # degenerate: no vertices, both sides of Thm5 are 0.
                lemma41_ok, agg_ok, cor_ok = True, True, True
                total_PQ, twoE = 0, 0
            else:
                lemma41_ok, agg_ok, cor_ok, total_PQ, twoE, max_PQ, delta = check_graph(n, mask, edge_list, bad_lines)
            all_lemma41_ok &= lemma41_ok
            all_agg_ok &= agg_ok
            all_cor_ok &= cor_ok
            graphs_checked += 1
            if n > 0:
                slack = total_PQ - twoE
                if min_slack is None or slack < min_slack:
                    min_slack = slack
                    min_slack_witness = (n, mask)
        ok_line = f"n={n}: graphs={n_graphs:6d}  Lemma4.1 match={all_lemma41_ok}  " \
                  f"Thm5 (sum>=2E) holds={all_agg_ok}  Cor5.1 (max>=delta) holds={all_cor_ok}"
        lines.append(ok_line)
        grand_ok &= all_lemma41_ok & all_agg_ok & all_cor_ok

    lines.append("")
    lines.append(f"Total graphs checked (n=0..6): {graphs_checked}")
    lines.append(f"Minimum Theorem-5 slack (sumPQ - 2E) observed: {min_slack} at (n,mask)={min_slack_witness}")
    lines.append(f"GRAND RESULT -- Lemma 4.1 exact match AND Theorem 5 AND Corollary 5.1 hold on ALL graphs to n=6: {grand_ok}")
    if bad_lines:
        lines.append("")
        lines.append("FAILURES (first 20):")
        lines.extend(bad_lines[:20])

    text = "\n".join(lines)
    with open(OUT, "w") as f:
        f.write(text + "\n")
    print(text)
    print("Full output:", OUT)


if __name__ == "__main__":
    main()
