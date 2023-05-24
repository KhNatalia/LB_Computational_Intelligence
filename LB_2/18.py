import numpy as np

# Create the random array
np.random.seed(100)
rand_arr = np.random.random([3, 3]) / 1e3

np.set_printoptions(suppress=True, precision=6)
print(rand_arr)
