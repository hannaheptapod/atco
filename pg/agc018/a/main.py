from math import gcd
n, k = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)

g = a[0]
for ai in a:
    g = gcd(g, ai)
    if g == 1: break

for ai in a:
    if ai >= k:
        if (ai-k)%g == 0:
            ans = 'POSSIBLE'
            break
        else: continue
    else:
        ans = 'IMPOSSIBLE'
        break
else: ans = 'IMPOSSIBLE'

print(ans)