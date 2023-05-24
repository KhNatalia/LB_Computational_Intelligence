import numpy as np

a = np.array([2, 6, 1, 9, 10, 3, 27])

b = np.where(np.logical_and(a > 5, a <= 10))

# one way
print(a[b])
# second way
print(a[(a > 5) & (a <= 10)])
