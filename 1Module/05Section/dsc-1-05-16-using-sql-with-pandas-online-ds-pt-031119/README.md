
# Using SQL with Pandas

## Introduction

Consider the structure of a **_Pandas DataFrame_**.  

<img src="df_example.png">


Now, let's consider the structure of a table from a **_SQL database_**.


<img src="sql_example.png">

You've probably noticed by now that they're essentially the same--a table of values, with each row having a unique index and each column having a unique name.  This allows us to quickly and easily access information when using SQL.  In this section, we'll learn how we can use SQL-style queries to query pandas DataFrames!

## Objectives
You will be able to:
- Understand the basic syntax for querying pandas DataFrames with SQL statements
- Understand and explain how Pandas can be used to work directly with .sql files
- Reference the pandasql package documentation as needed


## Using `.query()`

Pandas DataFrames come with a built in query method, which allows us to get information from DataFrames quickly without using the cumbersome slicing syntax.  

See the following examples:

```python
# Getting Data using slicing syntax
foo_df = bar_df[bar_df[bar_df['Col_1'] > bar_df['Col_2']]]

# Using The query method
foo_df = bar_df.query("Col_1 > Col_2")

# These two lines are equivalent!
```

Note that if we want to use `and` and `or` statements with the `.query()` method, we'll need to use `"&"` and `"|"` instead.

```python
foo_df = bar_df.query("Col_1 > Col_2 & Col_2 <= Col_3")
```

## Using SQL syntax with `pandasql`

Since SQL is such a powerful, comfortable tool for Data Scientists, some people had the bright idea of creating a library that lets users query DataFrames using SQL-style syntax.  This library is called [pandasql](https://pypi.org/project/pandasql/).

We can install `pandasql` using the bash comman `pip install pandasql`.

### Importing pandasql

In order to use `pandasql`, we need to start by importing a `sqldf` object from `pandasql`

```python
from pandasql import sqldf
```

Next, we'll write a lambda function that will make it quicker and easier to write queries.  Normally, we would have to pass in the global variables every time we use an object.  In order to avoid doing this every time, we'll write a lambda that does this for us. 

```python
pysqldf = lambda q: sqldf(q, globals())
```

Now, when we pass a query into `pysqldf`, the lambda will also pass along the globals for us, saving us that repetitive task. 

### Writing Queries

To write a query, we just format it as a multi-line string!

```python
q = """SELECT
        m.date, m.beef, b.births
     FROM
        meats m
     INNER JOIN
        births b
           ON m.date = b.date;"""
```

In order to query DataFrames, we can just pass in the query string we've created to our `sqldf` object that we stored in `pysqldf`.  This will return a DataFrame.  

```python
results = pysqldf(q)
```

## Summary

These advanced methods for querying DataFrames can make your life a lot easier by simplifying the syntax and allowing us to make use of SQL--use them to save yourself time and give keep your SQL skills strong!
