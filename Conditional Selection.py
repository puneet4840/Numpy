# Condition Selection means to retrieve or select elements using condition.
print()

import numpy as np

a1=np.arange(1,51)
print(a1)
print()

print(a1[a1>20])      # elements greater then 20
print()
print(a1[a1<10])      # elements less than 10
print()
print(a1[a1%2==0])    # even numbers
print()
print(a1[a1%2!=0])    # odd numbers
print() 
