N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)
    G[b].append(a)


for i in range(N):
    s = set()
    gi = G[i]
    for j in gi:
        for k in G[j]: s.add(k)
    if i in s: s.remove(i)
    for j in gi:
        if j in s: s.remove(j)
    ans = len(s)
    print(ans)