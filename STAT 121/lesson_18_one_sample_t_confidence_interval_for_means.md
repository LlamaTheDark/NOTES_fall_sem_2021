# STAT 121 Lesson 18 - One-sample $t$ confidence interval for means.
## More on Confidence Intervals
#### Phrasing
When we say,
$$
\text{
Construct a $C$% confidence interval for $\mu$
}
$$
We mean:
$$
\begin{align}
& \text{
	Find the highest number of SDs from $\mu$ that $\bar{X}$ can be
}\\
& \text{
	such there is a $C\%$ chance that $\bar{X}$ is within that range,
}\\
& \text{
	then present the values $\bar{X}$ can be in interval form.
}
\end{align}
$$
We know that our final interval will take the form of:
$$
\bar{X} \pm z^* \frac{\sigma}{\sqrt{n}}
$$
Where $z^*$ is the number of standard deviations away we need to be, based on the value of $C$. $z^*$ is also called the **confidence level** or **confidence factor**.

This is fairly easy to visualize. We just want the values that define the ends of the middle $C\%$ of the distribution. For example, we know that the middle 95% of data is within 2 standard deviations of a given normal distribution. So the bounds for a 95% confidence interval will be about $\bar{X} \pm 2 \frac{\sigma}{\sqrt{n}}$. Get it?

### Calculating Confidence Interval with $t$
When the standard deviation of the population is not known, we use the following to calculate our interval instead:
$$
\bar{X} \pm t^* \frac{s}{\sqrt{n}}
$$

This uses what's called **Student's $t$-distribution**. It's called this because the guy who invented it went under the pseudonym "Student".

### Student's $t$-distribution
**def.** Student's $t$-distribution can be defined as the distribution of the location of the sample mean relative to the true mean, divided by the sample standard deviation, after multiplying by the standard term $\sqrt{n}$.

It is essentially another distribution (not the normal distribution) which does not require the use of a population's standard deviation to construct confidence intervals for it.

I.e. we say that the random variable
$$
\frac{
	\bar{X}-\mu
}{
	\sigma / \sqrt{n}
}
$$
has a **standard normal distribution**. Then the random variable
$$
\frac{
	\bar{X}-\mu
}{
	s / \sqrt{n}
}
$$
has a **Student's $t$-distribution** with $n-1$ degrees of freedom (which is labeled as $\text{df}$ on the formula book table). [This wikipedia article](https://en.wikipedia.org/wiki/Degrees_of_freedom_(statistics)) is quite helpful in understanding degrees of freedom.

If you set these random variables equal to each other, you'll find that their frequencies are the same at the point where $s=\sigma$.

#### Properties of a $t$-distribution
* Symmetric
* Bell shaped
* mean = 0
* the smaller the $\text{df}$, the larger the spread
	* more uncertainty due to $s$.
* The larger the $\text{df}$, the closer the $t$-distribution is to the standard normal.

In summary if you don't know the standard deviation of the population then


Smart phones have changed the world and how we spend our time. A group of researchers at BYU want to estimate the mean daily number of minutes that BYU students spend on their phones. In fall 2019, they took a random sample of 430 BYU students and found that on average, students spend 312 minutes on their phones with a standard deviation of 54 minutes per day. The plot of the sample data showed no extreme skewness or outliers.  Calculate a 96% confidence interval estimate for the mean daily number of minutes that BYU students spend on their phones in fall 2019.  Do not round off in the intermediate steps, only the final answer should be rounded off to two decimal places. 
