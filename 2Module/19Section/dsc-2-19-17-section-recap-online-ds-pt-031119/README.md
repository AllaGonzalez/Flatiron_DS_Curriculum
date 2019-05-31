
# Section Recap

## Introduction

This short lesson summarizes the topics we covered in section 19 and why they'll be important to you as a data scientist.

## Objectives
You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## Key Takeaways
Section 19 was all about statistics - distributions and sampling - strengthening the foundation for module 3 as you start to work with a wider range of machine learning models. Some of the key takeaways include:
* There are two types of distributions - continuous, where (subject to measurement and/or storage precision) there are effectively an infinite number of possible values, and discrete, where there are a distinct, non-infinite number of options. For example, a persons height is continuous - assuming a suitably precise tape measure - whereas the number of bedrooms in a house is discrete
* One type of discrete distribution deals with a series of boolean events or trials - often called Bernoulli Trials
* With a Uniform distribution, every possible outcome is equally likely. Both continuous and discrete sets can have a Uniform distribution
* A Normal distribution is the classic "bell curve" wiuth 68% of the probability mass within 1 sd of the mean, 95% within 2 sd's and 99.7% within 3 sd's
* The Binomial distribution is the discrete version of a normal distribution
* Negative Binomial trials are used to answer questions like "how many times can I flip a coin until I fail (get a tails) 3 times in total?"
* The Negative binomial distribution reflects the probability distribution for a negative binomial trial
* A Geometric distribution is a special case of a Negative Binomial distribution where the cumulative number of failures is fixed as 1. So "how many times can I flip a coin before I get one tails?"
* The Poisson distribution can be used to display the likelihood of a given number of successes over a given time period - e.g. "how likely is it that 25 people walk into a store in a given hour?"
* The Exponential distribution can be used to describe the probability distribution of the amount of time it may take before a given event occurs
* The Central Limit Theorem states that often, independent random variables summed together will cnverge to a normal distribution as the number of variables increases
* Using Central Limit Theorem, we can work with non-normally distributed data sets as if they were normally distributed
* The Standard Error is a measure of spread - it is the standard deviation of samples from the sample mean
* A Confidence Level is used to describe how confident we are that a given parameter is within a given range. E.g. "there's an 80% chance (confidence level of 80%) the person is between 5'5 and 6'2"
* That range is called the Confidence Interval
* The z-critical value is the number of standard deviations you'd have to go from the mean of the normal distribution to capture the proportion of the data associated with the desired confidence level.
* If you don't know the standard deviation for a population, you also need to use T-distributions

