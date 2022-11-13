from collections import deque

INF = float('inf')


def main():
    global N, M, K, nodes, swits
    N, M, K = map(int, input().split())
    nodes = [list(map(int, input().split())) for _ in range(M)]
    swits = set(map(int, input().split()))

    ans = solve()
    print(ans)


def solve():
    graph = [[] for _ in range(2*N+1)]
    for u, v, a in nodes:
        graph[u + N*(1-a)].append((v + N*(1-a), 1))
        graph[v + N*(1-a)].append((u + N*(1-a), 1))
    for i in swits:
        graph[i].append((i+N, 0))
        graph[i+N].append((i, 0))

    return binary_bfs(graph)


def binary_bfs(graph):
    dist = [INF]*(2*N+1)
    dist[1] = 0

    deq = deque([1])
    while deq:
        u = deq.popleft()

        for v, c in graph[u]:
            if dist[v] < INF: continue

            dist[v] = dist[u]+c
            deq.append(v) if c else deq.appendleft(v)

    ret = min(dist[N], dist[2*N])
    return ret if ret < INF else -1


if __name__ == '__main__': main()
