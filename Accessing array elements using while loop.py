# Accessing array elements using while loop.
print()

from numpy import arange

a=arange(1,101,2)
i=0
while i<len(a):
    print(a[i],end=" ")
    i+=1
print()


a2=arange(1,11)
j=0
while j<len(a2):
    print(a2[j])
    j+=1
