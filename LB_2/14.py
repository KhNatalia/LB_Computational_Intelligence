import numpy as np


def maxx(x, y):
    """"Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


maxx(1, 5)

pair_max = np.vectorize(maxx, otypes=[np.ndarray])

a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])

print(pair_max(a, b))
