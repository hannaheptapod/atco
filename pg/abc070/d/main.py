from collections import deque


def main():
    N = int(input())
    G = [{} for _ in range(N)]
    for _ in range(N-1):
        a, b, c = map(int, input().split())
        G[a-1][b-1] = c
        G[b-1][a-1] = c
    Q, K = map(int, input().split())
    K -= 1
    query = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]

    dist = [-1]*N
    dist[K] = 0
    deq = deque([K])
    while deq:
        v = deq.popleft()
        for u, c in G[v].items():
            if dist[u] == -1:
                dist[u] = dist[v] + c
                deq.append(u)

    for x, y in query: print(dist[x] + dist[y])


if __name__ == '__main__': main()
