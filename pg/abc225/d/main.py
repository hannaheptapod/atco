from collections import deque
n, q = map(int, input().split())
g = [[0, 0] for _ in range(n)]
for _ in range(q):
    qi = list(map(int, input().split()))
    if qi[0] == 1:
        g[qi[1]-1][1] = qi[2]
        g[qi[2]-1][0] = qi[1]
    elif qi[0] == 2:
        g[qi[1]-1][1] = 0
        g[qi[2]-1][0] = 0
    else:
        x = qi[1]
        cnt = 1
        tran = deque([str(x)])
        now = x
        while g[now-1][0]:
            cnt += 1
            tran.appendleft(str(g[now-1][0]))
            now = g[now-1][0]
        now = x
        while g[now-1][1]:
            cnt += 1
            tran.append(str(g[now-1][1]))
            now = g[now-1][1]
        print(cnt, ' '.join(tran))