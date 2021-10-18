S = input()
T = 'chokudai'
N = len(S)
dp = [[1, 0,0,0,0,0,0,0,0] for _ in range(N + 1)]
mod = 10**9+7
for i in range(N):
    dp[i+1][0] = 1
    for j in range(8):
        dp[i+1][j+1] = dp[i][j+1]
        if S[i] == T[j]:
            dp[i+1][j+1] += dp[i][j]
        dp[i+1][j+1] %= mod
ans = dp[N][8]
print(ans)