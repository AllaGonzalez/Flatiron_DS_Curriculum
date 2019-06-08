
# Section Recap

## Introduction

This short lesson summarizes the topics we covered in section 22 and why they'll be important to you as a data scientist.

## Objectives
You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## Key Takeaways

The key takeaways from this section include:
* MLE can be used to calculate the estimations for expected mean and standard deviation of a normally distributed sample
* MAP estimations for thetas can be used in a predictive context with Naive Bayes
* The fundamental Naive Bayes assumption is that each feature makes an independent and equal (i.e. are identical) contribution to the outcome. This is known as the i.i.d assumption
* The most common approach to working with text is to vectorize it by creating a Bag of Words
* The first step is to tokenize the text, turning the document into a collection of space and/or punctuation delimited substrings (words)
* Tokenization also includes decisions about whether to lower case everything (almost always yes), and whether to use techniques like stemming and lemmitization to reduce each token into it's root word (running == runs == run)
* Finally in tokenization, you also want to ignore stop words - typically using a common NLP framework such as the Natural Language ToolKit (NLTK)
* After tokenization, then next step in making text computationally accessible is to vectorize it - whether through a simple word count or (where you have multiple documents) using TF-IDF to identify the most relevant words

