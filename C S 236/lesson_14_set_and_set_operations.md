# Set and Set Operations - 10/6/2021
## Definition
* A **set** is an **unordered** collection of objects
* These objects are called **elements** or **members** of the set
* A set is said to **contain** its elements
* We write $a \in A$ to denote that $a$ is an element of the set $A$
* We write $a \notin A$ to denote that $a$ is *not* and elemnet of the set $A$

## Empty Set
The **empty set** is the set that contains no elements, and is denoted by the symbol $\varnothing$ or $\emptyset$. That is
$$
\varnothing=\emptyset=\{\}
$$
* The *cardinality* or size of the empty set is 0
* A set containing the empty set is denoted as $\{\varnothing\}$ and has a cardinality of 1.
* The empty set is **not** inherently an element of each set.

## Universal Set
Often defined as $U$, the **universal set** contains all possible elements of the domain.

## Notation
For sets with **finite elements**, we put all elements contained by the set between curly braces $\{\}$. E.g.
$$
A=\{1, 2, 3\}
$$
You can also have sets which contain other sets (as seen in the empty set section) E.g.
$$
B=\{A, \{1, 2\}, \{7\}, g\}
$$

### Set Builder Notation
When we have a **non-finite** amount of elements, or if we just prefer it this way, we can use **set-builder notation** *to describe what elements are in a set without being explicit*. The notation is as follows:
$$
A=\{x|x\text{ satisfies some property}\}
$$
which may be read as
> $A$ is the set that contains element $x$ such that $x$ satisfies some property.

For example
$$
\begin{align}
A&=\{
	x|x\text{ is odd }\wedge 0<x<10
\}\\
\text{is equivalent to }
A&=\{1, 3, 5, 7, 9\}
\end{align}
$$

We can also restrict our listed variables to some domain in our definition. e.g.
$$
B=\{x \in \mathbb{Z}^+ | x\text{ is even }\wedge x <12\}
$$
Where $\mathbb{Z}^+$ is the set of all positive integers. You don't just have to do this with predefined sets like $\mathbb{ C },\mathbb{ R }, \mathbb{ N },$ etc... You can also use other sets you've created.

### Set Equivalence
* Two sets $A$ and $B$ are **equal** $\iff \forall x (x \in A \iff x \in B)$.
	* i.e. they are equal if and only if they have all the same elements
* If they are equal, we write $A=B$.

### Subsets
* The set $A$ is a **subset** of the set $B$ $\iff \forall x (x \in A \rightarrow x \in B)$
	* i.e. $A$ is a subset of $B$ if and only if every element in $A$ is an element in $B$.
* The notation $A \subseteq B$ denotes that $A$ is a subset of $B$.
* For every set $S$:
$$
\begin{align}
& 1. \quad \varnothing \subseteq S \qquad \\
& 2. \quad S \subseteq S
\end{align}
$$
#### Proper Subsets
* $A$ is a **proper subset** of $B$ if $A$ is a *subset* of $B$ but $A \neq B$.
* We denote this with $A \subset B$.

### Set Size
* The **size** or **cardinality** of a given set $S$ cannot be determined if the set is *infinite*.
	* $S$ is said to be *infinite* if it is **not** *finite*.
* The cardinality $n$ of the **finite** set $S$ is the number of distinct elements in $S$.
	* $n \in \mathbb{ Z }^+$
* $|S|$ denotes the cardinality of the set $S$.

### Power Set
* The **power set** of a set $S$ is the set of all subsets of $S$.
* It is denoted by $\mathcal{P}(S)$
* Alternate notation for the power set of $S$ is $2^S$
	* This stems from the cardinality of the power set of $S$
$$
|\mathcal{P}(S)|=|2^S|=2^{|S|}
$$

Worked example:

![](img/lesson_14_0)

## Set Operations
There are more than 6, but we're only going to talk about 6:
* union
* intersection
* difference
* complement
* Cartesian product
	* tuple

### Union, $\cup$
$$
A \cup B = \{x|x \in A \vee x \in B\}
$$

### Intersection, $\cap$
$$
A \cap B = \{x|x \in A \wedge x \in B\}
$$

##### Disjoint Sets
Two sets $A$ and $B$ are **disjoint** if $A \cap B = \varnothing$

### Set Difference
$$
A-B = \{x|x \in A \wedge x \notin B\}
$$
i.e. every element in $A$ that is not in $B$

##### Set Complement, $\bar{S}$
$$
\bar{S}=U-S
$$
i.e. the difference of $U$ and $S$; every element in the *universal set* that is not in $S$.

### Tuple
An *ordered $n$-tuple* is the ordered collection that has $a_1$ as its first element, $a_2$ as its second element, $\dots$, and $a_n$ as its $n$th element. We can write it as:
$$
(a_1, a_2, \dots, a_n)
$$

##### Ordered Pairs
An **ordered pair** is another way to say an ordered 2-tuple $(a, b)$.

### Cartesian Product
* Let $A$ and $B$ be sets
* The **Cartesian product** of $A$ and $B$ is the set of all ordered pairs where $a \in A$ and $b \in B$
* $A \times B$ denotes the Cartesian product of $A$ and $B$.
$$
A \times B = \{(a, b) | a \in A \wedge b \in B\}
$$

##### Cartesian product of more than 2 sets
* We can extend our definition above to $n$ sets: $A_1, A_2, \dots, A_n$.
* To find the Cartesian product of all these sets (i.e. $A_1 \times A_2 \times \dots \times A_n$) we follow the set notation:
$$
A_1 \times A_2 \times \dots \times A_n = \{
	(a_1, a_2, \dots, a_n) | a_i \in A_i \text{ for } i = 1, 2, \dots, n
\}
$$

##### Here's some helpful ways to think about calculating the Cartesian product:
---
***full disclosure: I don't know if this is legit or not. I may have made a mistake in the logic here. The code example below is golden though. In fact after coming back to it I'm almost certain this is wrong.***

Intuitively, you can use parenthesis to visualize the order of operations. i.e.
$$
(\dots((A_1 \times A_2) \times A_3) \dots ) \times A_n)
$$
This way, you're only doing the cartesian product of one two sets at a time so it's the same as the first description we saw.

Yeah so ***don't do this*** because what you're gonna end up with is the product of a Set and a Relation which changes whether order matters in some cases. See `lesson_15_relational_algebra_and_data_model.md`.

I'm gonna keep this here just as something to think about because realizing why it's wrong did help me learn more about this.

---

Even more intuitively, here's a block of code to create the Cartesian product of any amount of sets:
```py
def cartesian_product(A_1, A_2, ..., A_n):
	result = []
	for a_1 in A_1:
		for a_2 in A_2:
			...
				for a_n in A_n:
					result.append((a_1, a_2, ..., a_n))
	return result
```

##### Cardinality of Cartesian product
The *cardinality* of the Cartesian product of any number of sets is the product of the cardinalities of each individual set.
$$
|A_1 \times A_2 \times \dots \times A_n| = |A_1| \times |A_2| \times \dots \times |A_n|
$$
##### Cartesian product with the empty set, $\varnothing$
The empty set has no elements, and thus there are no possible combinations to be had between it and another set. It follows that $|\varnothing \times A|=0 \times A=0$

## Bit-string Representation of Sets
To represent sets with bit-strings, we can do the following:
* A `1` signifies that a set contains a given element.
* A `0` signifies a set does *not* contain a given element.
* The place of the `1` or `0` determines the element being spoken of.
* Let the universal set be $U=111 \dots 1$ where there are $n$ $1$s and therefore $n$ **bits** required to represent the set.
	* This is because the universal set contains all possible elements of a given domain.
* Then any other set can be defined in terms of the universal set.

Example:

$\text{Let $U=\{a, b, c, d, e\}$, $A=\{a\}$, and $B=\{b, c, e\}$}$

Then we say:
$$
\begin{align}
U&=11111\\
A&=10000\\
B&=01101
\end{align}
$$
