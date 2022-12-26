from itertools import product
from collections import deque


def main():
    global H, W, S
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]

    ans = 0
    for si, sj in product(range(H), range(W)): ans += solve(si, sj)
    print(ans)


def solve(si, sj):
    if S[si][sj] == '.': return 0
    ret = 0


if __name__ == '__main__': main()
