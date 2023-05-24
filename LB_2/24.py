import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None, encoding='windows-1251')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

max_s = sepallength.max()
min_s = sepallength.min()

S = (sepallength - min_s) / (max_s - min_s)
print(S)
