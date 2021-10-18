n, k = map(int, input().split())
mod = 10**9 + 7
ans = 0
for i in range(k, n + 2):
    mi = (i - 1) * i // 2
    ma = n * i - mi
    ans = (ans + ma - mi + 1) % mod
print(ans)