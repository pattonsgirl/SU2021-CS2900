# Project 1 - Draft Phase

## Setup:

In the 'Projects' folder of your reporitory, create a folder called 'Project1'.

Your work for this project will be done in this 'Project1' folder.

Create a `README.md` file that describes the project in this folder.  You can look at this site for [documentation on what a good README file contains](https://www.makeareadme.com/).  Cite sources you use for you project in this file (as part of the descriptions or as a section of resources).

Create a file called `.gitignore`.  Make sure you call it `.gitignore`.  Copy and paste the contents of the [template file](https://raw.githubusercontent.com/github/gitignore/master/Python.gitignore) as the contents of your `.gitignore` file.

`.gitignore` files list files and folders that you want git to ignore.  This helps a lot if you are on the command line lazy using `*` or tend to zone out and click buttons.  By default, the contents usually include files that are important for running code on your computer, but could be uniquely different on a different computer.  You are welcome to look through this file and fidget with it or to read the [documentation on `.gitignore` files](https://git-scm.com/docs/gitignore) to get a more in depth feel for its usage.

## Draft Phase Requirements:

1. Create a folder in your `Project1` folder called `data`.  In this folder, create a `README.md` file.  The `README.md` file should contain information on:
    - what your data set is
    - how you got it (including any fancy magic needed to make it happen)
        - Document enough that I can also get the data set if so inclined, kind of like how I've described how different data sets have been gathered in class
    - details about the data set, such as important columns that are relevant to your project

2. In the `data` folder, add any static data sets your project will use.  You are welcome to use web calls, just detail it in the README file

3. In your `Project1` folder, start coding towards your goal 
    - At minimum there should be clear effort in pulling out data for later use in visualization
    - Your rough draft can be in an `.ipynb` or `.py` file
    - Remember to use functions or loops when doing a repetitive task

4. An example visualization using the library you think is the right fit for the job or attempt at your final visualization.
    - Example: if you know you want to plot data on a world map, but your data isn't quite ready yet, show a sample visualization from the plotly geo documentation to show you are playing around.

5. Cite the source(s) you use for your code in the `README.md` file in your `Project1` folder.  You can temporarily add them as contents, but in your final draft that will need to go in your project documentation

## Submission:

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your project folder.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Projects/Project1

## Rubric:

- Project1 folder contains:
    - .gitignore file with contents specified (1 pt)
    - README.md file with project details (1 pt)
    - data folder with README.md and data sets (if static) (1 pt)
    - starter code notebooks / files (1 pt)

- Draft expectations:
    - data folder README contains instructions regarding data set (2 pts)
    - starter code has attempts at gathering appropriate data (2 pts)
    - sample visualization wither using data or demo code (2 pts)