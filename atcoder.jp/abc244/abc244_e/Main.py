import array

N, M, K, S, T, X = map(int, input().split())
MOD = 998244353
graph = [array.array('i', []) for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[array.array('i', [0]*(N+1)) for _ in range(2)] for _ in range(K+1)]
dp[0][0][S] = 1

for i in range(K):
    for j in range(1, N+1):
        for k in graph[j]:
            for x in range(2):
                if k == X: dp[i+1][1-x][k] = (dp[i+1][1-x][k] + dp[i][x][j]) % MOD
                else: dp[i+1][x][k] = (dp[i+1][x][k] + dp[i][x][j]) % MOD

ans = dp[-1][0][T]
print(ans)
