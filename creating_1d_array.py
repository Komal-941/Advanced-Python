## **function to creating 1D Array**

import numpy as np        #import numpy library as np

a = np.arange(10)         #**Arrange**
print(a)

a = np.arange(0,20,2)
print(a)
----------------------------------------------------------------------------------------------------------

a= np.linspace(1,100,5)                    # retruns evenly spaced numbers over a specified interval
print(a)
------------------------------------------------------------------------------------------------------------

a= np.random.randint(1,10,3)                   #Retrun random integers from start(include) to end(exclude)
a
-------------------------------------------------------------------------------------------------------------------------------

np.zeros(5)               #create array with zeroes
------------------------------------------------------------------------------------------------------------------------------

np.ones(5)                                 #create array with ones
----------------------------------------------------------------------------------------------------------------------------

a = np.array([10,20,30,40,50,60])
print(a)

a[0]                            #Acessing single value through indexing

a[::-1]                          #Acessing multiple value through slicing
----------------------------------------------------------------------------------------------------------------------------------------

a = np.array([10,20,30,40,50,60])
print(a)

b= a[[1,2,5]]                                    #Acessing multiple value through indexing
print(b)
--------------------------------------------------------------------------------------------------------------------------------------------

a = [1,2,3,4]                                  ##add a sigle value in array
b = np.array(a)
c = np.append(b,45)
print(c)

a = [1,2,3,4]
b = np.array(a)
c = np.append(b,[45,56,67])               #adding multiple values
print(c)
-----------------------------------------------------------------------------------------------------------------------------------------------
f = np.array([23,54,18,65])
g=np.delete(f,2)                              #removing multiple  items
print(g)

l=[1,9,4,6]
l.pop(1)                       ##removing single valu
print(l)
--------------------------------------------------------------------------------------------------------------------------------------
l=np.array([1,9,41,62,45,76])

l[[1,2,3]] = 90                     #Replacing a multiple index numbers with single value
print(l)

l = np.array([23,45,67,89])
l[[1,2]] = [54,76]                 #Replacing a multiple inex numbers with multiple values
print(l)
---------------------------------------------------------------------------------------------------------------------------------------------

#shallow copy
a = np.array([23,45,32,54])
print("a:",a)
b= a.copy()
print("b:",b)
b[0]=100
print("after modifying b:",b)
print("After modfiying a remians same: ",a)
---------------------------------------------------------------------------------------------------------------------------------------------------
"""**Sorting array**"""

a= np.array([34,1,100,67,80])
print(a)

b= np.sort(a)
print(b)

