# There are many useful functions in numpy to work with numpy array.
print()

import numpy as np

a=np.array([10,20,30,40,50])
print(a)
print()

# min() function : It returns minimum element from array.
print(np.min(a))
print()

# max() function: It returns maximum element from array.
print(np.max(a))
print()

# argmin() function: It returns position of minimum element.
print(np.argmin(a))
print()

# argmax() function: It returns position of maximum element.
print(np.argmax(a))
print()

# sqrt() function : It calculate square root of each element.
print(np.sqrt(a))
print()

### Trigonometric function

# sin() function: It returns sin value of each element.
print(np.sin(a))
print()

# cos() function: It returns cos value of each element.
print(np.cos(a))
print()

# tolist() function: It convert numpy array to python list.
lst=a.tolist()
print(lst)
print()

### Scalar math

# add() function: It adds given element to each element of the array.
print(np.add(a,10))
print()

# subtract() function: It subtracts given elements from each element of the array.
print(np.subtract(a,10))
print()

# multiply() function: It multiply given element to each element of the array.
print(np.multiply(a,10))
print()

# divide() function: It divide given element from each element of the array.
print(np.divide(a,10))
print()

# power() function:  It raise to power given element to each element of the array.
print(np.power(a,2))
print()

### Vectoe math

# log() function: It calculate log of each element of array.
print(np.log(a))
print()

# abs() function: It returns the positive value of negative element.
print(np.abs(a))
print()

# ceil() function: It rounds the higher nearest value of each element of the array.
a2=np.array([1.1,2.3,4.5,5.5,])
print(np.ceil(a2))
print()

# floor() function: It rounds the lower nearest value of each element of the array.
print(np.floor(a2))
print()

# round() function: It round the value to the nearest int.
a3=np.array([1.002341,2.102,3.798])
print(np.round(a3))
print()

### Statistics

# mean() function: It returns the mean of  array or matrics acc to rows and column.
mat1=np.arange(1,17).reshape((4,4))
print(np.mean(mat1,axis=1))
print()
print(np.mean(mat1,axis=0))
print()

# median() function: It returns the meadin of array or matrics acc to rows and column.
print(np.median(mat1,axis=1))
print()
print(np.median(mat1,axis=0))
print()

# var() function: It calculate the variance of the array or matrics.
print(np.var(a))
print()
print(np.var(mat1,axis=1))
print()

# std() funtion: It cvalculate the standard deviation of array or matrics.
print(np.std(a))
print()
print(np.std(mat1,axis=1))
print()
