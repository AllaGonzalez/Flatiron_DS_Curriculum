
# Permutations and Factorials



## Introduction

In the previous lab, you defined at a few sample spaces by counting the total number of possible outcomes. This is not very practical when sample spaces grow. In this lab, you'll be introduced to *permutations*, which will provide a structured way to help you define sample space sizes!

## Objectives

You will be able to: 
- Understand how to count permutations, and how factorials are the building blocks of permutations
- Understand how to mathematically derive how many permutations there are for big sets
- Understand how to compute permutations of a subset
- Learn about permutations with replacement and repetition

## Defining the sample space by counting

Let's consider the following example.

The Michael Jackson tribute band "Who's bad" is playing a free mini gig in Central Park next week. They have selected three all-time classics: "Billy Jean", "Bad" and "Thriller", but still have to decide the order they will play the songs in. Knowing this, how many playlists are possible?

It is easy and fairly quick to write down possible orders here:

"Thriller", "Bad", "Billy Jean"

"Thriller", "Billy Jean", "Bad"

"Billy Jean", "Thriller", "Bad"

"Billy Jean", "Bad", "Thriller"

"Bad", "Thriller", "Billy Jean"

"Bad", "Billy Jean", "Thriller"

That's it! When we count the possible outcomes, we get to 6 elements in the sample set. Now what if "Who's bad" plays a setlist of 4 songs? or 5? That's where the notion of *permutations* comes in handy.


## Permutations

The problem setting in general is that, there are $n$ objects, and we want to know how many *permutations* are possible.

This is a way how you can tackle this. You're the front singer and have to decide which song to play first. You have 3 songs to choose from, so 3 ways of chosing a first song. Then, you move on to the second song. You've chosen the first one, so you have 2 songs to choose from now. Etcetera. Mathematically, this boils down to:

 $ \text{# Jackson permutations} = 3*2*1 = 3 ! = 6$

Generalizing this to $n$, this means that the number of permutations with $n$ distinct objects is $n!$, or the factorial of $n$.

## Permutations of a subset

Now, lets consider another example. "Who's bad" is still playing a concert at central park, but the disagree on the final three songs that they will play. They only get a 12min gig slot, so they really can't play more than 3, yet they have a shortlist of 8 they need to pick from. How many final song selections are possible given this info? As for the first example, the order of the songs played is still important.

When the band members decide on the first song, they have 8 possible songs to choose from. When chosing the second song, they have 7 to choose from. Then for the third song, they have 6 left.

 $ \text{# Jackson k-permutations} = 8*7*6 = 336$

formalizing this, the question is how many ways we can select $k$ elements out of a pool of $n$ objects. The answer is 

$n*(n-1)*...*(n-k+1)$ or in other words, $P_{k}^{n}= \dfrac{n!}{(n-k)!}$

This is known as a $k$-permutation of $n$.

The idea is here that we only "care" about the order of the first $k$ objects. The order of the other $(n-k)$ objects doesn't matter, hence they're left out of the equation.

## Permutations with replacement

When talking about setlists, it makes total sense to assume that songs will not be played twice. This is not always how it works though. Let's consider throwing a dice. Imagine a bag with three marbles in it: a green one, a red one, and a blue one. Now we'll draw marbles three times in a row, but each time, we'll write down the marble color and *put it back in the bag* before drawing again.

Now the number of possible outcomes is $3 * 3 * 3$.

Except for the fact that marbles can be  put back in the bag,

Generalizing this to $n$, this means that the number of permutations with replacenent when having $n$ distinct objects is equal to $n^j$ where $j$ is the number of "draws".

## Permutations with repetition

Let's go back to the example where a teaching assistant has a meeting with 3 female and 3 male students. Here, we have n=6 objects, but unlike the previously discussed topics, there is **repetition** in this case. 

## Summary

Now you're well on your way to calculate all sorts of permutations using factorials - both for understanding the sample space, subsets, etc! Let's move on for some practice!
