# Zeros() function is used to create n-d array.
print()

import numpy as np

## zeros function

# 1-D array
a1=np.zeros(5,dtype=int)
print(a1)
print()


# 2-D array
a2=np.zeros((2,3),dtype=int)
print(a2)
print()


# 3-D array
a3=np.zeros((1,3,4),dtype=int)
print(a3)
print()


# 4-D array
a4=np.zeros((1,1,3,3))
print(a4)
print()

# 5-D array
a5=np.zeros((1,1,1,3,3))
print(a5)