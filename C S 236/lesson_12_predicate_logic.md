# Predicate Logic - 9/27/2021
## Introduction
Propositional logic can only express propositions. A **predicate** is a parameterized proposition. It's like a discrete function that maps a domain to a range whose codomain is $\{T, F\}.$

We define it as $P(x)$. They are also often called propositional functions. Here's an example:

| $x$ | $P(x)$ |
|-----|--------|
| $1$ | T
| $2$ | T
| $3$ | F
| $4$ | F

This table represents the proposition $x < 3$ for $x \in \{1,2,3,4\}$. Here's one that represents $y \text{ is odd}$ for $y \in \{1,2,3,4,5\}$.

| $y$ | $Q(y)$ |
|-----|--------|
| $1$ | T
| $2$ | F
| $3$ | T
| $4$ | F
| $5$ | T

## Quantifiers
A **quantifier** defines the extent to which a predicate is true or false. There are many types, 2 ones we'll talk about are:
1. The Universal Quantifier
2. The Existential Quantifier

### Universal Quantification
The **universal quantification** of $P(x)$ is the statement
$$
\text{$P(x)$ [is true] for all values $x$ in the domain.}
$$
The notation for this is
$$
\forall x P(x)
$$

This denotes the universal quantification of $P(x)$. $\forall$ is called the universal quantifier. You can also think of it as the words *for all*.

A **counterexample** of $\forall P(x)$ is a value of $x$ for which $P(x)$ is false.


### Existential Quantification
The **existential quantification** of $P(x)$ is the proposition
$$
\text{There exists an element $x$ in the domain such that $P(x)$ [is true].}
$$
The notation for this is
$$
\exists x P(x)
$$

This denotes the existential quantification of $P(x)$. $\exists$ is called the existential quantifier, and can is read as *there exists*.

### Precedence and Scope
The quantifiers $\forall$ and $\exists$ have higher precedence than all propositional logic operators. So
$$
\exists x P(x) \wedge Q(x)
$$
becomes
$$
\begin{alignat}{1}
\text{THIS:}\quad&[\exists x P(x)] \wedge Q(x)\\
\text{NOT THIS:}\quad&\exists x [P(x) \wedge Q(x)]
\end{alignat}
$$

However, this no raises a question of **scope**. In defining a variable's scope it is either:
* bound
	* We bind a variable $x$ to a predicate $P(x)$ with a quantifier or with a value.
* free
	* An unbound variable, or **free** variable, is not bound to any predicate.

When we have unbound variables, we don't really like it because we don't know how to handle it.

In the example above, $x$ is bound to $P(x)$, but $x$ is **free** in $Q(x)$. For now, we will use something we call **universal generalization** as convention:
* bound any unbound/free variables in predicates to the universal quantifier $\forall$
* rename any variables that are independent from one another to have unique names

This is what's going to be most useful in $\text{Datalog}$.

So the example above would go from:
$$
[\exists x P(x)] \wedge Q(x)\\
$$
to
$$
[\exists x P(x)] \wedge [\forall y Q(y)]\\
$$

A good analogy is with `C++` or any other programming language:
```cpp
{
	std::string test("testing the string bean");
	std::cout << test << std::endl;
}
// the following will generate a compilation error because test is out of scope
std::cout << test << std::endl;
```

## Logical Equivalences in Predicate Logic
Here are some useful logical equivalences we use in predicate logic:
$$
\begin{alignat}{1}
& 1. \quad & \forall x [P(x) \wedge Q(x)] \equiv \forall x P(x) \wedge \forall x Q(x) \\
& 2. \quad \neg & \forall x P(x) \equiv \exists x \neg P(x) \\
& 3. \quad \neg & \exists x P(x) \equiv \forall x \neg P(x)\\

\end{alignat}
$$
