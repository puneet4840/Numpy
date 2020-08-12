# Slicing means to retrieve elements from array
print()

import numpy as np

a1=np.array((1,2,3,4,5,6,7,8,9,10))
print(a1[0:len(a1)])
print(a1[0:])
print(a1[:len(a1)])
print(a1[::])
print(a1[:11])
print(a1[0:len(a1):2])
print(a1[0:4])
print(a1[4:])
print(a1[-1:-11:-1])
print(a1[-1:-5:-1])
print(a1[::-1])