# Array() function to create numpy array.

from numpy import array

## 0-D array.

a1=array(100)
print(a1)

## 1-D array
# using list in array function.

a2=array([1,2,3,4,5])
print(a2)

# using tuple in array function.

a3=array((1,2,3,4,5))
print(a3)

## 2-D array 

a4=array([[1,2,3],[4,5,6]])
print(a4)

## 3-D array

a5=array([[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]]])
print(a5)

