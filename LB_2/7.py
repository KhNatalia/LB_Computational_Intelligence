import numpy as np

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

a = np.vstack((a, b))
print(a)
