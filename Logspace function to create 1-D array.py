# Logspace() is used to create 1-D evenly spaced numbers array.
print()

from numpy import logspace

a1=logspace(1,20,num=20,base=2,dtype=int)
print(a1)
print()


a2=logspace(1,10,num=10,dtype=int,base=3)
print(a2)