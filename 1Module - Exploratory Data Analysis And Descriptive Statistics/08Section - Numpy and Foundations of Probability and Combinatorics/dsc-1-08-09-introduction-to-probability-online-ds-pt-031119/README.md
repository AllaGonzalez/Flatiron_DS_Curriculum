
# Introduction to Probability

## Introduction

Now that you understand the basics of sets, you'll learn how this knowledge can be used to calculate your first probabilities! In this section, you'll learn how to use sets to create probabilities, and you'll learn about the very foundations of probability through the three probability axioms.

## Objectives

You will be able to: 

- Learn about experiments, outcomes and event space
- Understand probability through the law of relative frequency
- Learn about the probability axioms
- Learn about the addition law of probability
- Learn that where each outcome is equally likely, the probability is equal to number of outcomes in the event space divided by number of outcomes in the sample space 

## Experiment and outcomes

Previously, we defined sets and related concepts. Now let's look at the set

$S= \{1,2,3,4,5,6\}$ being the possible outcomes when throwing a dice.

In this context, we'd call throwing the dice a *random experiment*. The result of this experiment is then called the outcome. Note that $S$ defines all the possible outcomes when throwing the dice once, so in fact, we can also call it the Universal set $\Omega$, as seen before.

In the context of experiments, we denote $S$ the **sample space**.

Other examples of sample spaces:
- Number of text messages a day:  $S = \{x \mid x \in \mathbb{Z}, x \geq 0\}$
- Hours of TV a day:  $S = \{x \mid x \in \mathbb{R}, 0 \leq x \leq 24 \}$

## Event space

In this context, we can also define the event space. The **event space** is a subset of the sample space, $E\subseteq S$

For example, the event "throwing a number higher than 4" would result in an event space $E= \{5,6\}$. Throwing an odd number would lead to an event space $E= \{1,3,5\}$. 


Summarized, the event space is a collection of events that we *care* about. We say that event $E$ happened if the actual outcome after rolling the dice belongs to the predefined event space  $E$.

Using the concepts of sample space and event space, we can now introduce the concept of **probability**.

Other examples of event spaces based on previously defined sample spaces:
- Low text message volume day:  $E = \{x \mid x \in \mathbb{Z}, 0 \leq x \leq 20 \}$
- Bingewatch day:  $E = \{x \mid x \in \mathbb{R}, x \geq 6 \}$

## Introduction to probability

### The law of relative frequency

While conducting an endless stream of experiments, the relative frequency by which an event will happen becomes a fixed number. 

Let's denote an event $E$, and $P(E)$ the probability of $E$ occurring. Next, let $n$ be the number of conducted experiments, and $S(n)$ the count of "succesful" experiments (i.e. the times that event $E$ happend). The formal definition of probability as a relative frequency is given by:

$$P(E) = \lim_{n\rightarrow\infty} \dfrac{S{(n)}}{n}$$


This is the basis of a frequentist statistical interpretation: an events probability is the ratio of the positive trails to the total number of trials as we repeat the process infinitely. 

For example, the probability of rolling a 5 on a 6 sided dice is the limit of the successes to trials as the number of trials goes to infinity.

In the early 20th century, Kolmogorov and Von Mises came up with 3 axioms that further expand upon this notion.

###  Probability axioms

The three axioms are

#### 1. Positivity

A probability is always bigger than or equal to 0, or $0 \leq P(E) \leq 1$

#### 2. Probability of a certain event

If the event of interest is the sample space, we say that the outcome is a certain event, or $P(S) = 1$

#### 3. Additivity 

The probability of the union of 2 exclusive events is equal to the sum of the probabilities of the individual events happening.

If $A \cap B = \emptyset $, then $P(A\cup B) = P(A) + P(B)$ 

### Addition law of probability

The additivity axiom is great, but most of the time events are not exclusive. A very important proberty is the **addition law or probability** or the **sum rule**.

$P(A\cup B) = P(A) + P(B) - P(A \cap B) $ 

Put in words, the probability that $A$ or $B$ will happen is the sum of the probabilities that $A$ will happen and that $B$ will happen, minus the probability that both $A$ and $B$ will happen.

## Summary

Well done! In this section, you learned how to use sets to get to probabilities. You learned about experiments, event spaces and outcomes. Next, you learned about the law of relative frequency and how it can be used to calculate probabilities, along with the three probability axioms.
