
# Geometric Distributions

## Introduction

In this lesson, we'll learn about the **_Geometric Distribution_** and how we can use it.

## Objectives

You will be able to:

* Understand and explain the Geometric Distribution and its uses 

## What is the Geometric Distribution?

Most people are initially confused the first time they hear about the **_Geometric Distribution_** because it's name seems a bit misleading.  Although the term _geometric_ brings to mind shapes, area, perimeter, and all the other fun stuff we learned in high school geometry class, the Geometric Distribution has nothing to do with these topics.  In this case, _Geometric_ just refers to the concept of multiplication.  The Geometric Distribution is a discrete probability distribution that helps us calculate the probability distribution of repeated independent events. 

If this reminds you of the **_Negative Binomial Distribution_** that we learned about in a previous lesson, then you're on the right track--the Geometric Distribution is just a special case of the Negative Binomial Distribution!

## Questions We Can Answer With The Geometric Distribution

To help us understand and remember what the Geometric Distribution is used for, let's look at it through the lens of the Negative Binomial Distribution.  Recall that the Negative Binomial Distribution tells us the probability of hitting a specific number of failures (or successes, depending on how we phrase our problem) on a specific round of independent trials where the probability of success is known and unchanging.  You may recall the example we solved in our previous lesson, which was "What is the probability distribution for flipping a fair coin before tails shows up a total of twice?"  In this case, the Probability $P$ is 0.5, the cumulative number of failures, $r$ is 2, and the number the random variable, $x$, is the number of trials it takes before the total number of coin flips that land on tails is 2.  

The Geometric Distribution is extremely similar.  Whereas $r$ is a parameter we choose ourselves in the Negative Binomial Distribution, in the Geometric Distribution r is always equal to 1!  In this way, any questions that we can answer with the Geometric Distribution are questions that we can also answer with the Negative Binomial Distribution.  The Geomtric Distribution, then, is just a subset of the Negative Binomial Distribution where $r$ always equals 1.

Whereas our previous example for the Negative Binomial Distribution was about how many times we could flip a coin before tails comes up twice, an equivalent question we could solve with the Geometric Distribution would be "What is the probability that I can flip a coin X times before it lands on tails?"  

## Geometric Distribution Equation

As mentioned previously, questions that can be answered with the Geometric Distribution fall under the  same constraints as the Negative Binomial Distribution:

* There are multiple trials
* The outcome is binary
* The probability of success is the same across each trial, and does not change
* Each trial is independent of other trials


The equation for the Geometric Distribution is:

$$P(X=x) = q^{(x\ -\ 1)}p$$

Where $$q = 1 - p$$


Let's break down how to read this equation, and what each element of the equation actually means:

$P(X=x)$: This is simpler than it looks. $X$ denotes the _Discrete Random Variable_, whereas the the smaller $x$ denotes that actual trial that we want to calculate the *Geometric Probability* for.  An easier, less mathematical way to phrase this statement might be:

> "If I flip a fair coin a certain number of times (X), tails will eventually come up. What is the probability that the random number of times happens to be 3? (x)"

$p$: The probability of failure for a given trial.  In our coin flip example, this would be 0.5.

$q$: (1 - p), which is the probability of success for a given trial. Again, remember, it makes no difference if these terms are flipped. The geometric distribution doesn't care if you decide that tails is a success or a failure, as long as you are consistent throughout your calculations. 

Note that in cases where there is an equal chance of both outcomes such as our coin flip example, p and q are the same thing.  This means that for "fair" trials where there is an equal chance of success or failure, we can further simplify our equation to $$P(X=x) = q^x$$

### Sample Problem 1

Let's use our newfound knowledge of the Geometric Distribution to answer a sample question about coin flips.  What are the odds that we can flip a fair coin 3 times in a row without landing on tails?

Let's start by defining our parameters:

p = 0.5 (fair coin flip)

x = 3

We can plug this into our Geometric Probability Formula to calculate the probability of this result:

$$P(X=3) = (0.5)^{(3 - 1)} * 0.5$$

$$P(X=3) = (0.5)^3 = 0.125$$

### Sample Problem 2

In cases where the probability of success and failure are not equal, this is a bit more interesting.  Let's examine a more interesting sample problem--Roulette!

On an American Roulette wheel, the chance of the ball landing on a black number is 47.4%, a red number is 47.4%.  The chances of the ball landing a green number (0 or 00) is 5.26%.  The longest recorded single-color streak in an American casino happened in 1943, when red won 32 consecutive times.  What is the probability of this happening?

This is a more interesting problem! Let's define our parameters:

p = 0.474 (chance of landing on red)

q = 0.526 (chance of landing on not red)

x = 32 (number of consecutive times that we're calculating the probability for).

We can plug these numbers right into our Geometric Probability Equation:

$$P(X=32) = 0.526^{(32 - 1)} * 0.474$$

Which comes out to:


```python
(0.526)**31 * 0.474
```




    1.0625182796895225e-09



The probability of this happening is so small that python has displayed the answer to us in scientific notation.  The `e-09` tells us that we need to move the decimal place to the left 10 spots, which brings our overall answer to:

$$0.0000000010625182796895225$$

Which is 

$$0.00000010625182796895225\%$$

Incredible, but that's the thing about randomness; anything is possible, and over a sufficient enough number of samples, even the most improbable things are likely to happen at least once!

## Phrasing Our Answer as a Distribution

In the examples above, we calculated a single probability. However, a more statistical way to think of these problems is to phrase it as a distribution, where we display the probability for every number in a given range. 

A more statistical way to phrase our last example question might be "What is the probability distribution of a roulette wheel successively landing on red?"

We can easily compute this using a little python:



```python
def geom_prob(p, x):
    q = 1 - p
    ex = x - 1
    return q**ex * p

# Let's test that it works
geom_prob(0.5, 3) # Expected Output 0.125
```




    0.125



Now that we have a function for computing the probability for a given x value, we can just use a for-loop to calculate the entire probability up to a highest given value of x that we're interested in.


```python
for x in range(1, 11):
    p = 0.474
    print("Probability of roulette landing on red {} times in a row: {:.5f}%".format(x, geom_prob(p, x) * 100))
```

    Probability of roulette landing on red 1 times in a row: 47.40000%
    Probability of roulette landing on red 2 times in a row: 24.93240%
    Probability of roulette landing on red 3 times in a row: 13.11444%
    Probability of roulette landing on red 4 times in a row: 6.89820%
    Probability of roulette landing on red 5 times in a row: 3.62845%
    Probability of roulette landing on red 6 times in a row: 1.90857%
    Probability of roulette landing on red 7 times in a row: 1.00391%
    Probability of roulette landing on red 8 times in a row: 0.52805%
    Probability of roulette landing on red 9 times in a row: 0.27776%
    Probability of roulette landing on red 10 times in a row: 0.14610%


## Summary

In this lesson, we learned about the **_Geometric Distibution_**, how to calculate probability distributions with it, it's relationship to the Binomial/Negative Binomial Distributions,  and how to apply it to real world problems!
