N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))

dp = [[0]*(N+1) for _ in range(61)]
for cu in range(N): dp[0][cu] = A[cu]
for p in range(1, 61):
    for cu in range(N): dp[p][cu] = dp[p-1][dp[p-1][cu]]

cu = 0
for p in range(60, -1, -1):
    if K & 1<<p: cu = dp[p][cu]

ans = cu + 1
print(ans)
