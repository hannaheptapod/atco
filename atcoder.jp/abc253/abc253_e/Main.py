import array

N, M, K = map(int, input().split())
MOD = 998244353

dp = array.array('i', [i for i in range(M+1)])

for _ in range(1, N):
    nxt = array.array('i', [0]*(M+1))

    for i in range(1, M+1):
        nxt[i] = dp[max(0, i-K)] + dp[M]-dp[min(M, i+K-1)] if K else dp[M]
        nxt[i] %= MOD

    for i in range(1, M+1):
        dp[i] = dp[i-1] + nxt[i]
        dp[i] %= MOD

ans = dp[-1]
print(ans)
