from collections import defaultdict
from itertools import permutations


def main():
    global N, M, graph
    N, M = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].add(b)
        graph[b].add(a)

    ans = solve()
    print(ans)


def solve():
    ret = 0
    for perm in permutations(range(2, N+1)):
        now = 1

        for i in range(N-1):
            if now not in graph[perm[i]]: break
            now = perm[i]
        else: ret += 1

    return ret


if __name__ == '__main__': main()
