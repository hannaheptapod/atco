n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
mod = 998244353
m = b[-1]
dp = [1] * (m+1)
for i in range(n):
    nx = [0] * (m+1)
    for j in range(a[i], b[i] + 1): nx[j] = dp[j]
    dp = nx
    for j in range(m):
        dp[j + 1] = (dp[j] + dp[j+1]) % mod
print(dp[m])