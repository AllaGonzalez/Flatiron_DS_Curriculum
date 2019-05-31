
# The Geometric and Negative Binomial Distributions - Lab

## Introduction

In this lab, you'll practice your knowledge on the geometric and negative binomial distributions!

## Objectives
You will be able to:
- Understand and explain the Negative Binomial Distribution and its uses
- Understand and explain Geometric Distributions and their uses

## Quick Recap

Recall that the binomial distribution describes the probability of a success or a failure outcome in an experiment that is repeated multiple times.

In fact, a binomial distribution describes a repeated bernoulli experiment. A bernoulli experiment can be seen as one trial where there is a known success rate $p$. Examples:
- Rolling a dice once where success is defined as throwing a 5 or higher, the probability of success is 1/3.
- Shooting at a basketball rink where the success probability is 70%.
- etc.

The binomial distribution then has 2 parameters: $n$ and $p$, where $n$ is the number of independent experiments.

The binomial and hypergeometric distribution describe the number of successes in a fixed number, independent repetitions of Bernoulli experiments. The negative binomial and geometric
distribution describe the number of independent repetitions to a *fixed* number of *successes*. The geometric distribution is a special case of the negative-binomial distribution.

To be more specific, the geometric distribution is the probability for which trial the first successful Bernoulli experiment will occur on. The more general version of this is the negative binomial distribution which is the probability for which trial the nth success will occur on.

## 1. Let's take a look at the classic coin flipping case.

**A)** What's the probability that the first success occurs on the 1st trial? (Yes its that intuitive.)

#Your answer here

**B)** What's the probability that the first success occurs on the 2nd trial?  
(Hint: Think of all the possible scenarios: Either the success occured on the first trial, the success occurred on the second trial, or there still was no success. These three scenarios should encompass all possible scenarios and thus have a total probability of 1. Calculate the probability that the first trial was successful. Calculate the probability that neither the first nor second trial was successful. It should now be straightforward to calculate the final scenario: that the second trial was the original success.)  


```python
#Your answer here
```

**C)** What's the probability that the first success occurs on the 3rd trial? The 5th?


```python
#Your answer here
```

## 2. Geometric Function
Now write a probability distribution function for a random variable y. The function should take in the probability, p of the success of an individual Bernoulli experiment. (In our previous coin flipping example, p=0.5.)


```python
def geometric_dist(y,p):
    """y is a discrete random variable. It should be an integer that is greater then zero.
    p is the probability of a success for the Bernoulli experiment to be conducted.
    This function should return the probability that the first successful Bernoulli experiment will occur on the yth trial."""
    prob = #The probability that the first successful bernoulli experiment occurs on the yth trial.
    return prob
```

## 3. Product Failures
Assume that the probability of a product working is 95%. Before shipping the products, the manufacturer is checking each product for defects. What is the probability that the 10th product checked is the first defective one found?


```python
#Code and answer here
prob = 
```

## 4. Product Failures take 2
In many cases, a manufacturer might only test a sample of the products for defaults. Assuming 95% of the products do indeed work, what is the probability that in testing 20 units, that none will be defective?


```python
#Code and answer here
prob = 
```

## 5. Consumer Profiling
A previous sample showed that 70% of U.S. shoppers prefer to buy groceries in store as compared to online.  
Calculate the probability that the 6th person interviewed is the first to prefer to buy groceries online.


```python
#Code and answer here
prob = 
```

## 6. Consumer Profiling 2
What is the probability that at least 6 people have to be interviewed before finding someone who prefers to buy groceries online? (Assuming the statistic is true.)


```python
#Code and answer here
prob = 
```

## Summary

Awesome, you've now learned about many use cases for the geometric and negative binomial distribution!
