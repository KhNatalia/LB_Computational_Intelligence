import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', encoding='windows-1251', usecols=[0, 1, 2, 3])
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan

any_nan_in_row = np.array([~np.any(np.isnan(row)) for row in iris_2d])
print(iris_2d[any_nan_in_row])
