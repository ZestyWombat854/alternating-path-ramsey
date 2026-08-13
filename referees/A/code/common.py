"""Shared primitives, built ONLY from statement.md's definitions."""
from itertools import combinations


def p_alt_edges(a):
    seq = []
    for t in range((a + 1) // 2):
        seq.append(t)
        if len(seq) < a:
            seq.append(a - 1 - t)
    seq = seq[:a]
    edges = set()
    for i in range(a - 1):
        edges.add(frozenset((seq[i], seq[i + 1])))
    assert len(edges) == a - 1
    return frozenset(edges)


def dih_group(a):
    rho0 = tuple((i + 1) % a for i in range(a))
    sigma0 = tuple((a - 1 - i) % a for i in range(a))

    def compose(f, g):
        return tuple(f[g[i]] for i in range(a))

    ident = tuple(range(a))
    seen = {ident}
    frontier = [ident]
    gens = [rho0, sigma0]
    while frontier:
        new_frontier = []
        for perm in frontier:
            for g in gens:
                np_ = compose(g, perm)
                if np_ not in seen:
                    seen.add(np_)
                    new_frontier.append(np_)
        frontier = new_frontier
    assert len(seen) == 2 * a
    return seen


def apply_perm(perm, edges):
    return frozenset(frozenset((perm[i], perm[j])) for e in edges for i, j in [tuple(e)])


def dih_orbit_edges(a):
    """All distinct edge-sets gamma(P_a^alt), gamma in Dih(a)."""
    base = p_alt_edges(a)
    G = dih_group(a)
    return list({apply_perm(perm, base) for perm in G})


def has_color_r_dih_copy(a, n, color, r, orbit=None):
    """color: dict {(i,j): 1 or 2} for i<j in [n]. Returns witness or None."""
    if orbit is None:
        orbit = dih_orbit_edges(a)
    for edges in orbit:
        for v in combinations(range(n), a):
            ok = True
            for e in edges:
                i, j = tuple(e)
                x, y = v[i], v[j]
                if x > y:
                    x, y = y, x
                if color[(x, y)] != r:
                    ok = False
                    break
            if ok:
                return (edges, v)
    return None


def has_clique(n, color, r, b):
    """Does the color-r graph on [n] contain a K_b?"""
    if b <= 1:
        return () if n >= 1 else None
    for S in combinations(range(n), b):
        if all(color[(i, j)] == r for i, j in combinations(S, 2)):
            return S
    return None


def check_property(a, b, n, color, orbit=None):
    """True iff this coloring of K_n has color-1 Dih(a)-copy of P_a^alt
    OR color-2 K_b (the defining property for R_dih)."""
    if b == 1:
        return True  # color-2 K_1 always exists trivially for n>=1
    if has_clique(n, color, 2, b) is not None:
        return True
    if a >= 2 and n >= a:
        if has_color_r_dih_copy(a, n, color, 1, orbit) is not None:
            return True
    return False
