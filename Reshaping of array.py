# Reshaping means to convert the dimension of array-
# Like 1D-2D,1D-3D,2D-3D,3D-1D,etc
print()

import numpy as np

## Reshaping 1D-2D

a1=np.arange(1,11)
a1=np.reshape(a1,(2,5))
print(a1)
print()

      # OR

a2=np.arange(1,11).reshape((2,5))
print(a2)
print()

## Reshaping 1D-3D

a3=np.arange(1,11).reshape((1,2,5))
print(a3)
print()


## Reshaping 2D-1D

a4=np.array([[1,2,3],[4,5,6]])
a4=np.reshape(a4,(6))
print(a4)
print()

      # OR

a5=np.array([[1,2,3],[4,5,6]]).reshape(6)
print(a5)
print()


## Reshaping 2D-3D

a6=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
a6=np.reshape(a6,(1,4,4))
print(a6)
print()

      #OR

a7=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]).reshape((1,4,4))
print(a7)
print()

## Reshaping 3D-1D

a8=np.zeros((1,3,3))
a8=np.reshape(a8,9)
print(a8)
print()
      #OR

a9=np.ones((1,5,5)).reshape(25)
print(a9)
print()

## Reshaping 3D-2D

a10=np.ones((1,5,5)).reshape(5,5)
print(a10)

