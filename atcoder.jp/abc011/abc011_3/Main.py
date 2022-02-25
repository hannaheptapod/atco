N = int(input())
NG = [int(input()) for _ in range(3)]

dp = [[False]*N + [N not in NG] + [False]*2 for _ in range(101)]
for i in range(1, 100 + 1):
    for j in range(N):
        if j in NG: dp[i][j] = False
        else: dp[i][j] = dp[i-1][j] or dp[i-1][j+1] or dp[i-1][j+2] or dp[i-1][j+3]

if dp[100][0]: ans = 'YES'
else: ans = 'NO'

print(ans)