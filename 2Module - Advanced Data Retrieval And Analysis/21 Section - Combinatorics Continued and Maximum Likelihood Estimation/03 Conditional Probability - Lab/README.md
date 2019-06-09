
# Conditional Probability - Lab

## Introduction

In order to be ready for real world applications of probability, it is important to understand what happens when probabilities are not independent. Very often, the probability of a certain event depends on other events happening! Let's see how this all works in this lab.

## Objectives

You will be able to:

- Understand and Explain the conditional probability - P(A∩B) = P(A|B) x P(B)
- Use the multiplication rule to find the probability of the intersection of two events
- Apply the techniques learned in the lesson to simple problems


## Exercise 1
A coin is tossed and a single 6-sided die is rolled. Find the probability of landing on the head side of the coin and rolling a 3 on the die.


```python
# Your solution
```

## Exercise 2
A school survey found that 9 out of 10 students like pizza. If three students are chosen at random **with replacement**, what is the probability that all three students like pizza?


```python
# Your Solution
```

## Exercise 3
70% of your friends like Chocolate flavored ice cream , and 35% like Chocolate AND like Strawberry flavors.

What percent of those who like Chocolate also like Strawberry?


```python
# Your solution 
```

50% of your friends who like Chocolate also like Strawberry

## Exercise 4
What is the probability of drawing 2 consecutive Aces from a Deck of cards. 


```python
# Your solution
```

## Exercise 5
In a manufacturing factory that produces a certain product, there are 100 units of the product, 5 of which are defective. We pick three units from the 100 units at random. 

What is the probability that none of them are defective?
Hint: Use chain rule


```python
# Your solution
```

## Exercise 6

Let's consider the example where 2 dice are thrown. Given that **at least one** of the dice has come up on a number higher than 4, what is the probability that the sum is 8?

Let i,j be the numbers shown on the dice . Denote events as below:

* **Event A is when Either i Or j is 5 or 6** (Keep an eye on either - or)
* **Event B is when i + j = 8**


* What is the size of sample space Ω ?
* What is P(A ∩ B) ?
* What is P(A) ?
* Use above to calculate P(B|A) .


```python
# Your solution
```

## Exercise 7

Let's consider a credit card example. At a supermarket, we randomly select customers and make notes of whether a given customer owns a Visa card (event A) or an Amex credit card (event B). Some customers own both cards.
You can assume that:

- P(A) = 0.5
- P(B) = 0.4
- both A and B = 0.25.


With the knowledge we have about conditional probabilities, compute and interpret the following probabilities:

- $P(B \mid A)$
- $P(B'\mid A)$
- $P(A\mid B)$
- $P(A'\mid B)$



```python
# Your solution
```

## Summary 

In this lab we practiced around conditional probability and its theorem with some simple problems. The key takeaway from this lab is to to be able to identify random events as dependent or independent and calculating the probability of their occurrence using appropriate methods. Next we'll start focusing on the some more conditional probability axioms, building on the knowledge we have thus far. 
