N = int(input())
T = [0] + list(map(int, input().split()))

sm = sum(T)

dp = [[1]+[0]*sm for _ in range(N+1)]
for i in range(1, N + 1):
    ti = T[i]
    for j in range(ti, sm + 1): dp[i][j] = max(dp[i-1][j], dp[i-1][j - ti])

ans = sm
for j in range(sm + 1):
    if dp[N][j]: ans = min(ans, max(j, sm - j))

print(ans)