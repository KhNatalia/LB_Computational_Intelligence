from functools import reduce

print(reduce(lambda x, y: x*y, (8, 2, 3, -1, 7)))
