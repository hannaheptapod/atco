from itertools import combinations
from collections import deque


def main():
    global H, W, C, dr
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]
    dr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    nbh = set()
    for i in range(H):
        for j in range(W):
            if C[i][j] != '.': continue
            for di, dj in dr:
                if 0 <= i+di < H and 0 <= j+dj < W and C[i+di][j+dj] == 'S': nbh.add((i, j))

    if len(nbh) < 2: ans = 'No'
    else:
        for s, g in combinations(nbh, 2):
            d = dfs(s, g)
            if d > 0:
                ans = 'Yes'
                break
        else: ans = 'No'

    print(ans)


def dfs(s, g):
    si, sj, gi, gj = *s, *g
    dist = [[-1]*W for _ in range(H)]
    dist[si][sj] = 0

    deq = deque([s])
    while deq:
        i, j = deq.popleft()
        for di, dj in dr:
            if 0 <= i+di < H and 0 <= j+dj < W and C[i+di][j+dj] == '.' and dist[i+di][j+dj] == -1:
                dist[i+di][j+dj] = dist[i][j] + 1
                deq.append((i+di, j+dj))

    return dist[gi][gj]


if __name__ == '__main__': main()
