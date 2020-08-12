# Sclicing means to retrieve elements from array.
print()

from numpy import arange,reshape

a=arange(1,26).reshape((5,5))
print(a)
print()

print(a[0])
print(a[4])
print(a[2][2])
print(a[:2,:2])
print()
print(a[:3,:3])
print()
print(a[1:4,1:4])
print()
print(a[1:,1:])
print()
print(a[3:5,3:5])
print()
print(a[:,2:])