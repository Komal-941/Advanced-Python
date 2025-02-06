

import numpy as np

import pandas as pd

"""## Load the data"""


"""**Method 1**"""

pd.read_excel("C:\\Users\\DELL\\Downloads\\PandasExample.xlsx")

"""**Method 2**"""

pd.read_excel("C:/Users/DELL/Downloads/PandasExample.xlsx")

"""**Method 3**"""

pd.read_excel(r"C:\Users\DELL\Downloads\PandasExample.xlsx")

pwd    #present working directory

"""**Method 4**"""

pd.read_excel("PandasExample.xlsx")   #works only whne excel file and jupyter notebook in a same folder or location
--------------------------------------------------------------------------------------------------------------------------------

### **Loading CSV file**

pd.read_csv(r"C:\Users\DELL\Downloads\Pandas Example CSV.csv")
