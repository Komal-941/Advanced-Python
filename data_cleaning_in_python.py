## Treating the wrong data - Replace the data or remove

#load the dataframe

df = pd.DataFrame({"Age" :[15,18,'18',19.4,"20+"],
                   "Gender":["male","female","female","female","male"]})
df

df.info()                 #will all datatypes & information about dataframe
-----------------------------------------------------------------------------------------------------

### Replace 

df["Age"]= df["Age"].replace({'20+':20, "18":18})
df["Age"]
-----------------------------------------------------------------------------------------------------------
df1 = pd.DataFrame({"Age":[15,14,15,15,20],
                   "Name":["Ks","vk","vs","ps","os"]})
df1

-----------------------------------------------------------------------------------------------------------
"""### Drop"""

df3.drop(index=[1,3],inplace = True)
-----------------------------------------------------------------------------------------------------------

"""## Treat the wrong data type - Covert to correct or required data type"""

df = pd.DataFrame({"Age" :[15,18,'18',19.4,20],
                   "Gender":["male","female","female","female","male"]})
df

df=df["Age"].astype(float)
-------------------------------------------------------------------------------------------------------------------

"""## Treat the duplicates - Remove"""

df= df.drop_duplicates()

# to drop multiple duplicates
df4.drop(index =[2,3])
------------------------------------------------------------------------------------------------------------------------------

"""## Treat missing values - Replace or Remove

### Remove
"""

#number of missing values in each column
df.isnull().sum()

"""**drop a column which has >30% of missing values**"""

df.drop(columns=["Gender"])

#wherver the missing values are there those rows will be deleted
df=df.dropna()
----------------------------------------------------------------------------------------------------------------------

"""### Replace - original data"""

df5= pd.DataFrame({"Age":[np.nan,24,19,20,22,56],
                  "Gender":["male",np.nan,"female",'female',np.nan,"male"]})
df5

df5["Age"]=df5["Age"].fillna(21)

df5["Gender"]=df5["Gender"].fillna("male")

df5
-----------------------------------------------------------------------------------------------------------------------------------------
"""### Replace -fill the data statistically(avrg)"""

df6= pd.DataFrame({"Age":[np.nan,24,19,20,22,56],
                  "Gender":["male",np.nan,"female",'female',np.nan,"male"]})
df6

df6["Age"].mean()

df6["Age"] = df6["Age"].fillna(df6["Age"].mean())
----------------------------------------------------------------------------------------------------------------------------------------
"""## Treating the Outliers"""

df= pd.DataFrame({"marks":[10,11,12,25,25,27,31,33,34,34,36,36,43,50,59]})
df

Q1 = df["marks"].quantile(0.25)
print("Q1:" ,Q1)

Q3 = df["marks"].quantile(0.75)
print("Q3:" ,Q3)

IQR = Q3 - Q1
print ("IQR:" , IQR)

lower_limit = Q1 -(IQR * 1.5)
print("lower_limit:" , lower_limit)

upper_limit = Q3 +(IQR * 1.5)
print("upper_limit:" , upper_limit)

"""**By using seaborn library**"""

import seaborn as sns

sns.boxplot(df["marks"])

"""**By using matplotlib library**"""

import matplotlib.pyplot as plt

plt.boxplot(df['marks'])
plt.show()

"""**How to extract outliers**"""

df[(df["marks"]<lower_limit) | (df["marks"]>upper_limit) ]

"""**How many outliers are there?**"""

df[(df["marks"]<lower_limit) | (df["marks"]>upper_limit) ].shape[0]

"""**what are the index numbers of outliers?**"""

df[(df["marks"]<lower_limit) | (df["marks"]>upper_limit) ].index.tolist()

