
# Section Recap

## Introduction

This short lesson summarizes the topics we covered in section 11 and why they'll be important to you as a data scientist.

## Objectives
You will be able to:
* Understand and explain what was covered in this section
* Understand and explain why this section will help you become a data scientist

## Key Takeaways

Who knew that drawing a line (or a plane) of best fit could be so complicated?! In this section we spent a lot more time looking into the logistics of creating and testing an effective model. Key takeaways:
* It often makes sense to perform a multiple linear regression with multiple predictor variables for the target variable
* Once you start using multiple predictors, you need to ensure that multicolinearity is not an issue for the variables you picked
* With multiple predictors you may also need to perform feature scaling and nomralization to ensure a variable with large values doesn't have undue influence on your predictions
* When you have a categorical predictor variable, you'll either need to perform label encoding or create a new binary variable for each category using one-hot encoding
* Both Statsmodel and Scikit-learn have powerful built in methods for performing linear regressions
* Scikit-learn has some built in capabilities for feature selection to determine the most predictive features in your data set
* When performing modeling, it's always important to split your data into training and testing sets to validate that your model works well on "new" data
* k-fold cross validation is a great way to run multiple train-test splits on your data set to maximize the quality of your predictions for a given set of data 

