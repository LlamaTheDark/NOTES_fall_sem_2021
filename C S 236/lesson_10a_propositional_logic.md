# Propositional Logic - 9/24/2021
## Definition
A **proposition** is a declarative sentence that is either true or false, but not both.

Examples (those checked are propositions):
- [x] The earth is round
- [ ] Are you sure the earth is round?
- [x] The sky is blue.
- [ ] Look up.
- [ ] Why does my head hurt?
- [x] My head hurts.

A **propositional variable** is a letter that represents a proposition. Usually we use $p,w,r,s,\dots$.

The **truth value** of a proposition is either true $T$ or false $F$. It represents the truthfulness of the proposition.

## Propositional Logic
**Propositional logic** is the area of logic that deals with propositions. When form new propositions using logical operators on existing propositions, we create **compound propositions**.

## Truth Table
A truth table functions much the same as a binary operation table does it's pretty self explanatory you'll see a bunch of em in the **logical operators** section.

## Logical operators
These are a lot like binary operators but with a little extra spice. For all these examples let $p$, $q$ and $r$ be propositions.
### Negation, $\neg$
| $p$ | $\neg{}p$ |
|-----|-----------|
| T   | F |
| F   | T |

* Negation of $p$ is $\text{not }p$
* `negation(p)=!p`

### Conjunction, $\wedge$
| $p$ | $q$ | $p \wedge q$ |
|-----|-----|--------------|
| T   | T   | T
| T   | F   | F
| F   | T   | F
| F   | F   | F

* Conjunction of $p$ and $q$ is $(p \text{ and } q)$
* `conjuction(p, q) = p && q`

### Disjunction, $\vee$
| $p$ | $q$ | $p \vee q$ |
|-----|-----|------------|
| T   | T   | T
| T   | F   | T
| F   | T   | T
| F   | F   | F

* Disjuntion of $p$ and $q$ is $(p \text{ or } q)$
* `disjunction(p, q) = p || q`

### Implication, $\rightarrow$
This one is sometimes called the *conditional statement*. In the statement $p\rightarrow q$, $p$ is called the **premise** and $q$ is called the **consequence**.

| $p$ | $q$ | $p \rightarrow q$ |
|-----|-----|------------|
| T   | T   | T
| T   | F   | F
| F   | T   | T
| F   | F   | T

* Implication of $p$ and $q$ is $(\text{if $p$, then $q$})$
	* it is false when $p$ is true and $q$ is false.
	* it is true otherwise.
* `implication(p, q) = (q == T) || (q == p)`
* `implication(p, q) = (!p) || q`

### Bi-implication, $\leftrightarrow$ or $\iff$
$p \iff q$ is called *biconditional statement*.

| $p$ | $q$ | $p \leftrightarrow q$ |
|-----|-----|------------|
| T   | T   | T
| T   | F   | F
| F   | T   | F
| F   | F   | T

* Bi-implication of $p$ and $q$ is (\text{$p$ if and only if $q$})
* `biimplication(p, q) = p == q`

### Precedence of Logical Operators
| Precedence | Operator |
|------------|----------|
| 1 | $\neg$
| 2 | $\wedge$
| 3 | $\vee$
| 4 | $\rightarrow$
| 5 | $\leftrightarrow$

We use left-to-right evaluation.
