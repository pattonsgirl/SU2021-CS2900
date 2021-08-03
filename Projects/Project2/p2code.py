import pandas as pd
import numpy as np
from pandas.core.reshape.merge import merge

hw_exams = pd.read_csv("id-hw-exams.csv")
id_section = pd.read_csv("id-section.csv")

#print(hw_exams.columns)
#print(id_section.columns)

# https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html
id_section['NetID'] = id_section['NetID'].str.lower()

#print(id_section.head(5))

df = pd.merge(hw_exams, id_section, left_on="SID", right_on="NetID")
df = df.drop(columns='SID')
df = df.drop(columns='Name')


#print(df.head(5))
#print(df.info())

# https://stackoverflow.com/questions/19071199/drop-columns-whose-name-contains-a-specific-string-from-pandas-dataframe
df = df.drop(columns=list(df.filter(regex=' - Submission Time')))

#print(df.info())

df['hw1_score'] = df['Homework 1'] / df['Homework 1 - Max Points']
df['hw2_score'] = df['Homework 2'] / df['Homework 2 - Max Points']
df['hw3_score'] = df['Homework 3'] / df['Homework 3 - Max Points']
df['hw4_score'] = df['Homework 4'] / df['Homework 4 - Max Points']
df['hw5_score'] = df['Homework 5'] / df['Homework 5 - Max Points']
df['hw6_score'] = df['Homework 6'] / df['Homework 6 - Max Points']
df['hw7_score'] = df['Homework 7'] / df['Homework 7 - Max Points']
df['hw8_score'] = df['Homework 8'] / df['Homework 8 - Max Points']
df['hw9_score'] = df['Homework 9'] / df['Homework 9 - Max Points']
df['hw10_score'] = df['Homework 10'] / df['Homework 10 - Max Points']

df = df.drop(columns=list(df.filter(regex='Homework ')))

df['ex1_score'] = df['Exam 1'] / df['Exam 1 - Max Points']
df['ex2_score'] = df['Exam 2'] / df['Exam 2 - Max Points']
df['ex3_score'] = df['Exam 3'] / df['Exam 3 - Max Points']

df = df.drop(columns=list(df.filter(regex='Exam ')))

#print(df.head(5))

# if a homework / exam was missed, make sure the score is 0
df = df.fillna(0)

#print(df.describe())

# Output a report that contains:
# For each homework and exam, the lowest and highest score and standard deviation
print("Homework 1:")
print(f"Lowest Score: {df['hw1_score'].min()}")
print(f"Highest Score: {df['hw1_score'].max()}")
print(f"Average Score: {df['hw1_score'].mean()}")
print(f"Standard Deviation from Average: {df['hw1_score'].std()}")
# would need matplotlib?
#hw1_plot = df['hw1_score'].plot.line()

# for each person, average homework score (across all homeworks)
#print(list(df.filter(regex='hw')))
homework_scores = df.filter(regex=r"^hw", axis=1)
#print(homework_scores.head(5))
df['hw_avg'] = homework_scores.mean(axis=1)
#print(df.head(5))

exam_scores = df.filter(regex=r"^ex", axis=1)
df['ex_avg'] = exam_scores.mean(axis=1)
#print(df.head(5))

df['final_score'] = (df['hw_avg'] * .6) + (df['ex_avg'] * .4)
df['final_score'] = df['final_score'] * 100

df["ceiling_score"] = np.ceil(df["final_score"])

letterGrade = []

for grade in df['ceiling_score']:
    #print(grade)
    #print(grade.dtype)
    # if statement series of doom
    if grade >= 90:
        letterGrade.append('A')
    elif 90 > grade >= 80:
        letterGrade.append('B')
    elif 80 > grade >= 70:
        letterGrade.append('C')
    elif 70 > grade >= 60:
        letterGrade.append('D')
    else:
        letterGrade.append('F')

print(letterGrade)

df['letter_grade'] = letterGrade

# print(df.head(5))

print(df.groupby('Section')['letter_grade'].value_counts())

# https://www.reddit.com/r/learnpython/comments/73z4e2/pandas_groupby_or_cut_dataframe_to_bins/

grade_range = [0, 60, 70, 80, 90, 100]
bins = pd.cut(df['ceiling_score'], grade_range)
#print(bins)
print(df.groupby(bins)['ceiling_score'].agg(['count']))
print(df.groupby(bins)['ceiling_score'].value_counts())
# print(df.pivot(index=bins, columns='Section', values='ceiling_score'))

print(df.corr())


#df['hw_sum'] = df.loc['hw1_score', 'hw2_score', 'hw3_score', 'hw4_score', 'hw5_score', 'hw6_score', 'hw7_score', 'hw8_score', 'hw9_score', 'hw10_score'].sum()
#sum_hw = df.loc[hw_list]
#print(sum_hw.head(5))

#hw_frame = df.loc[df.filter(regex='hw')]
#df['hw_avg'] = list(df.filter(regex='hw')).mean()
# for each person, average exam score (across all exams)
# for each person, compute final grade - homework was worth 60% of final grade, exams were worth 40% of final grade

# section comparison of final grades

#print(df.info())