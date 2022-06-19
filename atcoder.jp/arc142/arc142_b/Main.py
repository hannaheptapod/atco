N = int(input())
ans = [[0]*N for _ in range(N)]

y = x = (N-1)//2
dy, dx = (0, 1, 0, -1), (1, 0, -1, 0)
id = 0

for i in range(N**2):
    ans[y][x] = i//2 + 1 if not i%2 else N**2 - i//2

    y += dy[id]
    x += dx[id]
    if i < N**2-1 and not ans[y+dy[(id+1)%4]][x+dx[(id+1)%4]]: id=(id+1)%4

_=[print(*ai) for ai in ans]
