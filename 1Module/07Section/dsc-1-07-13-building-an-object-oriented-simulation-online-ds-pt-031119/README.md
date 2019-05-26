
# Building an Object-Oriented Simulation

## Introduction

In this lesson, we'll talk about best practices for simulating things in the real world using Object-Oriented Programming!

## Objectives

You will be able to:

* Use inheritance to to write D.R.Y. code 
* Understand the relationship between subclasses and superclasses
* Demonstrate an understand of the OO lifecycle, and the relationship between attributes and methods
* Create Object-Oriented data models that describe the real world with classes and subclasses


## Creating Stochastic Simulations

As a capstone for everything we've learned about Object-Oriented Programming, we'll be creating a **_Herd Immunity Simulation_**.


<img src='herd_immunity.gif'>


This simulation is meant to model the effects that vaccinations have on the way a communicable disease spreads through a population. The simulation we're building depends on just a few statistics that we'll borrow from the CDC or the WHO:

* `r0`, the average number of people a contagious person infects before they are no longer contagious (because they got better or they died)
* `mortality_rate`, the percentage chance a person infected with a disease will die from it.

The main workflow of simulation is as follows:

1. Create a `Person` class with the following attributes:
    * `alive`
    * `vaccinated`
    * `is_infected`
    * `has_been_infected`
    * `newly_infected`
    
1. Create a `Simulation` class with the following attributes:
    * `population`
    * `virus_name`
    * `num_time_steps`
    * `r0`
    * `percent_pop_vaccinated`

1. Create methods for our `Simulation` class that will cover each step of the simulation. We'll save the specifics of those for the lab, 

In order for our simulation to work, we'll need to define some rules for it:

* Each infected person will "interact" with 100 random people from the `population`. If the person the infected individual interacts with is sick, vaccinated, or has had the disease before, nothing happens. However, if the person the infected individual interacts with is healthy, unvaccinated, and has not been infected yet, then that person becomes infected. 

* At the end of each round, the following things happen:
    * All currently infected people either get better from the disease, or die, with the chance of death corresponding to the mortality rate of the disease. 
    * All people that were newly infected during this round become the new infected for next round.  
    
The simulation continues for the set number of time steps.  Any time someone dies or gets infected, we'll log it in a text file called `simulation_logs.txt`.  Once the simulation is over, we'll write some code to quickly parse the text logs into data and quickly visualize the results, so that we can run multiple simulations and answer questions like: 

* If vaccination rates for {disease x} dropped by 5%, how many more people become infected in an epidemic? How many more die?
* What does the spread of {disease x} through a population look like?

If this all seems a bit daunting, don't worry! We'll provide much more detail as we build this step-by-step during the lab. 

Let's move on to the lab and get started!

## Summary

In this lesson, you learned about best practices for simulating things in the real world using Object-Oriented Programming!
