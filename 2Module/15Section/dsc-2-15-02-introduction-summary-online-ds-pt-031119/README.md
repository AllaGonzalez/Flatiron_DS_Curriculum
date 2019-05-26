
# Introduction

## Introduction
This lesson summarizes the topics we'll be covering in section 15 and why they'll be important to you as a data scientist.

## Objectives
You will be able to:
* Understand and explain what is covered in this section
* Understand and explain why the section will help you to become a data scientist

## An Introduction to ORMs

In module 1 we learned about SQL (Structured Query Language) and relational databases. We also learned about OOP (Object Oriented Programming) - one of the most popular programming paradigms. Remember, OOP is an approach to programming where behavior (methods/functions) and state (variables) are composed into objects. Those objects ate often designed to model real world "things" like products, locations or people.

In this section, we're going to introduce Object Relational Mappers (ORMs) - libraries that make it easy for programers writing OO code to access and update information in a relational database without having to write a bunch of SQL by hand.

As a data scientist, you probably won't work with ORMs much yourselves. However, many of the databases that you pull information from will be populated by applications that use an ORM, so if you're trying to learn more about any issues with the quality of the data you are working with, you may well find yourself trawling through OO code with a bunch of ORM calls. In this section, you'll get practice writing OO Python code and exposure to the most popular ORM in the Python world - SQLAlchemy.

### Review of SQL(ite)

We kick off the section by doing a review of how to connect to a SQLite database and run queries against it. 

### Normalization

We then review relationship types and provide a little more information about database normalization and common "normal forms" you might come across.

### ERD Diagrams

Next, we take the time to imntroduce Entity Relationship Diagrams (ERDs) - the most common way for developers to document the schema (structure) of their databases - the tables and colums and their relationships.

### Introducing SQLAlchemy

After that, we introduce the concept of an ORM and provide you some hands on experience with using SQLAlchemy.

### Many:Many Relationships

We then have a lesson reminding us of the importance of join tables for storing information where there is a many:many relationship between tables.

### Querying using SQLAlchemy

We then provide some experience with querying a database using SQLAlchemy and storing the results in a Pandas data frame.

### Pulling it All Together

Finally, we ask you to read and underdtand an ERD diagram for the classic Microsoft Northwind Traders database and query from the database using SQLAlchemy to give you some more practice retrieving data using an ORM.


## Summary

In this section, you get to review working with SQL - the language that has historically unlocked the vast majority of data stored by most corporations. You also get practice writing OO Python code, and learn how to use the SQLAlchemy ORM for retrieving data efficiently into your application.

