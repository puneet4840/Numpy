# axis means dimension. We can use axis attribute in numpy function.
# if axis=1: Calculation will happen using row wise.
# if axis=0: Calculation will happen using column wisw.
print()

import numpy as np

a=np.arange(1,17).reshape((4,4))
print(a)
print()

print(np.min(a,axis=1))
print()
print(np.min(a,axis=0))
print()
print(np.max(a,axis=0))
print()
print(np.max(a,axis=1))