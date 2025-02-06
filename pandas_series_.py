
import numpy as np

import pandas as pd

"""# Pandas

## Pandas Series

**creating pandas series using list**
"""

l =[1,2,3,4]

array_l= np.array(l)             #each value in row = array
print(array_l)

array_l+5

pd_Series= pd.Series(l)         #each value in column = Pandas series
print(pd_Series)
pd_Series+5

a= [12,34.5,"srk",False]

a1 = np.array(a)
print(a1)
-------------------------------------------------------------------------------------------------------------------
"""**Creating a series using 1D array**"""

# by default the index numbers as 0,1,2
a =np.array([1,2,3,4])

a1 = pd.Series(a)
print(a1)
-------------------------------------------------------------------------------------------------------------------------------
"""**CReating a series using dict**"""

#in dict the key values are considered as index name or row names
#in case of dict we can't change the index names
b = {"ks":941,23:[67,65],90:(45.7,43),"value":True}
b1 = pd.Series(b)
print(b1)

