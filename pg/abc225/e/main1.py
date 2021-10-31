from decimal import Decimal
n = int(input())
inter = [[0, 0] for _ in range(n)]
for i in range(n):
    x, y = map(Decimal, input().split())
    inter[i][0] = (y-1) / (x**2 + (y-1)**2)**Decimal(1/2)
    inter[i][1] = y / ((x-1)**2 + y**2)**Decimal(1/2)
inter.sort(key=lambda x: x[1])
end = 0
ans = 0
for ii in inter:
    if end <= ii[0]:
        ans += 1
        end = max(end, ii[1])
print(ans)