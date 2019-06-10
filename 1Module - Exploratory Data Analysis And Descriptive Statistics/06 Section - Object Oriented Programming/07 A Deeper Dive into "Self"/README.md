
# A Deeper Dive into "self"

## Introduction
In this lesson, we are going to talk a little more about `self` in object oriented Python (OOP). We have seen a little bit about self when we learned about defining and calling instance methods. So far we know that `self` is always explicitly defined as our instance method's **first parameter**. We also know that instance methods implicitly use the instance object as the **first argument** when we call the method. By convention, we name this first parameter `self` since it is a reference to the object on which we are operating. Let's take a look at some code that uses `self`.

## Objectives

You will be able to:

* Use self
* Operate on self
* Use self to call instance methods

## Using `self`

In order to really understand self and how it's used, it is best to use an example. Let's use the example of a **Person** class. A class produces instance objects, and we know that objects are just pieces of code that bundle together attributes like descriptors and behaviors. A Person can have descriptors like `height`, `weight`, `age`, etc. and also have behaviors such as `saying_hello`, `eat_breakfast`, `talk_about_weather`, etc. 


```python
class Person():
    
    def say_hello(self):
        return "Hi, how are you?"
        
    def eat_breakfast(self):
        self.hungry = False
        return "Yum that was delish!"

gail = Person()
print("1.", vars(gail))
gail.name = "Gail"
gail.age = 29
gail.weight = 'None of your business!'
print("2.", gail.say_hello())
print("3.", gail.eat_breakfast())
print("4.", vars(gail))
```

    1. {}
    2. Hi, how are you?
    3. Yum that was delish!
    4. {'name': 'Gail', 'age': 29, 'weight': 'None of your business!', 'hungry': False}


Here we can seee that our person instance objects have two behaviors and we can add instance variables and assign values to them pretty easily. Note that we also can add instance variables to gail by using `self` inside our instance methods.

What if we wanted a method that introduces oneself? It would be similar to our `say_hello` method, but would probably at least include our name, right? Let's refactor our class to include a `introduce` method.


```python
class Person():
    
    def introduce(self):
        return "Hi, my name is Gail. It is a pleasure to meet you!"
    
    def say_hello(self):
        return "Hi, how are you?"
        
    def eat_breakfast(self):
        self.hungry = False
        return "Yum that was delish!"
        
gail = Person()
gail.name = "Gail"
the_snail = Person()
the_snail.name = "The Snail"
print("1. ", gail.introduce())
print("2. ", the_snail.introduce())
```

    1.  Hi, my name is Gail. It is a pleasure to meet you!
    2.  Hi, my name is Gail. It is a pleasure to meet you!


Uh oh! That's not quite right. We need our introduce method to be a bit more dynamic so that each Person instance object is able to introduce itself. This is where self comes in! `self`, after all, is the instance object we are asking to introduce it`self`. And since our instance method already has our instance object available, we can just interpolate our instance object's name attribute. 

Let's again refactor our class to make this change

## Operating on `self`


```python
class Person():
    
    def introduce(self):
        return f"Hi, my name is {self.name}. It is a pleasure to meet you!"
    
    def say_hello(self):
        return "Hi, how are you?"
        
    def eat_breakfast(self):
        self.hungry = False
        return "Yum that was delish!"
        
gail = Person()
gail.name = "Gail"
the_snail = Person()
the_snail.name = "the Snail"
print("1. ", gail.introduce())
print("2. ", the_snail.introduce())
```

    1.  Hi, my name is Gail. It is a pleasure to meet you!
    2.  Hi, my name is the Snail. It is a pleasure to meet you!


Great! See how the method is the same for both instance objects, but `self` is not the same. `self` always refers to the object which is being operated on. So, in the case of `gail`, the method returns the string with the `name` attribute of the instance object `gail`. 

Now let's think about some of our other behaviors that might be a bit more involved in order to make them dynamic. For example, everyone's favorite default conversation, the weather. It changes rapidly and seems to always be a choice topic for small talk. How would we create a method to introduce ourselves AND make a comment about the weather? Talk about a great way to start a friendship!

Let's see how we would do this with just a regular function:


```python
def say_hello_and_weather(instance_obj, weather_pattern):
    return f"Hi, my name is {instance_obj.name}! What wildly {weather_pattern} weather we're having, right?!"

say_hello_and_weather(the_snail, "overcast")
```




    "Hi, my name is the Snail! What wildly overcast weather we're having, right?!"



Alright, that is great but we want it as an instance method, right? So, let's go back to the drawing board with our Person class and see if we can get this awesome new greeting method figured out.


```python
class Person():

    def say_hello_and_weather(self, weather_pattern):
        # we are using self instead of instance_obj because we know self represents the instance object
        return f"Hi, my name is {self.name}! What wildly {weather_pattern} weather we're having, right?!"

the_snail = Person()
the_snail.name = "the Snail"
print("1. ", the_snail.say_hello_and_weather("humid"))
# notice that we are ONLY passing in the weather pattern argument
# instance methods **implicictly** pass in the instance object as the **first** argument
```

    1.  Hi, my name is the Snail! What wildly humid weather we're having, right?!


Awesome, we nailed it! Again, note that the only arguments we pass in are those that come after `self` when we define an instance method's parameters.

Now that we have figured out how to leverage self and even use instance methods with more than just `self` as an argument, let's look at how we can use self to operate on and modify an instance object.

Let's say it is `gail`'s birthday. Gail is 29 and she is turning 30. How do we make sure our instance object reflects that? Well, we can define an instance method that updates `gail`'s age


```python
class Person():

    def happy_birthday(self):
        self.age += 1
        return f"Happy Birthday to {self.name} (aka ME)! Can't believe I'm {self.age}?!"

the_snail = Person()
the_snail.name = "the Snail"
the_snail.age = 29
print("1. ", the_snail.age)
print("2. ", the_snail.happy_birthday())
print("3. ", the_snail.age)
```

    1.  29
    2.  Happy Birthday to the Snail (aka ME)! Can't believe I'm 30?!
    3.  30


Obviously, this method could be improved, but what is important to note is that not only can we use self to *read* attributes from the instance object, but we can also use self inside these methods to change the attributes of the instance object. 

Let's take this a step further and look at how we can call other methods using self. 

## Calling Instance Methods on `self`

Another very important behavior people have is eating. It is something that we all do and it helps prevent us from getting **hangry**, or angry because we're hungry.


```python
class Person():

    def eat_sandwhich(self):
        if (self.hungry):
            self.relieve_hunger()
            return "Wow, that really hit the spot! I am so full, but more importantly, I'm not hangry anymore!"
        else:
            return "Oh, I don't think I can eat another bite. Thank you, though!"
    
    def relieve_hunger(self):
        print("Hunger is being relieved")
        self.hungry = False

the_snail = Person()
the_snail.name = "the Snail"
the_snail.hungry = True
print("1. ", the_snail.hungry)
print("2. ", the_snail.eat_sandwhich())
print("3. ", the_snail.hungry)
print("4. ", the_snail.eat_sandwhich())
```

    1.  True
    Hunger is being relieved
    2.  Wow, that really hit the spot! I am so full, but more importantly, I'm not hangry anymore!
    3.  False
    4.  Oh, I don't think I can eat another bite. Thank you, though!


Awesome! We see that not only are we changing attributes of our instance object, we are also using `self` to call other instance methods, like we would do with the instance object outside of a function. 

## Summary

In this lesson, we examined how we use `self` in OOP. We first reviewed using `self` to define our instance methods appropriately. Next we looked at how we can operated on `self` and leverage it in order to make our instance methods a bit more re-usable and dynamic for each of our instance objects by interpolating our instance object's `name` attribute. We also looked at using more than just `self` as an argument in our methods and using self to change the attributes on an isntance object. Finally, we introduced using self to call other instance methods.
