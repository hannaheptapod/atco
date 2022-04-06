N = int(input())
A = [0] + list(map(int, input().split()))

dp = [1000]*(N+1)
for i in range(2, N+1):
    dp[i] = dp[i-1]
    for j in range(1, i): dp[i] = max(dp[i], dp[i-j] + (A[i] - A[i-j])*(dp[i-j]//A[i-j]))

ans = dp[-1]
print(ans)
