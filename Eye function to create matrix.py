# Eye() function is used to create matrix with diagonal 1.
print()

from numpy import eye

a1=eye(2,2,dtype=int)
print(a1)
print()


a2=eye(3,3,k=1)
print(a2)
print()

a3=eye(3,3,k=-1)
print(a3)
print()

a4=eye(4,4,dtype=int)
print(a4)