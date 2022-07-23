N, M = map(int, input().split())
X = [0] + list(map(int, input().split()))
B = [0]*(N+1)
for _ in range(M):
    C, Y = map(int, input().split())
    B[C] = Y

dp = [[0]*(i+1) for i in range(N+1)]
for i in range(1, N+1):
    dp[i][0] = max(dp[i-1])

    for j in range(1, i+1): dp[i][j] = dp[i-1][j-1] + X[i] + B[j]

print(max(dp[-1]))
