# Accessing array elements using from loop
print()

from numpy import array,zeros,ones

## without index

a1=array([1,2,3,4,5,6,7,8])
for item in a1:
    print(item,end=" ")
print()

a2=zeros((3,3),dtype=int)
for item in a2:
    print(item,end=" ")

a3=ones(5,dtype=int)
for item in a3:
    print(item,end=" ")


## with index

print()

a4=array((1,2,3,4,5,))
for i in range(len(a4)):
    print(a4[i],end="  ")