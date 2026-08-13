"""Part 1 (lower-bound construction) sanity + exact R_dih(a,b) checks via
SAT (kissat), cross-validated by brute force at the smallest cells.
"""
import itertools
import subprocess
import sys

sys.path.insert(0, ".")
from common import dih_orbit_edges, has_color_r_dih_copy, has_clique, check_property


def part1_construction(a, b):
    """Exact construction from Part 1's proof: n=(a-1)(b-1), b-1 blocks of
    size a-1, color 1 within block, color 2 across blocks."""
    n = (a - 1) * (b - 1)
    block = [i // (a - 1) for i in range(n)]
    color = {}
    for i, j in itertools.combinations(range(n), 2):
        color[(i, j)] = 1 if block[i] == block[j] else 2
    return n, color


def check_part1(a, b):
    if b < 2:
        return "SKIP(b<2, base case)"
    n, color = part1_construction(a, b)
    orbit = dih_orbit_edges(a)
    clique = has_clique(n, color, 2, b)
    copy = has_color_r_dih_copy(a, n, color, 1, orbit) if n >= a else None
    ok = clique is None and copy is None
    return f"n={n} avoids_color2_K{b}={clique is None} avoids_color1_copy={copy is None} -> {'OK' if ok else 'FAIL'}"


def brute_force_all(a, b, n):
    """Return True iff EVERY 2-coloring of K_n has the property."""
    pairs = list(itertools.combinations(range(n), 2))
    orbit = dih_orbit_edges(a) if n >= a else None
    for bits in itertools.product((1, 2), repeat=len(pairs)):
        color = dict(zip(pairs, bits))
        if not check_property(a, b, n, color, orbit):
            return False, color
    return True, None


def brute_force_exists_bad(a, b, n):
    """Return a coloring of K_n avoiding the property, if one exists."""
    pairs = list(itertools.combinations(range(n), 2))
    orbit = dih_orbit_edges(a) if n >= a else None
    for bits in itertools.product((1, 2), repeat=len(pairs)):
        color = dict(zip(pairs, bits))
        if not check_property(a, b, n, color, orbit):
            return color
    return None


def sat_cnf(a, b, n):
    pairs = list(itertools.combinations(range(n), 2))
    var = {p: k + 1 for k, p in enumerate(pairs)}
    clauses = []
    if b >= 2:
        for S in itertools.combinations(range(n), b):
            clauses.append([var[e] for e in itertools.combinations(S, 2)])
    if a >= 2 and n >= a:
        orbit = dih_orbit_edges(a)
        for edges in orbit:
            for v in itertools.combinations(range(n), a):
                clause = []
                for e in edges:
                    i, j = tuple(e)
                    x, y = v[i], v[j]
                    if x > y:
                        x, y = y, x
                    clause.append(-var[(x, y)])
                clauses.append(clause)
    return var, clauses


def run_kissat(var, clauses, path):
    nvar = len(var)
    with open(path, "w") as f:
        f.write(f"p cnf {nvar} {len(clauses)}\n")
        for c in clauses:
            f.write(" ".join(map(str, c)) + " 0\n")
    out = subprocess.run(["kissat", "-q", path], capture_output=True, text=True, timeout=120)
    line1 = out.stdout.splitlines()[0].strip() if out.stdout.strip() else "NOOUT"
    sat = None
    if "UNSATISFIABLE" in out.stdout:
        sat = False
    elif "SATISFIABLE" in out.stdout:
        sat = True
    assign = None
    if sat:
        vals = {}
        for line in out.stdout.splitlines():
            if line.startswith("v "):
                for tok in line[2:].split():
                    tok = int(tok)
                    if tok == 0:
                        continue
                    vals[abs(tok)] = tok > 0
        inv = {k: p for p, k in var.items()}
        assign = {inv[k]: (1 if v else 2) for k, v in vals.items()}
    return sat, assign


if __name__ == "__main__":
    cells = [(4, 2), (5, 2), (4, 3), (5, 3), (6, 3), (4, 4), (6, 2), (7, 2)]
    print("=== Part 1 construction sanity (avoids both at n=(a-1)(b-1)) ===")
    for a, b in cells:
        print(f"(a={a},b={b}):", check_part1(a, b))

    print()
    print("=== Exact R_dih via SAT (UNSAT at n=formula => upper bound holds) ===")
    for a, b in cells:
        n = 1 + (a - 1) * (b - 1)
        var, clauses = sat_cnf(a, b, n)
        cnf_path = f"../data/cnf_{a}_{b}.cnf"
        sat, assign = run_kissat(var, clauses, cnf_path)
        status = "UNSAT (theorem OK)" if sat is False else ("SAT -- COUNTEREXAMPLE!" if sat else "UNKNOWN")
        print(f"(a={a},b={b},n={n}) nvars={len(var)} nclauses={len(clauses)}: {status}")
        if sat:
            print("  COUNTEREXAMPLE COLORING:", assign)
            print("  cross-check property:", check_property(a, b, n, assign))
