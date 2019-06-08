
# Naive Bayes and Scikit-Learn - Codealong 

## Introduction

In this lesson, we'll gain experience using sklearn to work with text data and implement a Naive Bayesian Classifier, including sklearn pipelines!

## Objectives

You will be able to:

* Implement Basic NLP Tasks including stemming/lemmatization, tokenization, and word vectorization
* Implement a machine learning classifier to process text, run the classifier, and validate results 

## Getting Started

In this lesson, we'll see an example of how we can we can use professsional tools such as sklearn to work through a real world NLP task. For this lesson, we'll build a pipeline that processes the text and then trains a Naive Bayesian Classifier on the _Reuters dataset_.  This tutorial has been modified from the tutorial available in the [sklearn documentation](https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html).
## Loading Our Dataset

We need to start by loading in our dataset.  SKlearn has provided a helper file to do this for us, called `fetch_data.py`.  

To load the data:

1. Open a terminal window
2. Navigate to this directory
3. Run the command `python fetch_data.py`

**_NOTE:_** This dataset is decent size, coming it at ~14 mb compressed.  This helper file will download the file and then decompress the data, but will only update you as each step finishes.  If it seems like it's frozen, don't worry--just let it finish! It should take a few minutes. 

When the helper file has finished, you'll see two new folders in this directory--`20news-bydate-test` and `20news-bydate-train`.

In order to make things move a bit more quickly, we'll limit ourselves to only 4 of the available 20 categories.  


```python
categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
```

Now, we'll load in only the files that contains articles matching those categories. 


```python
from sklearn.datasets import fetch_20newsgroups
twenty_train = fetch_20newsgroups(subset='train', categories=categories, 
                                  shuffle=True, random_state=42)
```

We can check the names of our targets to confirm that we have the right ones. 


```python
twenty_train.target_names
```

Next, let's take a look at how many articles we have. 


```python
len(twenty_train.data)
```

We can even take a look at the filenames of the articles, and the articles themselves!


```python
print("First line of article")
print('\n'.join(twenty_train.data[0].split('\n')[:3]))

print('label: {}'.format(twenty_train.target_names[twenty_train.target[0]]))
```

It's also a good habit to inspect our labels to get a feel for what they look like.



```python
twenty_train.target[:10]
```

Now that we have our data, we can move onto preprocessing our text, which includes:

* Tokenizing our text
* Transforming our text to a vectorized format

Run the cell below to import everything we'll need for the remainder of this lab. 


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
np.random.seed(0)
%matplotlib inline
```

## Vectorizing Our Text

Now that we've loaded in the data, all that's left to do is to vectorize it, so that we can use it to train a **_Multinomial Naive Bayesian Classifier_**.

We'll start by using **Count Vectorization_** and then convert everything to **_Term Frequencies_** to normalize everything (otherwise, longer articles would naturally have higher word counts than shorter articles). 


```python
count_vectorizer = CountVectorizer()
x_train_counts = count_vectorizer.fit_transform(twenty_train.data)
```

Note that once we've fitted our vectorizer as we did above, we can use it's built-in dictionary to get the indices of any words we choose!


```python
count_vectorizer.vocabulary_.get('dog')
```

Note that the output above represents the index of the word "dog", not the actual count for how many times that word appears. However, we could use that index to look it up, if we chose to!

Once we have our Count Vectorizer, it's pretty easy to leverage sklearn's `TfidfTransformer` to convert these counts to **_Term Frequencies_** (which is what the 'tf' in 'tf-idf' stands for). 


```python
tf_transformer = TfidfTransformer(use_idf=False).fit(x_train_counts)
x_train_tf = tf_transformer.transform(x_train_counts)
```

## Fitting Our Classifier

Now that we've vectorized our data, we can create a `MultinomialNB` classifier and fit it to our vectorized data!



```python
clf = MultinomialNB()
clf.fit(x_train_tf, twenty_train.target)
```

Usually, we call `.fit()` and `.predict()` manually at first, so that we can change things around as needed experiment.  However, this can get a bit redundant--luckily, we can make use of sklearn's `Pipeline` class to automate many of the steps we've just done manually!


```python
text_clf = Pipeline([('count_vectorizer', CountVectorizer()), 
                     ('tfidf_vectorizer', TfidfTransformer()),
                     ('clf', MultinomialNB())
                    ])
```

Now that we have our pipeline object that contains the vectorization and transformation steps as well as our classifier, we can easily pass in unprocessed data and call things like `.fit()` and let the pipeline take care of all the steps we've outlined!


```python
text_clf.fit(twenty_train.data, twenty_train.target)
```

## Evaluating Classifier Performance 

Recall that in order to really get a feel for how well our classifier is performing, we need to check its performance against data it hasn't seen before. We do this by splitting off some of our labeled data into a **_Test Set_**.  We have already have a test set created thanks to the helper function that we used to load everything in. In the cell below, we'll use our pipeline object to create predictions.  We can then make use of the `metrics` module in sklearn to view a **_Classification Report_** that shows us how well our model performed! 

We'll start by loading in our test set, in the same way that we loaded in our training set.


```python
twenty_test = fetch_20newsgroups(subset='test', categories=categories, 
                                 shuffle=True, random_state=0)
test_articles = twenty_test.data
test_labels = twenty_test.target
```

Now, let's use our pipeline to create some predictions for our test data, and then compare the results to the corresponding labels.


```python
test_predictions = text_clf.predict(test_articles)
np.mean(test_predictions == test_labels) # Expected Output: 0.8348868175765646
```

**_83.4% accuracy--pretty good!_**  Let's round out this lab by viewing a full **_Classification Report_** for how our model performed for each given category:


```python
print(metrics.classification_report(test_labels, test_predictions, 
                              target_names=twenty_test.target_names))
```

## Summary

In this lesson, we worked through an example of how to use professional-quality tools such as **_sklearn_** to preprocess, vectorize, and classify real-world text data by predicting the categories of news articles using Naive Bayesian Classification. Great job!
