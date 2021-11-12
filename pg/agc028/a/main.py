from math import gcd
n, m = map(int, input().split())
s, t = input(), input()
g = gcd(n, m)
for i in range(g):
    if s[n*i//g] != t[m*i//g]:
        ans = -1
        break
    else: continue
else: ans = n*m // g
print(ans)