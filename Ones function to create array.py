# Ones() function is used to create n-d array.
print()

from numpy import ones,ndim

# 1-D array
a1=ones(5,dtype=int)
print(a1)
print()

# 2-D array
a2=ones((2,2),dtype=int)
print(a2)
print()

# 3-D array
a3=ones((1,2,2))
print(a3)
print()

# 4-D array
a4=ones((1,1,2,2),dtype=int)
print(a4)
print(a4.ndim)
print()

# 5-D array
a5=ones((1,1,1,2,2))
print(a5)
print(a5.ndim)
