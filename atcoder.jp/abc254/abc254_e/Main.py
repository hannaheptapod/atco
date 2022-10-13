from collections import deque


def main():
    global N, G
    N, M = map(int, input().split())
    G = [set() for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].add(b)
        G[b].add(a)

    Q = int(input())
    for _ in range(Q):
        x, k = map(int, input().split())
        print(solve(x, k))


def solve(x, k):
    st = set([x])

    for _ in range(k): st |= set.union(*[G[v] for v in st])

    return sum(st)


if __name__ == '__main__': main()
