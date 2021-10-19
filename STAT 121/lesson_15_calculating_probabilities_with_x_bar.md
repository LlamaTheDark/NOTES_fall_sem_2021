# STAT 121 Lesson 15 - Calculating Probabilities Associated with $\bar{X}$
## Statistical Practice For Dealing With $\bar{X}$ Probability
1. Take **one** sample of size $n$ from a population.
2. Compute the sample's mean $\bar{X}$ and call it an **estimate** of the total population's mean, $\mu$
3. Identify the implications of the sampling distribution of $\bar{X}$ on the **uncertainty** of this particular $\bar{X}$.

## Math Time
All symbols and terms used are as they have been previously defined to be unless otherwise specified hereafter. Okay so recall that to find the number of standard deviations away from the mean a value is (the $z$-score), we do:
$$
z=\frac{x-\mu}{\sigma}
$$
That's if we want a specific $x$ value of a population. What if instead we want to look at a sample with a sample mean $\bar{X}$? i.e. what if we want to find the probability that the *sample mean* $\bar{X}$ of a sample of $n$ individuals is (less than/greater than/equal to/whatever) some value? Then we can use this same equation but we'll have to substitute some things. We now are looking for the number of SDs our **sample mean** is away from the **population mean**.
$$
\begin{alignat}{1}
&(1) \quad & x \text{ becomes }\bar{X}
\\
&(2) \quad & \sigma \text{ becomes } s=\frac{\sigma}{\sqrt{n}}
\\
&(3) \therefore \quad & z=\frac{\bar{X}-\mu}{
	\frac{\sigma}{\sqrt{n}}
}

\end{alignat}
$$

## When to use what to calculate $z$
Use
$$
z=\frac{\bar{X}-\mu}{
	\frac{\sigma}{\sqrt{n}}
}
$$
When dealing with a sample mean **and** either:
* The population is normal
* The population is not normal (or it is not *known* whether it is normal) **but** the sample size $n>30$
	* This is the Central Limit Theorem
	* If the sample size is less than $n$ you can't make any safe conclusions.

Use
$$
z=\frac{x-\mu}{\sigma}
$$
When dealing with an individual value.

---
<div style='
	border-left: 4px dashed green;
	padding-left: 30px;
	margin-left: 3px;
'>

**e.g.** MLB player salaries have a right skewed distribution with μ =
$4.07 million and σ = $5.2 million. What is the probability that
 ̄x for a random sample of n = 36 player salaries is less than $3
million?

1. Compute z-score

$$
z=\frac{\bar{X}-\mu}{
	\frac{\sigma}{\sqrt{n}}
}
=\frac{ 3 - 4.07 }{
	\frac{ 5.2 }{\sqrt{ 36 }}
}
\approx -1.23
$$

2. Look up the z-score in a standard normal table to get probability

</div>

---

here's some python code to calculate this stuff for you:
```py
import numpy as np # for square root, you could also do n**0.5

def compute_z_individual(x, m, sd):
	return (x-m)/sd

def compute_z_sample_mean(x_bar, m, sd, n):
	return compute_z_individual(x_bar, m, sd/np.sqrt(n))

z = compute_z_sample_mean(3, 4.07, 5.2, 36)
print(z) # -1.234615...

```
