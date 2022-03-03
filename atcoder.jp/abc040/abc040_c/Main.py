N = int(input())
a = list(map(int, input().split()))

dp = [-1]*N
dp[0], dp[1] = 0, abs(a[1] - a[0])

for i in range(2, N): dp[i] = min(dp[i-2] + abs(a[i] - a[i-2]), dp[i-1] + abs(a[i] - a[i-1]))

ans = dp[-1]

print(ans)
