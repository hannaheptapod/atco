import array

N, M, K, S, T, X = map(int, input().split())
MOD = 998244353
graph = [array.array('i', []) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[array.array('i', [0, 0]) for _ in range(N+1)] for _ in range(K+1)]
dp[0][S][0] = 1

for i in range(K):
    for j in range(1, N+1):
        for k in graph[j]:
            for x in range(2):
                if k == X: dp[i+1][k][1-x] = (dp[i+1][k][1-x] + dp[i][j][x]) % MOD
                else: dp[i+1][k][x] = (dp[i+1][k][x] + dp[i][j][x]) % MOD

ans = dp[-1][T][0]
print(ans)
