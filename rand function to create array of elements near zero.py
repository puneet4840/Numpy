# rand() function is from random module and random module is also in numpy.
# This rand() function is used to create the array of elements near to zero.
print()

from numpy import random

a=random.rand(5)
print(a)
print()

## 2-D array

a1=random.rand(2,3)
print(a1)
print()

## 3-D array

a2=random.rand(1,3,3)
print(a2)