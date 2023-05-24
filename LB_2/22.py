import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None, encoding='windows-1251')
iris_2d = ([row.tolist()[:4] for row in iris_1d])
print(iris_2d)
