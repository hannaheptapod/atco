import heapq

N, M = map(int, input().split())
A = list(map(int, input().split()))
G = [set() for _ in range(N)]
cost = [[0, i] for i in range(N)]
for _ in range(M):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].add(v)
    G[v].add(u)
    cost[u][0] += A[v]
    cost[v][0] += A[u]

hq = cost.copy()  # 2層目が参照渡しになっている
heapq.heapify(hq)

ans = 0
erased = [False]*N
while hq:
    c, u = heapq.heappop(hq)
    if erased[u]: continue
    erased[u] = True
    ans = max(ans, c)

    for v in G[u]:
        if erased[v]: continue
        cost[v][0] -= A[u]  # hq[_][v] も更新される
        heapq.heappush(hq, cost[v])

print(ans)
