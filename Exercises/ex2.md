# Exercise Set 2 - NOT FINALIZED

## Setup:

This lab expects that you have already installed tools per the syllabus & lecture notes and have setup your course repository at https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME.  You can also [reference the install guide](https://github.com/pattonsgirl/SU2021-CS2900#Software)

For this lab, create a Jupyter Notebook in your `Exercises` folder called `ex2.ipynb`

**Put each `Part` of the exercise set in its own cell**

## Part 1:

Build on from the Favorite Numbers exercise in class:

Given a starting dictionary of:  
`fav_nums = {'sam':56, 'ken':98, 'saul':6}`  
And given a list of keys to look up of:  
`lookup = ('sam','ben','ken','paul','saul')`

Output each key's favorite number.  If the key does not exist in the dictionary, prompt for the user for the key's favorite number and add the key and its value to the fav_nums dictionary.  In addition, print the average favorite number.

Output format:
```
Favorite numbers:
    Sam     56
    Ben     78
    Ken     98
    Paul    2
    Saul    6
Bonus - Average Favorite Number:
    48
```

Hints:
- `.items()`
- `.values()`

Cite the source(s) you use for your code as comments.  You can cite your own brilliance

## Part 2:

Given a starting list of known_ips:
`known_ips = ['12.45.23.1', '89.34.23.67', '67.45.23.43', '90.32.65.98']`

Create a function that can take either an ip, or take a list of ips (depending on how you want to implement it).  The function should add the new ip addresses to the known ip addresses list with the following restrictions:
- Do not add duplicate ips to the known_ips list
- Do not add '1.1.1.1' to the known_ips list

The function should be used for the following lists of new_ips.  Depending on how you would like to implement it, you may choose to call your function in between each list:
```
new_ips = ['45.23.98.12', '89.23.21.9', '67.45.23.43', '1.1.1.1']
new_ips = ['1.1.1.1']
new_ips = ['78.34.23.21', '90.43.65.1']
```

Print the final list of known_ips:
```
Known ips:
    12.45.23.1
    89.34.23.67
    67.45.23.43
    90.32.65.98
    45.23.98.12
    89.23.21.9
    78.34.23.21
    90.43.65.1
```

Cite the source(s) you use for your code as comments.  You can cite your own brilliance


## Part 3:



Cite the source(s) you use for your code as comments.  You can cite your own brilliance

## Submission

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your notebook.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Exercises/ex2.ipynb