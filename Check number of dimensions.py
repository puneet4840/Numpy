# ndim attrinute is used to check the array dimension.
from numpy import array,ndim

##1-D array
# using tuple in python array.
a=array((1,2,3,4,5))
print(a)
print(f"Dimension: {a.ndim}")


## 2-D array

a1=array([[1,2,3],[4,5,6]])
print(a1)
print(f"Dimension:  {a1.ndim}")

## 3-D array

a2=array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(a2)
print(f"Dimension:  {a2.ndim}")