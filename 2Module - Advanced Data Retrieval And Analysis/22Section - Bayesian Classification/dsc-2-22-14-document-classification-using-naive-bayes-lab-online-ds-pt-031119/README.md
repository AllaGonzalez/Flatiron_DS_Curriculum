
# Document Classification using Naive Bayes - Lab

## Introduction

In this lab, we'll make use of our newfound Bayesian knowledge to classify emails as spam or not spam from the [UCI Machine Learning Repository's Spambase Dataset](https://archive.ics.uci.edu/ml/datasets/spambase).  

## Objectives

You will be able to:
* Work with a real-world dataset from the UCI Machine Learning Repository
* Classify emails as spam or not spam by making use of Naive Bayesian Classification
* Evaluate the quality of our classifier by building a Confusion Matrix

## Let's get started!

Run the cell below to import everything we'll need for this lab.


```python
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, f1_score
# Do not change the random seed, or else the tests will fail!
np.random.seed(0)
# %matplotlib inline
```

For this lab, we'll be working with the [Spambase Dataset](https://archive.ics.uci.edu/ml/datasets/spambase) from [UC Irvine's Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php). 

This dataset contains emails that have already been vectorized, as well as summary statistics about each email that can also be useful in classification.  In this case, the Data Dictionary containing the names and descriptions of each column is stored in a separate file from the dataset itself.  For ease of use, we have included the `spambase.csv` file in this repo.  However, we have not included the Data Dictionary and column names.  

In the cell below, read in the data from `spambase.csv`, store it in a DataFrame, and print the head.  

**_HINT:_** By default, pandas will automatically assume that the first row contains metadata containing the column names. Since our dataset does not have a row of metadata, pandas will mistakenly assume the values for the first email are the column names for each column.  You can prevent this by setting the `header` parameter to `None`.


```python
# Test 1: Do not change variable name!
df = None
```

As we can see, the dataset does not contain column names.  You will need to manually grab these from the [Dataset Description](https://archive.ics.uci.edu/ml/machine-learning-databases/spambase/spambase.names) and create an array containing the correct column names that we can set.  

Take a minute to visit the link above and get the names of each column.  There's no python magic needed here--you'll just need to copy and paste them over in the correct order as strings in a python array.  (It's not glamorous, but it's realistic.  This is a pretty common part of the Data Science Process.)

In the cell below, create the array of column names and then use this array to set the correct column names for the `df` object.  

**_NOTE:_** Be sure to read the Dataset Description/Documentation carefully.  Note that the last column of the dataset (we can call it `is_spam` is the last column of the actual dataset, although the data description has it at the top, not the bottom, of the list.  Make sure you get this column name in the right place, as it will be our target variable!


```python
# Test 2: Do not chang variable name!
column_names = None
```

## Cleaning and Exploring the Dataset

Now, in the cell below, use what you've learned to clean and explore the dataset.  Make sure you check for null values, and examine the descriptive statistics for the dataset.  

Try to create at least 1 visualization during this Exploratory Data Analysis (EDA) process. 

Use the cells below for this step. 

**_Remember_**, if you need to add more cells, you can always highlight a cell, press `esc` to enter command mode, and then press `a` to add a cell above the highlighted cell, or `b` to add a cell below the highlighted cell. 

## Analysis of Exploration

Did you notice anything interesting during your EDA? Briefly explain your approach and your findings below this line:
________________________________________________________________________________________________________________________________




## Creating Training and Testing Sets

Since we are using Naive Bayes for classification, we'll need to treat this like any other machine learning problem and create separate **_training sets_** and **_testing sets_** for **_holdout validation_**.  Otherwise, if we just trust the classifier's performance on the training set, we won't know for sure if the classifier has learned to detect spam emails in the real world, or just from this particular dataset.  

In the cell below:

* Store the target column in a separate variable and then remove it from the dataset. 
* Create training and testing sets using the [appropriate method](http://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) from `sklearn`.  

**_HINT:_** We want to make sure that the training and testing samples get same distribution of spam/not spam emails.  Otherwise, our model may get a training set that doesn't contain enough of one class to learn how to tell it apart from the other.  In order to deal with this problem, we can pass in the variable containing our labels to the `stratify` parameter.  For more information, see the documentation in the link above.  


```python
# Test 3: Do not change variable names!
target = None
clean_df = None


# Test 4: Do not change variable names!
X_train, X_test, y_train, y_test = None
```

## Fitting our Classifier

Now that we have split our data into appropriate sets, we need to fit our classifier before we can make predictions and check our model's performance.

Recall what you learned about the 3 different types of Naive Bayesian Classifiers provided by `sklearn`.  Given the distribution of our data, explain why each of the following classifier types is or isn't appropriate for this problem.

**_GaussianNB:_**  

**_BernoulliNB:_**   

**_MultinomialNB:_** 

In the cell below, create the appropriate classifier type and then `fit()` it to the appropriate training data/labels.


```python
clf = None

```

## Making Predictions

Now that we have a fitted model, we can make predictions on our testing data.  

In the cell below, use the appropriate method to make predictions on the data contained inside `X_test`.


```python
preds = None
```

## Checking Model Performance

Now that we have predictions, we can check the accuracy of our model's performance.  In order to do this, we'll use two different metrics: `accuracy_score` and `f1_score`.  For classification, accuracy is defined as the number of correct predictions (**_True Positives_** and **_True Negatives_**) divided by the total number of predictions.  

**_F1 Score_** is the harmonic mean of precision and recall. This tells us the accuracy, but penalizes the classifier heavily if it favors either **_Precision_** (Spam emails correctly identified, divided by all emails predicted to be spam) or **_Recall_** (the percentage of spam emails successfully caught, out of all spam emails) too much.  Don't worry if you aren't yet familiar with these terms--we'll cover these concepts in depth in later lessons!

In the cell below, use the appropriate helper functions from sklearn to get the accuracy and f1 scores for our model.  


```python
# Test 5: Do not change variable name!
accuracy = None

# Test 6: Do not change variable name!
f1 = None

print("Accuracy Score for model: {:.4}%".format(accuracy * 100))
print("F1 Score for model: {:.4}%".format(f1 * 100))
```

## Digging Deeper: Using a Confusion Matrix

Our model does pretty well, with ~81% accuracy.  However, we don't know _how_ it's failing on the 19% it got wrong.  In order to figure this out, we'll build a **_Confusion Matrix_**.

For every prediction our model makes, there are four possible outcomes:

**_True Positive:_** Our model predicted that the email was spam, and it was actually spam. 

**_True Negative:_** Our model predicted that the email was not spam, and it wasn't spam. 

**_False Positive:_** Our model predicted that the email was spam, but it wasn't.

**_False Negative:_** Our model predicted that the email wasn't spam, but it was.  


### Question:

Which type of misclassification is preferable to the other--False Positives or False Negatives?  In this given problem, which one is preferable to the other? Explain your answer below this line:
________________________________________________________________________________________________________________________________




### Building our Confusion Matrix

In the cell below, complete the `confusion_matrix` function.  This function should take in two parameters, `predictions` and `labels`, and return a dictionary counts for `'TP', 'TN', 'FP',` and `'FN'` (True Positive, True Negative, False Positive, and False Negative, respectively).  

Once you have completed this function, use it to create Confusion Matrices for both the training and testing sets, and complete the tables in the following markdown cell.

**_HINT:_** Your labels are currently stored in a pandas series.  To make things easier, consider converting this series to a regular old python list!


```python
# Test 7: Do not change function signature!
def confusion_matrix(predictions, labels):
    pass

# Test 8: Do not change variable names!
training_preds = None

# Test 9: Do not change variable names!
training_cm = {"TP": 1310, "TN": 1524, "FP": 567, "FN": 49}

# Test 10: Do not change variable names!
testing_cm = None

print("Training Confusion Matrix: {}".format(training_cm))
print("Testing Confusion Matrix: {}".format(testing_cm))
```

## Intepreting Our Results

Complete the tables below, and then use them to answer the following questions.


|  Training Results  | **Is Spam** | **Is Email** |
|:---------------:|:-------:|:--------:|
|  **Predicted Spam** |         |          |
| **Predicted Email** |         |          |
<br>

|  Testing Results  | **Is Spam** | **Is Email** |
|:---------------:|:-------:|:--------:|
|  **Predicted Spam** |         |          |
| **Predicted Email** |         |          |


How many emails are getting caught up in the spam filter? How many spam emails are getting through the filter?  Is this a model you would recommend shipping to production? Why or why not?
________________________________________________________________________________________________________________________________




Don't worry about tuning the model for now--that's a lengthy process, and we'll cover it in depth in later labs.  For now, congratulations--you just built a working spam filter using Naive Bayesian Classification!


## Summary

In this lab, we:
* Worked with a real-world dataset from the UCI Machine Learning Repository.
* Classified emails as spam or not spam by with a Naive Bayesian Classifier. 
* Built a Confusion Matrix to evaluate the performance of our classifier.   

