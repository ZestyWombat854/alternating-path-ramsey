# R_dih(P_a^alt, K_b) = 1 + (a-1)(b-1) for all a >= 4, b >= 1

> **Provenance note (added for submission).** This file is
> `proof-original-with-errata.md` with the dual-blind referees' two
> non-fatal findings (see the Errata / Post-referee repairs section at the
> end of this document) applied INLINE, each marked `[REPAIR ...]` at the
> point of change — four such marks in total: referee A's finding touches
> two locations (Lemma 2's statement and proof opening, in Part 2, and a
> clarifying sentence in Theorem 7's proof, in Part 6, explaining why
> Lemma 2's narrowed hypothesis is safe); referee B's finding touches one
> (Lemma 3.1's proof text, in Part 3); the fourth marks the Errata
> section itself, at the end of this document, reframed to say the fixes
> are now inline rather than pending. This note (the provenance note you
> are reading) is the only ADDED content with no `[REPAIR ...]` mark of
> its own, since it is new framing, not a repair of existing text. The
> untouched original — body exactly as audited, errata appended rather
> than folded in, per the sealed run's "never silently repair" protocol —
> is preserved verbatim in `proof-original-with-errata.md` in this same
> directory. Nothing else in this document was changed; diff the two files
> to see the complete, exact set of edits.

Self-contained proof. Notation: [m] = {0,1,...,m-1}. All graphs are on
vertex sets that are finite subsets of the integers, inheriting the usual
linear order; "increasing tuple" means listed in that order. For a graph
H and gamma in Sym([m]), gamma(H) denotes H relabeled by gamma. A
"monotone color-r embedding" of H into a colored complete graph on [n] is
an increasing map v: [m] -> [n] with {v_i,v_j} colored r for every edge
{i,j} of H.

Recall P_a^alt (a>=2) is the graph on [a] with edges given by consecutive
pairs of the sequence (0,a-1,1,a-2,2,...); Dih(a) = <rho,sigma> with
rho(i)=i+1 mod a, sigma(i)=a-1-i; a Dih(a)-copy of P_a^alt in color r is a
monotone color-r embedding of some gamma(P_a^alt), gamma in Dih(a); and
R_dih(P_a^alt,K_b) is the least n such that every 2-coloring of K_n has a
color-1 Dih(a)-copy of P_a^alt or a color-2 K_b (an ordinary monochromatic
b-clique, since K_b's Gamma-copy notion is order/shape-independent).

---

## Part 0. The orbit of P_a^alt

For c in Z/aZ, let M_c = {{i,j} subset [a] : i != j, i+j == c (mod a)},
and H_c = M_c union M_{c+1 mod a}.

**Lemma 0.1.** For a >= 3, P_a^alt = H_{a-1}.

*Proof.* Write the defining sequence as s_0,...,s_{a-1}, s_{2t}=t,
s_{2t+1}=a-1-t. The edges are the consecutive pairs: for i=2t,
{s_{2t},s_{2t+1}} = {t,a-1-t}, sum a-1; for i=2t+1,
{s_{2t+1},s_{2t+2}} = {a-1-t,t+1}, sum a =0 (mod a). So E(P_a^alt) is
contained in M_{a-1} union M_0 = H_{a-1}. The number of unordered pairs
from [a] summing to a-1 is floor(a/2); summing to a is ceil(a/2)-1; these
sum to a-1 = |E(P_a^alt)|. A subset of a finite set with equal
cardinality to the whole is the whole set, so P_a^alt = H_{a-1}. QED

**Lemma 0.2 (orbit and stabilizer).** For every a >= 3:
{gamma(P_a^alt) : gamma in Dih(a)} = {H_c : c in Z/aZ}, exactly a
distinct graphs, and Stab_{Dih(a)}(P_a^alt) has order exactly 2.

*Proof.* Working mod a throughout, rho(i) = i+1, sigma(i) = -1-i. For a
pair {j,k}: rho(j)+rho(k) = (j+k)+2, sigma(j)+sigma(k) = -2-(j+k) (mod a).
Hence rho(H_c) = H_{c+2}, sigma(H_c) = H_{-3-c} (indices mod a). So
Dih(a) acts on the index c via tau_1(c)=c+2, tau_2(c)=-3-c. Track the
orbit of c_0 = a-1 under <tau_1,tau_2>: if a is odd, gcd(2,a)=1 so tau_1
alone sweeps all of Z/aZ. If a is even, tau_1 alone sweeps only the a/2
values of one parity; tau_2(a-1) = -a-2 == -2 == a-2 (mod a), of the
opposite parity, and tau_1 from there sweeps the remaining a/2 values.
Either way the orbit of c_0 is all of Z/aZ, so {gamma(P_a^alt)} =
{H_c : c in Z/aZ} by Lemma 0.1.

The a sets M_c (c in Z/aZ) partition all pairs of [a] (each pair has a
unique sum mod a), and H_c = M_c union M_{c+1}. If H_c = H_{c'} with
c != c', disjointness of the M's forces {c,c+1} = {c',c'+1} as sets,
i.e. 2 == 0 (mod a) -- impossible for a >= 3. So the a graphs H_c are
pairwise distinct, giving orbit size exactly a. By orbit-stabilizer,
|Stab| = |Dih(a)| / a = 2a/a = 2. QED

---

## Part 1. Lower bound

**Theorem 1.** For all a >= 2, b >= 1: R_dih(P_a^alt,K_b) >= 1+(a-1)(b-1).

*Proof.* For b=1 this is immediate (n=0 has no vertex, hence no color-2
K_1; n=1 trivially has one). Assume b >= 2. Partition [(a-1)(b-1)] into
b-1 contiguous blocks of size a-1. Color {x,y} (x<y) color 1 if x,y lie
in the same block, color 2 otherwise.

The color-2 graph is complete (b-1)-partite (parts = blocks); any clique
meets each part at most once, so has size <= b-1 < b: no color-2 K_b.

For any gamma in Dih(a), gamma(P_a^alt) is, as an abstract graph,
isomorphic to P_a^alt (relabeling a graph preserves isomorphism type),
hence a Hamiltonian path on its a vertices: connected. Suppose some
increasing v: [a] -> [(a-1)(b-1)] gave a monotone color-1 embedding of
gamma(P_a^alt). Since each block has only a-1 < a elements, {v_0,...,
v_{a-1}} meets at least 2 blocks, so this partitions gamma(P_a^alt)'s
vertex set into >= 2 nonempty parts (by which block each v_i falls in).
A connected graph has an edge crossing every nontrivial partition of its
vertices; that edge maps to a pair in two different blocks, which is
color 2 -- contradicting that every edge of a color-1 embedding must be
color 1. So no color-1 Dih(a)-copy of P_a^alt exists in this coloring.

Hence K_{(a-1)(b-1)} admits a coloring avoiding both targets, so
R_dih(P_a^alt,K_b) > (a-1)(b-1), i.e. >= (a-1)(b-1)+1. QED

---

## Part 2. Reducing the upper bound to a degree condition

**Lemma 2 (degree reduction).** [REPAIR, referee A — was "b >= 1"; the
b=1 case is false as originally stated (see provenance note above) and is
handled directly in Theorem 7 below without this lemma, so the hypothesis
here is restricted to where the lemma is actually used and actually
true.] Fix a >= 4, b >= 2, n = 1+(a-1)(b-1). Let c be any 2-coloring of
the edges of K_n with no color-2 K_b, and let G be the color-1 graph on
[n]. Then there is a nonempty W subset [n] (with its inherited order)
such that every vertex of W has degree (within G restricted to W) at
least a-1.

*Proof.* Since b >= 2, n >= a. Since there is no color-2 K_b, the
independence number of G satisfies alpha(G) <= b-1 (an independent set of
size b in G is exactly a color-2 K_b).

Repeatedly delete, from the current graph (starting at all of [n]), any
vertex whose CURRENT degree is <= a-2, as long as one exists. If this
process empties [n] entirely, let v_1,...,v_n be the deletion order (so
v_i had degree <= a-2 among {v_i,...,v_n} at the moment of its deletion).
Color v_n,v_{n-1},...,v_1 in that (reverse) order greedily with a-1
colors: when coloring v_i, its already-colored neighbors are exactly its
neighbors among {v_i,...,v_n} (neighbors among v_1,...,v_{i-1} are not
yet colored), of which there are <= a-2, so a free color exists among
a-1. This is a proper (a-1)-coloring of G, so its color classes
(G-independent sets) partition [n] into <= a-1 parts, and the largest
has size >= ceil(n/(a-1)). Since n = (a-1)(b-1)+1, n/(a-1) =
(b-1) + 1/(a-1), strictly between b-1 and b, so ceil(n/(a-1)) = b. This
gives an independent set of size b, contradicting alpha(G) <= b-1.

So the deletion process cannot empty [n]; let W be the nonempty set
remaining when it terminates (no more low-degree vertices to delete).
Every vertex of W has degree >= a-1 within G restricted to W, by
construction. QED

---

## Part 3. Structural facts about P_p^alt

**Lemma 3.1 (self-similarity / peeling).** For p >= 2: in P_p^alt, rank 0
has degree exactly 1, with its unique edge to rank p-1. Deleting rank 0
and relabeling {1,...,p-1} -> {0,...,p-2} (subtract 1) yields exactly the
mirror of P_{p-1}^alt (mirror(K) := apply i -> (p-2)-i to K's edge set).

*Proof.* With s_k as in Lemma 0.1's proof (size p): value 0 occurs only
at k=0 (s_{2j}=0 forces j=0; s_{2j+1}=0 forces j=p-1, i.e.
k=2j+1=2p-1 [REPAIR, referee B — was "2p-3"], which exceeds p-1 for all
p >= 1), so rank 0's unique edge is {s_0,s_1} = {0,p-1}. Deleting s_0 leaves the sequence
(s_1,...,s_{p-1}) = (p-1,1,p-2,2,...); subtracting 1 termwise gives
(p-2,0,p-3,1,...). P_{p-1}^alt's own sequence is (0,p-2,1,p-3,...);
applying the mirror map t -> (p-2)-t termwise gives
(p-2,0,p-3,1,...) -- an exact match (checked by direct substitution in
both parities of the index). Since a sequence's graph depends only on
its consecutive pairs, and relabeling commutes with taking consecutive
pairs, the claim follows. QED

(This fact was independently re-derived and verified, including by
direct computation for p = 4..11, multiple times during the research
process behind this proof; it is not a delicate or fragile identity.)

**Lemma 3.1b (trimming from the far end).** For p >= 2, let e = floor(p/2).
In P_p^alt, e is the OTHER degree-1 vertex (besides rank 0 of Lemma 3.1),
and it occurs ONLY at the last position of the defining sequence. Deleting
e and applying the order-isomorphism [p]\{e} -> [p-1] (identity below e,
subtract 1 above e) yields P_{p-1}^alt DIRECTLY (not mirrored). In
particular, rank 0 is untouched by this deletion (e >= 1 for p >= 2), and
the resulting (p-1)-element sequence is exactly the original sequence
with its last term dropped.

*Proof.* With s_k as before: if p = 2k (even), s_{p-1} = s_{2k-1} =
p-1-(k-1) = p-k = k = p/2; if p = 2k+1 (odd), s_{p-1} = s_{2k} = k =
(p-1)/2. Either way s_{p-1} = floor(p/2) = e, and since (s_0,...,s_{p-1})
is a permutation of [p], e occurs nowhere else. So deleting e from the
sequence removes exactly the last term, leaving (s_0,...,s_{p-2})
unchanged as a sequence of values (a permutation of [p]\{e}); rank 0
(the first term) is untouched. Apply phi: [p]\{e} -> [p-1] (identity
below e, subtract 1 above e) termwise to (s_0,...,s_{p-2}). For k <= p-2
even, k=2t: s_k = t <= floor((p-2)/2) < e in both parities (direct
check), so phi(t)=t, matching P_{p-1}^alt's own term at position 2t
(namely t). For k <= p-2 odd, k=2t+1: s_k = p-1-t >= ceil((p+1)/2) > e
in both parities, so phi(p-1-t) = p-2-t, matching P_{p-1}^alt's own term
at position 2t+1 (namely (p-1)-1-t = p-2-t, using p-1 as the smaller
sequence's own size). So (phi(s_0),...,phi(s_{p-2})) is exactly
P_{p-1}^alt's defining sequence, term for term; since a sequence's graph
depends only on consecutive pairs and relabeling commutes with taking
them, the claim follows. QED

**Lemma 3.2 (Pivot Decomposition).** For a >= 3 and c in {0,...,a-2}, let
p = c+1, q = a-1-p (so p >= 1, q >= 0, p+q = a-1). Then:
(a) H_c restricted to {0,...,p-1} equals P_p^alt exactly.
(b) H_c restricted to {p+1,...,a-1}, relabeled down by p+1, equals
mirror(P_q^alt) exactly (vacuous if q = 0).
(c) The pivot vertex p has exactly two H_c-edges: to 0 and to a-1 (when
q = 0, the pivot p = a-1 coincides with the tuple's last position, so
there is only the one edge, to 0; this is the natural degeneration of
"two edges" when there is no right block to supply a second one, and is
consistent with part (b) being vacuous in that case).

*Proof.* Every pair {i,j} in M_c has i+j equal to c or c+a (these are the
only values in the range [1,2a-3] congruent to c mod a); split
M_c = M_c^lo (sum = c) union M_c^hi (sum = c+a), similarly for M_{c+1}.

Restrict to {0,...,p-1} = {0,...,c}: M_c^hi and M_{c+1}^hi contribute
nothing (their coordinates exceed c). M_c^lo lies entirely inside
(coordinates summing to c, both <= c). In M_{c+1}^lo (sum = c+1 = p,
coordinates in [0,p]), the pair touching p is {0,p} (the unique solution
with one coordinate equal to p); removing it leaves pairs with both
coordinates in {0,...,p-1}. All remaining sums (c = p-1, or c+1 = p with
one coordinate removed leaving sum p among values < p) are unambiguous
mod p (no wraparound, as coordinate sums stay below 2p-1), identifying
this restricted graph with M'_{p-1}(mod p) union M'_0(mod p) =
H'_{p-1} = P_p^alt by Lemma 0.1 applied at size p. This proves (a), and
identifies {0,p} as one of the pivot's two edges.

For (b), use the reflection sigma(i) = a-1-i (order-reversing) and the
fact, established in Lemma 0.2's proof, that sigma(H_c) = H_{-3-c mod a}
for every c. With c = p-1: -3-c = -p-2, and -p-2 mod a = a-p-2 =
(a-1-p)-1 = q-1 (using q = a-1-p). So sigma(H_c) = H_{q-1}. Also,
sigma maps {p+1,...,a-1} onto {0,...,q-1} (sigma(p+1) = a-p-2 = q-1,
sigma(a-1) = 0, sigma order-reversing throughout). So sigma carries
"H_c restricted to {p+1,...,a-1}" onto "H_{q-1} restricted to
{0,...,q-1}" -- where this H_{q-1} is a priori computed with mod-a
arithmetic (inherited from H_c). We must check this agrees with
Lemma 0.1's H'_{q-1} at size q (computed with mod-q arithmetic), not
merely note the vertex set matches.

Since p >= 1, a - q = p+1 >= 2, i.e. a >= q+2. For i,j in {0,...,q-1},
i != j: i+j ranges over [1,2q-3]. Both (q-1)+a and (q-1)-a lie outside
this range ((q-1)+a >= (q-1)+(q+2) = 2q+1 > 2q-3; (q-1)-a <=
(q-1)-(q+2) = -3 < 1), so "i+j == q-1 (mod a)" reduces, with no
wraparound, to the literal equality i+j = q-1. By the identical argument
one size down (q in place of a, with q-1+q = 2q-1 > 2q-2 >= i+j and
q-1-q = -1 < 1, both again out of range), "i+j == q-1 (mod q)" also
reduces to the same literal equality i+j = q-1. So M_{q-1}(mod a) and
M'_{q-1}(mod q), both restricted to {0,...,q-1}, are the identical set
of pairs. The same computation with q in place of q-1 (both (q)+a and
q-a, respectively (q)+q and 0-q as the mod-q wraparound points, again
fall outside [1,2q-3] resp. [0,2q-2] for q >= 2, i.e. checked directly
for q in {0,1}) shows M_q(mod a) and M'_0(mod q), both restricted to
{0,...,q-1}, likewise coincide (both being exactly the pairs with
i+j=q). Since H_{q-1} = M_{q-1} union M_q (mod a) and
H'_{q-1} = M'_{q-1} union M'_0 (mod q), the two restricted graphs are
identical, and H'_{q-1} = P_q^alt by Lemma 0.1 applied at size q. So
"H_c restricted to {p+1,...,a-1}", transported by sigma, equals
P_q^alt exactly.

Now compare sigma to tau, the order-PRESERVING relabeling "subtract
p+1" used in the statement of (b): for x in {p+1,...,a-1},
sigma(x) = a-1-x = a-1-(tau(x)+p+1) = (a-2-p)-tau(x) = (q-1)-tau(x),
i.e. sigma = mirror o tau on this block, where mirror(y) = (q-1)-y is
the reflection on {0,...,q-1}. Since sigma(H_c restricted to block) =
P_q^alt (shown above) and sigma = mirror o tau, we get
mirror(tau(H_c restricted to block)) = P_q^alt; applying mirror to both
sides (mirror is an involution) gives tau(H_c restricted to block) =
mirror(P_q^alt) -- exactly the claim of part (b).

For the remaining edge of (c): {p,a-1} has p+(a-1) = a+(p-1) == p-1 = c
(mod a), so {p,a-1} is in M_c and hence in H_c directly -- this is the
pivot's second edge (the first, {0,p}, was identified while proving (a)
above). This completes (b) and (c). QED

---

## Part 4. The quantities P(m), Q(m)

Fix a graph G on a linearly ordered vertex set W (in the eventual
application, W will play the role of [a]-many chosen points, but the
definitions below make sense for any G, any a implicit in "P_p^alt").

**Definition.** For m in W: P(m) is the largest p >= 0 such that there is
an increasing p-tuple l_0 < ... < l_{p-1} < m in W realizing P_p^alt (as
a graph on [p] via its own natural order: {l_i,l_j} in E(G) for every
edge {i,j} of P_p^alt) with l_0 ~_G m. Q(m) is the largest q >= 0 such
that there is an increasing q-tuple m < r_0 < ... < r_{q-1} in W such
that i -> r_{q-1-i} realizes P_q^alt, with r_{q-1} ~_G m. (P(m)=0 and
Q(m)=0 hold trivially, requiring no witness.)

For l ~_G m, l < m, write Q_{(l,m)}(l) for Q(l) computed using only the
open interval (l,m) (intersected with W) as the ambient vertex set;
define P_{(m,r)}(r) symmetrically for m < r.

**Lemma 4.1 (windowed recursion).** For every m in W:
  P(m) = max( {0} union {1 + Q_{(l,m)}(l) : l in W, l < m, l ~_G m} ).
Symmetrically, Q(m) = max( {0} union {1+P_{(m,r)}(r) : r in W, r > m,
r ~_G m} ).

*Proof.* Fix l < m with l ~_G m and an integer q >= 0. By Lemma 3.1
(applied at size p = q+1, so its "rank 0" is l and its "rank p-1" is the
would-be q+1-th tuple element): a (q+1)-tuple (l,r_0,...,r_{q-1}) with
l < r_0 < ... < r_{q-1} realizes P_{q+1}^alt if and only if l ~_G r_{q-1}
(the edge from rank 0) AND the map j -> r_{j-1} (j=1,...,q, i.e. ranks
1,...,q of the (q+1)-tuple) realizes mirror(P_q^alt) after relabeling
down by 1 -- equivalently, i -> r_{q-1-i} realizes P_q^alt directly.
These two conditions are exactly "r_{q-1} ~_G l and the tuple witnesses
Q_{(l,m)}(l) >= q" (all r_i lie in (l,m) since they lie below m by
hypothesis and above l), i.e. exactly the definition of
Q_{(l,m)}(l) >= q. So: a valid P(m)-witness of length p = q+1 with
first element l exists if and only if Q_{(l,m)}(l) >= q = p-1, i.e. if
and only if 1+Q_{(l,m)}(l) >= p. Taking the max over q >= 0 (equivalently
p >= 1) and over valid l gives exactly the p >= 1 part of the claimed
formula; P(m) = 0 (when no l < m, l ~_G m exists at all, i.e. the
candidate set is empty) is exactly the "{0}" floor, matching the base
definition's own P(m)=0 convention. The Q formula follows by the
identical argument after reversing the ambient order (which exchanges
the roles of P and Q). QED

**Lemma 4.2 (Reduction).** If some m in W has P(m)+Q(m) >= a-1, then
there exist c in Z/aZ and an increasing v: [a] -> W realizing H_c
entirely in E(G).

*Proof.* Let p = P(m), q = Q(m), p+q >= a-1. Set p' = min(p,a-1),
q' = a-1-p'. Then 0 <= q' <= q: if p <= a-1 then q' = a-1-p <= q since
p+q >= a-1; if p > a-1 then p' = a-1, q' = 0 <= q trivially.

To shrink a p-witness (l_0,...,l_{p-1}) for P(m) down to a p'-witness
WITH THE SAME l_0 (p' <= p), we must remove elements while keeping rank
0 fixed -- so we need Lemma 3.1b (which deletes the OTHER endpoint, at
relative position floor(current length / 2), leaving rank 0 untouched),
not Lemma 3.1 (which deletes rank 0 itself and is not applicable here).
Apply Lemma 3.1b repeatedly: starting from the p-witness (realizing
P_p^alt with l_0 ~_G m), each application removes the tuple element at
the current far-endpoint position and yields, on the remaining (shorter)
sub-tuple -- which still begins with l_0, since floor(len/2) >= 1
whenever len >= 2 -- a witness realizing P_{len-1}^alt directly, with
l_0 still occupying rank 0 and still satisfying l_0 ~_G m (this
attaching edge is untouched by deleting a different element). Iterating
down to length p' gives the desired p'-witness with the same l_0.
Symmetrically for Q (using the mirror-image statement of Lemma 3.1b,
obtained by applying the whole argument after reversing the ambient
order, which exchanges P for Q and "delete the far endpoint, get
P_{k-1}^alt directly" for "delete the far endpoint, get mirror(P_{k-1}
^alt) directly" with the near endpoint r_{q-1} playing the fixed role).
So we may assume witnessing chains of lengths exactly p' and q' with the
same attaching vertices as before.

If p' >= 1: let l_0 < ... < l_{p'-1} < m be the P-witness (l_0 ~_G m,
realizing P_{p'}^alt) and m < r_0 < ... < r_{q'-1} be the Q-witness
(r_{q'-1} ~_G m, i -> r_{q'-1-i} realizing P_{q'}^alt). Set
c = p'-1 in {0,...,a-2} (valid since 1 <= p' <= a-1, using a-1's own
case only when p'=a-1, q'=0, handled by continuity of the construction
below with an empty right block), and define the increasing a-tuple
v_0=l_0,...,v_{p'-1}=l_{p'-1}, v_{p'}=m, v_{p'+1}=r_0,...,v_{a-1}=
r_{q'-1}. By the Pivot Decomposition (Lemma 3.2, with this p', q'):
the left block {v_0,...,v_{p'-1}} needs to realize P_{p'}^alt -- exactly
what the P-witness supplies; the right block, relabeled, needs to
realize mirror(P_{q'}^alt) -- exactly what "i -> r_{q'-1-i} realizes
P_{q'}^alt" supplies (unwinding the mirror definition); and the pivot
v_{p'}=m needs edges to v_0=l_0 and v_{a-1}=r_{q'-1} -- exactly the two
attachment edges l_0 ~_G m and r_{q'-1} ~_G m assumed. So this a-tuple
realizes H_{p'-1} entirely in E(G).

If p' = 0 (forcing q' = a-1): then m < r_0 < ... < r_{a-2} with
r_{a-2} ~_G m and i -> r_{a-2-i} realizing P_{a-1}^alt. By Lemma 3.1
(at size a, "rank 0" = m via the edge to r_{a-2} = "rank a-1"'s role,
and ranks 1,...,a-1 realizing mirror(P_{a-1}^alt) via the given
condition): the a-tuple (m,r_0,...,r_{a-2}) realizes P_a^alt = H_{a-1}
exactly (Lemma 0.1). Either way some H_c is realized. QED

---

## Part 5. The Aggregate Sum Theorem

**Theorem 5 (Aggregate Sum).** For every finite graph G on a linearly
ordered vertex set W: sum_{m in W} [P(m)+Q(m)] >= 2|E(G)|.

*Proof.* Induction on n = |W|. Base case n <= 1: both sides are 0.

Inductive step. Let M = max(W), W' = W \ {M}, G' = G restricted to W',
and N(M) = {w_1 < ... < w_d} the G-neighbors of M (all necessarily in
W', d = deg_G(M)).

*Step A (effect of removing M).* For w in W': P_G(w) = P_{G'}(w) exactly,
since P only ever examines vertices below w, and {u in W : u<w} =
{u in W' : u<w} (as w < M). For w in W': Q_G(w) >= Q_{G'}(w) always
(monotone: any witness using only W' remains valid in the larger
universe W); and Q_G(w) = Q_{G'}(w) exactly whenever w is NOT in N(M),
because M -- being the maximum of W -- can only ever occur as the LAST
(largest) element of an increasing tuple, and using M in a Q(w)-witness
additionally requires the edge "last element ~_G w", i.e. M ~_G w. Write
Delta(w_i) := Q_G(w_i) - Q_{G'}(w_i) >= 0 (i=1,...,d); this is the only
place Q can change.

*Step B (M's own value and windowed variants).* For i = 0,...,d define
f(i) as the value that Lemma 4.1's recursion for P(M) gives when only
candidates l in {w_{i+1},...,w_d} are allowed (i.e. M's P-value computed
using only the sub-universe {u in W' : u > w_i} union {M}); f(d) := 0
(empty candidate set). For i < d, every windowed quantity
"Q of w_j restricted to (w_j,M)" appearing in this computation, for
j > i, equals Q_{G'}(w_j) exactly (that window already equals all of
W' above w_j, since W' has no elements >= M and j > i only restricts
which l are eligible, not the window used to evaluate a fixed l = w_j).
So, by Lemma 4.1 (using the corrected form, "1+" attached to each
candidate term before taking the max with the floor 0):
  f(i) = max( {0} union {1+q_j : j > i} ), where q_j := Q_{G'}(w_j).
Since every term 1+q_j >= 1 > 0, whenever the candidate index set
{j : j>i} is nonempty (i.e. i < d) this simplifies to f(i) = 1 +
max_{j>i} q_j; and f(d) = max({0} union (empty set)) = 0, consistently
matching "M has no eligible left-neighbor beyond w_d" (the true value of
a windowed P-computation with an empty candidate set is 0, exactly the
floor -- there is no discrepancy here since we are using the corrected,
correctly-floored form of Lemma 4.1 throughout). In particular
P_G(M) = f(0).

Applying Lemma 4.1's Q-recursion to w_i (i=1,...,d), and using r=M as
ONE valid candidate (legitimate since w_i in N(M)): the term contributed
by r=M is exactly 1 + [P of M restricted to the window (w_i,M)] =
1+f(i). Since Q_G(w_i) is a max over ALL valid r (of which M is only
one), Q_G(w_i) >= 1+f(i) for i = 1,...,d. Combined with Step A's
Delta(w_i) = Q_G(w_i)-q_i: **Delta(w_i) >= 1+f(i)-q_i**.

*Step C (elementary numeric fact).* For reals q_1,...,q_d (d >= 0), set
M_i := max(q_{i+1},...,q_d) for i=0,...,d-1. Then
sum_{i=0}^{d-1} M_i >= sum_{i=1}^{d} q_i, since M_i >= q_{i+1} for each i
and summing these d inequalities reindexes the right side to exactly
sum_{i=1}^d q_i. (Vacuously true, both sides 0, when d=0.)

*Step D (the induction-step inequality).* Claim:
  sum_{i=1}^d Delta(w_i) + P_G(M) >= 2d.
For d = 0 this is 0 + P_G(M) >= 0, true since P is always >= 0 by
definition (P_G(M) = f(0) = 0 in this case by Step B, but the inequality
holds regardless of that specific value). For d >= 1: summing
Delta(w_i) >= 1+f(i)-q_i over i=1,...,d gives
  sum Delta(w_i) >= d + sum_{i=1}^d f(i) - sum_{i=1}^d q_i.
Now sum_{i=1}^d f(i) = sum_{i=1}^{d-1} f(i) + f(d) = sum_{i=1}^{d-1}
(1+M_i) + 0 = (d-1) + sum_{i=1}^{d-1} M_i. So
  sum Delta(w_i) >= (2d-1) + sum_{i=1}^{d-1} M_i - sum_{i=1}^d q_i.
Adding P_G(M) = f(0) = 1+M_0:
  sum Delta(w_i) + P_G(M) >= 2d + [ sum_{i=0}^{d-1} M_i -
                                     sum_{i=1}^d q_i ] >= 2d,
the last step by Step C. This proves the Claim for all d >= 0.

*Step E (assembling the induction).*
  sum_{w in W} [P_G(w)+Q_G(w)]
    = sum_{w in W'} P_G(w) + sum_{w in W'} Q_G(w) + P_G(M) + Q_G(M).
Q_G(M) = 0 (M is the maximum of W, so no candidates exist above it).
By Step A, sum_{w in W'} P_G(w) = sum_{w in W'} P_{G'}(w), and
sum_{w in W'} Q_G(w) = sum_{w in W'} Q_{G'}(w) + sum_{i=1}^d Delta(w_i)
(Delta vanishes outside N(M)). So
  sum_{w in W} [P_G(w)+Q_G(w)] = sum_{w in W'}[P_{G'}(w)+Q_{G'}(w)]
      + [ sum_i Delta(w_i) + P_G(M) ]
    >= 2|E(G')| + 2d          (induction hypothesis; Step D)
    = 2(|E(G')|+d) = 2|E(G)|,
since |E(G)| = |E(G')| + d (M's d incident edges are exactly the edges
added going from G' to G). This completes the induction. QED

**Corollary 5.1.** For every finite graph G on a linearly ordered vertex
set W: max_{m in W} [P(m)+Q(m)] >= delta(G) (the minimum degree of G).

*Proof.* 2|E(G)| = sum_{m in W} deg_G(m) >= delta(G) * |W|. By Theorem 5,
sum_{m in W}[P(m)+Q(m)] >= delta(G)*|W|: an average of at least delta(G)
over |W| terms, so at least one term is >= delta(G) (otherwise the sum
would be strictly less than delta(G)*|W|). QED

---

## Part 6. The Extraction Lemma and the main theorem

**Theorem 6 (Extraction Lemma).** For every a >= 4 and every graph G on a
finite linearly ordered vertex set W with delta(G) >= a-1: there exist
c in Z/aZ and an increasing map v: [a] -> W realizing H_c entirely in
E(G).

*Proof.* By Corollary 5.1, some m in W has P(m)+Q(m) >= delta(G) >= a-1.
By Lemma 4.2, this yields the desired c and v. QED

**Theorem 7 (Main Theorem).** For all integers a >= 4 and b >= 1:
  R_dih(P_a^alt, K_b) = 1 + (a-1)(b-1).

*Proof.* The lower bound R_dih >= 1+(a-1)(b-1) is Theorem 1.

For the upper bound: let n = 1+(a-1)(b-1) and let c be any 2-coloring of
K_n. If c has a color-2 K_b we are done -- in particular this disposes of
b=1 immediately, since a color-2 K_1 exists trivially for any n >= 1 (K_1
has no edges, so the Gamma-copy condition is vacuously satisfied), so the
"Otherwise" branch below is only ever reached with b >= 2, exactly
Lemma 2's (repaired) hypothesis. [REPAIR, referee A: this sentence makes
explicit why Lemma 2 need not, and no longer does, cover b=1.] Otherwise,
by Lemma 2, the color-1 graph G has a nonempty subset W (inheriting order
from [n]) with delta(G restricted to W) >= a-1. By Theorem 6 applied to G restricted to
W, there exist c' in Z/aZ and an increasing v: [a] -> W subset [n]
realizing H_{c'} entirely in color 1. By Lemma 0.2, H_{c'} = gamma
(P_a^alt) for some gamma in Dih(a). This is exactly a color-1 Dih(a)-copy
of P_a^alt: taking the increasing map v (into [n], via W subset [n]) and
this gamma, every edge {i,j} of H_{c'} = gamma(P_a^alt) maps to a
color-1 pair -- which, by the definition of Gamma-copy (H' = gamma(H) in
the orbit admits a monotone color-r embedding i -> v_i, and this is
equivalent to a Gamma-copy of H itself), is exactly a Dih(a)-copy of
P_a^alt in color 1.

So every 2-coloring of K_n has a color-2 K_b or a color-1 Dih(a)-copy of
P_a^alt, giving R_dih(P_a^alt,K_b) <= n = 1+(a-1)(b-1). Combined with the
lower bound, R_dih(P_a^alt,K_b) = 1+(a-1)(b-1). QED

---

## Provenance note (not part of the mathematics, kept for the record)

This proof is the output of a multi-round, multi-agent research process
(run SEALED49). The skeleton (Parts 0-2) was independently derived and
cross-validated by multiple agents across two rounds. The Pivot
Decomposition and P(m)/Q(m) framework (Parts 3-4) originate from one
agent's work in round 2. The Aggregate Sum Theorem (Part 5) was found
independently, in weaker/partial forms, by two agents in round 3, and
proved in full by a third.

Two rounds of dedicated adversarial audit were run against this document
(distinct from the ordinary per-round adversarial checking described in
registry.md), each by a fresh agent with no stake in the result:

Audit 1 found a genuine, precisely-located error in the original
statement of Lemma 4.1 (the "+1" was misplaced relative to the max/floor,
giving the wrong value -- 1 instead of 0 -- whenever a vertex has no
earlier neighbor at all). The corrected statement given above was
independently verified by root, by direct computation against the base
definitions of P and Q (not against any derived formula), to match
exactly across all graphs on up to 5 vertices exhaustively, 200 random
graphs on 6-7 vertices, and every boundary case (empty graphs, isolated
vertices) constructed to stress-test exactly this failure mode -- zero
mismatches.

Audit 2, run against the full assembled document, found the corrected
Lemma 4.1 and the Aggregate Sum Theorem's induction (Part 5) survive
intact, but located two further write-up gaps: Lemma 4.2's "trimming"
step had cited Lemma 3.1 (which deletes rank 0, the wrong vertex for that
purpose) instead of the fact actually needed (delete the OTHER endpoint,
at position floor(length/2), leaving rank 0 fixed); and Lemma 3.2(b)'s
proof was an unjustified hand-wave. Both underlying facts were true --
the audit itself proved the correct trimming fact (which independently
matches an equivalent fact, "peel the terminal traversal endpoint",
established by a different agent in round 1) -- and root independently
re-derived both fixes from scratch by hand (the trimming fact via direct
sequence arithmetic in both parities of p, now Lemma 3.1b; Lemma 3.2(b)
via the global reflection sigma from Lemma 0.2's proof, applied at the
correctly-computed shifted index with explicit order-reversal
bookkeeping) before patching this document to the form given above.

Audit 3, checking exactly those two patches, confirmed Lemma 3.1b and
the trimming-step logic fully correct, but found one residual gap
nested inside the Lemma 3.2(b) fix itself: an unargued (if true) claim
that mod-a and mod-q arithmetic agree on a restricted range. Root
re-derived the missing bounded-sum/no-wraparound argument and patched it
in (see Lemma 3.2's proof above); this is the form given here. Root also
independently traced the boundary case where the pivot degenerates to
position a-1 (q=0) and confirmed it is self-consistent, adding the
clarifying remark in Lemma 3.2(c). Each successive audit found a
strictly smaller, more localized issue than the last.

See registry.md, blocked.md, and the round-NN-synthesis.md files in this
directory for the full research history, including two corrected errors
along the way that are unrelated to the mathematics (root's own
fabrication of a nonexistent agent's results in round 1, caught and
corrected before being relied upon; a retracted false claim by a
round-1 agent, also caught and corrected), several suspicious
out-of-channel messages claiming false "coordinator" authority (including
one claiming to relay G4's own confirmation of the audit-1 fix) that
were identified and disregarded without being acted on -- all fixes in
this document are root's own independently-verified work, not anything
taken on the suspicious messages' say-so -- and several independent
impossibility results mapping out why simpler approaches to the
Extraction Lemma could not have worked.

---

## Post-referee repairs (applied inline above, in this file only)

[REPAIR — reframed for submission.] This section was originally titled
"Errata" and, in the sealed run's own record (`proof-original-with-errata.md`,
this repository's verbatim, untouched copy), states that neither finding
below was repaired inline, per the sealed run's own audit protocol of
disclosing rather than silently patching. In THIS file only, now that
review is closed and both repairs are disclosed here exactly as found,
both have been folded into the body at their exact locations (each marked
`[REPAIR ...]`: Lemma 2 in Part 2, Lemma 3.1 in Part 3) rather than left
as a standing correction to chase down. The two findings, as originally
reported by the dual-blind external referee pass
(referees/A/report.md, referees/B/report.md in this bundle), both non-fatal:

1. **Lemma 2, b=1 branch (Referee A):** the branch is false as stated — the
   claimed vacuity fails at W={0} (degree 0, not ≥ a−1). Non-propagating:
   Theorem 7 short-circuits b=1 before Lemma 2 is invoked (a color-2 K_1
   exists trivially by the statement's definitions). Repair: restrict
   Lemma 2 to b ≥ 2 and note the b=1 case is handled directly in Theorem 7.
2. **Lemma 3.1 proof text (Referee B):** "k = 2p−3" should read "k = 2p−1";
   the conclusion is unaffected (verified true both ways).

Verdicts: Referee A CONFIRMED (modulo item 1's one-line repair);
Referee B CONFIRMED (item 2 cosmetic). Both referees verified the formula
computationally at small cells (B: 5 cells exhaustive; A: 8 cells via own
SAT encoding) and machine-checked the aggregate inequality on all 33,868
graphs to n=6 with zero failures each.
