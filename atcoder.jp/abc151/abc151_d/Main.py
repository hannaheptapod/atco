from itertools import combinations
from collections import deque
INF = 10**2
h, w = map(int, input().split())
s = [input() for _ in range(h)]
def solve(sy, sx, gy, gx):
    dst = [[INF for _ in range(w)] for _ in range(h)]
    def bfs():
        dq = deque()
        dq.insert(0, (sy, sx))
        dst[sy][sx] = 0
        while len(dq):
            y, x = dq.pop()
            if y == gy and x == gx: break
            for i in range(4):
                ny, nx = y+[1, 0, -1, 0][i], x+[0, 1, 0, -1][i]
                if ny>=0 and ny<h and nx>=0 and nx<w and s[ny][nx] != '#' and dst[ny][nx] == INF:
                    dq.insert(0, (ny, nx))
                    dst[ny][nx] = dst[y][x] + 1
        return dst[gy][gx]
    return bfs()
ans = -1
for combi in combinations(range(h*w), 2):
    si, sj, gi, gj = combi[0]//w, combi[0]%w, combi[1]//w, combi[1]%w
    if s[si][sj] == '#' or s[gi][gj] == '#': continue
    ans = max(ans, solve(si, sj, gi, gj))
print(ans)