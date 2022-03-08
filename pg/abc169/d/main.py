from collections import Counter
from bisect import bisect_right as br

N = int(input())

a = []
while N % 2 == 0:
    a.append(2)
    N //= 2
f = 3
while f * f <= N:
    if N % f == 0:
        a.append(f)
        N //= f
    else:
        f += 2
if N != 1:
    a.append(N)

trianglar = (1, 3, 6, 10, 15, 21, 28, 36, 45)

ans = 0
for e in Counter(a).values(): ans += br(trianglar, e)

print(ans)
