n, k = map(int, input().split())
mod = 10**9 + 7

ans = k % mod
if n >= 2:
    ans = (ans * (k - 1)) % mod
if n >= 3:
    tmp = 1
    l = k - 2
    m = n - 2
    while m:
        if m % 2:
            tmp = (tmp * l) % mod
        l = l*l % mod
        m >>= 1
    ans = (ans * tmp) % mod
print(ans)