
# Negative Binomial Distribution

## Introduction

In this lesson, you'll learn about negative binomial trials, and the negative binomial distribution!

## Objectives

You will be able to:

* Understand and explain the Negative Binomial Distribution and its uses


## Negative Binomial Trials

To understand the Negative Binomial Distribution, we first need to have a clear understanding of what it describes--**_Negative Binomial Trials_**. This sounds more intimidating that it actually is--the idea is actually pretty straightforward.  

Consider the following question:

I have a fair coin.  Let's consider heads a success, and tails a failure.  How many times can I flip the coin before I fail 3 times?

The first thought you'll probably have is that there's no single answer to this--instead, the answer falls across a distribution of probabilities.  It's possible that our first three flips in are all tails.  It's also possible (but exceedingly unlikely) that we flip the coin 100 times (or 1,000, or 1,000,000 times) and not still have heads show up less than 3 times in total. 

The **_Negative Binomial Distribution_** allows us to easily describe the probability distribution of the different ways a Negative Binomial Trial could work out.  

In more formal terms, the Negative Binomial Distribution requires the following parameters:

The Negative Binomial Distribution describes the number of successes $ k $ until observing a pre-determined number of failures $ r $ where the probability of success for each independent trail is $ p $.  

Note that since there's no such thing as half a tails or half a trial,  this means that the Negative Binomial Distribution is a **_Discrete Distribution_**, since it's concerned with multiple discrete, independent events. 

#### Sucess or Failure?

Note that depending on where you look, you'll see some sources that define $r$ as a fixed number of **_failures_**, while others will describe it as a fixed number of **_success_**.  Don't be confused by this--both of these definitions just describe two sides of the same coin (pun intended).  By definition, any trial with a binary outcome can equally be described in terms of failure or success.  For instance, saying "What is the probability that it takes me 6 coin flips to get tails twice?", it doesn't actually matter if we define tails as a "success" or as a "failure"--all that matters is that we calculate the probability that tails makes its 2nd appearance on the 6th flip.    

For the sake of simplicity, we'll define $r$ as the fixed number of **_failures_** throughout this lesson. 


#### Relationship to Binomal Distribution

You may recall the **_Binomial Distribution_** that we learned about previously.  Comparing and contrasting it with the Negative Binomial Distribution helps us better understand what each is used for. 

The **_Binomial Distribution_** describes the number of successes $ k $ achieved in $ n $ trials, where the probability of success is $ p $.

The **_Negative Binomial Distribution_** describes the number of successes $ k $  until observing $ r $ failures (or successes--this is arbitrary, and depends on how you phrase the question; it doesn't particularly matter if we define heads or tails as a failure, as long as we pick one).  Note that these failures do **_not_** need to be consecutive, just cumulative!

#### Putting It Into Words

Let's work through an example of phrasing a problem that would be described by the binomial distribution, and phrasing another problem that would be described by the negative binomial distribution. 

**_Binomial Distribution_**: "I flip a fair coin 5 times. What are the chances that I get heads 0 times? 1 time? 2 times? Etc..."

**_Negative Binomial Distribution_**: I flip a fair coin 5 times. What are the chances it takes me two flips to get heads twice? How about 3 flips to get heads twice? 4 Flips? Etc..."

### Defining Parameters

Now that we know what we know about the Negative Binomial Distribution, let's set some parameters for the coin-flipping experiment we described above and take a look at the corresponding Negative Binomial Distribution that describes it. 

Let's define our problem statement as:

"I'm going to flip a fair coin 10 times. I want to see how long it takes for the coin to land on heads 2 times.  What is the probability that this happens after 2 coin flips? After 3? ... After 10?"

The statement above describes a Negative Binomial Trial. Let's examine it and see if we can find the parameters that we can use to describe the corresponding Negative Binomial Distribution!

$ r = Number\ of\ Failures = 2 $, since we're interested in seeing how long it takes to land on heads a total of two times. 

$ x = Number\ of\ Trials $--this can be any number greater than 2.  It cannot be smaller than 2, because it is mathematically impossible to satisfy our pre-set condition if the number of trials is smaller than our target (it's impossible to get 2 heads out a single coin flip). 

$ p = Fair\ Coin = 0.5$, since a fair coin has a 50/50 chance of landing on either heads or tails. 

The easiest way to think of this is that the distribution has a **_Fixed Number r_** and a **_Random Variable X_**.  When we perform Negative Binomial Trials, we _know how many failures we're looking for_.  This number is denoted as the parameter $r$.  Our random variable is what we don't know--exactly how many trials $x$ it will take to reach our fixed number of failures $r$.    

### The Negative Binomial Formula

If we know the parameters, we can calculate our Negative Binomial Probability by pulling them into the following formula:

$b(x, r, P) =\  _{x-1}C_{\ r-1} * P^{\ r} * (1-P)^{\ x-r}  $ 

Don't worry if this looks pretty overwhelming.  We'll break it down.

Let's start by recalling our parameters:

$ r = 2 $

$ x = 10 $

$ P = 0.5 $ 

You may also be wondering what $_{x-1}C_{\ r-1}$ is the equation.  This is a mathematical notation that stands for $$\frac{(x-1)!}{((n-1)-(r-1))!(r-1)!}$$.  This equation probably looks scary, too, but don't worry--this is just the formula for the binomial distribution, which you've seen before. 

**_A Note on This Equation:_**  This equation is used to calculate the **_Negative Binomial Probability_**, which is just the probability for a given value of $x$, not the entire probability distribution.  If we want to know the Negative Binomial Probability for 10, we set $x=10$ and plug the parameters into this equation. If we want to know the probability for 3, we set $x=3$, and so on. 

#### What Exactly Are We Calculating?

When working with discrete probabilities, it sometimes helps to think of the corresponding trials as a tree diagram. Let's examine all the possible ways that that three coin flips can work out:

We could use our parameters and describe our problem as: What is the negative binomial probability of $b(x=3, r=2, p=0.5)$?

However, we could also phrase it in much more simple terms--what are the odds that we get our 2nd heads on the 3rd coin flip?

Logically, it follows that in order for heads to appear for the 2nd time on the 3rd coin flip, that means that heads must have appeared exactly once by the second trial.  We can generalize this statement further to say that in order for us to hit $r$ on the trial $x$, that means that this can only happen in situations where we have a count of $r-1$ on trial $x-1$.  Another way to phrase is by considering impossibilities at any given step--it's impossible to get our 2nd heads on the third flip if we have 0 heads on the second flip, and also if we had 2 heads on the second flip.  If $r=2$ and $x=3$, then our magic number for step $x=2$ is $r=1$. 

This brings us to that potentially scary equation we saw above. As we mentioned before, the **_Probability Mass Function_** for the **_Binomial Distribution_** hiding inside of that equation. That's one half of the equation above.  The other half of the equation is just calculating the odds that we reach $r$ on trial number $x$.

This means that we can break the equation down into two separate parts:

1. The probability that we have $r-1$ failures on trail $x-1$.  In the negative binomial probability equation, this is denoted by $_{x-1}C_{\ r-1}$.

2. The probability that we get failure $r$ on trial $x$. This is denoted by $P^{\ r} * (1-P)^{\ x-r}$

Since these trials are all independent, we can simply calculate our **_Negative Binomial Probability_** by just multiplying the two, giving us our original equation of:

$$b(x, r, P) =\  _{x-1}C_{\ r-1} * P^{\ r} * (1-P)^{\ x-r} $$

If we use this formula to and plug in the parameter values for our sample problem above, we get the following distribution:

| # Coin Flips | Probability |
|:------------:|:-----------:|
|       2      |     0.25    |
|       3      |     0.25    |
|       4      |    0.1875   |
|       5      |    0.125    |
|       6      |    0.0781   |
|     >= 7     |    0.1094   |


### Characteristics of the Negative Binomial Distribution

The **_mean_** of the Negative Binomial Distribution is: 

$$\mu = \frac{r}{p}$$

The **_variance_** of the Negative Binomial Distribution is:

$$\sigma^2 = \frac{r\ (1-p)}{p^{\ 2}}  $$

### Calculating Negative Binomial Probability with Numpy

Thanks to the wonders of numpy, we can avoid scary functions and calculate Negative Binomial Probabilities with a single line of code. Consider the following example code from the [numpy documenation for negative binomial sampling function](https://docs.scipy.org/doc/numpy-1.15.0/reference/generated/numpy.random.negative_binomial.html):

> A company drills wild-cat oil exploration wells, each with an estimated probability of success of 0.1. What is the probability of having one success for each successive well, that is what is the probability of a single success after drilling 5 wells, after 6 wells, etc.?

The following sample code is provided in the documentation to demonstrate how to solve this problem using the `negative_binomial()` function from the `numpy.random` module:


```python
import numpy as np

s = np.random.negative_binomial(1, 0.1, 100000)
for i in range(1, 11):
    probability = sum(s<i) / 1000000
    print("{} wells drilled, probability of success: {:.4f}%".format(i, probability * 100))
```

    1 wells drilled, probability of success: 0.9934%
    2 wells drilled, probability of success: 1.9007%
    3 wells drilled, probability of success: 2.7131%
    4 wells drilled, probability of success: 3.4476%
    5 wells drilled, probability of success: 4.1028%
    6 wells drilled, probability of success: 4.7032%
    7 wells drilled, probability of success: 5.2279%
    8 wells drilled, probability of success: 5.7135%
    9 wells drilled, probability of success: 6.1398%
    10 wells drilled, probability of success: 6.5318%


## Summary

In this lesson, we learned all about the **_Negative Binomial Distribution_**, as well as related concepts such as **_Negative Binomial Trials_** and **_Negative Binomial Probability_**.  
