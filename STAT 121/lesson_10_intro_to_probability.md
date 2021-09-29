# STAT 121 Lesson 10 - Introduction to Probability
## Probability Theory
Components:
1. Specify game/**experiment** (including **strategy**)
2. Specify possible **outcomes**
3. Specify **probability distribution**
	* i.e. long run proportion associated with each possible outcome

Rules:
* a probability must be a number between 0 and 1
$$
0\leq{}p\leq{}1
$$
* the sum of probabilities from all possible outcomes must equal 1
$$
\sum^n_{i=0}{p_i}=1
$$
* if two events cannot occur simultaneously, the probability either one or the other occurs equals the sum of their probabilities
$$
\text{
	If $A$ and $B$ are mutually exclusive events, $P(A \cup B) = P(A) + P(B)$
	}
$$
* the probability that an event does not occur equals 1 minus the probability that the event does occur
$$
\text{
	For an event $A,\quad P(\text{not }A)=1-P(A)$
}
$$

## Determining Probabilities
### Theoretical Probability
Theoretical (or *classical*) probability is determined by logic and the properties of the experiment. For a given event $A$,
$$
P(A)=
\frac{ \text{number of ways $A$ can occur} }{ \text{number of outcomes in the sample space} }\\
$$
### Empirical Probability
Empirical (or *observational* or *long-run*) probability is approximated by running the experiment many times and observing frequency of occurrence. An empirical probability is obtained from the **relative frequency** of an event $A$ where,
$$
\text{relative frequency of event $A$} = \frac{ \text{number of times $A$ occurred} }{ \text{total number of repetitions} }
$$
#### Law of Large Numbers
As the number of trials for the experiment increases, the *relative frequency* of the event approaches the *theoretical frequency* of the event.

## Learning Outcomes
* Enumerate or describe all possible outcomes of a random phenomenon or game of chance
* Define and give examples of the following terms:
	* Random phenomenon
	* Sample space
	* Event
	* Probability of an event
* Explain basic probability rules
* Distinguish between the two approaches for calculating probabilities: theoretical vs empirical
* Calculate probabilities for a given random phenomenon
