

# Type 1 and Type 2 errors - Lab

## Introduction

In this lab, you'll run some of your own simulations to learn more about type 1 and type 2 errors. Remember that, the result of a statistical hypothesis test and the corresponding decision of whether to reject or accept the null hypothesis is not infallible. A test provides evidence for or against the null hypothesis and then you decide whether to accept or reject it based on that evidence, but the evidence may lack the strength to arrive at the correct conclusion. Incorrect conclusions made from hypothesis tests fall in one of two categories, i.e. [Type 1 and Type 2 erros](https://en.wikipedia.org/wiki/Type_I_and_type_II_errors) By running some of these simulations, you should have a better idea of why a 95% confidence level is often used for hypothesis testing.


## Objectives

You will be able to:

* Explain why alpha = 0.05 is chosen as the cut off point for rejecting Null hypothesis in most scientific experiments
* Simulate Type I and Type II errors with alpha control to observe the output of an experiment
* Describe and differentiate between TYPE I and TYPE II errors
* Understand alpha and beta for representing false positive and false negative values

## Alpha and Beta

**Alpha (α):** is the probability of a type I error i.e. finding a difference when a difference does not exist. 

Most medical literature uses an alpha cut-off of 5% (0.05), indicating a 5% chance that a significant difference is actually due to chance and is not a true difference. 

**Beta (β):** is the probability of a type II error i.e. not detecting a difference when one actually exists. 

Beta is directly related to study power (Power = 1 – β) which we shall see in the next lesson. Most medical literature uses a beta cut-off of 20% (0.2), indicating a 20% chance that a significant difference is missed. 


Let's try to simulate and visualize this phenomenon using some Python code.


```python
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import math
import random 

import seaborn as sns
sns.set(color_codes=True)
```

 First, we create a population of 1000 elements with a mean of 100 and a standard deviation of 20.


```python
# Create a population with mean=100 and sd=20 and size = 1000
pop = np.random.normal(100, 20, 1000)
pop.dtype
sns.distplot(pop)
```




    <matplotlib.axes._subplots.AxesSubplot at 0x18648fc0780>




![png](index_files/index_5_1.png)


Lets take two sample from this population and comment of the difference between their and means and standard deviations. How would you ensure the independance between elements of these samples? 


```python
k = 100
sample1 = np.random.choice(pop,100,replace=True)

print ("Sample 1 Summary")
stats.describe(sample1)
```

    Sample 1 Summary





    DescribeResult(nobs=100, minmax=(48.805213677063804, 150.65090167588255), mean=96.24673360637617, variance=423.20457474058924, skewness=-0.05353301922536613, kurtosis=-0.29302775964422034)




```python
sample2 = np.random.choice(pop,100,replace=True)
print ("Sample 2 Summary")
stats.describe(sample2)
```

    Sample 2 Summary





    DescribeResult(nobs=100, minmax=(57.96868014684502, 159.29406605999827), mean=102.76786471724154, variance=420.45658021864733, skewness=0.29145404089799065, kurtosis=0.7249842236748019)



We can see can see that if we take two samples from this population, the difference between the mean of samples 1 and 2 is very small small (this can be tried repeatedly). We must sample with replacement in order to ensure the independance assumption between elements of the sample. 

There is, however, still a probability of seeing very large difference between values, even though they’re estimates of the same population parameters. In a statistical setting we’d interpret these unusually large differences as evidence that the two samples are statistically different. It depends on how you define statistical significance. In statistical tests this is done by setting a significance threshold `α` (alpha). Alpha controls how often we’ll get a type 1 error. A type 1 error occurs when our statistical test erroneously indicates a significant result.

We can run two sample t-test with independance assumption on these sample and as expected, the null hypothesis will be proven true due to similarities between distributions. We can also visualize the distribution to confirm the similarity between means and SDs. 


```python
# test the sample means
stats.ttest_ind(sample1, sample2)
```




    Ttest_indResult(statistic=-2.245116623023133, pvalue=0.02586635243662942)




```python
plt.figure("Test Samples")
sns.distplot(sample1, label='Sample1') 
sns.distplot(sample2, label='Sample2')
plt.legend()
plt.show()

```


![png](index_files/index_11_0.png)


## Simulating Type I and II errors

### Type I error
TYPE I error describes a situation where you reject the null hypothesis when it is actually true. This type of error is also known as a "false positive" or "false hit". The type 1 error rate is equal to the significance level α, so setting a higher confidence level (and therefore lower alpha) reduces the chances of getting a false positive.



### How alpha affects the prevalence of TYPE I errors.

Next, we shall see how alpha affects the rate of type 1 errors. 

> **Exercise:** Write a routine in Python to encapsulate the code shown above in order to repeat hypothesis tests on two randomly drawn distribution. The t-test will mostly fail to reject the null hypothesis, except, when by random chance you get a set of **extremely** different samples thus reject the null hypothesis (TYPE I ERROR). The frequency of such bad results depends upon the value of alpha. 

* Step 1: Create a population distribution (as shown above) 
* Step 2: Specify a number of hypothesis tests in numTests = 1000
* Step 3: Create a list of alpha values to explore (alpha_set) = [0.001, 0.01, 0.05, 0.1, 0.2, 0.5]
* Step 4: Create a pandas dataframe (sig_tests) to store 1000x5 = 5000 test results. 
* Step 5: Repeatedly take two random samples from population and run independant t-tests. 
* Step 6: Store P_value, alpha and a boolean variable to show whether null hypothesis was rejected or not (i.e. if p-value is less than alpha), for each of 5000 tests. 
* Step 7: Summarize/aggregate the results for presentation in a meaningful manner. 



```python
# Solution 

import pandas as pd

numTests = 100
alphaSet = [0.001, 0.01, 0.05, 0.1, 0.2, 0.5]
columns = ['err', 'p_val', 'alpha']
sigTests = pd.DataFrame(columns=columns)

# Create a population with mean=100 and sd=20 and size = 1000
pop = np.random.normal(100, 20, 1000)

# Create a counter for dataframe index values
counter = 1


```


```python
# Run the t-test on samples from distribution numTests x slphaSet times

for i in range(1,numTests+1):
    
    for alpha in alphaSet:

        # take two samples from the same population
            samp1 = np.random.choice(pop,100,replace=True)
            samp2 = np.random.choice(pop,100,replace=True)

            # test sample means
            result = stats.ttest_ind(samp1, samp2)

            # Evaluate whether Null hypothesis for TYPE I error
            if result[1] < alpha:
                 sigTests.loc[counter] = [1, result[1], alpha]
            else:
                 sigTests.loc[counter] = [0, result[1], alpha]

            counter += 1
```


```python
sigTests.head()
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
      <th>err</th>
      <th>p_val</th>
      <th>alpha</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0.0</td>
      <td>0.035702</td>
      <td>0.001</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.0</td>
      <td>0.415147</td>
      <td>0.010</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.0</td>
      <td>0.265434</td>
      <td>0.050</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0.0</td>
      <td>0.503467</td>
      <td>0.100</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0.0</td>
      <td>0.413219</td>
      <td>0.200</td>
    </tr>
  </tbody>
</table>
</div>



Now we have to summarize the results, this is done using pandas groupby() method which sums the “err” column for each level of alpha. The groupby method iterates over each value of alpha, selecting the type 1 error column for all rows with a specific level of alpha and then applies the sum function to the selection. 


```python
# group type 1 error by values of alpha
group_error = sigTests.groupby('alpha')['err'].sum()
group_error.plot.bar(title = "TYPE I ERROR - FALSE POSITIVES")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1864c686710>




![png](index_files/index_18_1.png)


Grouped data clearly shows that as value of alpha is increases from .001 to 0.5, the probability of TYPE I errors also increase.  

### Type II error 

This error describes a situation where you fail to reject the null hypothesis when it is actually false. Type II error is also known as a "false negative" or "miss". The higher your confidence level, the more likely you are to make a type II error.

## How alpha affects the prevalence of TYPE II errors.

> **Exercise** Write a code similar to above except samples should be taken from two different populations. introduce a new variable to represent the difference between two poulations. The hypothesis test should, in most cases, reject the Null hypothesis as samples belong to different populations, except, in extreme cases where there is no significant difference between samples i.e. a TYPE II error (False Negatives). Code should reflect how rate of false negatives is affected by alpha. 


```python
# Solution

numTests = 1000
diff = 10
ahpha_set =  [0.001, 0.01, 0.05, 0.1, 0.2, 0.5]
columns = ['err', 'p_val', 'alpha']
sigTests2 = pd.DataFrame(columns=columns)

counter = 1

for i in range(1,numTests+1):
    
    for alpha in alphaSet:

        # take two samples from different populations
            samp1 = np.random.normal(100, 20, 100)
            samp2 = np.random.normal(100+diff, 20, 100)

            # test sample means
            result = stats.ttest_ind(samp1, samp2)

            # Evaluate the Null hypothesis for TYPE II error (Note > as compared to < previously)
            if result[1] > alpha:
                 sigTests2.loc[counter] = [1, result[1], alpha]
            else:
                 sigTests2.loc[counter] = [0, result[1], alpha]

            counter += 1
```

Count of number of TYPE II errors according to alpha


```python
group_error2 = sigTests2.groupby('alpha')['err'].sum()

group_error2.plot.bar(title = "Type II ERROR - FALSE NEGATIVES")
```




    <matplotlib.axes._subplots.AxesSubplot at 0x1864c6ce7b8>




![png](index_files/index_24_1.png)


Grouped data clearly shows that as value of alpha is increases from .001 to 0.5, the probability of TYPE II errors decreases. 

### Why is an α level of 0.05 chosen as a cut-off for statistical significance?

The α level of 0.05 is considered the best balance to avoid excessive type I or type II errors. 


If we decide to use a large value for alpha : 

* Increases the chance of rejecting the null hypothesis
* The risk of a Type II error (false negative) is REDUCED
* Risk of a Type I error (false positive) is INCREASED

similarly, if we decide to use a very small value of alpha, it'll change the outcome as:
* Increases the chance of accepting the null hypothesis
* The risk of a Type I error (false positive) is REDUCED
* Risk of a Type II error (false negative) is INCREASED

From above, we can see that in statistical hypothesis testing, the more we try and avoid a Type I error (false positive), the more likely a Type II error (false negative) will occur. 

## Summary

The statistical key point here is that there is always a trade off between false positives and false negatives. By increasing alpha the number of false positives increases but the number of false negatives decreases as shown in bar graphs. The value of alpha=0.05 is considered a reasonable compromise between these two types of errors. Within the concept of “signifigance” there is embedded a trade-off between these two types of errors. 

> Think of “signifigance” as a compromise, between false positives and negatives, not as absolute determination.
