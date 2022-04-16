import array

MOD = 998244353
N, M, K = map(int, input().split())

dp = array.array('i', [1] + [0]*(N*M))
for i in range(N):
    nxt = array.array('i', [0]*(N*M + 1))

    for j in range(i, i*M + 1):
        for k in range(1, M+1):
            nxt[j+k] += dp[j]
            nxt[j+k] %= MOD

    dp = nxt

ans = sum(dp[1:K+1]) % MOD
print(ans)
