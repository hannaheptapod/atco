from collections import deque
h, w = map(int, input().split())
INF = h*w
s = [input() for _ in range(h)]
def solve(si, sj):
    res = -1
    dst = [[INF for _ in range(w)] for _ in range(h)]
    dq = deque()
    dq.appendleft((si, sj))
    dst[si][sj] = 0
    while len(dq):
        y, x = dq.pop()
        for i in range(4):
            ny, nx = y+[1, 0, -1, 0][i], x+[0, 1, 0, -1][i]
            if ny>=0 and ny<h and nx>=0 and nx<w and s[ny][nx] != '#' and dst[ny][nx] == INF:
                dq.appendleft((ny, nx))
                dst[ny][nx] = dst[y][x] + 1
    for gi in range(h):
        for gj in range(w):
            d = dst[gi][gj]
            if d < INF: res = max(res, d)
    return res
ans = -1
for si in range(h):
    for sj in range(w):
        if s[si][sj] != '#': ans = max(ans, solve(si, sj))
print(ans)