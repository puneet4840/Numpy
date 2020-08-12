# Linspace function is used to create 1-D evenly spaced array.
print()

from numpy import linspace,ndim,size,shape

a=linspace(1,100,num=10)
print(a)
print(a.ndim)
print(a.size)
print(a.shape)
print()


a1=linspace(1,100,num=20)
print(a1)
print(a1.ndim)
print(a1.size)
print(a1.shape)
print()


a2=linspace(100,200,num=8)
print(a2)