
# Class Variables and Instance Methods

## Introduction

In this lesson, we will introduce class variables and class methods. In Object Oriented Python, we use class variables to store information that relates to the class objects instead of each singular instance object. We use class methods to access and manipulate these pieces of information as well as any operations that are specific to the class level in lieu of the instance level. We will learn not only how to define and use class methods and variables, but also how to determine what information is relevant to a class as opposed to an instance.

## Objectives

You will be able to: 

* Understand class variables
* Understand class methods
* Access class variables with class methods
* Decide When to Use a Class Variable and a Class Method

## Understanding Class Variables

As with most new concepts in programming, it helps to start with some basic context. So, let's look at first what a class variable looks like.


```python
class Dog:
    
    _species = "canine"
    
print(Dog._species)
```

This example is very basic, but if we look at what we have here, it looks like a simple variable that we define inside of a class, but outside of any methods inside our class. We can also see that we can access this class variable the same way we would a variable on an instance object, although, we should probably adhere to similar design patterns that we use when we want to access an instance object's instance variables, right? Right! But we'll get to that in a bit. For now, just know that class variables are defined the same as regular variables in Python, with the notable exception that they are defined **inside** a class.

Now, before we move onto class methods, we need to take a deeper look at how instance objects can also access class variables -- say what?! 

Let's refactor our dog class a bit and take a look:


```python
class Dog:
    
    _species = "canine"
    
    def __init__(self, breed, name, age):
        self._breed = breed
        self._name = name        
        self._age = age        

new_dog = Dog("Airedale", "The Dude", "13")
print("1. ---", Dog._species, "--- This is a class object accessing its class variable")
print("2. ---", new_dog._species, "--- This is an *instance object* accessing its class's class variable")
```

Let's disect what's going on here. A class *obviously* has access direct to its class variable, that makes sense. However, the instance object seems to also have access to it. In fact, what is happening here is that the instance object is **trying** to access an instance variable called `_species`. However, when an instance object cannot find the requested instance variable, it then checks the class to see if there is a class variable that matches what was requested. So, when we request `_species` from the `new_dog` instance, it fails to find the instance variable, but since the class has a `_species` variable, that will be returned. 

If we have a `_species` instance variable, the instance variable will then simply return the instance object's instance variable.


```python
class Dog:
    
    _species = "canine"
    
    def __init__(self, species, breed, name, age):
        self._species = species
        self._breed = breed
        self._name = name        
        self._age = age        

new_dog = Dog("HI IM A CANINE", "Airedale", "The Dude", "13")
print("1. ---", Dog._species, "--- This is a class object accessing its class variable")
print("2. ---", new_dog._species, "--- This is an instance object accessing its **intstance** variable")
```

> **Note:** Although the class and instance variables in the example above have the same name, they are completely independent from one another. Changing the class variable will not change the instance variable and vice versa.

## Understanding Class Variables

Now that we are total experts on class variables let's look at class methods!


```python
class Dog:
    
    _species = "canine"
    
    @classmethod
    def species(cls):
        return cls._species

print("1. ---", Dog._species, "--- This is the dog class directly accessing its class variable")
print("2. ---", Dog.species(), "--- This is the dog class invoking the species *class method* to access its class variable")
```

Let's unpack the above code line by line. 

First, we see we still have the same class variable we started out with. Great, we understand that. Now, we see what looks like a pretty normal method called `species`, but there are two notable differences. Instead of using the `@property` decorator, which we use for instance methods, we are using the `@classmethod` decorator. Additionally, we see that the parameter in this method is `cls` (for class) instead of our usual `self`. So, what does this all mean? Let's start with the decorator, `@classmethod`. 

The `@classmethod` decorator tells our class that this method is bound to the class scope. This means that the `cls` parameter will always be the actual class object (i.e. `Dog`). It is important to note this because it is possible to call a class method on an instance object. So, in the above example, if we had an instance object `new_dog` and invokes the species method (i.e. `new_dog.species()`), the `cls` argument would **still** point to the **class** Dog.

The `cls` parameter is a bit more straightforward. Just as `self` is the convention for instance methods, `cls` is the convention for class methods. If both were `self`, it would be a bit confusing, so, we define the parameter as `cls` to indicate that the future argument will be the class object.

Let's look at an example to give more context around how this all works.


```python
class Dog:
    
    _species = "canine"
    
    def __init__(self):
        self._species = "I'm a dog INSTANCE"
    
    @classmethod
    def species(cls):
        return cls._species
    
    
new_dog = Dog()
print("1. ---", Dog._species, "--- This is the dog **class** directly accessing its class variable")
print("2. ---", new_dog._species, "--- This is an **instance object** of the dog class accessing its own instance variable")
print("3. ---", Dog.species(), "--- This is the dog class invoking the species *class method* to access its class variable")
print("4. ---", new_dog.species(), "--- This is an **instance object** of the dog class invoking the *class method*")
```

As we can see in the example above, even when we use an instance object to execute a class method, the method continues to be bound to and refer to the class, Dog. 


>**Note:** Although an instance object can call a class method, class objects will raise an argument error if they are invoked by a class object.

## Accessing Class Variables with Class Methods

As we already know, in Python we can always directly access our instance variables and instance objects. However, we want to introduce design pattern best practices in order to build a more scalable and secure, bug free program. To that effect, we will also adhere to these design patterns so that our class variables are protected and made 'private' just like our instance variables.

What does that look like? Well it's not much different from the way we treat our instance methods. So, if we want to change our class variables, we will define **class** methods for them which then perform the process(es) we would like. 

Before we get started, it is helpful to introduce a common pattern for creating class variables. If we think about a class churning out puppies like there is no tomorrow, how are we going to keep track of all those puppies? We can't make them all by hand and save them to individual variables. That would be a nightmare to keep track of and organized. But what if we could have a list where we keep all these dog instances? That way we would have a container for our instances and a convenient place to access them whenever we want to see all of our instance objects. Well, that is where a class variable would come in handy. Let's look at an example of this below:


```python
class Dog:
    
    _all = []
    
    def __init__(self, breed, name, age):
        self._breed = breed
        self._name = name        
        self._age = age  
    
    @classmethod
    def add_dog(cls, dog_instance):
        cls._all.append(dog_instance)
        return cls._all
    
biscuit = Dog("Airedale", "Biscuit", 12)
biscuit = Dog("Airedale", "Biscuit", 12)
biscuit = Dog("Airedale", "Biscuit", 12)
print("1. ---", Dog._all, "--- Checking the Dog class's class variale _all")
print("2. ---", Dog.add_dog(biscuit), "--- Using the add_dog class method to add a new dog instance to _all")
print("3. ---", Dog._all, "--- Checking the Dog class's class variale _all")
```

Alright, let's break down what is going on here. We have our class variable `_all` which points to an empty list, we have our init method that creates intance variables for our instance methods, and finally we have our class method `add_dog` that uses the `cls` argument to access our class variables `_all` and then appends the given dog instance object to the list. Now, when we want to add a dog instance to our collection of dogs in order to keep track of them, we simply need to use the `add_dog` method and pass in the new dog instance.

## Deciding When to Use a Class Variable and a Class Method

Deciding when to use a class variable or a class method may seem a bit contrived or not clear at the moment. So, let's see if we can define some guidelines for this decision process. 

When deciding anything in programming it is important to ask *`why am I making this decision?`*. If you can't supply a good reason, then it might not be the best decision. If you can, you know you're writing good code. In the case of deciding when to define a class variable or function you can make this question even more specific by asking yourself, *`is this information relevant to an instance object, or the class object?`*.

Let's think in terms of our `_all` variable. Is a collection of every instance object more relevant to the class itself or an individual instance of the class? Well, reasonable we can figure it is the the class that should be responsible for knowing all the instance objects it creates and an individual instance object shouldn't really need to know all the instances ever created for the class it belongs to. With that knowledge we can safely say that it is infact the class object that should have this `_all` variable, so, it would be a **class variable**. 

When we think about defining a class method, it follows similar logic. Is the responsibility of this method to operate on or return information for an instance object or a class object? If the method is meant to return a class variable or operate on a class variable, then it is definitely appropriate to define a class method. 

As long as there is a clear reasoning for a programming decision, we can feel confident when making decisions such as deciding whether we want to define a class method/variable or an instance method/variable.

## Summary

In this lab, we introduced class methods and variables. We first looked at how to define a class variable and how to define a class method. Once we were able to define these, we learned how to implement conventional design patterns that help us organize our classes so that it is easier to scale, and we are able to add a bit of security to our programs. We then moved on to deciding when and where to use class methods and variables by adhering to the general practice of always having a clear reason for making a decision to add to or change our code.
