# Regular Expressions - 9/1/2021
## Definition
Regular expressions as I understand them now are a few predefined sets that interact with eachother with some cool operations.

*Note: There are no wildcards (match anything w/ a prefix or postfix) in our formal definition of regular expressions. However, in application, you're almost definitely going to have wildcards.*

## Formal language definitions
* Symbol: an element of a set
* String: a sequence of symbols
* Language: a set of strings
* Word: A string of a language
* Vocabulary: A finite, non-empty set of symbols.
	* Like an alphabet containing all the letters (symbols) you wanna use.

## Recognizers and Generators
|expression|definition|
|---|---|
|$\phi$|Represents the empty set|
|$\lambda$|Represents the set containing the empty string|
|$x$ where $x \in I$|Represents the set $\{x\}$ with one symbol $x$|
|($\text{AB}$)|Represents the concatenation of the sets represented by $\text{A}$ and $\text{B}$|
|($\text{A}\cup\text{B}$)|Represents the union of the two sets.|
|$\text{A*}$|represents the **Kleene** closure of the set represented by $\text{A}$|

These definitions are recursive - they define base cases.

 * **Recognizers**: constructs which accept a language.
 * **Generators**: Constructs which create strings of a specific language.

e.g.
$$(0 \cup 1)\text{*}$$
is binary including $\lambda$. If you don't want lambda present you can do:
$$(0 \cup 1)(0 \cup 1)\text{*}$$

## Practice Problems
`You can find these in pdf/practice/`

1.
$$ab\text{*}a$$

2.
$$0\text{*}\cup{}1\text{*}$$

3.
$$1\cup(12)\cup(123)\cup(1234)$$
or
$$1(\lambda{}\cup{}2(\lambda{}\cup{}3(\lambda\cup{}4)))$$

4.
$$L = \{\lambda, ab, ba, abab, baba, ababab, bababa, \dots\}$$

5.
$$L = \{0, 110, 11110, 1111110, \dots\}$$

6.
$$L = \{11, 0, \lambda, 333, 2, 22, 222, 2222, \dots\}$$
