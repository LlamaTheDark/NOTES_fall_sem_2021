# STAT 121 Lesson 20 - Overview of Hypothesis Testing
## Statistical Inference
**def.** To draw conclusions about **parameters** using **statistics** <u>with</u> a measure of **uncertainty**.

Two main methods:
1. **confidence interval** to estimate a parameter.
2. **test of significance** to assess a claim about a parameter.

## Test of Significance
The goal of a test of significance is to answer the question:

<div style='
	padding: 0px 100px;
'>

Is the observed *difference from the claim* **real**, or is it **chance**?
</div>

### Reasoning
1. Make claim about a **parameter** value.
2. Compare observed statistic to claimed value
3. A difference so **large** that it would **rarely happen** if the claim were true, is strong evidence that the claim is **not** true.
	* To decide, assume the claim is true and use *sampling distribution* to calculate probability of a difference as large as observed.

### Proof By Contradiction
A test of significance will almost always assume a claim that the researchers think is <u>not true</u>.
* If good evidence exists *against* this claim, then the opposite of the claim must be true.
* This is often called the **null hypothesis** $H_0$.

### Four Elements of Tests of Significance
1. Claim 1 and Claim 2
	* Opposing claims about an unknown parameter.
	* Presumption is claim 1 unless there is strong evidence against it.
	* Claim 1: null hypothesis $H_0$
		* Always involves equality ($=$)
		* e.g. $\mu=300 \text{ppm}$
	* Claim 2: alternative hypothesis $H_a$
		* Always involves inequality ($\neq$, $<$, $>$)
		* e.g. $\mu > 300 \text{ppm}$
2. Outcome
	* Standardized outcome that measures how far the outcome diverges from claim 1.
	* Represented by a standardized statistic called a **test statistic**.
		* A measure of the **strength of agreement** between the test statistic and $H_0$.
		* Often denoted as the $p$-value.
3. Assessment of Evidence
	* How likely is it to get this outcome if claim 1 is true?
4. Conclusion
	* Disprove or fail to disprove claim 1, thereby supporting claim 2.
	* > An outcome that would rarely happen if claim 1 is true is good evidence that claim 1 is not true; hence we believe claim 2 is true.
	* For this, we define a measure of uncertainty, which is the probability of falsely rejecting $H_0$.
		* Often denoted as the $\alpha$-value.
		* Defines what it means to be a rare outcome.

### Test Statistic
**def.** A number that summarizes the data for a test of significance. It does this by comparing an estimate of the parameter from sample data with the value of the parameter given in the null hypothesis. e.g. a test statistics $t$ could be:
$$
t=\frac{\bar{x}-\mu_0}{s/\sqrt{n}}
$$
Representing the number of standard deviations away from the mean a sample mean is from the true mean.

### $p$-value
The $p$-value is a probability. This mean's it falls in the range $[0, 1]$. It represents the probability that we could have observed $H_a$ given that $H_0$ is true.

#### $\alpha$-value
$\alpha$ is a probability that we set called the **significance level**. It's a prespecified value that determines whether $p$ is unlikely enough. i.e.
$$
\begin{align}
\text{
	if
} p \leq \alpha&:
\text{
	reject $H_0$
}\\
else&:
\text{do not reject/fail to reject $H_0$}
\end{align}
$$

Note that we don't **prove** $H_0$ by doing this. We either disprove it (as far as we're statistically concerned) or fail to disprove it.

The choice for $\alpha$ is subjective. You don't want it to be too high or you'll get false positives / misleading results.

### Conclusions
* Rejecting $H_0$ means the difference seen is real, not due to chance.
* 3 parts to a conclusion:
 	1. Compare $p$-value to $\alpha$.
	2. Declare decision to reject or fail to reject $H_0$.
	3. Relay conclusion in context.
