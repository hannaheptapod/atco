n, m = map(int, input().split())
sta = [[0, False]] + [[1, False] for _ in range(n)]
sta[1][1] = True
ans = 1
for _ in range(m):
    x, y = map(int, input().split())
    sta[x][0] -= 1
    sta[y][0] += 1
    if sta[x][1]:
        if not sta[x][0]:
            sta[x][1] = False
            ans -= 1
        if not sta[y][1]:
            sta[y][1] = True
            ans += 1
print(ans)