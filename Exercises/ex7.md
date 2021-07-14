# Exercise Set 7

## Setup:

This lab expects that you have already installed tools per the syllabus & lecture notes and have setup your course repository at https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME.  You can also [reference the install guide](https://github.com/pattonsgirl/SU2021-CS2900#Software)

For this lab, create a Jupyter Notebook in your `Exercises` folder called `ex6.ipynb`

**Put each `Part` of the exercise set in its own cell**

**Cite the source(s) you use for your code as comments.  You can cite your own brilliance**

## Part 1:


Given the following dictionaries: 
```
set1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

set2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

scores3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}
```

Use concatenate / append and join / merge to get a final dataframe that looks like:
```
  subject_id first_name last_name  test_id
0          1       Alex  Anderson       51
1          2        Amy  Ackerman       15
2          3      Allen       Ali       15
3          4      Alice      Aoni       61
4          4      Billy    Bonder       61
5          5     Ayoung   Atiches       16
6          5      Brian     Black       16
7          7      Bryce     Brice       14
8          8      Betty    Btisan       15

```

## Part 2: 

Given these two data sets:
- https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-abbrevs.csv
- https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-population.csv

Read them in a dataframes, and merge the data together.  Drop the 'abbreviation' column

Hints:
- Do the two sets of data have a common column name?
- Do the two sets of data have columns of data that correlate?
- Puch them to use 'how'
- Investigate `left_on` and `right_on`: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.merge.html

Sample segment of final dataframe:
```
     state/region     ages  year   population    state
0              AL  under18  2012    1117489.0  Alabama
1              AL    total  2012    4817528.0  Alabama
2              AL  under18  2010    1130966.0  Alabama
3              AL    total  2010    4785570.0  Alabama
4              AL  under18  2011    1125763.0  Alabama
...           ...      ...   ...          ...      ...
2539          USA    total  2010  309326295.0      NaN
2540          USA  under18  2011   73902222.0      NaN
2541          USA    total  2011  311582564.0      NaN
2542          USA  under18  2012   73708179.0      NaN
2543          USA    total  2012  313873685.0      NaN
```

## Part 3: 

Using code, find out the following:
- Identify which columns are missing data

## Part 3:
- https://raw.githubusercontent.com/jakevdp/data-USstates/master/state-areas.csv

Data sets: https://github.com/jakevdp/data-USstates/
Given population, area, by year info, and by age group info
Goal: rank US states and territories by their 2010 population density


# Submission

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your notebook.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Exercises/ex6.ipynb