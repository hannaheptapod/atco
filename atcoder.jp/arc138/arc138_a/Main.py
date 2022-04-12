import array
from bisect import bisect

N, K = map(int, input().split())
A = array.array('i', map(int, input().split()))

mx = [A[K]]
for ai in A[K+1:]: mx.append(max(mx[-1], ai))

ans = 1<<30
for i in range(K):
    ai = A[i]
    id = bisect(mx, ai)
    if id >= N - K: continue

    ans = min(ans, id + K - i)

print(ans if ans < 1<<30 else -1)
