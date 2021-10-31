from decimal import Decimal
n = int(input())
inter = [[0, 0] for _ in range(n)]
for i in range(n):
    x, y = map(Decimal, input().split())
    inter[i][0] = (y-1)/x
    if x > 1: inter[i][1] = y/(x-1)
    else: inter[i][1] = 10**10
inter.sort(key=lambda x: x[1])
end = 0
ans = 0
for ii in inter:
    if end <= ii[0]:
        ans += 1
        end = max(end, ii[1])
print(ans)