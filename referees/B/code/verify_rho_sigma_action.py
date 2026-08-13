"""
Direct check of the group-action-on-index claims from Lemma 0.2's proof,
reused as a load-bearing step inside Lemma 3.2(b): rho(H_c) = H_{c+2}
and sigma(H_c) = H_{-3-c mod a}, for every a and every c. Computed via
two independent codepaths: H_c from Part 0's raw definition
(verify_lemmas_part3.H_c) and the permutation action from defs.py
(statement.md's rho/sigma generators), composed via
defs.apply_perm_to_edges (statement.md's gamma(H) definition).
"""
from defs import apply_perm_to_edges
from verify_lemmas_part3 import H_c

OUT = "../data/rho_sigma_action.txt"


def main():
    lines = []
    ok = True
    checked = 0
    for a in range(3, 26):
        rho = tuple((i + 1) % a for i in range(a))
        sigma = tuple((a - 1 - i) % a for i in range(a))
        for c in range(a):
            Hc = H_c(a, c)
            rho_Hc = apply_perm_to_edges(rho, Hc)
            sigma_Hc = apply_perm_to_edges(sigma, Hc)
            target_rho = H_c(a, (c + 2) % a)
            target_sigma = H_c(a, (-3 - c) % a)
            ok_rho = (rho_Hc == target_rho)
            ok_sigma = (sigma_Hc == target_sigma)
            checked += 1
            if not (ok_rho and ok_sigma):
                ok = False
                lines.append(f"MISMATCH a={a} c={c} ok_rho={ok_rho} ok_sigma={ok_sigma}")
    lines.append(f"Checked {checked} (a,c) pairs, a=3..25.")
    lines.append(f"rho(H_c)=H_(c+2) and sigma(H_c)=H_(-3-c mod a) hold in ALL cases: {ok}")
    text = "\n".join(lines)
    with open(OUT, "w") as f:
        f.write(text + "\n")
    print(text)
    print("Full output:", OUT)


if __name__ == "__main__":
    main()
