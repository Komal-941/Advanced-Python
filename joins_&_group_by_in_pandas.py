## Combining DataFrame


df1 = pd.DataFrame({"city":["mumbai","delhi","bangalore","hyderabad"],
                   "temperature":[45,45,40,36]})
df1

df2 = pd.DataFrame({"city":["delhi","bangalore","mumbai","chennai","kolkata"],
                   "humidity":[68,65,75,70,76]})
df2

pd.concat([df1,df2],axis = 1)                   #joining two df
--------------------------------------------------------------------------------------------------------------------
"""## Merge of 2 different DataFrames"""

df1

df2


left_merge = pd.merge( df1 , df2, on ="city", how="left")
left_merge
--------------------------------------------------------------------------------------------------------------------------------------------

right_merge = pd.merge( df1 , df2, on ="city", how="right")
right_merge
------------------------------------------------------------------------------------------------------------------------------------------------
right_merge1 = right_merge.iloc[:,[0,2,1]]        #changed the seq for column
right_merge1
----------------------------------------------------------------------------------------------------------------------------------------------
#will go for common values only

inner_merge = pd.merge( df1 , df2, on ="city", how="inner")
inner_merge
-------------------------------------------------------------------------------------------------------------------------------------------------
#will merge two tables , with all the values: consider one value for once only
#prints with unique values only

outer_merge = pd.merge( df1 , df2, on ="city", how="outer")
outer_merge
----------------------------------------------------------------------------------------------------------------------------------------------------
"""**Unique**"""

example = pd.DataFrame({"city":["mumbai","delhi","bangalore","hyderabad"],
                   "temperature":[45,45.9,40,36]})
example
-----------------------------------------------------------------------------------------------------------------------------------------------------
"""## **Group by**"""


df.groupby("Gender")["Age"].min()          #will give the rsult after grouping & gives result for each group

df.groupby("Gender")["Age"].max()

df.groupby("Gender")["Salary"].min()

