
# Naive Bayes Classifier in Numpy - Lab

## Introduction
Naive Bayes classifiers are a **family of probabilistic classifiers** based on Bayes' theorem, with an assumption that each feature is independent from one another. Previously we looked at the learning mechanism of this classifier in terms of maximizing the posterior probability. In this lab we shall learn to code a **Gaussian Naive Bayes Classifier** from scratch , and also learn to use scikitlearn library for this task.   

## Objectives

You will be able to:

- Build a Naive Bayes Classifier in Python and Numpy to make predictions on unseen data 

## Building a Gaussian NB Classifier

Below we shall attempt to build a naive Bayes classifier in using numpy calculations only. Python offers sophisticated implementations of this algorithm in SciKitLearn which we shall look at in the following lesson. Here we will use the equations we have learned so far, and put them into action for a very simple example. 

## Problem:  Gender Classification 

Let's work with a small toy-data with continuous features (height, weight, foot size) and a target variable (Person: male or a female). We would work on building a classifier that can learn the joint probability of data and the target variables and classify a new example as a male of female. 

Note : You may also use a multinomial distribution for footsize (categrocial). Let's just assume they are all continuous for now.

### Read the data `gender.csv` into Pandas data frame and inspect its content. 


```python
import numpy as np
import pandas as pd
data = None
data
# 	Person	height	weight	foot size
# 0	male	6.00	180	12
# 1	male	5.92	190	11
# 2	male	5.58	170	12
# 3	male	5.92	165	10
# 4	female	5.00	100	6
# 5	female	5.50	150	8
# 6	female	5.42	130	7
# 7	female	5.75	150	9
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Person</th>
      <th>height</th>
      <th>weight</th>
      <th>foot size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>male</td>
      <td>6.00</td>
      <td>180</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>male</td>
      <td>5.92</td>
      <td>190</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>male</td>
      <td>5.58</td>
      <td>170</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>male</td>
      <td>5.92</td>
      <td>165</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>female</td>
      <td>5.00</td>
      <td>100</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>female</td>
      <td>5.50</td>
      <td>150</td>
      <td>8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>female</td>
      <td>5.42</td>
      <td>130</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>female</td>
      <td>5.75</td>
      <td>150</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



So a very small dataset, but this will help us better understand how the classifier works in more detail. The results surely wont be groundbreaking. We can see that gender is shown as strings male/female . Let's change "male" to 0 and "female" to 1 and make a binary categorical variable. 

### Index the labels $[male, female] \rightarrow [0, 1] $.


```python
# Subset data and assign 0 and 1 

data
# Person	height	weight	foot size
# 0	0	6.00	180	12
# 1	0	5.92	190	11
# 2	0	5.58	170	12
# 3	0	5.92	165	10
# 4	1	5.00	100	6
# 5	1	5.50	150	8
# 6	1	5.42	130	7
# 7	1	5.75	150	9
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Person</th>
      <th>height</th>
      <th>weight</th>
      <th>foot size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>6.00</td>
      <td>180</td>
      <td>12</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>5.92</td>
      <td>190</td>
      <td>11</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0</td>
      <td>5.58</td>
      <td>170</td>
      <td>12</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0</td>
      <td>5.92</td>
      <td>165</td>
      <td>10</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>5.00</td>
      <td>100</td>
      <td>6</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1</td>
      <td>5.50</td>
      <td>150</td>
      <td>8</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1</td>
      <td>5.42</td>
      <td>130</td>
      <td>7</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1</td>
      <td>5.75</td>
      <td>150</td>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>



This is great. Now that we have our data in the format that we need, we can start focusing on the Naive Bayes equation and take our experiment forward. 

We have our data data $x = (x_{1}, \ldots, x_{n})$ (height, weight, footsize) to be classified, Using joint probabilities between data and target class (Person), NB classifier assigns a discrete probability to all examples of feature data as shown below:

$$ p(C_{k}|x_{1}, \ldots, x_{n} )$$

Here, $K$ represents the numbers on classes in the target variable. 

### Gaussian PDF
With continuous data, we assume that the features for each class are distributed according to a Normal/Gaussian distribution and class probability can be calculated using Gaussian PDF function below

$$ f(x) = \dfrac{1}{\sqrt{2 \pi \sigma^2}} \cdot exp\bigg(\dfrac{-(x - \mu)^2}{2 \sigma^2}\bigg) $$

Where $\sigma^2$ represents the variance of the values in $x$, while $\mu$ represents the mean of the values in $x$. So to calculate the distribution function, we first need to calculate the mean and variance of each variable with respect to the target classes (male or female). 

### Segment (subset) the dataset by class (male/female) and calculate the mean and var of features for male and female classes. 

Before we can compute for the probability distribution for features $x$, we must first compute for the mean $\mu$ and variance $\sigma^{2}$ values of $x_{i}$ for each $k$ class.


```python
# Your code here 


# Example output

# Mean values for male features
# height         5.855
# weight       176.250
# foot size     11.250
# dtype: float64

# Variance values for male features
# height         0.035033
# weight       122.916667
# foot size      0.916667
# dtype: float64

# Mean values for female features
# height         5.4175
# weight       132.5000
# foot size      7.5000
# dtype: float64

# Variance values for female features
# height         0.097225
# weight       558.333333
# foot size      1.666667
# dtype: float64
```

### Decision Rule

In order to build a functional classifier from the model above, we need some kind of a decision rule, (this applies to all classifiers). For our NB classifier, we use the $ARGMAX$ function for identifying a unknown target class for a new example.

$$ \hat{y} = argmax_{k \in \{1,\ldots,K\}} \bigg(p(C_{k}) \prod_{i=1}^{n} p(x_{i}|C_{k})\bigg) $$

Now that we have the $\mu$ and $\sigma^{2}$ values for each features $x_{i}$ per $k$-class, let us now write a function for our $likelihood$ computation, i.e. 

$$p(x_{i}|C_{k})$$. 

Recall that we are going to plugin the likelihood computation into the Gaussian probability density function,

$$ p(x = x_{i} | C_{k}) = \dfrac{1}{\sqrt{2 \pi \sigma_{k}^{2}}} \cdot exp\bigg(\dfrac{-(x_{i} - \mu_{k})^2}{2 \sigma_{k}^{2}}\bigg) $$

### Implement the `likelihood(xi, mu, var)` function from above equation


```python
def likelihood(xi, mu, var):
     pass
```

So this is our function for computing likelihood. We shall now compute the $prior$ probability for $k$-classes. 

There are two ways to do this: 
- Give an equal probability for each $k$-classes i.e. a uniform prior
- (number of class samples) / (total number of samples). 

For this small dataset, we have equal number of classes , and both approaches will lead us to have . uniform prior anyway. we shall get a prior probabiity of 0.5 since there are exactly 4 samples for each class.

### Declare prior probability of both target classes


```python
class_priors = None
class_priors


# array([0.5, 0.5])
```

Great, with our `class_priors` array $p(C_{k})$, we have everything we need to solve the equation.

### Classify a new example

We can now classify an un-labeled data. 

### Add a new example with features (but no target) to our dataset. 


```python
# Add a new example with features of your choice (keep them reasonable)


# Person	height	weight	foot size
# 0	0	6.00	180	12
# 1	0	5.92	190	11
# 2	0	5.58	170	12
# 3	0	5.92	165	10
# 4	1	5.00	100	6
# 5	1	5.50	150	8
# 6	1	5.42	130	7
# 7	1	5.75	150	9
# 8	-99	6.00	130	8 <-- new example
```

> Using value -99 or similar values for unknowns in a dataset is a common way of processing data without generating Nan errors , yet keep the unknown identifiable by putting in some unlikely value i.e. -99 or -1 , which can later be searched for.

Let's calculate likelihood (probability of unknown class given new data) of each xi for the new example. 

### Using` likelihood()`, get likelihood values  `height`, `weight` and `footsize`  for new example. 


```python
# height feature
x_1 = None
# weight feature
x_2 = None
# foot size feature
x_3 = None

x_1, x_2, x_3

# (array([1.57888318, 0.22345873]),
#  array([5.98674302e-06, 1.67892979e-02]),
#  array([0.00131122, 0.2866907 ]))
```




    (None, None, None)



This completes our Gaussian likelihood $p(x=x_{1} | C_{k})$. 

Now that we have all the likelihood values and our prior probabilities, the variables in our equation are now complete. Now we need to calculate the formula 
$$p(C_{k}) \prod_{i=0}^{n} p(x_{i}|C_{k})$$

In this particular example , it can be written simply as:

$$ prediction = prior \times x_{1} \times x_{2} \times x_{3} $$ 


### Calculate the class prediction for new example using above formula


```python
prediction = None
prediction
```

### Normalizing with "Evidence" P(X)

Recall that Gaussian $p(x_{i} | C_{k})$ equation gives a probability density, not a probability distribution. To get the equivalent probability distribution, we  need to **normalize** the probability density. Recall the denominator in Bayes laws , also known as "Probability of Data" or "Evidence" is calculated as below:


$$ \sum_{i = 0}^{k - 1} \Bigg( p(c_{i}) \prod_{j = 0}^{n - 1} p(x_{j} | c_{i}) \Bigg) $$

Concretely, the `evidence` may be computed as follows in this case,

$$ evidence = {p(male)\ p(height|male)\ p(weight|male)\ p(foot\ size|male)\\ +\ p(female)\ p(height|female)\ p(weight|female)\ p(foot\ size|female)} $$

> The `evidence` is the sum of all joint probability $p(C_{k}, x)$.



### Normalize the predictions using the equation for `evidence` we have defined above


```python
evidence = None
posterior = None
```


```python
posterior
# array([1.15230663e-05, 9.99988477e-01])
```

#### Sanity check

The `posterior` probability values SHOULD now sum up to 1, i.e. a probability distribution. Let's check for it. 


```python
# Uncomment to check 
#np.sum(posterior)

# 1.0
```




    1.0



### Bring in `ARGMAX` , the decision rule

So now we have posterior class probabilities for each class, that sum up to 1. So naturally, which ever class shows a higher probability, will be chosen as the prediction. 

$$ \hat{y} = argmax_{k \in \{1,\ldots,K\}} \bigg(p(C_{k}) \prod_{i=1}^{n} p(x_{i}|C_{k})\bigg) $$

### To get our predicted class, use the $np.argmax()$ function with `posterior`



```python
# Predict the class using argmax

# The Naive Bayes predicts Class: 1
```

Recall that the index `1` refers to `female`, hence our classifer predicts that a probable class for new example is `female`. Neat isn't it. Pretty naive , yet highly effective.

## Level Up - Optional 

- Read the dataset `diabetes.csv` into your code and modify the code it to perform predictions on presence or absence of diabetes using a number of available features and a target variable. 

You may need to covert some of the code into functions to help you process your data faster as this now has 8 features. 

## Summary 

In this lab, we looked at building a Naive Bayes classifier from scratch. This was not a complete machine learning experiment as we rather focused on the seeing how the algorithm performs in relation to underlying mathematics. NExt we shall look at how to achieve this functionality in SciKitLearn. 
