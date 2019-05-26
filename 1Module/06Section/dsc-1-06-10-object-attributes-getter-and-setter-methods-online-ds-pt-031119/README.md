
# Object Attributes - Setter and Getter Methods

## Introduction
We have now covered Python classes, instance objects, instance methods, and instance variables. Now that we know what these things are and how they work together, we need to think about how we *want* these parts of our program to work together. Said another way, we need to think about making our programs a bit more secure and prevent users from making unwanted changes or creating bad data. To that effect, we will want to use design patterns for creating private instance variables or defining instance methods that provide ways to update instance variables indirectly. These methods are called setters and getters, because they both read and write (get and set) the private instance variable information we would like to access. Let's get started!

## Objectives

You will be able to: 

* Create private instance variables
* Understand setter and getter methods
* Understand properties

## Private Instance Variables
Let's take the example of a bank account. Now, when we think about (or try not to think about) going to the bank and opening an account, terms, fees, and regulations all come to mind. You have to have a minimum balance to open your account, you need to maintain a certain balance, you cannot overdraft your account without incurring a fee, etc. All of those things, current balance, balance minimum, max withdrawal amount, over draft fees can call be thought about as attributes of a bank account. If you know of a bank that doesn't have these *attributes*, **please** let the rest of us know.

Let's build out an OO bank acount for our example to introduce getters, setters, and private variables.


```python
class BankAccount():
    pass


new_account = BankAccount()

new_account.balance = 1000
new_account.minimum_balance = 250
new_account.max_withdrawal = 150
        
print (vars(new_account))
```

    {'balance': 1000, 'minimum_balance': 250, 'max_withdrawal': 150}


We have a new bank account and it's already burning a whole in our digital pockets... So, let's take some money out and go on a shopping spree!

Uh oh! We just bought a pair of new selvedge denim jeans and bought a round of drinks for our coworkers at a happy hour (cause, why not?), and on top of that we took out some cash to lend to our friend for lunch because they forgot their wallet, but our friend also went to Eleven Madison Park for lunch.


```python
# new jeans purchase
new_account.balance -= 250
# take out cash to fund friends fancy lunch 
new_account.balance -= 250
# round of drinks for your whole team
new_account.balance -= 350
print(vars(new_account))
```

    {'balance': 150, 'minimum_balance': 250, 'max_withdrawal': 150}


Alright, woah. First of all, we need to get our spending under control. Second, we broke all the terms and regulations of our new bank account... So, that's not good. Perhaps if our bank acoount's program was a bit more secure we wouldn't be down $750.

Let's see if we can refactor our BankAccount class to try and enforce the regulations.

First, we don't really want anyone to be able to directly manipulate these attributes. We probably want to create methods that do these actions for us. That way, we are preventing someone from accidentally (or purposefully) breaking a regulation our bank has set for us, and we can use our functions to check if the action we are doing is allowed or not. 

First, we should make it so that accessing these attributes like the account `balance` isn't so straightforward by using **private** instance variables. Private instance variables are declared by prepending an underscore `_` (i.e. `_balance`).

Note that the underscore only **indicates** that the instance variable is private. It does **not** change our ability to access or change its value. However, we can now safely define an instance method with the name of our intended attribute (i.e. `def balance(self):`) and it will not conflict or be confused with the instance variable `balance`.


```python
class BankAccount():
    pass


new_account = BankAccount()

new_account._balance = 1000 # now indicated to be a *private* instance variable 
new_account._minimum_balance = 250 # now indicated to be a *private* instance variable
new_account._max_withdrawal = 150 # now indicated to be a *private* instance variable
        
print (vars(new_account))
```

    {'_balance': 1000, '_minimum_balance': 250, '_max_withdrawal': 150}


Great! We have our instance variables set up so that we are indicating that they are *private* and therefore should not be accessed directly by a user or another program. Instead, to update these attributes we'll need intance methods called **setters and getters**.

## Setter and Getter Methods

Setter and getter methods are instance methods that control the access (getter) of instance variables and the changing (setter) of instance variables. Like we said earlier, we will have programs where we want to guard against unintended behavior, bad data, etc. (i.e. withdrawing too much money from our bank).

To reinforce the private nature of our instance variables as well as create ways to make our program more dynamic and well structured, we implement these setter and getter methods. Remember, anything that **changes** an instance variable is a **setter** method. Anything that **only accesses** an instance variable is a **getter** method. Take a look at the example below:


```python
class BankAccount():
    
    def set_balance(self, amount):
        self._balance += amount
    
    def get_balance(self):
        return self._balance
        
    def make_withdrawal(self, amount_requested):
        if (self.check_min_bal(amount_requested)):
            return self.check_min_bal(amount_requested)
        if (self.check_max_withdrawal(amount_requested)):
            return self.check_max_withdrawal(amount_requested)
        else: 
            self.set_balance(-amount_requested)
            return f"${amount_requested}"
            
    def check_min_bal(self, amount_requested):
        if ((self.get_balance() - amount_requested) > self._minimum_balance):
            return False
        else:
            return f"Sorry, you do not have enough funds to withdrawal ${amount_requested} and maintain your minimum balance of ${self._minimum_balance}"
    
    def check_max_withdrawal(self, amount_requested):
        if (self._max_withdrawal > amount_requested):
            return False
        else:
            return f"Sorry, your maximum withdraw amount is {self._max_withdrawal}"
        
    def make_deposit(self, amount_to_deposit):
        try: 
            (float(amount_to_deposit))
            self.set_balance((float(amount_to_deposit)))
            return f"Thank you for the deposit of ${amount_to_deposit}. Your balance is now: ${self._balance}"
        except:
            return f"{amount_to_deposit} is not a number"

# just a regular function that makes an account and initializes its properties... what a good idea
def make_account():
    new_account = BankAccount()
    new_account._balance = 0
    new_account._minimum_balance = 250
    new_account._max_withdrawal = 150 
    return new_account

account_two = make_account()
print("1.", account_two.get_balance())
print("2.", account_two.set_balance(1000)) # returns None since assignment returns None
print("3.", account_two.get_balance())
print("4.", account_two.make_withdrawal(1000))
print("5.", account_two.make_withdrawal(100))
print("6.", account_two.make_withdrawal(300))
print("7.", account_two.make_deposit(250))
print("8.", account_two.make_deposit(2.50))
print("9.", account_two.make_deposit("hello"))
print("10.", vars(account_two))
```

    1. 0
    2. None
    3. 1000
    4. Sorry, you do not have enough funds to withdrawal $1000 and maintain your minimum balance of $250
    5. $100
    6. Sorry, your maximum withdraw amount is 150
    7. Thank you for the deposit of $250. Your balance is now: $1150.0
    8. Thank you for the deposit of $2.5. Your balance is now: $1152.5
    9. hello is not a number
    10. {'_balance': 1152.5, '_minimum_balance': 250, '_max_withdrawal': 150}


Okay, so, we now have methods that allow us to change our account balance without having to access the account balance directly. On top of that, we have other instance methods that are preventing someone from making an unwanted or an unallowed action. Note that with our refactored class, we have changed our instance varaibles to have a leading `_` to signify that the variable is **private**.

With the `make_withrawal` instance method, we are making sure that any amount requested ensures that our minimum account balance is maintained and that we do not exceed our maximum withdrawal allowance. Our `make_deposit` instance method is checking to see if the input is in fact a number before making the deposit. If we don't make sure our input is a number, we leave ourselves vulnerable to errors, and errors are no good. 

Let's now look at our getter and setter methods, `get_balance` and `set_balance`. Notice that our fucntions that make deposits and make witdrawals are calling the setter and getter methods now instead of accessing the instance variables directly. In fact, the only methods that accesses the instance variables directly are the setter and getter methods, `set_balance` and `get_balance`. 

# Properties
Now that we have our private instance variables and setter and getter methods, we should think about whether it is better to have a method called `get_balance` or a method called just `balance`? What about `set_balance`? It would be way easier if we could just have one method to call for both the set and get operations. After all, they are both just changing the balance and naming these functions another way can make it hard to implement a convention. This is where **property()** comes into play. Before we dig too much into what property is, let's look at how it works in the example below:


```python
class BankAccount():
    
    def set_balance(self, amount):
        print("SETTING BALANCE")
        self._balance += amount
    
    def get_balance(self):
        print("GETTING BALANCE")
        return self._balance
        
    def make_withdrawal(self, amount_requested):
        if (self.check_min_bal(amount_requested)):
            return self.check_min_bal(amount_requested)
        if (self.check_max_withdrawal(amount_requested)):
            return self.check_max_withdrawal(amount_requested)
        else: 
# ----------- NOTE THE CHANGE FROM self.set_balance(amount) TO self.balance = amount --------------- #
            self.balance = -amount_requested
            return f"${amount_requested}"
            
    def check_min_bal(self, amount_requested):
# ----------- NOTE THE CHANGE FROM self.get_balance() TO self.balance = --------------- #
        if ((self.balance - amount_requested) > self._minimum_balance): 
            return False
        else:
            return f"Sorry, you do not have enough funds to withdrawal ${amount_requested} and maintain your minimum balance of ${self._minimum_balance}"
    
    def check_max_withdrawal(self, amount_requested):
        if (self._max_withdrawal > amount_requested):
            return False
        else:
            return f"Sorry, your maximum withdraw amount is {self._max_withdrawal}"
        
    def make_deposit(self, amount_to_deposit):
        try: 
            (float(amount_to_deposit))
# ----------- NOTE THE CHANGE FROM self.set_balance(amount) TO self.balance = amount --------------- #
            self.balance = float(amount_to_deposit)
            return f"Thank you for the deposit of ${amount_to_deposit}. Your balance is now: ${self._balance}"
        except:
            return f"{amount_to_deposit} is not a number"
    
# ----------- HERE is where we are using the property() function ----------------------------------- #
    balance = property(get_balance, set_balance)

    
    
# just a non-class function that makes an account and initializes its properties... what a good idea
def make_account():
    new_account = BankAccount()
    new_account._balance = 0
    new_account._minimum_balance = 250
    new_account._max_withdrawal = 150 
    return new_account

account_three = make_account()
print("1.", account_three.get_balance())
print("2.", account_three.set_balance(1000)) # returns None since assignment returns None
print("3.", account_three.get_balance())
print("4.", account_three.make_withdrawal(1000))
print("5.", account_three.make_withdrawal(100))
print("6.", account_three.make_withdrawal(300))
print("7.", account_three.make_deposit(250))
print("8.", account_three.make_deposit(2.50))
print("9.", account_three.make_deposit("hello"))
print("10.", vars(account_three))
```

    GETTING BALANCE
    1. 0
    SETTING BALANCE
    2. None
    GETTING BALANCE
    3. 1000
    GETTING BALANCE
    GETTING BALANCE
    4. Sorry, you do not have enough funds to withdrawal $1000 and maintain your minimum balance of $250
    GETTING BALANCE
    SETTING BALANCE
    5. $100
    GETTING BALANCE
    6. Sorry, your maximum withdraw amount is 150
    SETTING BALANCE
    7. Thank you for the deposit of $250. Your balance is now: $1150.0
    SETTING BALANCE
    8. Thank you for the deposit of $2.5. Your balance is now: $1152.5
    9. hello is not a number
    10. {'_balance': 1152.5, '_minimum_balance': 250, '_max_withdrawal': 150}


It is important to look closely at what has changed in our new class. We've added comments to point out the notable differences between our previous BankAccount class and this one. We also added print statements so that we can clearly see that our 'get_balance' and 'set_balance' methods are getting called even after we create our new balance *property*.

Now, that we are using **property()**, we can refer to our setter and getter methods as the same name, `balance`. However, note that when we use `balance` to get and set our bank account's balance, we do **NOT** invoke the function. In fact our `balance` property getter and setter looks like our original instance variable, `balance`. That is exactly what we wanted! 

How does our balance property know how to handle when to get or when to set? Well, let's look at the method signature for property()

```python
property(fget=None, fset=None, fdel=None, doc=None)
# fget is our getter method
# fset is our setter method
# fdel is our delete method
# doc is like a string, but we don't need to worry about this argument right now
```

The `property()` function returns a property object, which has three methods, `getter()`, `setter()`, and `delete()`. Theses each are capable of assigning methods to get, set, and delete an attribute of an isntance object. So, our notation can actually be broken down a bit. Let's take a look:

```python
# balance is now a **property object**
balance = property(get_balance, set_balance)

    TO

# balance is now a **property object**
balance = property()
balance.getter = get_balance
balance.setter = set_balance
```

Now when we try to perform **assigment**, our property calls the **setter** method, and when we try to simply **access** the property without assigning or deleting, our property invokes the **getter** method. 

## Summary

In this lab, we introduced Python class design patterns for using private instance variables, getter and setter instance methods, as well as using the property function to create property objects. By prepending an underscore to an instance variable, we are indicating that this variable should be treated as a private instance variable and that it should only be accessed through a getter or setter method instead of direct access. By using getter and setter methods we are able to build in validations for our instance variables ensuring that they remain the datatype and value range that we expect in our program. To make our program even more intuitive we can use property objects to encapsulate our getter and setter methods into a single object. We then are able to invoke these methods as if they were an instance variable, with the added bonus that we are using our getter and setter methods to interact with the actual instance variable.
