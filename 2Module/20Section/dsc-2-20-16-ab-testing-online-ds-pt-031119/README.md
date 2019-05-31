
# A/B Testing

## Introduction

The goal of statistics is almost always to infer characteristics about a general population from a sample. We've previously looked heavily at estimation of parameters, which invoked a discussion of estimation and confidence intervals. Another common application of statistics is to accept or refute a particular claim. This practice is referred to as both A/B testing and hypothesis testing. 

## Objectives
You will be able to:

* Design, structure, and run an A/B test

## The Null Hypothesis: $H_0$

The first step to conducting an A/B test is to define a null hypothesis. Typically, the null hypothesis is the claim that a researcher is hoping to refute. For example, a medical researcher might hope to show that a new drug is more effective then a previous treatment option. Common practice is then to define the null hypothesis as the contrary: there is no difference between the two drugs. The researcher hopes to refute the null hypothesis thereby proving their claim by contradiction. Again this is the first step of conducting an A/B test. Explicitly state the null hypothesis ($H_0$).

We might start with something like: $Drug_a$ is more effective then $drug_b$.
However, as we will discuss, we will want to make this statement more quantitative so that we can determine sample sizes in comparison to type I and II errors. 

For our example, let's say that we have already determined the effectiveness of $drug_b$ to be .76

We can now state our null hypothesis as:

**$H_0$: effectiveness drug_a = 0.76**

## The alternative hypothesis

**$H_1$: effectiveness drug_a > 0.76**

## Test Statistic

Once the null hypothesis has been stated, a test statistic must be chosen in order to determine its validity. In our previous examples, we looked at t-tests and z-tests and their associated p-values. These are always the techniques employed when looking at population and sample means, since by the central limit theorem, we know that the mean of repeated samples form a normal distribution. 

## Rejection Region

Finally, once the test statistic is determined, we must set a rejection region. This is the value of our test statistic that defines the boundary between us accetping and rejecting the null hypothesis. 

## Type I and II Errors

A type I error is when we reject the null hypothesis, $H_0$, when it is actually true. The probability of a type I error occuring is denoted by $\alpha$ (pronounced alpha).  

A type II error is when we accept the null hypothesis, $H_0$, when it is actually false. The probability of a type II error occuring is denoted by $\beta$ (pronounced beta).

## Determing an acceptable sample size

Typically, we will start by stating the null hypothesis, choosing a test-statistic (a z-test or t-test for a normal distribution) and then stating an acceptable $\alpha$ parameter associated with type I errors. Once done, we must determine an acceptable sample size to reduce type II errors. That is, type I and type II errors are intrinsically linked; determining a lower rejection region will lower $\alpha$ but increase $\beta$. However, by increasing our sample size we can maintain a chose $\alpha$ value and reduce $\beta$ as well.  

With our current formulation of a hypothesis test, we can determine the necessary sample size for a desired $\alpha$ and $\beta$ combination. 

## $n=\frac{(z_\alpha+z_\beta)^2\sigma^2}{(\mu_1-\mu_0)^2}$

In our example stated above, $\mu_1=.76$ and $\mu_0=.76$. However, we could potentially make more general comparison statement such as:

$h_0: effectiveness = .76$

$h_1: effectiveness > .8$

in which case the values of the preceding equation would become:

$\mu_0 = .76$

and 

$\mu_1 = .8$


Finally, we have the variance, $\sigma^2$. Typically this will not be known for the population, at which point we can use our standard estimate using the sample variance itself s.

Let's now investigate how we would calculate this in python:



```python
import scipy.stats as st
```


```python
def compute_n(alpha, beta, mu_0, mu_1, var):
    z_alpha = st.norm.ppf(alpha)
    z_beta = st.norm.ppf(beta)
    num = ((z_alpha+z_beta)**2)*var
    den = (mu_1 - mu_0)**2
    return num/den

alpha = .01 #Part of A/B test design
beta = .01 #Part of A/B test design
mu_0 = .76 #Part of A/B test design
mu_1 = .8 #Part of A/B test design
var = .1 #sample variance

compute_n(alpha, beta, mu_0, mu_1, var)
```




    1352.9736077635823



Thus, if we wish to be able to detect with a fairly high degree of confidence as proposed, we would need a sample size of 1353 participants. Alternatively, we could ease our desired alpha and beta parameters which would also reduce the required sample size.

## Summary

When researching, we are often presented with two choices for stating our question. One is to estimate a parameter in question, such as the procedures previously examined for estimating the mean of a population. Alternatively, we may wish to test the validity of a claim, whether we can refute that claim, or whether we should withold judgement. Here we further examined how you can determine a required sample size after formulating a hypothesis test. In practice, it is up to the practitioner to determine the appropriate alpha, beta, and sample size that is determined to be both satisfactory confidence and a viable sample size to attain.
