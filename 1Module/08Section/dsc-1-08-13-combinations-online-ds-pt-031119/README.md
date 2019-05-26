
# Combinations

## Introduction

In the previous section, you learned about how to apply permutations. Permutations come in handy when we want to know how many ways we can order sets. Now what if order is not important? That's where *combinations* come in.

## Objectives

You will be able to: 

- Understand how combinations are used when the order is not important
- Be able to use and interpret the mathematical formula of combinations


## Why combinations?


In some settings, the order of the selection is not important.

Let's go back to our "Who's bad" example. Imagine that the Michael Jackson cover band is playing 3 songs out of their 8 song repertoire. How many ways can they select songs, assuming that the **order of the chosen songs is not important**? Here, we just want to know *which* three songs they play, and not which song goes first, second and last.

We can use a backward rationale here. We know that when order *did* matter, our answer was $8*7*6$. When having three elements, there are 6 possible orders (ABC, ACB, CAB, CBA, BAC, BCA), so we get to the answer by dividing our previous answer by 6. 

This type of problem setting can be solved by using *combinations*.
In general, combinations answer the question: "how many ways can we create a subset $k$ out of $n$ objects?". The subset is not ordered. 

$$\displaystyle\binom{n}{k} = \dfrac{P_{k}^{n}}{k!}=\dfrac{ \dfrac{n!}{(n-k)!}}{k!} = \dfrac{n!}{(n-k)!k!}$$

Note how *6* in our Michael Jackson example $= 6 = 3!$, as expected.

##  Summary

In this section, you learned what combinations are and how to use them. let's put this knowledge into practice!
