n = int(input())
x, y = map(int, input().split())
a, b = [], []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
inf = 0x7fff
dp = [[[inf for _ in range(y + 1)] for _ in range(x + 1)] for _ in range(n + 1)]
dp[0][0][0] = 0

for i in range(1, n + 1):
    for j in range(x + 1):
        for k in range(y + 1):
            dp[i][min(j + a[i - 1], x)][min(k + b[i - 1], y)] = min(dp[i][min(j + a[i - 1], x)][min(k + b[i - 1], y)], dp[i - 1][j][k] + 1)
            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])

if dp[n][x][y] != inf: ans = dp[n][x][y]
else: ans = -1

print(ans)