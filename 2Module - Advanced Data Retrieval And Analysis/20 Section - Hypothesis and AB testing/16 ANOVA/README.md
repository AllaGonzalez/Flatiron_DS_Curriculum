
# ANOVA 

## Introduction

ANOVA (Analysis of Variance) is a method for generalizing of previous discussion regarding statistical tests to multiple groups. As we will see, ANOVA then partitions our total sum of square of deviations (from the mean) into sum of squares for each of these groups and sum of squares for error. 

## Objectives

You will be able to:
* Use ANOVA for testing multiple pairwise comparisons
* Understand and explain the methodology behind ANOVA tests


## Explanation of ANOVA

Again ANOVA generalizes our procedures to test differences, such as in the mean of populations, between multiple groups. We start with sample observations from multiple groups. Since ANOVA is looking to explain the total variance as combinations of variance from the various groups, we typically design a multiple groups experiment to test various independent factors that we hypothesis may influence the overall result. For example, in our A/B testing example of email templates, we could use ANOVA to simultaneously compare the effectiveness of various template changes. The control group could be our original template, and successive groups would have one specific change from that control template. The first group might have a new Subject line but an identical email. Another might have the original subject line but a new greeting within the body of the email. Successive groups would change a singular aspect of the original [control] template, but otherwise be identical. Once we have sample observations from each of these templates, we can then use ANOVA to analyze and compare their effectiveness.  

The general idea is to break the sum of square of deviations into multiple parts: the sum of squares of deviations of the mean of each of these test groups to the observations within the group itself, and the sum of squares of deviations of the mean of these test groups to the mean of all observations. 

Let's return to our example to illustrate this. ANOVA is looking to describe overall variation from all of our sample observations. The theoretical motivation is that we are looking to break the overall variation apart as a combination of the variation from each of these individual factors as well as unaccounted for error or chance. After all, it is unreasonable to account for all influencing factors. In our email example, we will expect response variation from the people themselves, and while we may break apart our participants into demographic groups, forming additional groups within our ANOVA test, there will continue to be variation within the groups themselves.   

After decomposing total variance as variance of the individual factors to their group mean (sum of square for treatments SST) and variance of these groups to the overall mean (sum of square for error SSE), we can compare these quantities using an f-distribution, which becomes our test statistic.

Higher values of the F-statistic indicate a higher probability of that factor being influential. As with other distributions, we can also quantify this in terms of a desired signifigance level $\alpha$. For example, if we desire to have a .05 significance level as before, we would be looking for f values such that:

$F>F_\alpha$

## Generating an ANOVA Table (AOV) in Python


```python
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
```

    /Users/lore.dirick/anaconda3/lib/python3.6/site-packages/statsmodels/compat/pandas.py:56: FutureWarning: The pandas.core.datetools module is deprecated and will be removed in a future version. Please use the pandas.tseries module instead.
      from pandas.core import datetools


## Loading the Data

As usual, we start by loading in a dataset of our sample observations. This particular table is of salaries in IT and has 4 columns:
* S - the individuals salary
* X - years of experience
* E - education level (1-Bachelors, 2-Masters, 3-PHD)
* M - management (0-no management, 1-yes management)


```python
df = pd.read_csv('IT_salaries.csv')
df.head()
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
      <th>S</th>
      <th>X</th>
      <th>E</th>
      <th>M</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>13876</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>11608</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>18701</td>
      <td>1</td>
      <td>3</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>11283</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11767</td>
      <td>1</td>
      <td>3</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



## Generating the ANOVA Table

In order to generate the ANOVA table, we will fit a model and then generate the table from this object. The syntax for defining the model is a little different then what we've seen previously.  Our formula will be written as:

```Control_Column ~ C(factor_col1) + factor_col2 + C(factor_col3) + ... + X```

** *We indicate categorical variables by wrapping them with ```C() ```**


```python
formula = 'S ~ C(E) + C(M) + X'
lm = ols(formula, df).fit()
table = sm.stats.anova_lm(lm, typ=2)
print(table)
```

                    sum_sq    df           F        PR(>F)
    C(E)      9.152624e+07   2.0   43.351589  7.672450e-11
    C(M)      5.075724e+08   1.0  480.825394  2.901444e-24
    X         3.380979e+08   1.0  320.281524  5.546313e-21
    Residual  4.328072e+07  41.0         NaN           NaN


## Reading the Table

For now we will simply focus on the outermost columns. On the left, you can see our various groups, and on the right, the probability that the factor is indeed influential. Values < .05 (or whatever we set $\alpha$ to) indicate rejection of the null hypothesis. In this case, we can see all three factors appear influential, with management being the potentially most significant, followed by years experience and finally, educational degree.

## Summary

In this lesson, we examined the ANOVA technique to generalize A/B testing methods to multiple groups and factors.
