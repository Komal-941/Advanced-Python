# -*- coding: utf-8 -*-
"""Joins & Group by in Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RK2jbCf__gMQ9JuqE-ijkiUbl1ZkzPns

## Combining DataFrame
"""

df1 = pd.DataFrame({"city":["mumbai","delhi","bangalore","hyderabad"],
                   "temperature":[45,45,40,36]})
df1

df2 = pd.DataFrame({"city":["delhi","bangalore","mumbai","chennai","kolkata"],
                   "humidity":[68,65,75,70,76]})
df2

pd.concat([df1,df2],axis = 1)

"""## Merge of 2 different DataFrames"""

df1

df2

''' Firstly go for Left table(df1) will print the left table and then will check for the RHS table (df2) for common values
whichever the values are avaible in both common column will print other ignores'''

left_merge = pd.merge( df1 , df2, on ="city", how="left")
left_merge

''' Firstly go for Right table(df2) will print the left table and then will check for the LHS table (df1) for common values
whichever the values are avaible in both common column will print other ignores (whichevr has no value in other will print as nan)'''

right_merge = pd.merge( df1 , df2, on ="city", how="right")
right_merge

right_merge1 = right_merge.iloc[:,[0,2,1]]        #changed the seq for column
right_merge1

#will go for common values only

inner_merge = pd.merge( df1 , df2, on ="city", how="inner")
inner_merge

#will merge two tables , with all the values: consider one value for once only
#prints with unique values only

outer_merge = pd.merge( df1 , df2, on ="city", how="outer")
outer_merge

"""**Unique**"""

example = pd.DataFrame({"city":["mumbai","delhi","bangalore","hyderabad"],
                   "temperature":[45,45.9,40,36]})
example

"""## **Group by**"""

df

df.groupby("Gender")["Age"].min()          #will give the rsult after grouping & gives result for each group

df.groupby("Gender")["Age"].max()

df.groupby("Gender")["Salary"].min()

