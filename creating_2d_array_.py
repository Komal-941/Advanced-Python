# 2D Array

import numpy as np

a =[[1,2,3],[4,5,6]]
b =np.array(a)
print(b)
   

b = np.array([[3,45,67],[45,67,78],[34,65,21]])   #both rows should have same no. of items
print(b)
b.ndim

b.shape

l = [[42]]

l1 = np.array(l)
print(l1)

print(l1.ndim)
print(l1.shape)

y = [[1,2,3],[4,5,np.nan]]           # to mark the missing value

y1 = np.array(y)
print(y1)
print(y1.ndim)
print(y1.shape)
-----------------------------------------------------------------------------------------------------------------------------------------------
"""**Zeros matrix**"""

np.zeros((3,),dtype=int)

np.zeros((3,2),dtype=int)
--------------------------------------------------------------------------------------------------------------------------------------
"""**Unity Matrix**"""

np.ones((2,3),dtype=float)

np.ones((4,3),dtype=int)
--------------------------------------------------------------------------------------------------------------------------------------------
# identy matrix
np.eye(2,3)              #eye is use to create identy matrix

np.eye(4,4)
-----------------------------------------------------------------------------------------------------------------------------------------------
#diagonal matrix
np.diag([1,2,3])          #in diagonal matrix if we give a imput as 1D that 1 row it gives output as 2D
------------------------------------------------------------------------------------------------------------------------------------------------

**Extracting a single value**

a = [[1,2,3,4],[67,43,29,66],[23,19,54,np.nan],[10,93,53,84]]

b = np.array(a)
print(b)                   #because of missing value np.nan all values converted to float

b[2,3]

b[1,2]
--------------------------------------------------------------------------------------------------------------------------------------------------------------
"""**Extracting a multiple value**

- array[list of row index no. , list of coloumn index no.]
"""

a = [[1,2,3,4],[67,43,29,66],[23,19,54,34],[10,93,53,84]]

b = np.array(a)
b[[1,2],:]            #rows 1& 2 and all the column

b[:,[1,3]]
-----------------------------------------------------------------------------------------------------------------------------------------------------

#replacing single value
b[1,2] = 50
print(b)

#replacing double value
b[[1,3],[3,2]] = 80,90
print(b)
-------------------------------------------------------------------------------------------------------------------------------------------------
"""**Reshape**

- converting 1D to 2D
"""

f = np.arange(8)
print(f)
print(f.shape)

print(f.reshape(4,2))
-------------------------------------------------------------------------------------------------------------------------------------------------
"""**Sort**

- row sort --> axis ==1
- column sort --> axis ==0
- **syn**  np.sort(array,axis=)
"""

h = np.array([[888,999,000],[329,321,np.nan],[672,493,847]])
print(h)      #as missing value nan is there all values converted to float

print(np.sort(h,axis=0))      #columns are adjusted

