import Sealed49.Defs
import Sealed49.Orbit

/-!
# Sealed49.Aggregate — Part 4-5: P(m), Q(m) and the Aggregate Sum Theorem

candidate-proof.md Part 4 (the `P(m)`, `Q(m)` quantities and Lemma 4.1's
windowed recursion) and Part 5 (Theorem 5, the Aggregate Sum Theorem, and
Corollary 5.1). Depends on `Sealed49.Orbit` for `palt_adj_iff`, which Lemma
4.1's proof needs (via Lemma 3.1, reformulated below as
`realizes_palt_succ_iff`).
-/

namespace Sealed49

open scoped Classical
noncomputable section

/-- candidate-proof.md Part 4: `P(m)`'s witness predicate. `p = 0` is the
trivial case ("P(m)=0 holds trivially, requiring no witness"). For
`p = p'+1`: an increasing tuple `l` of length `p'+1`, contained in `W`,
lying entirely below `m`, realizing `P_{p'+1}^alt`, with `l_0 ~_G m`. -/
def PWitness {n : ℕ} (G : SimpleGraph (Fin n)) (W : Finset (Fin n)) (m : Fin n) : ℕ → Prop
  | 0 => True
  | p' + 1 => ∃ l : Fin (p' + 1) ↪o Fin n, (∀ i, l i ∈ W) ∧ (∀ i, l i < m) ∧
      Realizes (Palt (p' + 1)) G l ∧ G.Adj (l ⟨0, Nat.succ_pos p'⟩) m

/-- `P(m)`: the largest `p` with a `PWitness`, bounded by `n` (a strictly
increasing `Fin p ↪o Fin n` forces `p ≤ n`, so `n` is a safe search bound
for `Nat.findGreatest`). -/
def P {n : ℕ} (G : SimpleGraph (Fin n)) (W : Finset (Fin n)) (m : Fin n) : ℕ :=
  Nat.findGreatest (PWitness G W m) n

/-- `Q(m)`'s witness predicate: symmetric to `PWitness`, using `mirrorGraph`
to encode "`i ↦ r_{q-1-i}` realizes `P_q^alt`" (see the `Realizes` /
`mirrorGraph` docstrings in Defs.lean for why these coincide). -/
def QWitness {n : ℕ} (G : SimpleGraph (Fin n)) (W : Finset (Fin n)) (m : Fin n) : ℕ → Prop
  | 0 => True
  | q' + 1 => ∃ r : Fin (q' + 1) ↪o Fin n, (∀ i, r i ∈ W) ∧ (∀ i, m < r i) ∧
      Realizes (mirrorGraph (q' + 1) (Palt (q' + 1))) G r ∧
      G.Adj (r ⟨q', Nat.lt_succ_self q'⟩) m

/-- `Q(m)`, symmetric to `P(m)`. -/
def Q {n : ℕ} (G : SimpleGraph (Fin n)) (W : Finset (Fin n)) (m : Fin n) : ℕ :=
  Nat.findGreatest (QWitness G W m) n

/-- Lemma 3.1 (candidate-proof.md Part 3), reformulated directly in terms of
`Realizes`/pointwise adjacency rather than graph equality: for `q ≥ 1`
(`p = q+1 ≥ 2`), a `(q+1)`-tuple realizes `P_{q+1}^alt` iff its first and
last entries are `G`-adjacent (rank 0's unique edge, to rank `p-1`) and its
tail (dropping the first entry) realizes `mirror(P_q^alt)`. Proved directly
from `palt_adj_iff` (Orbit.lean) rather than the source's "delete rank 0"
argument. -/
theorem realizes_palt_succ_iff {n q : ℕ} (hq : 1 ≤ q) (G : SimpleGraph (Fin n))
    (v : Fin (q + 1) → Fin n) :
    (∀ i j : Fin (q + 1), (Palt (q + 1)).Adj i j → G.Adj (v i) (v j)) ↔
      G.Adj (v 0) (v (Fin.last q)) ∧
        ∀ i j : Fin q, (mirrorGraph q (Palt q)).Adj i j → G.Adj (v i.succ) (v j.succ) := by
  have hmirror : ∀ i j : Fin q, (mirrorGraph q (Palt q)).Adj i j ↔
      i ≠ j ∧ (i.val + j.val = q - 2 ∨ i.val + j.val = q - 1) := by
    intro i j
    show (Palt q).Adj (Fin.rev i) (Fin.rev j) ↔ _
    rw [palt_adj_iff, Fin.val_rev, Fin.val_rev]
    constructor
    · rintro ⟨hne, h | h⟩ <;> refine ⟨fun he => hne (by rw [he]), ?_⟩ <;> omega
    · rintro ⟨hne, h | h⟩ <;>
        refine ⟨fun he => hne (Fin.rev_injective he), ?_⟩ <;> omega
  constructor
  · intro h
    refine ⟨h 0 (Fin.last q) ?_, fun i j hij => h i.succ j.succ ?_⟩
    · rw [palt_adj_iff]
      have h0ne : (0 : Fin (q + 1)) ≠ Fin.last q := by
        simp only [ne_eq, Fin.ext_iff, Fin.val_zero, Fin.val_last]
        omega
      refine ⟨h0ne, Or.inl ?_⟩
      simp only [Fin.val_zero, Fin.val_last]
      omega
    · rw [palt_adj_iff]
      rw [hmirror] at hij
      obtain ⟨hne, hsum⟩ := hij
      refine ⟨fun he => hne (by
        have hv : (i.succ).val = (j.succ).val := congrArg Fin.val he
        simp only [Fin.val_succ] at hv
        exact Fin.ext (by omega)), ?_⟩
      simp only [Fin.val_succ]
      omega
  · rintro ⟨h0, htail⟩ i j hij
    rw [palt_adj_iff] at hij
    obtain ⟨hne, hsum⟩ := hij
    by_cases hi0 : i = 0
    · subst hi0
      have hjq : j = Fin.last q := by
        apply Fin.ext
        simp only [Fin.val_zero] at hsum
        simp [Fin.last]
        omega
      rw [hjq]; exact h0
    · by_cases hj0 : j = 0
      · subst hj0
        have hiq : i = Fin.last q := by
          apply Fin.ext
          simp only [Fin.val_zero] at hsum
          simp [Fin.last]
          omega
        rw [hiq]; exact h0.symm
      · obtain ⟨i', rfl⟩ := Fin.eq_succ_of_ne_zero hi0
        obtain ⟨j', rfl⟩ := Fin.eq_succ_of_ne_zero hj0
        apply htail
        rw [hmirror]
        refine ⟨fun he => hne (by rw [he]), ?_⟩
        simp only [Fin.val_succ] at hsum
        omega

end
end Sealed49
