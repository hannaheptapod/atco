l, r = map(int, input().split())
mod = 10**9 + 7
l_o = 19
r_o = 19

def sigman2(n):
    sigma = (1 + n) * n // 2 % mod
    return sigma
for i in range(19):
    if 10**i > l:
        if l_o == 19:
            l_o = i
    if 10**i > r:
        r_o = i
        break
if r_o == l_o:
    ans = l_o * (sigman2(r) - sigman2(l - 1)) % mod
elif r_o - l_o == 1:
    ans = l_o * (sigman2(10 ** l_o - 1) - sigman2(l - 1)) % mod
    ans = (ans + r_o * (sigman2(r) - sigman2(10 ** (r_o - 1) - 1))) % mod
else:
    ans = l_o * (sigman2(10 ** l_o - 1) - sigman2(l - 1)) % mod
    for i in range(l_o + 1, r_o):
        ans += (i * (sigman2(10 ** i - 1) - sigman2(10 ** (i - 1) - 1))) % mod
    ans = (ans + r_o * (sigman2(r) - sigman2(10 ** (r_o - 1) - 1))) % mod
print(ans)