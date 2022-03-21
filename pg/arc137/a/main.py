from math import gcd

L, R = map(int, input().split())

for diff in range(R-L, 0, -1):
    for x in range(L, R-diff+1):
        if gcd(x, x+diff) == 1: break
    else: continue
    break

ans = diff
print(ans)
