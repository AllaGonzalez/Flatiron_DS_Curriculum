
# Bayes' Theorem - Lab

## Introduction

In this lab, we shall try to put some of the formulas to practice that we came across with in the previous lesson. 

## Objectives
* Understand and describe the Bayesian theorem from conditional probabilities
* Describe the roles of Prior, Likehood and Posterior components of Bayes Theorem 
* Understand and perform simple applications of Bayes Theorem for sensitivity and specificity

## Exercise 1
### If a single card is drawn from a standard deck of playing cards, What is the probability of seeing a king ?


```python
# Your solution
```




    0.07692307692307693



### If evidence is provided (for instance, someone looks at the card) that the single card is a **face card**, what would be the posterior probability according to Bayes theorem?


```python
# Your Solution
```




    0.3333333333333333



## Exercise 2
#### 1. A couple has two children, the older of which is a boy. What is the probability that they have two boys?
#### 2. A couple has two children, one of which is a boy. What is the probability that they have two boys?


```python
# Explain events as:
# A = both children are boys
# B = older child is a boy 
# C = One of the children is a boy 
```


```python
# Part 1
# Your solution
```




    0.5




```python
# Part 2 
# Your solution
```




    0.3333333333333333



## Exercise 3 - Bayesian Disease Diagnosis

[Visit this link for an insight into Bayesian Disease Daignosis](http://doingbayesiandataanalysis.blogspot.com/2013/01/bayesian-disease-diagnosis-with.html)



A disease test is advertised as being 99% accurate 

* If a patient has the disease,they  will test positive 99% of the time.

* If you don't have the disease, they will test negative 99% of the time. 

* 1% of all people have this disease 

#### Now a patient tests positive, what is the probability that you actually have the disease?


```python
# Your solution
```




    0.5



## Summary 

In this lab, we saw a few simple examples of Bayesian logic and how we can add prior information to our calculation, in order to update our beliefs about the certain events. Bayesian logic works in numerous ways and it is not within the scope of this section to give you a deep dive in complex Bayesian problems. You are advised to re-visit the provided links when you have a better understanding of Bayesian inference. 
