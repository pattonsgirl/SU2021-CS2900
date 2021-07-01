# Exercise Set 5

## Setup:

This lab expects that you have already installed tools per the syllabus & lecture notes and have setup your course repository at https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME.  You can also [reference the install guide](https://github.com/pattonsgirl/SU2021-CS2900#Software)

For this lab, create a Jupyter Notebook in your `Exercises` folder called `ex5.ipynb`

**Put each `Part` of the exercise set in its own cell**

## Part 1:

Create a DataFrame from the following lists. Use the list names as the column titles
```
number = [1, 4, 7, 25, 10, 13]
pokemon = ['bulbasaur', 'charmander', 'squirtle', 'pikachu', 'caterpie', 'weedle']
evolution = ['venusaur', 'charizard', 'blastoise', 'raichu', 'butterfree', 'beedrill']
p_type = ['grass', 'fire', 'water', 'electric', 'bug', 'bug']
hp = [25, 55, 32, 34, 21, 23]
```

## Part 2:

Display the following dataframe views:

- Only the bugs
- Only the pokemon with less than 30 hp
- Only the pokemon name and hp for pokemon with hp less than 30

## Part 3:

Read in the Chipotle dataset into a DataFrame.  The dataset is here:
- https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv

You'll be using the dataframe to find out information in the following exercises.

Display the first and last 10 entries in the dataframe.

Cite the source(s) you use for your code as comments.  You can cite your own brilliance

Hint:
- https://www.kite.com/python/answers/how-load-a-.tsv-file-into-pandas-dataframe
- .head() and .tail()

## Part 4:

Print a dataframe that shows all details for order 110.

## Part 5:

Print a dataframe the shows the choice descriptions for Chicken Soft Tacos in order 18

## Part 6:

For the item price column, convert the prices to floats.

Hint:
- https://pbpython.com/currency-cleanup.html
    - I looked at the alternative solutions section, as a bigger hint.  You should still fidget.

## Part 7:

Find the maximum item price.

Display a dataframe that shows only the order id, the quantity, and the item name for item(s) ordered at the maximum price.

Hint:
- numpy!

## Part 8:

Use pandas & numpy to figure out:

How many items were ordered in order 577?

Hint:
- I converted the resultant frame splice to a numpy array.  
    - You could use the in class rainfall example to see something similar to what I did
    - I used this stratedgy to solve the next few exercises as well

## Part 9: 

Use pandas & numpy to figure out:

What is the total order price for order 577?

## Part 10:

Use pandas & numpy to figure out:

How many orders of 'Steak Bowl' were placed?

## Extra Credit 1 (10%):

Find the maximum quanitity of items ordered.

Display a dataframe that shows only the order id, the quantity, and the item name for item(s).

## Extra Credit 2 (10%):

Find the total cost of each order.  Output the result in its own list or add a result column to the dataframe that corresponds to the order.

# Submission

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your notebook.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Exercises/ex5.ipynb

## Extra Practice Resources:

The links below will not count for credit, but it can be helpful to practice on more datasets.

- https://www.w3resource.com/python-exercises/pandas/index.php 
- https://www.pythonprogramming.in/pandas-examples.html
- https://pynative.com/python-pandas-exercise/

