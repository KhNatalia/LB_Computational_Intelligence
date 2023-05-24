import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None, encoding='windows-1251')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

print(np.percentile(sepallength, q=[5, 95]))
