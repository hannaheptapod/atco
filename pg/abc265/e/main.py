MOD = 998244353

N, M = map(int, input().split())
A, B, C, D, E, F = map(int, input().split())

O = set(tuple(map(int, input().split())) for _ in range(M))

dp = [[1]]
for i in range(N):
    nxt = [[0]*(i+2) for _ in range(i+2)]

    for a in range(i+1):
        for b in range(i+1):
            x, y = a*A + b*C + (i-a-b)*E, a*B + b*D + (i-a-b)*F

            if (x+A, y+B) not in O:
                nxt[a+1][b] += dp[a][b]
                nxt[a+1][b] %= MOD

            if (x+C, y+D) not in O:
                nxt[a][b+1] += dp[a][b]
                nxt[a][b+1] %= MOD

            if (x+E, y+F) not in O:
                nxt[a][b] += dp[a][b]
                nxt[a][b] %= MOD

    dp = nxt

ans = sum(sum(dpi) for dpi in dp) % MOD
print(ans)
