
n, q = map(int, input().split())
g = [[-1, -1]] + [[0, 0] for _ in range(n)]
def get_first(i):
    if g[i][0]: return get_first(g[i][0])
    return i
for _ in range(q):
    qi = list(map(int, input().split()))
    if qi[0] == 1:
        g[qi[1]][1] = qi[2]
        g[qi[2]][0] = qi[1]
    elif qi[0] == 2:
        g[qi[1]][1] = 0
        g[qi[2]][0] = 0
    else:
        f = get_first(qi[1])
        ans = ''
        now = f
        cnt = 0
        while True:
            cnt += 1
            ans += ' ' + str(now)
            if g[now][1]: now = g[now][1]
            else: break
        print(str(cnt) + ans)