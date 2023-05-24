s1 = {'a', 'b'}
s2 = {'c', 'd', 'a'}
#first way
s1.update(s2)
print(s1)
#second way
print(set.union(s1, s2))
