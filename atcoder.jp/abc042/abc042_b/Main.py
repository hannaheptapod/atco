n, l = map(int, input().split())
ss = [input() for _ in range(n)]
i = 0
while i < n-1:
    if ss[i]+ss[i+1] <= ss[i+1]+ss[i]: i+= 1
    else:
        ss[i], ss[i+1] = ss[i+1], ss[i]
        i = max(i-1, 0)
ss = [''] + ss
dp = [['']*(n+1) for _ in range(n+1)]
dp[n][1] = ss[-1]
for i in range(n-1, 0, -1):
    for j in range(1, n-i+2):
        if dp[i+1][j]: dp[i][j] = min(dp[i+1][j], ss[i]+dp[i+1][j-1])
        else: dp[i][j] = ss[i]+dp[i+1][j-1]
print(dp[1][n])