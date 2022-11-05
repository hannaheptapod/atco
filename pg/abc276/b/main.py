def main():
    N, M = map(int, input().split())
    graph = [set() for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    for g in graph[1:]:
        ans = len(g), *sorted(g)
        print(*ans)


if __name__ == '__main__': main()
