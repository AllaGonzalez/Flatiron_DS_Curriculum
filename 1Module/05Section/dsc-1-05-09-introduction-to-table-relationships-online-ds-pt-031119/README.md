
# Introduction to Table Relationships

## Introduction

In this lesson, we'll relate data from one table to data from another table using foreign keys. 

## Objectives
You will be able to:
* Understand the benefits of using related tables in SQL databases

## Why Relate Tables?

It's hard to imagine an application that saves data but doesn't relate it. For example––a Facebook user is associated to other users via "friendships", an Amazon user has a shopping cart full of items, a blog's author has many posts and posts might in turn have many tags. All of these examples require different datasets to be related or associated to one another. 

## Relating Tables with Foreign Keys

Continuing the posts and authors examples, you could say that an author *has many* posts. The reciprocal of this would be that a post *belongs to* an author. Now we need to figure out how we can represent that relationship within the constraints of SQLite. If you were writing just plain Python, how would you represent this relationship? Well we could have some dictionaries; one for an Author with the author's name, email, etc. and a key for `posts` which points to a list of dictionaries that contain all the information for a particular post (i.e. `title`, `content`, `date_written`, `author`, etc.) This is an okay way to model the relationship, but there is no data type for lists in SQL. You can only have `INTEGER`, `FLOAT`, and `TEXT`. So developers had to figure out how to relate two rows or records (a `Post` and an `Author`) using only those data types. Is there any way we can convert an `INTEGER` into a specific row in a table? OH YEAH. The `id` column or `PRIMARY KEY` for each row is a unique `INTEGER` identifier for that row. Let's say the Post "10 Ways to Pet Your Cat" is written by "Joe Burgess", and Joe's `id` is 5. We just need to add a new column to our Posts table with the `id` of the Author that it's related to. Let's call this column `author_id`.

Why didn't we do the reverse? Why didn't we add a list of Post IDs to a single Author row? The answer is pretty straight forward. Is there an list data type? Is there really any way to store multiple items in a single column? Nope! So we just set up the relation in one direction.

This `author_id` column is called a **foreign key**.

To associate one table to another, give one table a column called `foreign key` with a type of `INTEGER` and insert the primary key of another table row into that column. In other words, if we have a blogging app, we might have a users table and a posts table. Posts belong to the user that wrote that post. So, the posts table would have a foreign key column. An individual post's foreign key value would be the primary key ID of the user who authored that post. 

This is a little confusing, so let's build out our own example together. 

### Code Along I: Relating Cats to Owners

Let's say we are creating an app that helps a veterinary office manage the pets it sees as patients and the owners of those pets. Let's say this vet is very particular and specializes in cats. Our app will have a database that has a `cats` table and an `owners` table. We will need a way to relate, or connect, these two tables such that a given cat is associated to its owner and a given owner is associated to the cat (or cats) it owns.

For this exercise, we'll be working with a `pets_database`. In your notebook, create the database with the following commands:
```python
import sqlite3
connection = sqlite3.connect('pets_database.db')
cursor = connection.cursor()
```


```python
# create db, connection, and cursor here
```

Let's set up our two tables now. 

#### Step 1: Creating the Cats Table

Create the table with the following SQL statement:

```sql
CREATE TABLE cats ( id INTEGER PRIMARY KEY, name TEXT, age INTEGER, breed TEXT);
```


```python
# create table here
```

Now, go ahead and insert the following cats into the table:

```sql
INSERT INTO cats (name, age, breed) VALUES ("Maru", 3, "Scottish Fold");

INSERT INTO cats (name, age, breed) VALUES ("Hana", 1, "Tabby");
```


```python
# insert data here
```

#### Step 2: Creating the Owners Table

First, we need to create our owners table. An owner should have an ID that is a primary key integer and a name that is text: 

```sql
CREATE TABLE owners (id INTEGER PRIMARY KEY, name TEXT);
```


```python
# create owners table here
```

Now that we have our owners table, we can add a foreign key column to the pets table. 


```python
cursor.execute('''CREATE TABLE owners (id INTEGER PRIMARY KEY, name TEXT);''')
```

#### Step 3: Add Foreign Key to Cats Table

Use the following statement to add this column: 

```sql
ALTER TABLE cats ADD COLUMN owner_id INTEGER;
```


```python
# alter table here
```

To check your cats table schema when there are multiple tables, we can execute the following SQL statement: `SELECT * FROM sqlite_master WHERE name="cats"`. This will return only the table in the database that has the name `cats`.

```python
[('table',
  'cats',
  'cats',
  2,
  'CREATE TABLE cats ( id INTEGER PRIMARY KEY, name TEXT, age INTEGER, breed TEXT)')]
```

Great, now we're ready to associate cats to their owners by creating an owner and assigning that owner's ID to certain cats' `owner_id` column.

 #### Step 4: Associating Cats to Owners

First, let's make a new owner: 

```sql
INSERT INTO owners (name) VALUES ("mugumogu");
```


```python
# insert new owner record here
```

Check that we did that correctly with the following statement: 

```sql
SELECT * FROM owners;
```


```python
# check new owner record here
```

You should see the following: 


```sql
[(1, 'mugumogu')]
```

Mugumogu is the owner of both Hana and Maru. Let's create our associations: 

```sql
UPDATE cats SET owner_id = 1 WHERE name = "Maru";
UPDATE cats SET owner_id = 1 WHERE name = "Hana";
```

Let's check out our updated `cats` table: 

```sql
SELECT * FROM cats WHERE owner_id = 1;
```


```python
# check updated cats table here
```

This should return:

```sql
[(1, 'Maru', 3, 'Scottish Fold', 1), (2, 'Hana', 1, 'Tabby', 1)]
```

### Establishing Foreign Key: Determining Which Table Gets a "foreign key" Column

Why did we decide to give our `cats` table the foreign key column and not the `owners` table? Similarly, in the example from the beginning of this exercise, why would we give a `posts` table a foreign key of `user_id` and not the other way around? 

Let's look at what would happen if we tried to add cats directly to the `owners` table.

Adding the first cat, "Maru", to the owner "mugumogu" would look something like this: 

| id | name | cat_id|
|----|------|-------|
| 1  | mugumogu | 1 |

So far so good. But what happens when we need to add a second cat, "Hana", to the same owner?

| id | name | cat_id1| cat_id2 |
|----|------|-------|----------|
| 1  | mugumogu | 1 | 2        |

What if this owner gets *yet another cat?* We'd have to keep growing our table horizontally, potentially forever. That is not efficient, or organized. 

We can also think about the relationship between our owners and our cats in the context of a "has many" and "belongs to" relationship. An owner can have many cats, but –– at least for the purposes of this example –– a cat can only belong to one owner. Similarly, a user can write many posts, but each post was written by, and therefore belongs to, only one user.

The thing that "has many" is considered to be the parent. The thing that "belongs to" we'll call the child. The child table gets the foreign key column, the value of which is the primary key of that data's/row's parent. 

Practice SQL Queries on <a href="http://sqlbolt.com/lesson/select_queries_review">SQLBolt</a>.

## Summary

Great job! You now understand the benefits of using related tables in SQL databases, and how to establish a foreign key.
