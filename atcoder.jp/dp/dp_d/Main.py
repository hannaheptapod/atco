N, W = map(int, input().split())
item = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(W+1) for _ in range(N+1)]

for i in range(1, N+1):
    w, v = item[i]
    for j in range(1, W+1):
        if j < w: dp[i][j] = dp[i-1][j]
        else: dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[-1][-1])