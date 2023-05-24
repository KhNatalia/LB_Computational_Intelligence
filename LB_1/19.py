d = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
d = [x for (i, x) in enumerate(d) if i not in (0, 4, 5)]
print(d)
