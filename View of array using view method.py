# view means to create the another array that shares different memory location.
# But any change will also bew reflect in original array.
# It can be done in slicing of array and using view method.
print()

import numpy as np

a1=np.arange(1,21)
print(f"Original:  {a1}")
print(f"Id Original: {id(a1)}")
a1[1:11]=0
print(f"View:  {a1[0:11]}")
print(f"Original:  {a1}")

      #OR
print()

a=a1.view()
print(a)
print(f"Id View:  {id(a)}")
