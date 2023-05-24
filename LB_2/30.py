import numpy as np

a = np.array([1, 3, 7, 1, 2, 6, 0, 1])

doublediff = np.diff(np.sign(np.diff(a)))
print(np.where(doublediff == -2)[0] + 1)
