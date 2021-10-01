# Tautologies and Logical Equivalences - 9/24/2021
## Definitions
A **tautology** is a compound proposition that is always true, no matter the truth values of its propositional variables. e.g.
* $p \vee T$

A **contradiction** is a compound proposition that is always false. e.g.
* $p \wedge F$

A **contingency** is a compound proposition that is neither a *tautology* or a *contradiction*. e.g.
* $p \vee F$

## Logical Equivalence
### Definition
Let $p$ and $q$ be compound propositions. Then they are **logically equivalent** if $p \rightarrow q$ is a tautology, and we write
$$
p \equiv q
$$

### Useful Equivalences and Examples
1. Identity
$$
p \wedge T \equiv p \\
p \vee F \equiv p
$$
2. Domination
$$
p \vee T \equiv T \\
p \wedge F \equiv F
$$
3. Distributive
$$
p \wedge (q \vee r) \equiv (p \wedge q) \vee (p \wedge r) \\
p \vee (q \wedge r) \equiv (p \vee q) \wedge (p \vee r)
$$
4. Conditional-Disjunctive Equality
$$
p \rightarrow q \equiv \neg p \vee q
$$
5. Negation
$$
p \vee \neg p \equiv T \\
p \wedge \neg p \equiv F
$$
6. De Morgan's Laws
$$
\neg (p \wedge q) \equiv \neg p \vee \neg q \\
\neg (p \vee q) \equiv \neg p \wedge \neg q
$$

## Conjunctive Normal Form (CNF)
**CNF** is a standard form of compound propositions. In it, propositional variables and expressions are:
* *grouped* by **disjunction**
* *separated* by **conjunction**

Furthermore, **no compound propositions can be negated in CNF**. i.e. it can only precede an atomic proposition. i.e. none of this: $\neg(p\rightarrow q)$

It's helpful to use equivalences $(4)$ and $(6)$ above when converting compound propositions to CNF. Take the following example:
$$
(p \rightarrow q) \wedge r \wedge (r \rightarrow p)
$$
We can convert our implications to disjunction using $(4)$ so that we only have disjunctions and conjunctions.
$$
(\neg p \vee q) \wedge r \wedge (\neg r \vee p)
$$
And boom you got yaself some CNF.
