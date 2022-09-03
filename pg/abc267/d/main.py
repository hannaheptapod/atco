N, M = map(int, input().split())
A = list(map(int, input().split()))

dp = [0 for _ in range(M+1)]
for i in range(N):
    nxt = [0 for _ in range(M+1)]
    for j in range(min(i+1, M)):
        if j == i: nxt[j+1] = dp[j] + (j+1)*A[i]
        else: nxt[j+1] = max(dp[j+1], dp[j] + (j+1)*A[i])

    dp = nxt

print(dp[M])
