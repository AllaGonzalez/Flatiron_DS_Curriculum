
# Introduction

## Introduction
This lesson summarizes the topics we'll be covering in section 22 and why they'll be important to you as a data scientist.

## Objectives
You will be able to:
* Understand and explain what is covered in this section
* Understand and explain why the section will help you to become a data scientist

## Bayesian Classification

We've learned a reasonable amount about Bayes theorem and how to apply it, but to date it's mainly been in the context of coin tosses. It's a great domain for learning the principles, but it's fairly unlikely that when you get a job as a data scientist you're mainly going to be concerned with predicting "heads" or "tails"!

In this section, we're going to look at how to build a Naive Bayesian Classifier for document classification, providing a lightweight introduction to the much more useful field of Natural Language Processing.

### MLE with Normal Distributions

We start by showing how to calculate the estimations for expected mean and standard deviation for a given population using Maximum Likelihood Estimation (assuming a normal distribution of the data).

### MAP and Naive Bayes Classifier

We then extend our MLE approach by showing how Maximum A Posteriori estimations for thetas can be used in a predictive context as the basis of a Naive Bayes classifier.

### Naive Bayes Assumptions and Applications

Next up, we look at some of the properties, assumptions and applications of Naive Bayes Classifiers to help you to get a better sense of how and when to use them.

### Naive Bayes Classifier Labs

We then give you some hands on experience of building a Gaussian Naive Bayes (NB) Classifier from scratch in NumPy to classify likely gender based on height, weight and foot size. We then ask you to implement a breast cancer diagnosis system, again using a NB Classifier. 

### NLP and Word Vectorization

Before we can start to use Naive Bayes to create a document classifier, it's important to cover some foundational concepts in Natural Language Processing (NLP). We start by explaining what NLP is and then introduce the process of cleaning and tokenization (and stemming, lemmatization and removal of stop words) to turn a document into a "bag of words" with each remaining word representing one dimension in an n-dimensional space. We also introduce the concept of Term Frequency - Inverse Document Frequency (TF-IDF) for highlighting words that potentially contain more information than others within a document. You then get to tokenize lyrics from both Garth Brooks and Kendrick Lamar to see if you can teach a computer to tell the difference between the two! (If you can't tell the difference between the two, that is a problem that this course will unfortunately be unable to remedy!)

### Naive Bayes and SciKit-Learn

Next up we run you through a code along, getting some hands on practice using sklearn to work with text to implement a NB Classifier.

### Document Classification using Naive Bayes

We then ask you to bring it all together by working with a real world dataset to classify emails as spam or ham (not spam) using a NB Classifier.

### Optimality of Naive Bayes

As a professional data scientist it will be essential for you to read research papers to keep up with advancements in the field. To give you some more practice doing so, we finish up the section by asking you to review a research paper that covers some naive Bayes models and discusses various applications of the classifier.


## Summary

NLP is a huge topic that we will return to later in the course, but it's also a great application for NB classifiers which are still used to solve certain NLP classification problems. This section acts as both an introduction to NLP and an application of the MLE, MAP and Bayes Theorem content that we covered in the last section.
