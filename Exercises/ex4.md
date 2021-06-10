# Exercise Set 4

## Setup:

This lab expects that you have already installed tools per the syllabus & lecture notes and have setup your course repository at https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME.  You can also [reference the install guide](https://github.com/pattonsgirl/SU2021-CS2900#Software)

For this lab, create a Jupyter Notebook in your `Exercises` folder called `ex4.ipynb`

**Put each `Part` of the exercise set in its own cell**

## Part 1:

There is a forecast from the National Weather Service in [forecast.json](forecast.json).  Copy this file and its contents to your `Exercises` folder (an example of how to do this was given 6/2 using "Raw" and copy / paste).

Create a list of temperatures by programatically (using code) pulling out the temperature for each item in the list.  If you need a hint on how to parse the file, refer to the beginning of lecture 6/9.

## Part 2:

Using the list, create a visualization using the `matplotlib.pyplot` module.  Give your chart a title and label the y-axis at minimum.


## Part 3:

Project research.  Put your answers in a cell and convert the cell to markdown.  I'll provide feedback based on what you supply.

1. Find a data set that interests you. It is recommended to work with a smallish dataset (less than 1 GB).  Below are some sites you can browse for datasets.  There are some suggested ideas below if you don't have anything in particular in mind.  
    - https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
    - https://www.kaggle.com/datasets 

2. What would you like to discover about this data?

3. What visualization seems useful to either help with the discovery, or as an additional discovery?

4. Cite a source that will help you get to your goals.  This could be a visualization similar to one you are trying to create.

Ideas:

1. TV viewership - create a single visualization with a line graph for each tv show listed in the data set.  Determine which show has the lowest viewweship and which show has had the steepest decline in viewership.
    - [Dataset to reference](https://people.sc.fsu.edu/~jburkardt/data/csv/news_decline.csv)

2. Car accidents & weekdays - histogram of which day of the week had a car crash.  Determine if there is any correlation.
    - [Dataset to reference](https://people.sc.fsu.edu/~jburkardt/data/csv/crash_catalonia.csv)

3. Parse auth.log.csv for usernames and ip addresses.  Get count of all usernames - determine top 5. Generate pie chart of username's attempted.  


## Submission

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your notebook.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Exercises/4.ipynb

## Extra Credit (up to 10%):

Choose one or both of the following ways to improve your work in Parts 1 & 2:

**Data gathering cleanup (5%)**: You may have notice that the days listed are not all "days" - they also include nights.  Use some logic to make sure that the only temperatures added to your list of temperatures are days of the week (ie. Monday, Tuesday, etc.)

**Better x-axis labels (5%)**: Get a list of "names" in addition to the temperatures.  Chart the names with the temperatures, and have the names display on your visualization.

Note: this will have some parallels to the code we wrote in class 6/9 if you need a reference.