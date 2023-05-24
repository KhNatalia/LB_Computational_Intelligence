x = int(input())
nums = list(range(1 , x + 1))
dic = {x: x ** 2 for x in nums}
print(dic)
