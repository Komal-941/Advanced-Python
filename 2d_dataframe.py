
import numpy as np                          #importing numpy library

import pandas as pd                          # importing pandas library

## Pandas Dataframe (2D)

- **CReating a dataframe using dict**


b = {"ks":941,23:[67,65],90:(45.7,43),"value":True}
b1 = pd.DataFrame(b)
print(b1)
---------------------------------------------------------------------------------------------------------------------------------------------
"""**CReating a dataframe using nested list**"""

l =[[1,2],[3,4],[5,6]]
l1=pd.DataFrame(l)
print(l1)

l = [1,2,3,4]
l2=pd.DataFrame(l)
print(l2)
----------------------------------------------------------------------------------------------------------------------------------------------------
"""**CReating a dataframe using 2d array**"""

d =np.array([[1,2],[4,7],[7,8]])

d1 = pd.DataFrame(d)
print(d1)

d =np.array([[1,2],[4,7],[7,8]])

d1 = pd.DataFrame(d,index=["A","B","C"],columns=["a","b"])
print(d1)



