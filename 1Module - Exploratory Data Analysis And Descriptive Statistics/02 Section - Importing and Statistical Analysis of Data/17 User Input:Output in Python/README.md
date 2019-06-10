
# User Input and Output in Python

### Objectives 

* Get User input as strings and numbers, process the data and output the results

### User input in Python

To get user input in Python, the command you use is `input()`. You can store the result in a variable, and use it to your heart’s content. Remember that the result you get from the user will be a string, even if they enter a number.

For example, run the following cell:


```python
name = input("Give me your name: ")
print("Your name is " + name)
```

    Give me your name: Trump
    Your name is Trump


What happens at the end of `input(`) is that it waits for the user to type something and press ENTER. Only after the user presses ENTER does the program continue.

### Manipulating strings (a few ways)

What you get from the `input()` function is a string. What can you do with it?

First: Make the string into a number. Let’s say you are 100% positive that the user entered a number. You can turn the string into an integer with the function `int()`. (Later we will see what to do when the user does NOT enter a number and you try to do this, for now don’t worry about that problem). 

Here is what this looks like:


```python
age = input("Enter your age: ")
age = int(age)
print ("You are", age , "years old" )
```

    Enter your age: 30
    You are 30 years old


Unlike using `+` for string concatenation as seen earlier, we simply use a `,` for joining strings with numbers. You can also convert a `int` to `str` and use concatenation normally. e.g.


```python
print ("You are " + str(age) + " years old")
```

    You are 30 years old


### Example: 
Let's create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.


```python
name = input("What is your name: ")
age = int(input("How old are you: "))
year = str((2018 - age)+100)
print(name + " will be 100 years old in the year " + year)
```

    What is your name: Billy
    How old are you: 42
    Billy will be 100 years old in the year 2076


### Summary

This lesson introduced you to character input / output and string manipulation. We also saw how we can take user input, do some basic processing and provide feedback to user, based on the input. In following lessons, we will see how to make output conditional to user input i.e. different processing and output messages based on input.   
