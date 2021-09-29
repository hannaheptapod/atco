n = int(input())
mod = 10**9 + 7

def pow(x, num):
    res = 1
    while num:
        if num % 2: res = res * x % mod
        x = x * x % mod
        num >>= 1
    return res % mod

ans = pow(10, n) - 2 * pow(9, n) + pow(8, n)

print(ans % mod)