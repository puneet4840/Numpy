# diag function is used to create matrix with list of elements we provide as diaginal.
print()

from numpy import diag

a1=diag([1,2,3,4,5])
print(a1)
print()

a2=diag((1,2),k=1)
print(a2)
print()

a3=diag((1,2),k=-1)
print(a3)
print()


a4=diag((1,2))
print(a4)

