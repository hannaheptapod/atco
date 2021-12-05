n, p = map(int, input().split())
g = 1
for i in range(2, int(-(-p**0.5 // 1)) + 1):
    tmp = 0
    while p%i == 0:
        tmp += 1
        p //= i
    if tmp >= n: g *= i
    if p > 1: continue
    break
if n == 1: g *= p
print(g)