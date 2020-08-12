# copy() method is used to create the copy of the existing array.
# But any change will not reflect in the original array.
print()

import numpy as np

a1=np.arange(1,21)
print(a1)
print(f"Id original:  {id(a1)}")
print()

a2=a1.copy()
print(f"Copy:  {a2}")
print(f"Id copy:  {id(a2)}")