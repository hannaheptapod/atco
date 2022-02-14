n = int(input())
v = [[0, 0, 0]] + [list(map(int, input().split())) for _ in range(n)]
dp = [[0, 0, 0] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(3): dp[i][j] = max(dp[i-1][(j+1)%3], dp[i-1][(j+2)%3])+v[i][j]

ans = max(dp[-1])

print(ans)