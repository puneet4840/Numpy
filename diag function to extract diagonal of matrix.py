# diag() function is also used extract the diagonal of matrix.
print()

from numpy import diag,reshape,arange

a1=arange(1,10).reshape((3,3))
print(a1)
print(f"Diagonal:  {diag(a1,k=-1)}")
print(f"Diagonal:  {diag(a1,k=0)}")
print(f"Diagonal:  {diag(a1)}")