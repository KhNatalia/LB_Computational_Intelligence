import math

x = int(input())

#Math function
print(math.factorial(x))

#Cycle
res = 1
for i in range(1, x + 1):
    res *= i
print(res)

#Recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(x))
