n = int(input())
s = input()
at = 'atcoder'
mod = 10**9 + 7

h, w = n + 1, 7 + 1
dp = [[0]*w for _ in range(h)]
dp[0][0] = 1

for i in range(1, h):
    dp[i][0] = dp[i-1][0] % mod
    for j in range(1, w):
        if s[i-1] == at[j-1]: dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % mod
        else: dp[i][j] = dp[i-1][j] % mod

ans = dp[h-1][w-1]
print(ans)