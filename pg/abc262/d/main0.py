MOD = 998244353

N = int(input())
a = list(map(int, input().split()))

ans = N
dp = {i: {} for i in range(1, N+1)}
for i in range(N):
    for j in range(i, 0, -1):
        for k in dp[j].items():
            if a[i]+k[0] not in dp[j+1]: dp[j+1][a[i]+k[0]] = k[1]
            else: dp[j+1][a[i]+k[0]] += k[1]

            if not (a[i]+k[0])%(j+1): ans = (ans+k[1])%MOD

    if a[i] not in dp[1]: dp[1][a[i]] = 1
    else: dp[1][a[i]] += 1

print(ans)
