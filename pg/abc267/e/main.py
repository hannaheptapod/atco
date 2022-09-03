N, M = map(int, input().split())
A = list(map(int, input().split()))
G = [set() for _ in range(N)]
C = [0]*N
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)
    C[u] += A[v]
    C[v] += A[u]


def f(X):
    cost = C.copy()
    s = [v for v in range(N) if cost[v] <= X]
    done = set(s)

    while s:
        v = s.pop()

        for i in G[v]:
            if i in done: continue
            cost[i] -= A[v]
            if cost[i] <= X:
                s.append(i)
                done.add(i)

    return len(done) == N


ok, ng = N*max(A), -1
while ok > ng+1:
    md = (ok+ng)//2

    if f(md): ok = md
    else: ng = md

print(ok)
