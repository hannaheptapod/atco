n, d = map(int, input().split())
mod = 998244353
def pow2(num):
    res = 1
    x = 2
    while num:
        if num % 2: res = res * x % mod
        x = x * x % mod
        num >>= 1
    return res % mod
dos = [pow2(i) for i in range(2*n + 1)]
ans = 0
for i in range(d + 1):
    ans %= mod
    j = d - i
    if i >= n: break
    elif j >= n: continue
    elif i == 0 or j == 0:
        a = dos[n - d] - 1
        ans += a * dos[d - 1]
    else:
        a = dos[n - max(i, j)] - 1
        ans += a * dos[i - 1] * dos[j - 1]
ans = (ans * 2) % mod
print(ans)