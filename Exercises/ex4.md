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

Project research:

1. Find a data set that interests you. It is recommended to work with a smallish dataset for more (less than 1 GB).  If you are out of ideas, there are ideas below you can use or template off of.  
    - https://people.sc.fsu.edu/~jburkardt/data/csv/csv.html
    - https://www.kaggle.com/datasets 
2. What would you like to discover about this data?

3. What visualization seems useful to either help with the discovery, or as an additional discovery?

Ideas:

1. Weather compare - compare this year's temperature to a few year's ago for Dayton, OH.  Only using high temperatures, create a line graph with both. Determine if there has been a change. 

2. Car accidents & weekdays - histogram of which day of the week had a car crash.  Determine if there is any correlation

3. Parse auth.log for usernames, timestamps, ip addresses, and ports.  Get count of all usernames - determine top 5. Generate pie chart of username's attempted.  


## Submission

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your notebook.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Exercises/4.ipynb

## Extra Credit (up to 10%):

Choose one or both of the following ways to improve your work in Parts 1 & 2:

**Data gathering cleanup (5%)**: You may have notice that the days listed are not all "days" - they also include nights.  Use some logic to make sure that the only temperatures added to your list of temperatures are days of the week (ie. Monday, Tuesday, etc.)

**Better x-axis labels (5%)**: Get a list of "names" in addition to the temperatures.  Chart the names with the temperatures, and have the names display on your visualization.

Note: this will have some parallels to the code we wrote in class 6/9 if you need a reference.