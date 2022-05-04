from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

ans = 0
for i in range(1, N+1):
    seen = [False]*(N+1)

    deq = deque([i])
    while deq:
        now = deq.popleft()
        if seen[now]: continue
        seen[now] = True

        for nxt in graph[now]: deq.append(nxt)

    ans += sum(seen)

print(ans)
