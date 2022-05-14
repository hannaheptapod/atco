from collections import deque

N, M = map(int, input().split())
edges = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
graph = {i: set() for i in range(N)}
for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)

ans = 0
for a, b in edges:
    graph[a].remove(b)
    graph[b].remove(a)

    seen = [False]*N
    deq = deque([0])
    while deq:
        now = deq.popleft()
        if seen[now]: continue
        seen[now] = True

        for nxt in graph[now]: deq.append(nxt)

    if not all(seen): ans += 1

    graph[a].add(b)
    graph[b].add(a)

print(ans)
