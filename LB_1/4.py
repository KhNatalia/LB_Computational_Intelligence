dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
x = int(input())
if dic.setdefault(x):
    print('yes')
else:
    print('no')
