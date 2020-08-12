# There are three methods to manipulate the array elements.
# 1: append: It add element at the end.
# 2: insert: It add element at partiular position.
# 3: delete: It delete elements row or column wise.
print()

import numpy as np

a=np.array([1,2,3,4,5])
print(a)
print()

# append element

np.append(a,99)
print(a)

# insert element

np.insert(a,0,100)
print(a)