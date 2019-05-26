
# Interpreting Significance and P-values 

## Introduction

In this lesson, we shall build on some of the ideas mentioned during significance testing with z-scores. Such an approach can help us associate a confidence level to our model's output which could be very important during decision making. 

## Objectives

You will be able to:

* Interpret the p-value and regression coefficients
* Describe model suitability in terms of obtained significance results


## Let's get started

We can apply the the ideas of hypothesis testing in a regression context as well as statistical inference. The general approach of hypothesis testing remains the same i.e. We develop a set of hypotheses including null hypothesis and alternative hypothesis. The way we conduct these tests is that we try to reject the null hypothesis with an associated alpha level as a threshold for calling our results significant , or otherwise. We set some statistic according to the nature of underlying data and analytical question and check the significance of our results. 

## Hypothesis Testing in Regression 

During regression, we try to measure the model parameters (coefficients ) so our null and alternative hypotheses must also get set up in those terms. Think about the simple regression experiment that we conducted on the advertising dataset. For a simple dataset like this, we can set up our hypotheses as follows:

> **NULL HYPOTHESIS (Ho): There is no relationship between amount spent on TV advertisement and sales figures.**

For our null hypothesis to be true, In y= mx+c , m has to be zero so y is simply equal to the intercept. 

> **ALTERNATIVE HYPOTHESIS (Ha): There is "some" relation between amount spent on TV advertisement and sales figures.**

So for above, rejecting the null hypothesis would help us associate some significance with our results

Just like for statistical significance, we reject the null (and thus believe the alternative) if the 95% confidence interval does not include zero for co-efficient. In other terms 

#### the p-value represents the probability that the coefficient is actually zero. 

Let's import the code from our previous lesson and see if we can check for this p value. 



```python
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import scipy.stats as stats
plt.style.use('fivethirtyeight')

data = pd.read_csv('Advertising.csv', index_col=0)
f = 'sales~TV'
f2 = 'sales~radio'
model = smf.ols(formula=f, data=data).fit()
model2 = smf.ols(formula=f2, data=data).fit()

```

We can now check for the p-value associated with intercept as below.


```python
model.pvalues
```




    Intercept    1.406300e-35
    TV           1.467390e-42
    dtype: float64



Note that we generally ignore the p-value for the intercept. 

#### Interpreting results

Here is how you would interpret this output

>If the 95% confidence interval includes zero, the p-value for that coefficient will be greater than 0.05. If the 95% confidence interval does not include zero, the p-value will be less than 0.05. Thus, a p-value less than 0.05 is one way to decide whether there is likely a relationship between the feature and the response. 

Again, using 0.05 as the cutoff is just a convention.

In this case, the p-value for TV is far less than 0.05, and so we believe that there is a relationship between TV ads and Sales. With alpha set to 0.05, we can claim to have 95% confidence on the outcome.  
Try running above and check for p values for `radio` and see how would interpret the outcome. 

## Additional Resources

You are encouraged to visit following links to see more examples and explanations around:hypothesis testing in regression 

[Hypothesis Test for Regression Slope](https://stattrek.com/regression/slope-test.aspx)

[Regression Continued](http://www.stat.ucla.edu/~cochran/stat10/winter/lectures/lect18.html)

## Summary 

In this lesson, we saw how to apply the ideas of hypothesis testing in regression analysis to associate significance and confidence level with our model. We used this with our previous regression model to check the association. In the next lab, we shall combine all the ideas around simple linear regression with ols on a slightly more complex dataset with a much greater number of features. 
