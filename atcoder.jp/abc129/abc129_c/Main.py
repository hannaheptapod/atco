n, m = map(int, input().split())
mod = 10**9 + 7
hole = [False]*(n+1)
for _ in range(m): hole[int(input())] = True
a0, a1 = 0, 1
for i in range(1, n+1):
    if hole[i]: ai = 0
    else: ai = a0 + a1
    a0, a1 = a1, ai
ans = ai % mod
print(ans)