## 1D Operation

**Arithmetic Operation**

import numpy as np                        #importing numpy library

a = np.array([0,1,2,3,4])
b = np.array([9,8,7,6,5])
c = a+2
print(c)

d = b-2             #shape has to be same (means the item in each array should be same)
print(d)

e = a*b
print(e)

f = a**2
print(f)
---------------------------------------------------------------------------------------------------------------------------------------------
"""**Comparison Operator**"""

import numpy as np
a=np.array([10,20,30,40])
b=np.array([10,20,30,50])
c=np.array([10,20,30,40])

a == b             #shape of both arrays have to be as the same
------------------------------------------------------------------------------------------------------------------------------------------------
"""**Mathematical Operators**"""

x = np.array([10,2,30,40])
print(x)

np.exp(x)

np.log(x)

np.log(y)                   #warning has been ignored

