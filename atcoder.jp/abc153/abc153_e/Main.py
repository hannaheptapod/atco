INF = 10**9
H, N = map(int, input().split())

dp = [0] + [INF]*H

for _ in range(N):
    a, b = map(int, input().split())

    for i in range(1, H + 1):
        if i < a: dp[i] = min(dp[i], b)
        else: dp[i] = min(dp[i], dp[i-a] + b)

ans = dp[H]
print(ans)