s = int(input())
m = 10**9

x, y = s//m + 1, s%m
if x == m+1: x, y = m, m

print(1, 0, 0, m, x, y)