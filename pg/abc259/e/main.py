from collections import defaultdict
from bisect import insort

N = int(input())
primes = defaultdict(lambda: [0])
A = [[] for _ in range(N)]
for i in range(N):
    m = int(input())
    for _ in range(m):
        p, e = map(int, input().split())
        insort(primes[p], e)
        A[i].append((p, e))

id = {p: i for i, p in enumerate(sorted(primes.keys()))}

st = set()
for ai in A:
    tmp = [1]*len(primes)

    for p, e in ai:
        if primes[p][-2] < e: tmp[id[p]] = 0

    st.add(''.join(map(str, tmp)))

ans = len(st)
print(ans)
