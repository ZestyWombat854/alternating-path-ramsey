"""
Task 3(b): exhaustive verification of R_dih(P_a^alt, K_b) = 1+(a-1)(b-1)
at small cells, built ONLY from statement.md's definitions (defs.py) --
uses the "equivalently: some H' in the orbit admits a monotone color-r
embedding" formulation stated in statement.md, not the proof's H_c
machinery.

For each (a,b): let n = 1+(a-1)(b-1).
  UPPER BOUND check: exhaustively scan all 2^C(n,2) colorings of K_n;
    confirm NONE avoid both targets (i.e. R_dih <= n).
  LOWER BOUND check: exhaustively scan all 2^C(n-1,2) colorings of K_{n-1};
    confirm AT LEAST ONE avoids both targets (i.e. R_dih > n-1).
Together these pin R_dih(P_a^alt,K_b) = n exactly, independent of the
candidate proof's own machinery.
"""
import itertools
import time
import numpy as np
from defs import palt_edges, dihedral_group, orbit_of_graph

OUT = "../data/R_dih_small_cells.txt"


def edge_index_map(n):
    edge_list = list(itertools.combinations(range(n), 2))
    idx = {e: i for i, e in enumerate(edge_list)}
    return edge_list, idx


def color1_pattern_masks(a, n, idx):
    """All required-edge bitmasks for a color-1 Dih(a)-copy of P_a^alt in
    K_n: for every increasing a-tuple v and every H' in the Dih(a)-orbit
    of P_a^alt, the mask of edges {v_i,v_j} for {i,j} in E(H')."""
    edges = palt_edges(a)
    G = dihedral_group(a)
    orbit = orbit_of_graph(edges, a, G)
    assert len(orbit) == a
    masks = []
    for v in itertools.combinations(range(n), a):
        for H in orbit:
            m = 0
            for e in H:
                i, j = tuple(e)
                x, y = v[i], v[j]
                if x > y:
                    x, y = y, x
                m |= (1 << idx[(x, y)])
            masks.append(m)
    return masks


def color2_clique_masks(b, n, idx):
    """All required-edge bitmasks for a color-2 K_b in K_n: for every
    b-subset, the mask of all its internal edges."""
    masks = []
    for s in itertools.combinations(range(n), b):
        m = 0
        for (i, j) in itertools.combinations(s, 2):
            m |= (1 << idx[(i, j)])
        masks.append(m)
    return masks


def count_bad_colorings(a, b, n, sample_bad=1):
    """Return (bad_count, E, example_bad_mask_or_None)."""
    edge_list, idx = edge_index_map(n)
    E = len(edge_list)
    if b == 1:
        # color-2 K_1 is realized by ANY single vertex trivially (0 edges
        # required) -- so if n>=1, EVERY coloring has a color-2 K_1: bad
        # count is 0 whenever n>=1, and the "b=1" cell is degenerate.
        return (0 if n >= 1 else (1 if n == 0 else None)), E, None

    c1_masks = color1_pattern_masks(a, n, idx)
    c2_masks = color2_clique_masks(b, n, idx)

    colorings = np.arange(1 << E, dtype=np.int64)
    has_c1 = np.zeros(len(colorings), dtype=bool)
    for m in c1_masks:
        has_c1 |= (colorings & m) == 0
    has_c2 = np.zeros(len(colorings), dtype=bool)
    for m in c2_masks:
        has_c2 |= (colorings & m) == m

    bad = ~(has_c1 | has_c2)
    bad_count = int(bad.sum())
    example = None
    if bad_count > 0:
        example = int(np.argmax(bad))
    return bad_count, E, example


def run_cell(a, b, lines):
    n = 1 + (a - 1) * (b - 1)
    t0 = time.time()
    lines.append(f"--- (a,b)=({a},{b})  formula n=1+(a-1)(b-1)={n} ---")

    # Upper bound: at n, zero bad colorings expected.
    bad_n, E_n, ex_n = count_bad_colorings(a, b, n)
    t1 = time.time()
    lines.append(f"  UPPER n={n}: E={E_n}, colorings=2^{E_n}={1<<E_n if E_n<40 else 'huge'}, "
                 f"bad_count={bad_n}  [{'PASS: R_dih<=n' if bad_n==0 else 'FAIL -- counterexample exists!'}]  "
                 f"({t1-t0:.1f}s)")
    if bad_n and bad_n > 0 and ex_n is not None:
        lines.append(f"    counterexample coloring bitmask (edges color2 where bit=1): {ex_n:0{E_n}b}")

    # Lower bound: at n-1, at least one bad coloring expected.
    nm1 = n - 1
    t2 = time.time()
    bad_nm1, E_nm1, ex_nm1 = count_bad_colorings(a, b, nm1)
    t3 = time.time()
    lines.append(f"  LOWER n-1={nm1}: E={E_nm1}, bad_count={bad_nm1}  "
                 f"[{'PASS: R_dih>n-1' if bad_nm1 and bad_nm1>0 else ('PASS (b=1 vacuous case)' if b==1 else 'FAIL -- no avoiding coloring at n-1!')}]  "
                 f"({t3-t2:.1f}s)")
    lines.append("")
    return bad_n == 0 and (b == 1 or (bad_nm1 is not None and bad_nm1 > 0))


def main():
    lines = []
    lines.append("Exhaustive R_dih(P_a^alt,K_b) verification, built only from")
    lines.append("statement.md definitions (defs.py). For each cell: exhaustively")
    lines.append("scan ALL 2-colorings of K_n (upper bound) and K_{n-1} (lower bound).")
    lines.append("")
    cells = [(4, 2), (4, 3), (5, 2), (6, 2), (7, 2)]
    all_ok = True
    for (a, b) in cells:
        ok = run_cell(a, b, lines)
        all_ok = all_ok and ok
    lines.append(f"ALL CELLS CONFIRM R_dih(P_a^alt,K_b)=1+(a-1)(b-1) EXACTLY: {all_ok}")
    text = "\n".join(lines)
    with open(OUT, "w") as f:
        f.write(text + "\n")
    print(text)
    print("Full output:", OUT)


if __name__ == "__main__":
    main()
