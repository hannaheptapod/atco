from itertools import combinations


def main():
    global N, M, A
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    ans = solve()
    print(ans)


def solve():
    G = [set() for _ in range(N)]
    for u, v in combinations(range(N), 2):
        w = (pow(A[u], A[v], M) + pow(A[v], A[u], M)) % M
        G[u].add((v, w))
        G[v].add((u, w))


if __name__ == '__main__': main()
