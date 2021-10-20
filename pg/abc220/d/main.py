n = int(input())
a = list(map(int, input().split()))
mod = 998244353

dp = [0 for _ in range(10)]
dp[a[0]] = 1

for i in range(1, n):
    ai = a[i]
    dpt = dp.copy()
    for j in range(10):
        dp[j] = dpt[(j - ai)%10]
    for j in range(10):
        dp[ai*j%10] += dpt[j]

for i in range(10):
    print(dp[i] % mod)