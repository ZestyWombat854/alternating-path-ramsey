import Sealed49.Orbit
import Sealed49.Aggregate

/-!
# Sealed49.AxiomAudit

Engineering rule 3: `#print axioms` every top-level theorem actually
proved in this project, so `verify.sh` can grep the output for anything
beyond the target set (`propext`, `Classical.choice`, `Quot.sound`).

There is no `Main.lean` in this snapshot: the pinned statement
(`R_dih(P_a^alt,K_b) = 1+(a-1)(b-1)`) is not yet proved end-to-end (see
`notes/LEAN49-status.md` for exactly which steps remain), and this project
never uses placeholder proofs — so nothing claiming the full theorem is
stated here. Every theorem below is a genuine, fully-proved component.
-/

#print axioms Sealed49.palt_eq_Hgraph
#print axioms Sealed49.actGraph_rho_hgraph
#print axioms Sealed49.actGraph_sigma_hgraph
#print axioms Sealed49.realizes_palt_succ_iff
