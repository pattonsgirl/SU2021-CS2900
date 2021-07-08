# Exercise Set 6

## Setup:

This lab expects that you have already installed tools per the syllabus & lecture notes and have setup your course repository at https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME.  You can also [reference the install guide](https://github.com/pattonsgirl/SU2021-CS2900#Software)

For this lab, create a Jupyter Notebook in your `Exercises` folder called `ex6.ipynb`

**Put each `Part` of the exercise set in its own cell**

**Cite the source(s) you use for your code as comments.  You can cite your own brilliance**

## Part 1:

You will be using [silly-survey-v2.csv](silly-survey-v2.csv) in this folder.  Since this repo and the data in it is public, here is the link if you'd rather use it: https://github.com/pattonsgirl/SU2021-CS2900/blob/main/Exercises/silly-survey-v2.csv 

This is slightly different from what was provided in class, so I recommend viewing the csv.

Perform the following starting actions on the dataset:
- drop the "Timestamp" column
- rename the columns to easier names.  For example: `'Favorite color of provided'` becomes `'color'`
- for the column where users chose a major, replace `Other` values with `NON` for non major
- for the column where users type their own number, convert the values to type `int` or `float`.  If the value cannot be converted, have it become `NaN`
- print the cleaned dataset / dataframe

## Part 2:

Use code to find answers to the following questions:
1. Mean favorite number when user inputs number of their choice
2. Mode favorite number when user is given a set to choose from
3. How many users chose "CEG" as their major?
4. A new question was added to the survey - how many answered the question: "Oh no, this is new"?
5. How many users chose the number "42" from the selection of choices?
6. How many users chose the number "42" from the selection of choices and chose the major "CEG"?


Sample of expected format:
```
# Sample question: how many users answers all questions on the survey?
# in notebook cell:
# drop all rows that contain NaN values
only_non_nans = survey_results.dropna()
# this gets the by column count
print(only_non_nans.count())
# can count indices remaining
print("Number of users who answered all questions on survey")
print(len(only_non_nans.index))
```

## Part 3:

A little more interaction:

Let the user choose a query set.  Prompt the user for a major and one of the numbers that could be selected.

Return the results for:
1. How many users chose the major
2. How many users chose the number from the selection of choices
3. How many users chose the number from the selection of choices and chose the major

## Part 4:

Adventures in visualization:

Create a pie chart using:
- favorite colors
- favorite numbers from the given selection

Create a histogram using:
- favorite numbers that users get to type.  Set a reasonable number of bins

# Submission

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your notebook.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Exercises/ex6.ipynb


## Other

Modify your project to use pandas to read in your data.  If you do this, leave a note for me to go check your modifications.


