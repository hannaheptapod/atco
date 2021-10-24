s = input()
l = len(s)
mod = 998244353
ans = int(s)
if l > 1:
    pow = 1
    dos = 2
    i = l - 2
    while i:
        if i % 2: pow = pow*dos % mod
        dos = dos**2 % mod
        i >>= 1

    ev = [0]*l
    ev[0] = 2*pow % mod
    for i in range(1, l): ev[i] = (ev[i - 1]*5 + pow) % mod

    ans = 0
    for i in range(l):
        x = int(s[l - 1 - i])
        ans = (ans + x*ev[i]) % mod
print(ans)