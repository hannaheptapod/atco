N, M = map(int, input().split())
MOD = 998244353

L = len(bin(M)[2:])
if L < N: ans = 0
else:
    num = [(2**(i-1) if 2**i <= M else M-2**(i-1)+1)%MOD for i in range(L+1)]

    dp = [[1]+[0]*L for _ in range(L+1)]

    for i in range(1, L+1):
        for j in range(1, min(i, L)+1):
            dp[i][j] = dp[i-1][j-1]*num[i] + dp[i-1][j]
            dp[i][j] %= MOD

    ans = dp[-1][N]

print(ans)
