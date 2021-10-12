# Relational Algebra and Data Model - 10/8/2021
## Definitions
### Relation
* A **relation** is a set of tuples which is a subset of the **Cartesian product** of some number of sets.
* So take a bunch of sets and get the Cartesian product of them all. Any subset of that is called a relation on those sets. i.e.
$$
\text{A relation $R$ on $n$ sets $A_1,A_2,\dots,A_n$ is defined as any $R$ such that:}\\
R \subseteq A_1 \times A_2 \times \dots \times A_n
$$

#### $n$-ary Relation
An **$n$-ary relation** is a relation on $n$ sets.

##### Binary Relation
If $n=2$, the relation is called a **binary relation**.

e.g. $R \subseteq A \times B$ where $A$ and $B$ are sets.

#### Relations on a (Single) Set
A **relation on a set** $A$ denotes a relation from $A$ to $A$. i.e.
$$
R \subseteq A \times A
$$

### Relational Hierarchy
![](img/lesson_15_0.png)

## Relation Operations
There's 3 key operators for relations:
* union
* intersection
* difference

Remember that relations are just sets, so these are actually the same as they would be for sets. In fact I'm not even going to go over them. Go to [this file](pdf/RelationalAlgebra.pdf) if you really want to see the worked examples.

There is one key different operator and that's...
### Relational Cross-product
