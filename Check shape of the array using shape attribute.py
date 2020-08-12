# shape attribute is used to chekc hte shape of any array
print()

import numpy as np

a1=np.array([1,2,3,4,5])
print(a1.shape)

a2=np.random.randint(1,21,20).reshape(4,5)
print(a2.shape)

a3=np.array([[[1,2,3],[4,5,6],[7,8,9]]])
print(a3.shape)