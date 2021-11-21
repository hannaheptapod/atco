mod = 10**9 + 7
def fac(num):
    res = 1
    for i in range(1, num+1): res = res*i % mod
    return res
n, m = map(int, input().split())
if abs(n - m) > 1: ans = 0
elif abs(n - m) == 1: ans = fac(n)*fac(m)
else: ans = fac(n)*fac(m) * 2
print(ans % mod)