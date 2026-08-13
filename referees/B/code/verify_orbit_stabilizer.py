"""
Task 3(a): orbit/stabilizer claims for several a, both parities.
Built ONLY from statement.md definitions (defs.py), via direct group
action -- NOT via the proof's H_c shortcut (Lemma 0.2's own machinery is
checked separately, cross-referenced, in verify_lemmas_part3.py).
"""
from defs import palt_edges, dihedral_group, orbit_of_graph, stabilizer_size

OUT = "../data/orbit_stabilizer.txt"

lines = []
lines.append("Orbit/stabilizer of P_a^alt under Dih(a), computed directly from")
lines.append("statement.md's definitions (defs.py), a=3..25 (both parities).")
lines.append("Claim under test (Lemma 0.2): orbit size = a exactly, |Stab| = 2 exactly.")
lines.append("")

all_ok = True
for a in range(3, 26):
    edges = palt_edges(a)
    G = dihedral_group(a)
    assert len(G) == 2 * a
    orb = orbit_of_graph(edges, a, G)
    stab = stabilizer_size(edges, a, G)
    ok = (len(orb) == a) and (stab == 2)
    all_ok = all_ok and ok
    parity = "odd" if a % 2 else "even"
    lines.append(f"a={a:2d} ({parity:4s})  |Dih(a)|={len(G):3d}  orbit={len(orb):2d}  stab={stab}  OK={ok}")

lines.append("")
lines.append(f"ALL PASS (a=3..25): {all_ok}")

with open(OUT, "w") as f:
    f.write("\n".join(lines) + "\n")

print("\n".join(lines[-3:]))
print("Full output:", OUT)
