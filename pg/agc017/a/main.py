def ncr(n, r):
    res = 1
    for i in range(n, n-r, -1): res *= i
    for i in range(r, 0, -1): res //= i
    return res
n, p = map(int, input().split())
a = list(map(int, input().split()))
num = [0]*2
for ai in a: num[ai%2] += 1
ans = 2**(num[0]) * sum([ncr(num[1], r) for r in range(p, num[1]+1, 2)])
print(ans)