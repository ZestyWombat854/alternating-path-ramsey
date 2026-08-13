import Sealed49.Defs

/-!
# Sealed49.Orbit — Part 0: the orbit of `P_a^alt`

Formalizes candidate-proof.md Part 0: Lemma 0.1 (`P_a^alt = H_{a-1}`) and
Lemma 0.2 (orbit and stabilizer of `P_a^alt` under `Dih(a)`).
-/

namespace Sealed49

open scoped Classical

section AltSeqVal

/-- Sanity check on the sequence definition (statement.md lines 9-10):
`s_0 = 0`. -/
example (a : ℕ) : altSeqVal a 0 = 0 := rfl

theorem altSeqVal_lt (a i : ℕ) (h : i < a) : altSeqVal a i < a := by
  unfold altSeqVal
  split <;> omega

/-- The core arithmetic fact behind Lemma 0.1's forward direction: consecutive
sequence values sum to `a-1` (even position) or `a` (odd position). -/
theorem altSeqVal_add (a i : ℕ) (h : i + 1 < a) :
    altSeqVal a i + altSeqVal a (i + 1) = a - 1 ∨ altSeqVal a i + altSeqVal a (i + 1) = a := by
  simp only [altSeqVal]
  rcases Nat.even_or_odd i with ⟨t, ht⟩ | ⟨t, ht⟩
  · left; split_ifs <;> omega
  · right; split_ifs <;> omega

theorem altSeqVal_two_mul (a t : ℕ) : altSeqVal a (2 * t) = t := by
  simp only [altSeqVal]; split_ifs <;> omega

theorem altSeqVal_two_mul_add_one (a t : ℕ) : altSeqVal a (2 * t + 1) = a - 1 - t := by
  simp only [altSeqVal]; split_ifs <;> omega

end AltSeqVal

section PaltCharacterization

/-- Direct characterization of `P_a^alt`-adjacency purely in terms of vertex
values: `{x,y}` is an edge iff `x+y = a-1` or `x+y = a`. This is the content
of Lemma 0.1's forward computation, proved directly (both directions) rather
than via the source's cardinality-counting argument. -/
theorem palt_adj_iff (a : ℕ) (x y : Fin a) :
    (Palt a).Adj x y ↔ x ≠ y ∧ (x.val + y.val = a - 1 ∨ x.val + y.val = a) := by
  have hxlt := x.isLt
  have hylt := y.isLt
  simp only [Palt, SimpleGraph.fromRel_adj]
  constructor
  · rintro ⟨hxy, ⟨i, hi, hx, hy⟩ | ⟨i, hi, hy, hx⟩⟩ <;>
      · have h := altSeqVal_add a i hi
        exact ⟨hxy, by omega⟩
  · rintro ⟨hxy, hsum | hsum⟩
    · have hval : x.val ≠ y.val := Fin.val_injective.ne hxy
      rcases lt_or_gt_of_ne hval with hlt | hgt
      · refine ⟨hxy, Or.inl ⟨2 * x.val, by omega, ?_, ?_⟩⟩
        · rw [altSeqVal_two_mul]
        · rw [altSeqVal_two_mul_add_one]; omega
      · refine ⟨hxy, Or.inr ⟨2 * y.val, by omega, ?_, ?_⟩⟩
        · rw [altSeqVal_two_mul]
        · rw [altSeqVal_two_mul_add_one]; omega
    · have hval : x.val ≠ y.val := Fin.val_injective.ne hxy
      rcases lt_or_gt_of_ne hval with hlt | hgt
      · refine ⟨hxy, Or.inr ⟨2 * x.val - 1, by omega, ?_, ?_⟩⟩
        · have e1 : 2 * x.val - 1 = 2 * (x.val - 1) + 1 := by omega
          rw [e1, altSeqVal_two_mul_add_one]; omega
        · have e2 : 2 * x.val - 1 + 1 = 2 * x.val := by omega
          rw [e2, altSeqVal_two_mul]
      · refine ⟨hxy, Or.inl ⟨2 * y.val - 1, by omega, ?_, ?_⟩⟩
        · have e1 : 2 * y.val - 1 = 2 * (y.val - 1) + 1 := by omega
          rw [e1, altSeqVal_two_mul_add_one]; omega
        · have e2 : 2 * y.val - 1 + 1 = 2 * y.val := by omega
          rw [e2, altSeqVal_two_mul]

end PaltCharacterization

section HgraphCharacterization

theorem mgraph_adj_iff (a : ℕ) (c : ZMod a) (x y : Fin a) :
    (Mgraph a c).Adj x y ↔ x ≠ y ∧ (x.val : ZMod a) + (y.val : ZMod a) = c := by
  simp only [Mgraph, SimpleGraph.fromRel_adj]
  constructor
  · rintro ⟨hxy, h | h⟩
    · exact ⟨hxy, h⟩
    · exact ⟨hxy, by rw [add_comm]; exact h⟩
  · rintro ⟨hxy, h⟩
    exact ⟨hxy, Or.inl h⟩

theorem hgraph_adj_iff (a : ℕ) (c : ZMod a) (x y : Fin a) :
    (Hgraph a c).Adj x y ↔
      x ≠ y ∧ ((x.val : ZMod a) + (y.val : ZMod a) = c ∨ (x.val : ZMod a) + (y.val : ZMod a) = c + 1) := by
  simp only [Hgraph, SimpleGraph.sup_adj, mgraph_adj_iff]
  tauto

/-- Translate a natural-number sum equation to `Fin a`-vertex `ZMod a` sum:
for `k < a`, the `ZMod a` equation holds iff the nat sum is `k` (the
"no-wraparound" case) or `k+a` (the "one wraparound" case, since
`x.val+y.val < 2*a` always). The case split (`hc`) is threaded explicitly
through to the final `omega` call, since `omega` cannot itself reason about
`%` by a non-literal modulus. -/
theorem natSum_eq_natCast_iff (a k : ℕ) (x y : Fin a) (hk : k < a) :
    (x.val : ZMod a) + (y.val : ZMod a) = (k : ZMod a) ↔
      x.val + y.val = k ∨ x.val + y.val = k + a := by
  have hxlt := x.isLt
  have hylt := y.isLt
  rw [← Nat.cast_add, ZMod.natCast_eq_natCast_iff, Nat.ModEq]
  rcases lt_or_ge (x.val + y.val) a with hc | hc
  · rw [Nat.mod_eq_of_lt hc, Nat.mod_eq_of_lt hk]
    omega
  · have step : (x.val + y.val) % a = (x.val + y.val - a) % a := by
      conv_lhs => rw [show x.val + y.val = (x.val + y.val - a) + a by omega]
      exact Nat.add_mod_right _ _
    rw [step, Nat.mod_eq_of_lt (show x.val + y.val - a < a by omega), Nat.mod_eq_of_lt hk]
    omega

end HgraphCharacterization

section Lemma01

/-- Lemma 0.1: for `a ≥ 3`, `P_a^alt = H_{a-1}`. -/
theorem palt_eq_Hgraph (a : ℕ) (ha : 3 ≤ a) :
    Palt a = Hgraph a ((a - 1 : ℕ) : ZMod a) := by
  ext x y
  rw [palt_adj_iff, hgraph_adj_iff]
  have e1 : ((a - 1 : ℕ) : ZMod a) + 1 = (a : ZMod a) := by
    push_cast [Nat.cast_sub (by omega : 1 ≤ a)]
    ring
  rw [e1, ZMod.natCast_self,
      natSum_eq_natCast_iff a (a - 1) x y (by omega),
      show (0 : ZMod a) = ((0 : ℕ) : ZMod a) from (Nat.cast_zero).symm,
      natSum_eq_natCast_iff a 0 x y (by omega)]
  have hxlt := x.isLt
  have hylt := y.isLt
  constructor
  · rintro ⟨hxy, h⟩
    have hval : x.val ≠ y.val := Fin.val_injective.ne hxy
    exact ⟨hxy, by omega⟩
  · rintro ⟨hxy, h⟩
    have hval : x.val ≠ y.val := Fin.val_injective.ne hxy
    exact ⟨hxy, by omega⟩

end Lemma01

section Lemma02Core

/-- Casting `Fin a` addition to `ZMod a` agrees with `ZMod a`'s own
addition (bridges `Fin a`'s ring-like operations to the `ZMod a` cast used
throughout `Mgraph`/`Hgraph`). -/
theorem fin_val_cast_add (a : ℕ) (x y : Fin a) :
    ((x + y : Fin a).val : ZMod a) = (x.val : ZMod a) + (y.val : ZMod a) := by
  rw [Fin.val_add, ZMod.natCast_mod, Nat.cast_add]

/-- `ρ⁻¹` shifts the `ZMod a` cast down by `1`. -/
theorem rho_symm_shift (a : ℕ) (ha : 2 ≤ a) (i : Fin a) :
    (((finRotate a).symm i).val : ZMod a) + 1 = (i.val : ZMod a) := by
  haveI : NeZero a := ⟨by omega⟩
  have hone : (1 : Fin a).val = 1 := by rw [Fin.val_one', Nat.mod_eq_of_lt (by omega)]
  have h1 : (finRotate a).symm i + 1 = i := by
    conv_rhs => rw [← Equiv.apply_symm_apply (finRotate a) i]
    exact (finRotate_apply ((finRotate a).symm i)).symm
  have h2 : (((finRotate a).symm i + 1 : Fin a).val : ZMod a) = (i.val : ZMod a) := by rw [h1]
  rw [fin_val_cast_add, hone, Nat.cast_one] at h2
  exact h2

/-- `σ`'s `ZMod a` cast is `-1 - i` (statement.md's `σ(i)=m-1-i`, cast). -/
theorem sigma_cast (a : ℕ) (i : Fin a) :
    ((Fin.rev i).val : ZMod a) = -1 - (i.val : ZMod a) := by
  rw [Fin.val_rev, Nat.cast_sub (by omega : i.val + 1 ≤ a), Nat.cast_add, Nat.cast_one,
      ZMod.natCast_self]
  ring

/-- ρ(H_c) = H_{c+2} (candidate-proof.md Part 0's computation for `ρ`). -/
theorem actGraph_rho_hgraph (a : ℕ) (ha : 2 ≤ a) (c : ZMod a) :
    actGraph (rhoPerm a) (Hgraph a c) = Hgraph a (c + 2) := by
  ext x y
  show (Hgraph a c).Adj ((finRotate a).symm x) ((finRotate a).symm y) ↔ (Hgraph a (c + 2)).Adj x y
  rw [hgraph_adj_iff, hgraph_adj_iff]
  have hx := rho_symm_shift a ha x
  have hy := rho_symm_shift a ha y
  have hne : (finRotate a).symm x ≠ (finRotate a).symm y ↔ x ≠ y :=
    ⟨fun h he => h (by rw [he]), fun h he => h ((finRotate a).symm.injective he)⟩
  rw [hne]
  constructor
  · rintro ⟨hxy, h | h⟩
    · exact ⟨hxy, Or.inl (by linear_combination h - hx - hy)⟩
    · exact ⟨hxy, Or.inr (by linear_combination h - hx - hy)⟩
  · rintro ⟨hxy, h | h⟩
    · exact ⟨hxy, Or.inl (by linear_combination h + hx + hy)⟩
    · exact ⟨hxy, Or.inr (by linear_combination h + hx + hy)⟩

/-- σ(H_c) = H_{-3-c} (candidate-proof.md Part 0's computation for `σ`). -/
theorem actGraph_sigma_hgraph (a : ℕ) (c : ZMod a) :
    actGraph (sigmaPerm a) (Hgraph a c) = Hgraph a (-3 - c) := by
  ext x y
  show (Hgraph a c).Adj ((sigmaPerm a).symm x) ((sigmaPerm a).symm y) ↔
      (Hgraph a (-3 - c)).Adj x y
  have hxe : (sigmaPerm a).symm x = Fin.rev x := by unfold sigmaPerm; rfl
  have hye : (sigmaPerm a).symm y = Fin.rev y := by unfold sigmaPerm; rfl
  rw [hxe, hye, hgraph_adj_iff, hgraph_adj_iff]
  have hx := sigma_cast a x
  have hy := sigma_cast a y
  have hne : Fin.rev x ≠ Fin.rev y ↔ x ≠ y :=
    ⟨fun h he => h (by rw [he]), fun h he => h (Fin.rev_injective he)⟩
  rw [hne]
  constructor
  · rintro ⟨hxy, h | h⟩
    · exact ⟨hxy, Or.inr (by linear_combination -h + hx + hy)⟩
    · exact ⟨hxy, Or.inl (by linear_combination -h + hx + hy)⟩
  · rintro ⟨hxy, h | h⟩
    · exact ⟨hxy, Or.inr (by linear_combination -h + hx + hy)⟩
    · exact ⟨hxy, Or.inl (by linear_combination -h + hx + hy)⟩

end Lemma02Core
end Sealed49
