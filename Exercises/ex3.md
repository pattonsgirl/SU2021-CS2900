# Exercise Set 3

## Setup:

This lab expects that you have already installed tools per the syllabus & lecture notes and have setup your course repository at https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME.  You can also [reference the install guide](https://github.com/pattonsgirl/SU2021-CS2900#Software)

For this lab, create a Jupyter Notebook in your `Exercises` folder called `ex3.ipynb`

**Put each `Part` of the exercise set in its own cell**

## Part 1:

Create a list of 40 random numbers between 5 and 50.  Output the list to the following file formats:

1. to a standard text file called `basic-data.txt`
2. to a YAML file called `basic-data.yaml`
3. to a JSON file called `basic-data.json`

Make sure in GitHub all three files exist in your `Exercises` folder.

Manually created lists will not count for credit.  Use the `random` module or some other means to generate random numbers.

Cite the source(s) you use for your code as comments.  You can cite your own brilliance

## Part 2:

Use one of the three formats you created to read the data in from a file.  Using the data in the file, output the following information about the list:

1. Mean
2. Median
3. Mode

Cite the source(s) you use for your code as comments.  You can cite your own brilliance

## Part 3:

There is a forecast from the National Weather Service in [forecast.json](forecast.json).  Copy this file and its contents to your `Exercises` folder (an example of how to do this was given 6/2 using "Raw" and copy / paste).

Read in the file (as JSON).  Using code, output the contents of the "detailedForecast" property for "Tuesday".

Hardcoding the output will not count for credit - use code to look into the nested dictionaries and lists.

Hints:
- break the data down by playing with dictionary keys.  
- use variables as save points to narrow down the scope of the data as you go

Cite the source(s) you use for your code as comments.  You can cite your own brilliance

## Submission

1. Commit and push your changes to your repository.  Verify that these changes show in your course repository, https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBNAME

2. In Pilot, paste the link to your notebook.  Sample link: https://github.com/WSU-kduncan/cs2900-python-YOURGITHUBUSERNAME/blob/main/Exercises/ex3.ipynb

## Documentation: Using the NWS API

- [API Documentation](https://weather-gov.github.io/api/general-faqs)
- Using with the latitude and longitude for Dayton, OH: https://api.weather.gov/points/39.75,-84.19
- Getting just the daily forecast data for Dayton, OH: https://api.weather.gov/gridpoints/ILN/43,67/forecast