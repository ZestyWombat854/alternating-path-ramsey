"""Check Lemma 2 (degree reduction / core nonemptiness), b>=2 case, and
probe the b=1 case explicitly (suspected bug)."""
import itertools


def all_graphs(n):
    verts = list(range(n))
    pairs = list(itertools.combinations(verts, 2))
    for bits in itertools.product((0, 1), repeat=len(pairs)):
        E = frozenset(p for p, b in zip(pairs, bits) if b)
        yield verts, E


def alpha_le(E, W, k):
    """True iff independence number of (W,E) is <= k (no independent set of size k+1).
    E holds sorted-pair tuples (i,j), i<j, matching all_graphs()."""
    for S in itertools.combinations(W, k + 1):
        if all((x, y) not in E for x, y in itertools.combinations(S, 2)):
            return False
    return True


def core(E, W, threshold):
    W = list(W)
    E = set(E)
    changed = True
    while changed:
        changed = False
        deg = {w: 0 for w in W}
        for e in E:
            i, j = tuple(e)
            deg[i] += 1
            deg[j] += 1
        for w in list(W):
            if deg[w] <= threshold:
                W.remove(w)
                E = {e for e in E if w not in e}
                changed = True
                break
    return W


def check_b1(a):
    """Lemma 2's own b=1 claim: n=1, W={0} nonempty, degree(restricted)>=a-1."""
    n = 1 + (a - 1) * 0
    W = [0]
    E = frozenset()
    d = 0  # only possible degree in a 1-vertex graph
    holds = d >= a - 1
    return n, W, d, a - 1, holds


def check_b_ge2(a, b, nmax_exhaustive):
    n = 1 + (a - 1) * (b - 1)
    threshold = a - 2
    fails = []
    checked = 0
    if n <= nmax_exhaustive:
        for W, E in all_graphs(n):
            if alpha_le(E, W, b - 1):
                checked += 1
                W2 = core(E, W, threshold)
                if not W2:
                    fails.append((a, b, list(E)))
    return n, checked, fails


if __name__ == "__main__":
    print("=== Lemma 2, b=1 case: is the literal claim true? ===")
    for a in (4, 5, 6, 7):
        n, W, d, need, holds = check_b1(a)
        print(f"a={a}: n={n}, W={W}, actual degree={d}, required>= {need}, HOLDS={holds}")

    print()
    print("=== Lemma 2, b>=2 case: (a-1)-core nonempty whenever alpha<=b-1, n=(a-1)(b-1)+1 ===")
    for a, b in [(4, 2), (5, 2), (4, 3), (5, 3), (6, 2)]:
        n, checked, fails = check_b_ge2(a, b, nmax_exhaustive=8)
        print(f"a={a} b={b} n={n}: exhaustive={'yes' if n<=8 else 'skip(too big)'} graphs_with_alpha<=b-1={checked} failures={len(fails)}")
