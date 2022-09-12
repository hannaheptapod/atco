from collections import defaultdict, deque

N, Q = map(int, input().split())
G = defaultdict(lambda: set())
for _ in range(N-1):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].add(b)
    G[b].add(a)
P = [0]*N
for _ in range(Q):
    p, x = map(int, input().split())
    P[p-1] += x

deq = deque([[0, -1]])
while deq:  # imos法
    v, pa = deq.pop()
    for u in G[v]:
        if u == pa: continue
        P[u] += P[v]
        deq.append([u, v])

print(*P)
