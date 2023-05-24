import numpy as np

a = np.array([1, 2, 3])

print(np.hstack((np.tile(a[0], 3), np.tile(a[1], 3), np.tile(a[2], 3), np.tile(a, 3))))
