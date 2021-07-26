# Project 2

## Setup:

In your `Projects` folder, create a new folder called `Project2`.  Create a `data` folder that contains the data linked below.

Two data files are provided for this project:
- [p2-data/id-hw-exams.csv](p2-data/id-hw-exams.csv)
    - This file contains info about student grades in the course.
    - 'First Name' - student first name
    - 'Last Name' - student last name
    - 'SID' - similar to your w#
    - 'Homework 1' - student score for homework assignment
    - 'Homework 1 - Max Points' - maximum score for homework assignment
    - 'Homework 1 - Submission Time' - homework assignment submission time
    - Repeat for Homeworks 2 - 10
    - 'Exam 1' - student score for exam
    - 'Exam 1 - Max Points' - maximum score for exam
    - 'Exam 1 - Submission Time' - exam submission time
    - Repeat for Exams 2 & 3

- [p2-data/id-section.csv](p2-data/id-section.csv)
    - This file contains info about students enrolled in the course.
    - 'ID' - think university ID
    - 'Name' - full name of student
    - 'NetID' - similar to your w#
    - 'Email Address' - email address for student
    - 'Section' - which section of the course the student enrolled in


The goal of this project is to use these data files to generate a final report for the instructor filled with statistics about grade performance.  Get as fancy as you'd like with the report output - you can ship it to a text file (or other format), or just put the output in your README file.

## Data Ingestion

1. Merge the two data set together
    - I pulled out the 'left_on' and 'right_on' from exercise set 7 since the ideal columns to merge on are named differently
2. Drop the timestamp columns for homeworks and exams
    - this is a cool time to play with `filter` and to use the regex option.  Don't overthink - find the common thing these column names have
3. If an homework / exam was missed (blank / null / nan), then fill in the score with a 0

## Data Prep

1. For each user, calculate the score they recieved on each homework - store the result in a new column
2. For each user, calculate the score they recieved on each exam - store the result in a new column
3. For each user, calculate the score their average homework score - store the result in a new column
    - Hints:
        - For this, your going to need to play with specifying the axis.  Here's a push:
        - `only_user_homework_scores = all_info.filter(regex=r"^hw", axis=1)`
        - Now to calculate the mean, remember we don't want the mean of the column - we want for a user == for a row... <sub>axis</sub>
4. For each user, calculate the score their average exam score - store the result in a new column
5. For each user, calculate the score their final grade - store the result in a new column
    - Homeworks are worth 60% of the final grade
    - Exams are worth 40% of the final grade

- Notes: 
    - You may choose to have scores be in percents instead of decimals - * 100
    - You may choose to remove the points awarded and max points columns once you have created the percentage scores.
        - ex. 'Homework 1' and 'Homework 1 - Max Points' can go once 'hw1_score' is calculated

## Generate a Report

Project report can be text from your code output that you format into your README, a separate text file (markdown would be nice), or, fanciest, play with generating a PDF. There's no score based on how you output, just that a report exists.

**Sample report is in `Project2` folder: [Project2](Project2/README.md)**

1. For each homework and exam, output:
    - lowest score - df['homework1_score'].min
    - highest score
    - average score
    - standard deviation
```
# Sample output per homework / exam:
Homework 1:
Lowest Score: 0.0
Highest Score: 1.0
Average Score: 0.7752499999999999
Standard Deviation from Average: 0.13725550257303776
```

2. Output the final grade distribution based on all sections
    - A section breakdown (like in the sample report) is easy if you are using letter grades.  Otherwise just provide numbers across all sections
    - Hint: if using the numeric grades, [check out `.cut`](# https://www.reddit.com/r/learnpython/comments/73z4e2/pandas_groupby_or_cut_dataframe_to_bins/)
    - Hint: both `groupby` and `value_counts` may come in handy if you did letter grades (see extra credit)

3. See if there was any correlation between homework or exam grades and final grades
    - Put differently, did students who did well (80% and above) recieve high final grades (80% and above)?
    - Hint: `.corr`

## Extra Credit 1 (10%)

- For each user, calculate the letter grade based on their final grade - store the result in a new column
    - Hint: give mapping a go

## Extra Credit 2 (10%)

- In your report, include one or more visualizations that benifit the report findings.  Make sure axis are labeled and legends are provided (if needed)

## Submission:

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Projects/Project1

## Rubric (still defining 7/21):

- Project2 folder contains:
    - README.md file with project details (1 pt)
    - data folder with data sets specified (1 pt)
    - project code in .py file / files (1 pt)

- Project2 expectations:
    - Project2 folder README.md contains 
        - summary of project (1 pt)
        - link to generated report OR report contents (output from code) (1 pt)
    - Project code goals
        - does anything / runs something without error (1 pt)
        - data ingestion steps done (3 pts)
        - data prep steps done (5 pts)
        - generates report with 3 key elements (3 pt)

### Sources

- Data gathered from RealPython GitHub repo: https://github.com/realpython/materials/tree/master/pandas-gradebook-project/data 
- Project idea from: https://realpython.com/pandas-project-gradebook/ 