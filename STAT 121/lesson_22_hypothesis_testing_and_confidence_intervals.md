# Lesson 22 - Hypothesis Testing & Confidence Intervals
## Effect of Sample Size on Hypothesis Testing

$$
\begin{align}
t&=\frac{\bar{x}-\mu_0}{\frac{s}{\sqrt{n}}}\\\\
t&=\sqrt{n}*\frac{\bar{x}-\mu_0}{s}
\end{align}
$$

Thus we see that the test statistic is proportional to the sample size. A few things to note:
* $|\bar{x}-\mu_0|$
	* The magnitude of the observed effect
	* Measures how far the sample mean deviates from the hypothesized mean.
	* The greater the magnitude of the difference, the smaller the $p$-value.
* $\frac{s}{\sqrt{n}}$
	* Measures how much random variation we expect
	* The larger the sample size, the smaller the $p$-value.


##### Practical Importance
* Results are *statistically significant* when $p\leq\alpha$
* Results are **practically important** when the observed effect ($|\bar{x}-\mu_0|$) is large or important enough to matter.
	* Rather than a numerical conclusion, practical importance is determined by intuition.

There are 2 things that we need to look out for when we're considering practical importance:
* Sample size may be **too small** to detect significance
* Sample size may be **so large** that results are *always* significant.

## Solutions for a 2-sided $p$-test
1. Inspector Significance
	* Conduct test of significance at $\alpha=0.05$
	* Compare $p$-value with $\alpha$ and draw conclusions
2. Inspector Interval
	* Construct $95\%$ confidence interval for $\mu$
	* See if $H_0$ is in interval and draw conclusions.
