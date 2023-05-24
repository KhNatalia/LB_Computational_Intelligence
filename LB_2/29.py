import numpy as np
from scipy.spatial import distance

a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7, 8])

print(np.linalg.norm(a - b))
print(distance.euclidean(a, b))
