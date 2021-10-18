import collections
N, K = map(int, input().split())
A = list(map(int, input().split()))
cdict = collections.Counter(A)
c = sorted(cdict.values())
v = len(c) - K
ans = 0
if v > 0:
    for i in range(v):
        ans += c[i]
print(ans)