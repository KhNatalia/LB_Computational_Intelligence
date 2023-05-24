import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', encoding='windows-1251', usecols=[0, 1, 2, 3])

print(np.correlate(iris_2d[:, 1], iris_2d[:, 3]))
print(np.corrcoef(iris_2d[:, 1], iris_2d[:, 3]))
