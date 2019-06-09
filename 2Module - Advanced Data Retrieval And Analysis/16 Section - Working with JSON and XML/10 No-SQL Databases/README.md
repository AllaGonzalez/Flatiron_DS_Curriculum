
# No-SQL Databases

## Introduction
SQL, is by far the most common database language. It is known as a relational database and is organized into a series of tables, as we have seen. While less common, there are also a number of alternatives to SQL and relational databases. Some of the ones we'll discuss here include:
* MongoDB
* Cassandra
* Neo4j
* graphql
* Hadoop

## Objectives
You will be able to:
* Compare and contrast SQL and NoSQL databases, including their strengths and weaknesses
* Identify use cases where NoSQL may be more appropriate than SQL databases

## Relational Databases

As discussed, most databases are SQL databases, which is a type of relational database. Relational databases store data as tables which can be combined using keys between those tables.

### SQL 

There are many different SQL implementations including:
    * MySQL
    * PostgreSQL
    * SQLite
    * Oracle
    * Microsoft SQL Server
    * Microsoft Azure SQL

## Key - Value Databases

Key value databases, are one of the most simplistic database systems, simply storing data as key-value pairs, just like python dictionaries. The most common implementation is Redis.

### Redis
Initial release: 2009

Redis has been used by large companies including github and instagram. It is by far the most common key-value database.

## Document Model Databases

Document model databases are a subclass of key-value databases. The initial concept is of documents such as json or xml. The database stores these documents using key-value pairs. However, unlike key-value databases, document model databases have the additional ability to access information within these documents directly.

### MongoDB
Initial release: 2009


MongoDB is one of the most popular sql alternatives. It represents data very similar to the JSON format we have been investigating today. It also supports a distributed model where data can be stored across multiple computers.

## Wide Column Databases

Wide column databases can be thought of as tables where the data in each column can vary from row to row. 

### Cassandra
Initial release: 2008

Cassandra was initially developed internally at Facebook and was later released as an open source software, eventually being picked up and maintained by the Apache Foundation. It was developed for handling large amounts of data to be distrubted across multiple servers. It is notable for being particualrly reliable and not having a single failure point.

## Graph Databases

Graph databases expand upon the idea of document databases, adding in the concept of relations between documents. This makes certain operations and mappings such as connectivity of the graph of data very easy. However, individual data nodes may not be indexed which can mean that they are not directly accessible on their own but must be accessed via their relationship to more central objects.

### Neo4j
Initial release: 2007

Neo4j is probably the most popular graph database. It stores all its data as nodes, edges or attributes.

### GraphQL
Initial release: 2015

GraphQL was developed internally at Facebook and allows users to define specific data structures when requesting data from servers. 

## Choosing an Appropriate Database

There are many consideration when choosing a database including the size of the project, anticipated use cases, and development costs. One obvious and straightforward consideration is training and familiarity. This contributes to the popularity of SQL. Size and use cases are also incredibly imporatant considerations. For personal projects or small businesses, you may not even need a database and can perhaps simply use a csv or json file. As data grows, a database management system is often needed. Until scale continues to grow, any of these choices could meet needs. One of the biggest drawbacks of relational databases such as sql is that they don't scale well horizontally (such as adding columns). In such scenarios, some of the alternative models provide more computationally effective solutions at scale.

## Additional Resources 

Check out https://db-engines.com/en/ranking for a ranking of various databases as well as much more information about them!

## Summary
In this lesson we reviewed database systems, covering some of the most popular implementations of several types.
