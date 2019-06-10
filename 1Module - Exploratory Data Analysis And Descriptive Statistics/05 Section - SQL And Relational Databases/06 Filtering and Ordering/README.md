
# Filtering and Ordering

## Introduction

In this lesson, we'll cover how to write SQL queries to retrieve and add specific data to SQL database tables.

## Objectives
You will be able to:
* Limit the number of records returned by a query using `LIMIT`
* Filter results using `BETWEEN` and `IS NULL`
* Order the results of your queries by using `ORDER BY` (`ASC` & `DESC`)


## What is a SQL Query?

The term "query" refers to any SQL statement that retrieves data from your database. In fact, we've already written a number of SQL queries using basic `SELECT` statements. We've already seen how to retrieve single units of data, or rows, with queries like these:

To select all of the rows from a `cats` table:

```sql
SELECT * FROM cats;
```

To select only rows representing data meeting certain conditions:

```sql
SELECT * FROM cats WHERE name = "Maru";
```

What if, however, we wanted to select the oldest cat? Or all of the cats that don't currently belong to an owner? Or all of the cats with short names?

Data storage isn't very useful if we can't manipulate, view, and analyze that data. Luckily for us, SQL is actually a powerful tool for doing just that.

In this exercise, we'll walk through executing a handful of common and handy SQL queries.

## Code Along: SQL Queries

### Creating our Database

In this code along, we'll be creating a `cats` table in a `pets_database.db`.

First let's create our `pets_database` by running the following commands.

```python
import sqlite3 
connection = sqlite3.connect('pets_database.db')
cursor = connection.cursor()
```


```python
# create database connection here
```

Good work. Now if we look at our file directory, a new file should have appeared called `pets_database.db`! This is the binary representation of the database. You can think of this like a .jpg file. It won't open up in a text editor, but it does open up in the image viewer app. It is the same way for .db files. They won't open in your editor, but they can be read by the appropriate database engine.

Now that we have a database and a cursor object that is connected to our database, let's create our `cats` table along with `id`, `name`, `age`, `breed`, and `owner_id` columns.

```python
cursor.execute('''CREATE TABLE cats ( id INTEGER PRIMARY KEY, name TEXT, age INTEGER, breed TEXT, owner_id INTEGER );''')
```


```python
# create table here
```

Let's add some cats to our `cats` table to make this more interesting:

```python
cursor.execute('''INSERT INTO cats (name, age, breed, owner_id) VALUES ("Maru", 3 , "Scottish Fold", 1);''')
cursor.execute('''INSERT INTO cats (name, age, breed, owner_id) VALUES ("Hana", 1 , "Tabby", 1);''')
cursor.execute('''INSERT INTO cats (name, age, breed) VALUES ("Lil\' Bub", 5, "American Shorthair");''')
cursor.execute('''INSERT INTO cats (name, age, breed) VALUES ("Moe", 10, "Tabby");''')
cursor.execute('''INSERT INTO cats (name, age, breed) VALUES ("Patches", 2, "Calico");''')
```


```python
# insert data here
```

Let's check out our `cats` table now:

```python
cursor.execute('''SELECT * FROM cats;''').fetchall()
```

> **Note:** the method `.fetchall()` returns a `list` where each record is represented as a `tuple`, which you can think of as a `list`-like object. If we would like to retrieve an element from a `tuple`, we simply access it by-index -- similar to how we access the elements of a normal Python list. (i.e. `example_tuple[0]` - returns element at index `0`)


```python
# select all data from cats data here
```

This should return:

```python
[(1, 'Maru', 3, 'Scottish Fold', 1),
 (2, 'Hana', 1, 'Tabby', 1),
 (3, "Lil' Bub", 5, 'American Shorthair', None),
 (4, 'Moe', 10, 'Tabby', None),
 (5, 'Patches', 2, 'Calico', None)]
```

### `ORDER BY`

The first query modifier we'll explore is `ORDER BY`. This modifier allows us to order the table rows returned by a certain `SELECT` statement. Here's a boilerplate `SELECT` statement that uses `ORDER BY`:

```python
cursor.execute('''SELECT column_name FROM table_name ORDER BY column_name ASC|DESC;''').fetchall()
```

Let's select our cats and order them by age:

```python
cursor.execute('''SELECT * FROM cats ORDER BY age;''').fetchall()
```


```python
# select all cats order by age here
```

This should return the following:

```python
[(2, 'Hana', 1, 'Tabby', 1),
 (5, 'Patches', 2, 'Calico', None),
 (1, 'Maru', 3, 'Scottish Fold', 1),
 (3, "Lil' Bub", 5, 'American Shorthair', None),
 (4, 'Moe', 10, 'Tabby', None)]             
```

When using `ORDER BY`, the default is to order in ascending order. If we want to specify though, we can use `ASC` for "ascending" or `DESC` for "descending." Let's try to select all of our cats and sort them by age in descending order.

```python
cursor.execute('''SELECT * FROM cats ORDER BY age DESC;''').fetchall()
```


```python
# select cats order by age descending here
```

This should return

```python
[(4, 'Moe', 10, 'Tabby', None),
 (3, "Lil' Bub", 5, 'American Shorthair', None),
 (1, 'Maru', 3, 'Scottish Fold', 1),
 (5, 'Patches', 2, 'Calico', None),
 (2, 'Hana', 1, 'Tabby', 1)]        
```

### `LIMIT`

What if we want the oldest cat? If we want to select extremes from a database table––for example, the employee with the highest paycheck or the patient with the most recent appointment––we can use `ORDER BY` in conjunction with `LIMIT`.

`LIMIT` is used to determine the number of records you want to return from a dataset. For example:

```sql
SELECT * FROM cats ORDER BY age DESC LIMIT 1;
```

> **Note:** When we would only like the first result (or one result as is the case in the example above) we can use the sqlite3 method `.fetchone()` which, instead of returning a list of results, returns the first result (or the record at index 0). We can use this in-place of or in conjunction with `LIMIT 1` in order to get back a single element.


```python
cursor.execute('''SELECT * FROM cats ORDER BY age DESC LIMIT 1;''').fetchone()
# OR
# cursor.execute('''SELECT * FROM cats ORDER BY age DESC;''').fetchone() # returns the same element as the above
```

This part of the statement: `SELECT * FROM cats ORDER BY age DESC` returns all of the cats in order from oldest to youngest. Setting a `LIMIT` of `1` returns just the first, i.e. oldest, cat on the list.

Execute the above statement and you should see:

```python
(4, 'Moe', 10, 'Tabby', None)            
```
Let's get the two oldest cats:

```sql
SELECT * FROM cats ORDER BY age DESC LIMIT 2;
```


```python
# select the two oldest cats here
```

Execute that statement and you should see:

```python
[(4, 'Moe', 10, 'Tabby', None), (3, "Lil' Bub", 5, 'American Shorthair', None)]          
```

### `BETWEEN`

As we've already established, being able to sort and select specific data sets is important. Continuing on with our example, let's say we urgently need to select all of the cats whose age is between 1 and 3. To create such a query, we can use `BETWEEN`. Here's an boilerplate `SELECT` statement using `BETWEEN`:

```sql
SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;
```

Let's try it out on our `cats` table:

```sql
SELECT name FROM cats WHERE age BETWEEN 1 AND 3;
```


```python
# find all records between ages 1 and three here
```

This should return:

```python
[('Maru',), ('Hana',), ('Patches',)]
```

### `NULL`

Let's say the administrator of our Pets Database has found a new cat. This kitty doesn't have a name yet, but should be added to our database right away. We can add data with missing values using the `NULL` keyword.

Let's insert our new cat into the database. Our abandoned kitty has a breed, but no name or age as of yet:

```sql
INSERT INTO cats (name, age, breed) VALUES (NULL, NULL, "Tabby");
```


```python
# insert new record here
# retrieve all records from the cat table here
```

Now, if we look at our `cats` data with `SELECT * FROM cats;`, we should see:

```python
[(1, 'Maru', 3, 'Scottish Fold', 1),
 (2, 'Hana', 1, 'Tabby', 1),
 (3, "Lil' Bub", 5, 'American Shorthair', None),
 (4, 'Moe', 10, 'Tabby', None),
 (5, 'Patches', 2, 'Calico', None),
 (6, None, None, 'Tabby', None)]                  
```

We can even select the mysterious, nameless kitty with the following query:

```sql
SELECT * FROM cats WHERE name IS NULL;
```


```python
# select cats where the name field is null here
```

This should return the following:

```python
[(6, None, None, 'Tabby', None)]
```

### `COUNT`

Now, we'll talk about a SQL aggregate function, `COUNT`.

**SQL aggregate functions** are SQL statements that retrieve minimum and maximum values from a column, sum values in a column, get the average of a column's values, or count a number of records that meet certain conditions. You can learn more about these SQL aggregators [here](http://www.sqlclauses.com/sql+aggregate+functions) and [here](http://zetcode.com/db/sqlite/select/).

For now, we'll just focus on `COUNT`. `COUNT` will count the number of records that meet certain condition. Here's a standard SQL query using `COUNT`:

```sql
 "SELECT COUNT([column name]) FROM [table name] WHERE [column name] = [value]"
```
Let's try it out and count the number of cats who have an `owner_id` of `1`:

```sql
SELECT COUNT(owner_id) FROM cats WHERE owner_id = 1;
```


```python
# retrieve the count of cats whose owner id = 1 here
```

This should return:

```python
(2,)
```

### `GROUP BY`

Lastly, we'll talk about the handy aggregate function `GROUP BY`. Like its name
suggests, it groups your results by a given column.

Let's take our table of cats

```bash
id          name        age         breed          owner_id  
----------  ----------  ----------  -------------  ----------
1           Maru        3           Scottish Fold  1         
2           Hana        1           Tabby          1         
3           Lil\' Bub   5           American Shor            
4           Moe         10          Tabby                    
5           Patches     2           Calico                   
6                                   Tabby                    
```

Here, we can see at a glance that there are three tabby cats and
one of every other breed — but what if we had a larger database
where we couldn't just tally up the number of cats *grouped by*
breed? That's where — you guessed it! — `GROUP BY` comes in handy.

``` sql
SELECT breed, COUNT(breed) FROM cats GROUP BY breed;
```


```python
# execute GROUP BY sql statement here
```

This should return

```python
[('American Shorthair', 1), ('Calico', 1), ('Scottish Fold', 1), ('Tabby', 3)]
```

GROUP BY is a great function for aggregating results into different
segments — you can even use it on multiple columns!

```sql
SELECT breed, owner_id, COUNT(breed) FROM cats GROUP BY breed, owner_id;
```


```python
# execute multiple column group by statement here
```

This should return:

```python
[('American Shorthair', None, 1),
 ('Calico', None, 1),
 ('Scottish Fold', 1, 1),
 ('Tabby', None, 2),
 ('Tabby', 1, 1)]
```

### Note on `SELECT`

We are now familiar with this syntax:

```sql
SELECT name FROM cats;
```

However, you may not know that this can be written like this as well:

```sql
SELECT cats.name FROM cats;
```

Both return:

```python
[('Maru',), ('Hana',), ("Lil' Bub",), ('Moe',), ('Patches',), (None,)] 
```

SQLite allows us to explicitly state the tableName.columnName we want to select. This is particularly useful when we want data from two different tables.

Imagine we have another table called `dogs` with a column for the dog names:

```sql
CREATE TABLE dogs (
	id INTEGER PRIMARY KEY,
	name TEXT
);
```

```sql
INSERT INTO dogs (name) VALUES ("Clifford");
```


If we want to get the names of all the dogs and cats, we can no longer run a query with just the column name.
`SELECT name FROM cats,dogs;` will return `Error: ambiguous column name: name`.

Instead, we must explicitly follow the tableName.columnName syntax.
```sql
SELECT cats.name, dogs.name FROM cats, dogs;
```

You may see this in the future. Don't let it trip you up.

<p class='util--hide'>View <a href='https://learn.co/lessons/sql-queries-basic-readme'>Basic SQL Queries</a> on Learn.co and start learning to code for free.</p>

## Summary

In this lesson, you expanded your SQL knowledge by learning how to modify your data using statements like `ORDER BY`. 
Additionally, you learned how to filter and limit your results.
