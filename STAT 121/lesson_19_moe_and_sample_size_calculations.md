# STAT 121 Lesson 19 - Margin of Error and Sample Size Calculations

###### Recall:
| Term | Definition |
|------|------------|
| Confidence Interval | A range of plausible values that the population parameter could be. <br>$\bar{x} \pm z^* * \frac{\sigma}{\sqrt{n}}$
| Margin of Error | <ul><li>Maximum difference between statistics and aprameter at stated confidence level.</li><li>Accounts for uncertainty due to sampling variability only</li><li>Does not account for non-response, undercoverage, bad sampling, etc...</li></ul><br>$z^* * \frac{\sigma}{\sqrt{n}}$
| Point estimator | $\bar{x}$
| Confidence multiplier | $z^*$
| Standard deviation of point estimator | $\frac{\sigma}{\sqrt{n}}$

## Confidence Interval
**def.** A range of plausible values that the population parameter could be.

$$
\bar{x} \pm z^* * \frac{\sigma}{\sqrt{n}}
$$

#### Important properties
1. The margin of error controls the width of the interval
2. $\text{sample size } \propto \frac{1}{\text{margin of error and width}}$
3. $\text{confidence} \propto \text{margin of error and width}$

### Calculating margin of error:
$$
\text{margin of error} \overset{\text{let}}{=}
m=
\frac{z^* \sigma}{\sqrt{n}}
$$

$$
n=(\frac{z^* \sigma}{m})^2
$$

### Confidence interval when $\sigma$ is unknown
$$
\bar{x} \pm t^* \frac{s}{\sqrt{n}}
$$

### Conditions for Confidence Intervals to Work
1. Data come from a random sample
2. Population distribution is normal or sample size is large enough ($n>30$)
