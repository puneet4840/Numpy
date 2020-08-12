# We can access array elements using its index.
# By default begin from 0
print()

import numpy as np

## 1D array

a1=np.array((10,20,30,40,50))
print(a1[0])
print(a1[1])
print(a1[2])
print(a1[3])
print(a1[4])
a1[4]=10
print(a1)

print()

## 2D array

a2=np.arange(1,10).reshape((3,3))
print(a2)
print(f"First row:  {a2[0]}")
print(f"Second row:  {a2[1]}")
print(f"Third row:  {a2[2]}")
print()
print(f"First colomn:  {a2[0][0]}")
a2[0]=99
print(a2)
