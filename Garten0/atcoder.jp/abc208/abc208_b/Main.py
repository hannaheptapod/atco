from math import factorial

n = int(input())
i = 1
while factorial(i) < n:
    i = i + 1
sum = 0
while n != 0:
    d = n // factorial(i)
    n -= d * factorial(i)
    sum += d
    i -= 1
print(sum)
