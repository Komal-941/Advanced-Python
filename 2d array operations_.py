# **Mathematical Operation**

- **1. Arithmetic Operation**


i = np.array([[1,2,3],[45,21,82]])
print(i)

print("after adding :10 will be added to each value")
print(i+5)
------------------------------------------------------------------------
i1 = np.array([[21,34,56],[76,24,89],[21,93,49]])
i2=np.array([[34,56,78],[21,65,87],[27,45,91]])

print(i1+i2)

print(i1-i2)

print(i1*i2)
------------------------------------------------------------------------------------------------------------------------------------------
"""**Joining Multiple 2D arrays**"""

a = np.array([[1,2],[4,7],[8,2]])
print(a)

b=np.array([[4,8],[2,7],[9,3]])
print(b)

print(np.hstack((a,b)))    #all the values in horizontal line combined as one row

print(np.concatenate((a,b),axis=1))           #same like hstack


print(np.vstack((a,b)))

print(np.concatenate((a,b),axis=0))           #same like vstack

