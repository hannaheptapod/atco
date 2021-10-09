n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max = b[-1]
mod = 998244353

if any([bi - ai < 0 for ai, bi in zip(a, b)]): ans = 0
else:
    dp = [0 for _ in range(max)]
    for j in range(a[0], b[0] + 1): dp[j-1] = 1
    for i in range(1, n):
        ai, bi = a[i], b[i]
        for j in range(ai, bi + 1): dp[j-1] = (dp[j-2] + dp[j-1]) % mod
        for j in range(1, ai): dp[j-1] = 0
    ans = sum(dp) % mod
print(ans)