import operator

d = {'cccc': 2, 'bbbb': 3, 'aaaa': 1}

sorted_item = sorted(d.items(), key=operator.itemgetter(1))
print('Sort for items')
print(sorted_item)
sorted_item = sorted(d.items(), key=operator.itemgetter(0))
print('Sort for key')
print(sorted_item)
# list_for_item = list(d.items())
# list_for_item.sort(key=lambda i: i[1])
# print('Sort for items')
# for i in list_for_item:
#     print(i[0], ':', i[1])
# print('Sort for key')
# list_for_key = list(d.keys())
# list_for_key.sort()
# for i in list_for_key:
#     print(i, ':', d[i])
