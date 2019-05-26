
# Querying With SQLAlchemy

## Introduction

In this lesson, we'll explore all the ways that we can use SQLAlchemy to query a database!

## Objectives

You will be able to:

* Write nested queries with SQLAlchemy
* Use SQLAlchemy to for tables with many-to-many relationships

## Connecting to A Database

Recall that we in order to connect to a database with SQLAlchemy, we need to create an `engine`, bind it to a new session with a `sessionmaker`, and then create a new `Session` object.

For example:

```python
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("sqlite:///some_database.sqlite", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
```

## Inspecting a Database

Once we've connected to a database with SQLAlchemy, we can easily inspect the database to learn things like:

* The tables included in the database
* The column names for each table

We do this by making use the of `inspect` module provided by SQLAlchemy.  We can create an inspector by using the `inspect` fuction and passing in our engine, and then making use of various methods from our `inspector` object to get the names of tables, or info on the tables themselves.

For example:

```python
from sqlalchemy import inspect

inspector = inspect(engine)

# Get names of tables in database
print(inspector.get_table_names())

# Get column names for a specific table
print(inspector.get_columns('Some_table'))
```

## Executing Raw SQL Statements

We can easily execute raw SQL statements by just passing them in as strings to the appropriate methods.  We do this by using our `engine` object to `.connect()` to the database, and then using this connection object to `.execute()` the SQL statements that we have written as a python string.

Note that this returns an object containing all the results, not just the raw results.  To get all the results, we can call the results object's `.fetchall()` method.  Note that the results only remain in the results object until `fetchall()` has been called exactly once. If you need it again, then you'll need to execute the query a second time!

For example:

```python
con = engine.connect()
rs = con.execute("SELECT * FROM Some_Table")

print(rs.fetchall())
```

## Incorporating Pandas DataFrames

The results returned from raw SQL queries are often pretty hard to read since they don't contain any structure.  However, we can fix this problem by creating a pandas DataFrame and passing in the data returned from `rs.fetchall()`!

For example:

```python
import pandas as pd
rs = con.execute("SELECT col1, col2 from Some_Table")
df = pd.DataFrame(rs.fetchall())
df.head()
```

Note that using this method will produce a DataFrame with the correct data in the correct columns, but the columns themselves will not be labled.  

The better way to incorporate pandas is to make use of the `pd.read_sql_query()` method.  When using this method, we pass in two parameters:

1. The SQL query we want to execute, in the form of a string
2. The `engine` object we created to connect to our database with SQLAlchemy

This has the benefit of grabbing the appropriate metadata from the table to label the DataFrame columns correctly. It also saves us a few extra lines of code!

Example:
```python
df = pd.read_sql_query("SELECT * FROM [group]", engine)
df.head()
```

**_NOTE:_** In the example above, notice that we have wrapped the table name, `'group'`, in square brackets.  This is because `'Group'` is a reserved keyword in SQL (remember, case doesn't matter). In order to specify that we are talking about a table with that name and not using the Keyword, we wrap the table name in square brackets.  

Note that we can make use of `pd.read_sql_query()` to execute any valid SQL statement, including JOINs.  Just write the query as if you would when working directly with a Relational Database Management System!

## Using SQLAlchemy `Session` Objects

Using raw SQL to work with a database is nice, but SQLAlchemy is more than just a way to connect to a database--it's an **_Object-Relational Mapper_**, which means that we can use it to map our Database tables directly to Python classes.  Once we've done this, we can think of each row as a unique object, and work with it in the same way. This makes things much easier for us if we need to incorporate our data into a program that makes use of the Object-Oriented paradigm. 

### Creating Mappings

All the extra functionality our ORM provides hinges on the idea that we have mappings created. When working with a new database, these are often created manually.  However, for data scientists, it is much more common to be tasked with working with data from a pre-existing database. Creating the mappings manually for each table in a professional database is tedious and not realistic--luckily, SQLAlchemy provides a way for us to create these mappings automatically!

To create mappings:

1. Import `MetaData`
1. Import `automap_base` from `sqlalchemy.ext.base`
1. Create a MetaData object
1. Use the MetaData object's `.reflect()` method, and pass in our `engine` as the only parameter.
1. Use `automap_base` and pass in our `metadata` for the `metadata` keyword.  This is typically stored in the `Base` variable.
1. Call `Base.prepare()`
1. Map each class to the corresponding class inside of `Base,classes`.

See the following code for an example:

```python
from sqlalchemy import MetaData
from sqlalchemy.ext.automap import automap_base

metadata = MetaData()

metadata.reflect(engine)

Base = automap_base(metadata=metadata)

Base.prepare()

Table1, Table2 = Base.classes.Table1, Base.classes.Table2
```

In the example above, we only created mappings for `Table1` and `Table2` to demonstrate the syntax.  It is important to note that if our database also contained other tables such as `Table3` and `Table4`, we would **not** be able to access them using the ORM functionality until we declare mappings for them, as we did for `Table1` and `Table2`.

### Using `session.query()`

One of the most handy tools that the SQLAlchmey ORM provides is the ability to use `session.query()` to query our database while still using object-oriented syntax.  Each result returned from `session.query()` gives us each instance packaged as an object. 

Example:

```python
for instance in session.query(Table1):
    print(instance.column1)
```

Note that in the example above, `Table1` as a Class, not a string. We can access any column in that table by accessing it as an attribute found on the objects returned by `session.query(Table1)`, which will all be `Table1` objects. 

### Mimicking SQL Functionality

Note that we can mimic SQL functionality such as `ORDER BY` by using the corresponding `.order_by()` method.  

```python
for instance in session.query(Table1).order_by(Table1.Id):
    # Do something...

```

You'll find that other method such as `group_by()` also exist. For a full list of the methods available, see the [documentation](https://docs.sqlalchemy.org/en/latest/orm/query.html)


### Implicit JOINs

One cool feature of using the ORM functionality to query our data is the ability to write clean and easy JOIN statements using the `.filter()` method to join two entities implicitly based on whatever criteria we set. 

Take this example from the SQLAlchemy documentation:

```python
for u, a in session.query(User, Address).\
                     filter(User.id==Address.user_id).\
                     filter(Address.email_address=='jack@google.com').\
                     all():
    print(u)
    print(a)
```

Note that there are many other cool things that SQLAlchemy can do, but they are outside the scope of this lesson. However, we highly encourage you to take a look at the SQLAlchemy documentation and follow some of the tutorials they've made available--SQLAlchemy has a learning curve, but it's very powerful once you know how to use it!
