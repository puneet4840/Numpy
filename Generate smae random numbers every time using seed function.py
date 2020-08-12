# seed() function is used to generate the same random number at every time.
print()

import numpy as np

np.random.seed(1)
a1=np.random.randint(1,50,10)
print(a1)


a2=np.random.randint(1,50,10)
print(a2)