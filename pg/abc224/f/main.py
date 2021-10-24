s = input()
l = len(s)
mod = 998244353

def pow2(i):
    res = 1
    dos = 2
    while i:
        if i % 2: res = res*dos % mod
        dos = dos**2 % mod
        i >>= 1
    return res

ev = [0]*l
ev[0] = pow2(l - 1) % mod
for i in range(1, l): ev[i] = (ev[i - 1]*5 + pow2(l - 2)) % mod

ans = 0
for i in range(l):
    x = int(s[l - 1 - i])
    ans = (ans + x*ev[i]) % mod
print(ans)