
# MLE with Normal Distributions

## Introduction
In the previous section, we looked at an introduction to Bayesian inferencing and learned how conditional probabilities along with law of total probability can be used in a predictive context. We looked at how Maximum likelihood and A posteriori estimations can be used to calculate the posterior probability by learning some unknown variable theta, given all the available data.  In this is lesson, we shall look at using this Bayesian setting in a Gaussian context i.e. when the underlying random variables are normally distributed. 

## Objectives
You will be able to:

* Understand and describe how MLE works with normal distributions
* Calculate the MLE estimations for expected mean and variance 

## A Quick recap

Given some parameterized distribution $P(X|θ)$, and an collection of (independent) samples $x_1,…,x_m$, we can compute the probability of observing this set of samples under the distribution, which is simply given by:


$$P(x_1,\ldots,x_m|\theta) = \prod_{i=1}^m P(x_i|\theta)$$



We maximize this function, to identify the maxima with respect to theta, and take its log to simplify the likelihood equation shown below:

$$\ell(\theta) = \frac{1}{m} \sum_{i=1}^m \log P(x_i|\theta)$$

Here we explicitly write $ℓ$ as a function of θ because we want to emphasize the fact **this likelihood depends on the parameters**. (1/m is an arbitrary scaling factor). 

## MLE with Normal Distributions

So far we have been looking at coin toss experiments and working with binomial distributions for our understanding. Let's take this a bit further and try to work with Gaussian/Normal distributions. Now consider the same idea as shown above, but with a Normal distribution. We know the parameters used to desribe a normal distribution are $(\mu~and~\sigma^2)$. Where $\mu$ is the mean and sigma squared identifies the variance in the data. But what if we know that , $x_1, x_2, ..., x_n ∼ N(\mu, \sigma^2)$ in this case but we dont know the value of $\mu$.

>$x_1, x_2, ..., x_n ∼ N(\mu, \sigma^2)~~~-~~~ A~normal~distribution~is~normally~shown~using~such~notation.$ 

So just like above, We can set up a likelihood equation: $P(X|\mu, \sigma)$, and find the value of that maximizes it by taking its derivative w.r.t theta and solve for $X$. 

## Maximum Likelihood Estimation for $\mu$ and $\sigma^2$

As long as $x_1, ..., x_n$ are independent and from the same distribution, these will fulfill our i.i.d assumption.  We can write down our $P(X|\theta)$ equation for the normal distribution case as below:

$$P(x|\mu, \sigma^2) = \prod_{i=1}^n P(x_i|\mu, \sigma^2)$$

And our likelihood function:

$$\ell(x) = \prod_{i=1}^n P(x_i|\mu, \sigma^2)$$

$$L(x) = \frac{1}{\sqrt{2  \pi  \sigma^2}}\prod_{i=1}^n\exp\frac{(x_i-\mu)^2}{2\sigma^2}~~ - ~~Normal~PDF$$ 

After taking the log likelihood and removing some constants, we get the following equation:

$$\log(L(x)) = \ell(x) ∝ \sum_{i=1}^{n} - (x_i - \mu)^2$$

Note: $\ell$ denotes the "log likelihood" as compared to $L$, used for likelihood. 
We can take the derivative of this value and set it equal to zero, to maximize. The $\mu$ value can be solved as:

$$\mu_{MLE} = \frac{\sum_{i=1}^{n}x_i}{n} $$

We can similarly calculate the MLE for variance following similar steps to get the result as :

$$\sigma_{MLE}^2 = \frac{\sum_{i=1}^{n}(x_i - \mu_{MLE})^2}{n} $$

**Note:** *A detailed derivation of above final MLE equations with proofs can be seen [at this website](https://www.statlect.com/fundamentals-of-statistics/normal-distribution-maximum-likelihood). *

Next We shall try to implement this in python to get a better understanding of how such estimations work. 


## Summary 

In analytics, most of the real world data is normally modeled under a normal distribution (think of central limit theorem and why this is the case). It is imperative that you can develop an intuition around how these distributions get represented and are inferred in analysis. A good mathematical understanding of the processes in data manipulations goes a long way. Let's try to see how we can translate this understanding in Python in the following lab. 
