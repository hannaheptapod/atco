from collections import defaultdict
from bisect import bisect_left


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    edges, lengs = defaultdict(list), defaultdict(int)
    for i, ai in enumerate(A):
        edges[ai].append(i)
        edges[ai+1].append(i)
        lengs[ai] += 1
        lengs[ai+1] += 1

    for i in range(M):
        x, y = 1, 0

        while y < M:
            id = bisect_left(edges[x], y if y != i else y+1)
            if id == lengs[x]: break

            y = edges[x][id]
            if y == i: y += 1
            x = x+1 if A[y] == x else x-1

            y += 1

        print(x)


if __name__ == '__main__': main()
